## NiFi

<https://nifi.apache.org/>

<https://habr.com/ru/articles/905828/>

## Example: Sensor Data Pipeline MQTT — Collect → Convert → Store in Database

```
[Sensors] ──► [NiFi: Ingest] ──► [NiFi: Transform] ──► [NiFi: Write] ──► [Oracle DB]
```

NiFi models everything as **FlowFiles** (data packets) flowing through **Processors**   
connected by **Relationships** (success, failure, retry).


### Step 1 — Collect Data from Sensors (Every Minute)

NiFi offers several processors depending on how sensors publish data:

| Sensor Protocol | NiFi Processor |
|---|---|
| MQTT (IoT standard) | `ConsumeMQTT` |
| HTTP/REST endpoint | `InvokeHTTP` + `GenerateFlowFile` (scheduled) |
| TCP/UDP socket | `ListenTCP` / `ListenUDP` |
| Modbus / OPC-UA | `GetFile` or custom script via `ExecuteScript` |
| CSV/JSON file drop | `GetFile` / `ListenHTTP` |

**Scheduling:** Every processor has a **Run Schedule**. Set it to `1 min` (cron: `0 * * * * ?`) in the processor config. NiFi will trigger the processor on that interval.

**Example flow for MQTT sensors:**
```
[ConsumeMQTT]
  topic: sensors/temperature/+
  broker: tcp://mqtt-broker:1883
  Run Schedule: 0 * * * * ?   ← every 1 minute
```

The raw payload (JSON, CSV, binary) becomes a FlowFile.

---

### Step 2 — Parse & Convert Units of Measure

This is where NiFi's transformation processors shine.

### 2a. Parse the raw payload
Use **`EvaluateJsonPath`** to extract fields from JSON sensor data:
```
sensor_id  → $.device_id
raw_value  → $.value
unit       → $.unit
timestamp  → $.ts
```
These become **FlowFile Attributes** (key-value metadata).

### 2b. Convert units with `UpdateAttribute` or `ExecuteScript`

**Option A — Simple math with `UpdateAttribute` (Expression Language):**
```
# Celsius → Fahrenheit
value_converted = ${raw_value:multiply(1.8):plus(32)}

# Meters → Feet
value_converted = ${raw_value:multiply(3.28084)}

# Pa → PSI
value_converted = ${raw_value:multiply(0.000145038)}
```

**Option B — Complex logic with `ExecuteScript` (Python/Groovy):**
```python
# Groovy example
import groovy.json.JsonSlurper

def flowFile = session.get()
def json = new JsonSlurper().parseText(
    flowFile.getAttribute('raw_payload')
)

def converted = json.unit == 'C' 
    ? json.value * 1.8 + 32   // to Fahrenheit
    : json.value

// Write back to FlowFile attribute
flowFile = session.putAttribute(flowFile, 'value_converted', converted.toString())
flowFile = session.putAttribute(flowFile, 'unit_out', 'F')
session.transfer(flowFile, REL_SUCCESS)
```

**Option C — `JoltTransformJSON`** for structural transformation + unit mapping using JOLT spec DSL (great for complex JSON reshaping).

### 2c. Build the final record with `ReplaceText` or `AttributesToJSON`
Compose a clean JSON or SQL-ready payload:
```json
{
  "sensor_id": "TEMP_001",
  "value_f": 98.6,
  "unit": "F",
  "collected_at": "2026-04-24T10:00:00Z"
}
```

---

### Step 3 — Write to Oracle Database

### 3a. Set up the Oracle DBCPConnectionPool (Controller Service)
This is a shared connection pool configured once and reused by all DB processors:
```
Database Connection URL:  jdbc:oracle:thin:@//oracle-host:1521/ORCL
Database Driver Class:    oracle.jdbc.OracleDriver
Driver JAR Location:      /opt/nifi/lib/ojdbc8.jar   ← you add this
Username:                 nifi_user
Password:                 ••••••
Max Total Connections:    10
```

> ⚠️ You must manually download `ojdbc8.jar` from Oracle and place it in NiFi's lib directory — Oracle doesn't allow redistribution.

### 3b. Write with `PutDatabaseRecord` (recommended) or `ExecuteSQL`

**`PutDatabaseRecord`** is the modern, schema-aware approach:
```
Record Reader:       JsonTreeReader
Statement Type:      INSERT
Table Name:          SENSOR_READINGS
DBCPConnectionPool:  [your Oracle pool above]
```

It automatically maps JSON fields → Oracle columns by name.

**Target Oracle table:**
```sql
CREATE TABLE SENSOR_READINGS (
    id          NUMBER GENERATED ALWAYS AS IDENTITY,
    sensor_id   VARCHAR2(50),
    value_raw   NUMBER(10,4),
    value_conv  NUMBER(10,4),
    unit_in     VARCHAR2(10),
    unit_out    VARCHAR2(10),
    collected_at TIMESTAMP,
    inserted_at  TIMESTAMP DEFAULT SYSTIMESTAMP
);
```

## Complete Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     NiFi Canvas                             │
│                                                             │
│  [ConsumeMQTT]                                              │
│  schedule: 1 min  ──► [EvaluateJsonPath]                   │
│                              │                              │
│                              ▼                              │
│                       [UpdateAttribute]                     │
│                       (unit conversion                      │
│                        via Expression                       │
│                        Language)                            │
│                              │                              │
│                              ▼                              │
│                       [AttributesToJSON]                    │
│                       (build output record)                 │
│                              │                              │
│                    ┌─────────┴──────────┐                  │
│                 success              failure                │
│                    │                    │                   │
│                    ▼                    ▼                   │
│           [PutDatabaseRecord]    [LogMessage]               │
│           Oracle connection      + [PutFile]                │
│                                  (error archive)            │
└─────────────────────────────────────────────────────────────┘
```


### Key Best Practices

**Reliability:** Always connect the `failure` relationship to a `LogAttribute` + `PutFile` processor to archive failed FlowFiles for reprocessing — never leave a relationship unconnected.

**Back-pressure:** NiFi has built-in back-pressure on queues between processors. If Oracle is slow, NiFi buffers FlowFiles in its internal content repo rather than dropping data.

**Provenance:** Every FlowFile is tracked end-to-end. You can replay any failed record from NiFi's Data Provenance UI with a single click.

**Scaling:** If sensor volume grows, you can increase processor concurrent tasks or deploy NiFi as a cluster — the flow definition doesn't change.

**Security:** Use NiFi's `SSLContextService` for encrypted MQTT/HTTPS connections and store DB passwords in NiFi's encrypted `Sensitive Properties Key` vault, never in plaintext.

---

This gives you a fully auditable, retry-safe, schema-aware pipeline from raw sensor readings to a normalized Oracle table — with unit conversion happening in-flight, all configured through NiFi's drag-and-drop UI with no custom application code required for the basic case.

### Setup on MacBook 
```
/opt/homebrew/opt/nifi/libexec/bin
nifi stop
./nifi.sh set-single-user-credentials admin admin1234567890
nifi start
```
Как работает Apache NiFi
```
NiFi состоит из нескольких ключевых компонентов, каждый из которых играет важную роль в обработке данных.

FlowFiles — это единицы данных, которые перемещаются по системе.
Каждый FlowFile похож на конверт с письмом,
в котором содержатся сама информация и важные метаданные (например, время получения,
источник и идентификатор). Благодаря этому можно всегда проследить,
откуда пришли данные и что с ними делали.

Processors (Процессоры) — это строительные блоки, выполняющие конкретные операции с FlowFiles.
Например, один процессор может считывать данные из текстового файла,
другой — фильтровать ненужные записи,
а третий — отправлять результат в базу данных или другой сервис.

Пример. Если вам нужно обработать список заказов, один процессор может читать данные из файла,
другой — отбирать заказы на сумму выше определенного порога,
а третий — отправлять эти данные в систему отчетности.

Connections (Соединения)Соединения связывают процессоры, направляя поток данных от одного блока к другому. 

Flow Controller и Content RepositoryFlow Controller управляет всей логикой обработки:
он распределяет задачи между процессорами, контролирует очереди данных и следит за тем,
чтобы все работало гладко. Content Repository — это хранилище, где сохраняются сами данные,
что позволяет при необходимости повторно обращаться к ним или анализировать историю обработки.
```

 файл nifi.properties, где можно настроить параметры, такие как порты, пути к репозиториям,   
 лимиты памяти и другие важные опции.

 Запуск NiFi. Запустите программу с помощью соответствующего скрипта  
 (bin/nifi.sh start для Linux или bin/nifi.bat start для Windows). 

###  Apache NiFi vs. Apache Airflow
<https://habr.com/ru/companies/neoflex/articles/766524/>

```
Apache Airflow ориентирован на планирование и оркестрацию пакетных задач.   
Это как расписание поездов, где каждый рейс строго запланирован, а NiFi работает в режиме непрерывного потока данных,   
подобно управлению дорожным движением, где важна мгновенная реакция на изменение ситуации.
Когда использовать NiFi:  Если задача требует постоянной обработки поступающих данных в реальном времени,   
NiFi обеспечит гибкость и оперативность, чего не всегда можно добиться с Airflow.
```
<img width="505" height="385" alt="image" src="https://github.com/user-attachments/assets/5bad6c64-30f7-47de-8d44-fc874f89d1eb" />


<https://habr.com/ru/companies/tbank/articles/743886/>
NiFi — потоковый инструмент, и хороший вариант его использования — загружать небольшие порции данных через небольшие промежутки времени.  
Желательно избегать загрузки всей информации за длительный период,   
если вам все-таки нужно реализовать подобный сценарий, читайте об этом в прошлой статье:  
<https://habr.com/ru/companies/tbank/articles/659795/>


<https://habr.com/ru/companies/arenadata/articles/845790/> working with DB
в основе записей в NiFi находится Apache Avro

<https://habr.com/ru/companies/arenadata/articles/877126/>


```
У каждого FlowFile есть обязательные атрибуты (Core Attributes), которые генерируются системой при создании FlowFile, прохождении его через различные отношения (очереди).

filename — имя файла, которое может быть применено для хранения данных локально либо удалённо.

path — директория, которая может быть применена для хранения данных.

uuid — уникальный идентификатор, однозначно указывающий на этот FlowFile.

entryDate — дата и время создания FlowFile в миллисекундах с 1 января 1970, в формате UTC.

lineageStartDate — время появления в системе самого старого предка текущего файла, в миллисекундах, в формате UTC.

fileSize — количество байт, составляющих контент. This attribute represents the number of bytes taken up by the FlowFile’s Content.

Такие атрибуты, как uuid, entryDate, lineageStartDate и fileSize,  
генерируются системой и не могут быть изменены в ходе обработки пользовательской функцией.

В NiFi есть ряд процессоров, предназначенных для работы с атрибутами,
перечисленные в разделе Attribute Extraction:

- EvaluateJsonPath. С помощью выражений JSONPath можно выполнить обмен данными между атрибутами и контентом.

- EvaluateXPath. Аналогично предыдущему, только применяется XPath.

- EvaluateXQuery. Аналогично предыдущему, только применяется запрос XQuery.

- ExtractText. Позволяет извлечь в атрибут текст по регулярному выражению.

- HashAttribute. Позволяет применять функции хеширования над списком атрибутов и помещать результат в определённый атрибут.

- HashContent. Применяет функцию хеширования над контентом и помещает результат в атрибут.

- IdentifyMimeType. Определяет тип контента и помещает значение в атрибут.

- UpdateAttribute. Процессор позволяет изменять либо создавать атрибуты,  
при этом возможно применять специальный язык Expression Language 
```
### Expression Language (EL) 
```
 Это очень мощный инструмент работы с метаданными.
Каждое выражение в EL начинается со знака $ и  обрамляется фигурными скобками — ${выражение}.  
 В самом выражении прописываем атрибут и функцию над ним.
Например, проверим, что в атрибуте, содержащем имя файла, такое же значение,
 как и в идентификаторе FlowFile.
Для этого прочитаем атрибут filename и сравним его с атрибутом
uuid — ${filename:equals(${uuid})}.

Функция отделена от аргумента знаком «:»,
и таких функций может быть много.
 Например, выражение
${filename:startWith(“some_value”):not()}
возвращает true, если имя файла не начинается со строки «some_value».
```
