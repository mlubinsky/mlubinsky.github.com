```
from bdp.common.schema.base import Schema
#schema="ios_app_estimates_weekly_i"
schema="mps_bin_kpi_o"
schema_obj = Schema.factory(schema)

print(schema_obj)

print("is_csv=",schema_obj.is_csv)
if schema_obj.is_csv:
    print("is_tab delimiter=",schema_obj.csv_delimiter == '\t')

print("schema_obj.fields")
print(schema_obj.fields)

for f in schema_obj.list_all_files():
    print(f)
```

Result:
```
{ 'bucket': 'aardvark-prod-dca-data',
  'columns': [ 'unified_product_id:long',
               'unified_category_id:long',
               'product_id:long',
               'country_code:string',
               'genre_id:long',
               'device_code:string',
               'market_code:string',
               'monetization_score:double',
               'engagement_score:double',
               'acquisition_score:double',
               'sentiment_score:double'],
  'file_format': 'delta',
  'orig_table': 'oss/MPS_BIN_KPI_V2/version=${version}/range_type=${range_type}/date=${date}',
  'primary_key': [ 'product_id',
                   'unified_product_id',
                   'country_code',
                   'device_code',
                   'market_code',
                   'genre_id'],
  'schema_name': 'mps_bin_kpi_o',
  'schema_params': {},
  'table': 'oss/MPS_BIN_KPI_V2/version=${version}/range_type=${range_type}/date=${date}',
  'type': 's3'}
is_csv=False
schema_obj.fields
['unified_product_id', 'unified_category_id', 'product_id', 'country_code', 'genre_id', 'device_code', 'market_code', 'monetization_score', 'engagement_score', 'acquisition_score', 'sentiment_score']
aardvark-prod-dca-data/oss/MPS_BIN_KPI_V2/version=1.1.2/range_type=WEEK/date=2021-05-01/_SUCCESS
aardvark-prod-dca-data/oss/MPS_BIN_KPI_V2/version=1.1.2/range_type=WEEK/date=2021-05-01/part-00001-057675ec-4776-44fe-a04a-2e658f6b133d.c000.snappy.parquet

```
