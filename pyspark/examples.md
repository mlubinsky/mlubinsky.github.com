1. Customer Segmentation Analysis
Business Scenario
Retail companies need to segment customers based on purchasing behavior, demographics, and engagement patterns to create targeted marketing campaigns.

Production-Grade PySpark Script
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, datediff, current_date, sum as spark_sum, avg, count
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Customer Segmentation") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.databricks.delta.autoCompact.enabled", "true") \
    .getOrCreate()

# Load customer data
customers = spark.read.format("delta").load("/mnt/data/customers")
transactions = spark.read.format("delta").load("/mnt/data/transactions")

# Join datasets and calculate RFM metrics
rfm_data = transactions.groupBy("customer_id").agg(
    datediff(current_date(), max(col("transaction_date"))).alias("recency"),
    count("transaction_id").alias("frequency"),
    spark_sum("amount").alias("monetary")
)

# Join with customer demographics
customer_features = rfm_data.join(customers, "customer_id")

# Prepare features for clustering
feature_cols = ["recency", "frequency", "monetary", "age"]
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
data_with_features = assembler.transform(customer_features)

# Determine optimal number of clusters using Elbow method
wcss = []
for k in range(2, 11):
    kmeans = KMeans(k=k, seed=1)
    model = kmeans.fit(data_with_features)
    wcss.append(model.summary.trainingCost)

# Based on elbow method analysis, select optimal k
optimal_k = 4  # This would be determined programmatically in production

# Train final model
kmeans = KMeans(k=optimal_k, seed=1)
model = kmeans.fit(data_with_features)

# Add cluster predictions to data
clustered_customers = model.transform(data_with_features)

# Analyze cluster characteristics
cluster_analysis = clustered_customers.groupBy("prediction").agg(
    avg("recency").alias("avg_recency"),
    avg("frequency").alias("avg_frequency"),
    avg("monetary").alias("avg_monetary"),
    avg("age").alias("avg_age"),
    count("customer_id").alias("cluster_size")
)

# Save results to Delta table
clustered_customers.write.format("delta").mode("overwrite").save("/mnt/data/customer_segments")

# Display cluster analysis
display(cluster_analysis)
Explanation
This script implements RFM (Recency, Frequency, Monetary) analysis combined with K-means clustering to segment customers. It first calculates how recently customers purchased (recency), how often they purchase (frequency), and how much they spend (monetary value).

These metrics, along with demographic data, are used as features for K-means clustering. The script determines the optimal number of clusters using the Elbow method, then applies the final model to segment customers.

The results are saved to a Delta table for downstream marketing applications. This approach enables personalized marketing strategies based on customer behavior patterns.

2. Real-time Fraud Detection
Business Scenario
Financial institutions need to detect fraudulent transactions in real-time to prevent financial losses and protect customers.

Production-Grade PySpark Script
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, window, expr, when, count, avg, stddev
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml import Pipeline

# Initialize Spark Session with streaming configurations
spark = SparkSession.builder \
    .appName("Real-time Fraud Detection") \
    .config("spark.sql.streaming.checkpointLocation", "/mnt/checkpoints/fraud_detection") \
    .config("spark.sql.shuffle.partitions", "200") \
    .getOrCreate()

# Define schema for incoming transaction data
schema = StructType([
    StructField("transaction_id", StringType(), True),
    StructField("customer_id", StringType(), True),
    StructField("merchant", StringType(), True),
    StructField("category", StringType(), True),
    StructField("amount", DoubleType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("location", StringType(), True)
])

# Read streaming data from Kafka
transaction_stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "transactions") \
    .option("startingOffsets", "latest") \
    .load() \
    .select(expr("CAST(value AS STRING)")) \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Load historical transaction data for feature engineering
historical_transactions = spark.read.format("delta").load("/mnt/data/historical_transactions")

# Calculate customer behavior patterns from historical data
customer_patterns = historical_transactions.groupBy("customer_id").agg(
    avg("amount").alias("avg_amount"),
    stddev("amount").alias("stddev_amount"),
    count("transaction_id").alias("transaction_count")
)

# Join streaming data with customer patterns
enriched_stream = transaction_stream.join(
    customer_patterns,
    "customer_id",
    "left_outer"
)

# Feature engineering
enriched_stream = enriched_stream.withColumn(
    "amount_zscore",
    when(col("stddev_amount") > 0, (col("amount") - col("avg_amount")) / col("stddev_amount")).otherwise(0)
)

# Add time-based features
windowed_transactions = enriched_stream \
    .withWatermark("timestamp", "1 hour") \
    .groupBy(
        "customer_id",
        window("timestamp", "1 hour", "15 minutes")
    ) \
    .agg(
        count("transaction_id").alias("tx_count_1h"),
        sum("amount").alias("tx_amount_1h")
    )

# Join back to the main stream
final_stream = enriched_stream.join(
    windowed_transactions,
    (enriched_stream.customer_id == windowed_transactions.customer_id) &
    (enriched_stream.timestamp >= windowed_transactions.window.start) &
    (enriched_stream.timestamp <= windowed_transactions.window.end),
    "left_outer"
)

# Load pre-trained fraud detection model
from pyspark.ml.pipeline import PipelineModel
fraud_model = PipelineModel.load("/mnt/models/fraud_detection_model")

# Apply model to detect fraud
predictions = fraud_model.transform(final_stream)

# Filter fraudulent transactions
fraud_alerts = predictions.filter(col("prediction") == 1.0)

# Write fraud alerts to Delta table for immediate action
query = fraud_alerts.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/checkpoints/fraud_alerts") \
    .start("/mnt/data/fraud_alerts")

# Also send high-priority alerts to a Kafka topic
kafka_query = fraud_alerts \
    .select(to_json(struct("*")).alias("value")) \
    .writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("topic", "fraud_alerts") \
    .option("checkpointLocation", "/mnt/checkpoints/kafka_fraud_alerts") \
    .start()

# Wait for termination
spark.streams.awaitAnyTermination()
Explanation
This script implements a real-time fraud detection system using structured streaming in PySpark. It ingests transaction data from Kafka, enriches it with historical customer behavior patterns, and applies a pre-trained machine learning model to identify potentially fraudulent transactions.

The system calculates z-scores for transaction amounts to detect anomalies and uses time-windowed aggregations to identify unusual transaction patterns within short time periods. Detected fraud alerts are written to both a Delta table for investigation and a Kafka topic for immediate action by the security team.

The streaming job uses checkpointing for fault tolerance and watermarking to handle late-arriving data, making it robust for production environments.

3. Log File Processing and Analysis
Business Scenario
IT operations teams need to analyze application logs to identify errors, performance bottlenecks, and security issues across distributed systems.

Production-Grade PySpark Script
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_extract, window, count, when, expr, from_json
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, IntegerType

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Log Analysis") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.shuffle.partitions", "100") \
    .getOrCreate()

# Define log schema
log_schema = StructType([
    StructField("timestamp", TimestampType(), True),
    StructField("level", StringType(), True),
    StructField("service", StringType(), True),
    StructField("message", StringType(), True),
    StructField("host", StringType(), True),
    StructField("request_id", StringType(), True)
])

# Read logs from storage
logs = spark.read.format("json") \
    .schema(log_schema) \
    .load("/mnt/logs/application_logs/*.json")

# Clean and prepare data
cleaned_logs = logs.filter(col("timestamp").isNotNull()) \
    .withColumn("hour_of_day", hour(col("timestamp"))) \
    .withColumn("day_of_week", dayofweek(col("timestamp"))) \
    .withColumn("is_error", when(col("level").isin("ERROR", "FATAL"), 1).otherwise(0)) \
    .withColumn("is_warning", when(col("level") == "WARN", 1).otherwise(0))

# Extract error codes from messages
error_pattern = r"error code: (\d+)"
cleaned_logs = cleaned_logs.withColumn(
    "error_code",
    regexp_extract(col("message"), error_pattern, 1)
)

# Register as temp view for SQL analysis
cleaned_logs.createOrReplaceTempView("logs")

# Analyze error trends by service
error_by_service = spark.sql("""
    SELECT
        service,
        COUNT(*) as total_logs,
        SUM(is_error) as error_count,
        SUM(is_warning) as warning_count,
        ROUND(SUM(is_error) * 100.0 / COUNT(*), 2) as error_percentage
    FROM logs
    GROUP BY service
    ORDER BY error_percentage DESC
""")

# Analyze error patterns over time
error_trends = cleaned_logs \
    .groupBy(window("timestamp", "1 hour"), "service") \
    .agg(
        count("*").alias("total_logs"),
        sum("is_error").alias("error_count")
    ) \
    .withColumn("error_rate", col("error_count") / col("total_logs")) \
    .orderBy("window", "service")

# Identify common error patterns
common_errors = spark.sql("""
    SELECT
        error_code,
        COUNT(*) as occurrence_count,
        FIRST(message) as sample_message
    FROM logs
    WHERE error_code != ''
    GROUP BY error_code
    ORDER BY occurrence_count DESC
    LIMIT 10
""")

# Identify correlated errors across services
service_correlations = spark.sql("""
    SELECT
        a.service as service_a,
        b.service as service_b,
        COUNT(*) as correlation_count
    FROM logs a
    JOIN logs b
    ON a.request_id = b.request_id
    WHERE a.service != b.service
    AND a.is_error = 1 AND b.is_error = 1
    GROUP BY a.service, b.service
    ORDER BY correlation_count DESC
    LIMIT 20
""")

# Save results to Delta tables
error_by_service.write.format("delta").mode("overwrite").save("/mnt/analysis/error_by_service")
error_trends.write.format("delta").mode("overwrite").save("/mnt/analysis/error_trends")
common_errors.write.format("delta").mode("overwrite").save("/mnt/analysis/common_errors")
service_correlations.write.format("delta").mode("overwrite").save("/mnt/analysis/service_correlations")

# Create alerts for anomalous error rates
anomalies = error_trends \
    .filter(col("error_rate") > 0.05) \
    .orderBy(col("window").desc())

# Write anomalies to alerting system
anomalies.write.format("delta").mode("overwrite").save("/mnt/alerts/error_anomalies")
Explanation
This script processes application logs to identify patterns, errors, and anomalies across distributed systems. It first loads JSON-formatted logs, cleans the data, and extracts key information like error codes using regular expressions. The script then performs multiple analyses: error rates by service, error trends over time, common error patterns, and correlated errors across services that might indicate cascading failures.

It uses both DataFrame operations and SQL queries to demonstrate different approaches to log analysis. The results are saved to Delta tables for visualization and reporting. Finally, it identifies anomalous error rates that exceed a threshold (5% in this example) and writes them to an alerting system for immediate investigation. This comprehensive log analysis helps IT teams proactively identify and resolve issues before they impact users.

4. E-commerce Purchase Pattern Analysis
Business Scenario
E-commerce companies need to analyze customer purchase patterns to optimize inventory, improve product recommendations, and increase sales.

Production-Grade PySpark Script
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, split, count, sum as spark_sum, desc, datediff, current_date
from pyspark.sql.window import Window
from pyspark.ml.fpm import FPGrowth

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("E-commerce Purchase Pattern Analysis") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.shuffle.partitions", "200") \
    .getOrCreate()

# Load transaction data
transactions = spark.read.format("delta").load("/mnt/data/transactions")
products = spark.read.format("delta").load("/mnt/data/products")
customers = spark.read.format("delta").load("/mnt/data/customers")

# Join with product information
enriched_transactions = transactions.join(
    products,
    transactions.product_id == products.product_id
).join(
    customers,
    transactions.customer_id == customers.customer_id
)

# Calculate product sales metrics
product_metrics = enriched_transactions.groupBy("product_id", "product_name", "category").agg(
    count("transaction_id").alias("sales_count"),
    spark_sum("quantity").alias("units_sold"),
    spark_sum("price").alias("revenue")
).orderBy(desc("revenue"))

# Calculate category performance
category_metrics = enriched_transactions.groupBy("category").agg(
    count("transaction_id").alias("sales_count"),
    spark_sum("quantity").alias("units_sold"),
    spark_sum("price").alias("revenue")
).orderBy(desc("revenue"))

# Identify seasonal trends
enriched_transactions = enriched_transactions.withColumn(
    "month", month(col("transaction_date"))
)

seasonal_trends = enriched_transactions.groupBy("category", "month").agg(
    spark_sum("price").alias("revenue")
).orderBy("category", "month")

# Identify frequently purchased together products (market basket analysis)
# Prepare data for FP-Growth algorithm
basket_data = transactions.groupBy("order_id").agg(
    collect_list("product_id").alias("products")
)

# Convert product IDs to strings for FP-Growth
basket_data = basket_data.withColumn(
    "items",
    expr("transform(products, x -> cast(x as string))")
)

# Apply FP-Growth to find frequent itemsets
fpgrowth = FPGrowth(itemsCol="items", minSupport=0.01, minConfidence=0.5)
model = fpgrowth.fit(basket_data)

# Get frequent itemsets
frequent_itemsets = model.freqItemsets

# Get association rules
association_rules = model.associationRules

# Join with product names for better readability
def get_product_names(item_list):
    return [products.filter(col("product_id") == int(item)).select("product_name").first()[0]
            for item in item_list]

# Convert to Python to apply the function
frequent_itemsets_pd = frequent_itemsets.toPandas()
frequent_itemsets_pd["product_names"] = frequent_itemsets_pd["items"].apply(get_product_names)

# Convert back to Spark DataFrame
from pyspark.sql.types import ArrayType, StringType
spark.createDataFrame(frequent_itemsets_pd) \
    .write.format("delta").mode("overwrite").save("/mnt/analysis/frequent_itemsets")

# Calculate customer purchase patterns
customer_patterns = enriched_transactions.groupBy("customer_id").agg(
    count("transaction_id").alias("transaction_count"),
    countDistinct("product_id").alias("unique_products"),
    spark_sum("price").alias("total_spend"),
    avg("price").alias("avg_transaction_value"),
    datediff(current_date(), max("transaction_date")).alias("days_since_last_purchase")
)

# Identify high-value customers
windowSpec = Window.orderBy(desc("total_spend"))
high_value_customers = customer_patterns \
    .withColumn("spend_rank", rank().over(windowSpec)) \
    .filter(col("spend_rank") <= 100)

# Save results to Delta tables
product_metrics.write.format("delta").mode("overwrite").save("/mnt/analysis/product_metrics")
category_metrics.write.format("delta").mode("overwrite").save("/mnt/analysis/category_metrics")
seasonal_trends.write.format("delta").mode("overwrite").save("/mnt/analysis/seasonal_trends")
association_rules.write.format("delta").mode("overwrite").save("/mnt/analysis/association_rules")
customer_patterns.write.format("delta").mode("overwrite").save("/mnt/analysis/customer_patterns")
high_value_customers.write.format("delta").mode("overwrite").save("/mnt/analysis/high_value_customers")
Explanation
This script performs comprehensive e-commerce purchase pattern analysis to drive business decisions. It calculates product and category performance metrics, identifies seasonal trends, and performs market basket analysis using the FP-Growth algorithm to find products frequently purchased together.

The script also analyzes customer purchase patterns to identify high-value customers. The results are saved to Delta tables for use in inventory planning, product recommendations, and targeted marketing campaigns. The market basket analysis is particularly valuable for cross-selling opportunities, store layout optimization, and bundle promotions.

By understanding which products are frequently purchased together, e-commerce companies can increase average order value and improve customer satisfaction.

5. IoT Sensor Data Processing
Business Scenario
Manufacturing companies need to process and analyze data from thousands of IoT sensors to monitor equipment health, predict maintenance needs, and optimize production.

Production-Grade PySpark Script
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, window, avg, stddev, min, max, count, expr, when
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("IoT Sensor Data Processing") \
    .config("spark.sql.streaming.checkpointLocation", "/mnt/checkpoints/iot_processing") \
    .config("spark.sql.shuffle.partitions", "200") \
    .getOrCreate()

# Define schema for sensor data
sensor_schema = StructType([
    StructField("device_id", StringType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("temperature", DoubleType(), True),
    StructField("pressure", DoubleType(), True),
    StructField("humidity", DoubleType(), True),
    StructField("vibration", DoubleType(), True),
    StructField("machine_id", StringType(), True),
    StructField("facility_id", StringType(), True)
])

# Read streaming sensor data from Kafka
sensor_stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "sensor_data") \
    .option("startingOffsets", "latest") \
    .load() \
    .select(from_json(col("value").cast("string"), sensor_schema).alias("data")) \
    .select("data.*")

# Load machine metadata
machine_metadata = spark.read.format("delta").load("/mnt/data/machine_metadata")

# Join streaming data with machine metadata
enriched_stream = sensor_stream.join(
    machine_metadata,
    "machine_id",
    "left_outer"
)

# Calculate real-time statistics in 5-minute windows
windowed_stats = enriched_stream \
    .withWatermark("timestamp", "10 minutes") \
    .groupBy(
        "machine_id",
        window("timestamp", "5 minutes")
    ) \
    .agg(
        avg("temperature").alias("avg_temperature"),
        avg("pressure").alias("avg_pressure"),
        avg("humidity").alias("avg_humidity"),
        avg("vibration").alias("avg_vibration"),
        stddev("temperature").alias("stddev_temperature"),
        stddev("vibration").alias("stddev_vibration"),
        count("*").alias("reading_count")
    )

# Load normal operating thresholds
thresholds = spark.read.format("delta").load("/mnt/data/operating_thresholds")

# Join with thresholds to detect anomalies
anomaly_detection = windowed_stats.join(
    thresholds,
    "machine_id",
    "left_outer"
)

# Flag potential issues
anomaly_detection = anomaly_detection \
    .withColumn(
        "temperature_alert",
        when(
            (col("avg_temperature") > col("max_temperature_threshold")) |
            (col("avg_temperature") < col("min_temperature_threshold")),
            1
        ).otherwise(0)
    ) \
    .withColumn(
        "vibration_alert",
        when(
            col("avg_vibration") > col("max_vibration_threshold"),
            1
        ).otherwise(0)
    ) \
    .withColumn(
        "pressure_alert",
        when(
            (col("avg_pressure") > col("max_pressure_threshold")) |
            (col("avg_pressure") < col("min_pressure_threshold")),
            1
        ).otherwise(0)
    ) \
    .withColumn(
        "alert_level",
        when(
            (col("temperature_alert") + col("vibration_alert") + col("pressure_alert")) >= 2,
            "HIGH"
        ).when(
            (col("temperature_alert") + col("vibration_alert") + col("pressure_alert")) == 1,
            "MEDIUM"
        ).otherwise("NORMAL")
    )

# Write anomaly alerts to Delta table
anomaly_query = anomaly_detection \
    .filter(col("alert_level").isin("HIGH", "MEDIUM")) \
    .writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/checkpoints/anomaly_alerts") \
    .start("/mnt/data/anomaly_alerts")

# Aggregate data for long-term storage and analysis
daily_aggregates = enriched_stream \
    .withWatermark("timestamp", "1 day") \
    .groupBy(
        "machine_id",
        "facility_id",
        date_trunc("day", col("timestamp")).alias("date")
    ) \
    .agg(
        avg("temperature").alias("avg_temperature"),
        avg("pressure").alias("avg_pressure"),
        avg("humidity").alias("avg_humidity"),
        avg("vibration").alias("avg_vibration"),
        min("temperature").alias("min_temperature"),
        max("temperature").alias("max_temperature"),
        min("pressure").alias("min_pressure"),
        max("pressure").alias("max_pressure"),
        count("*").alias("reading_count")
    )

# Write daily aggregates to Delta table
daily_query = daily_aggregates \
    .writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/checkpoints/daily_aggregates") \
    .start("/mnt/data/daily_sensor_aggregates")

# Load historical data for predictive maintenance model
historical_data = spark.read.format("delta").load("/mnt/data/historical_sensor_data")
maintenance_events = spark.read.format("delta").load("/mnt/data/maintenance_events")

# Join historical sensor data with maintenance events
training_data = historical_data.join(
    maintenance_events,
    (historical_data.machine_id == maintenance_events.machine_id) &
    (historical_data.date <= maintenance_events.maintenance_date) &
    (historical_data.date >= date_sub(maintenance_events.maintenance_date, 30)),
    "inner"
)

# Feature engineering for predictive maintenance
training_data = training_data \
    .withColumn(
        "days_to_maintenance",
        datediff(col("maintenance_date"), col("date"))
    )

# Prepare features for model training
feature_cols = ["avg_temperature", "avg_pressure", "avg_humidity", "avg_vibration",
                "stddev_temperature", "stddev_vibration"]
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
training_data = assembler.transform(training_data)

# Train Random Forest model to predict days until maintenance needed
rf = RandomForestRegressor(featuresCol="features", labelCol="days_to_maintenance")
model = rf.fit(training_data)

# Save model for batch predictions
model.write().overwrite().save("/mnt/models/maintenance_prediction_model")

# Wait for termination
spark.streams.awaitAnyTermination()
Explanation
This script implements a comprehensive IoT sensor data processing pipeline for manufacturing equipment monitoring. It ingests streaming sensor data from Kafka, enriches it with machine metadata, and performs real-time anomaly detection by comparing sensor readings against predefined thresholds.

The system generates alerts for potential equipment issues based on multiple sensor readings, enabling proactive maintenance. The script also aggregates data for long-term storage and analysis, reducing storage costs while preserving valuable insights.

Additionally, it trains a predictive maintenance model using historical sensor data and maintenance events, which can predict when equipment is likely to need maintenance. This end-to-end solution helps manufacturing companies reduce downtime, optimize maintenance schedules, and extend equipment life.

6. Social Media Sentiment Analysis
Business Scenario
Marketing teams need to analyze social media mentions to understand brand perception, track campaign performance, and identify emerging issues.

Production-Grade PySpark Script
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf, explode, split, count, sum as spark_sum, when, window
from pyspark.sql.types import StringType, ArrayType, StructType, StructField, TimestampType
from pyspark.ml.feature import Tokenizer, StopWordsRemover, CountVectorizer, IDF
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline
from pyspark.ml.pipeline import PipelineModel

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Social Media Sentiment Analysis") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.shuffle.partitions", "100") \
    .getOrCreate()

# Define schema for social media posts
post_schema = StructType([
    StructField("post_id", StringType(), True),
    StructField("platform", StringType(), True),
    StructField("user_id", StringType(), True),
    StructField("text", StringType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("location", StringType(), True),
    StructField("followers_count", IntegerType(), True),
    StructField("hashtags", ArrayType(StringType()), True)
])

# Read streaming social media data from Kafka
social_stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "social_media_posts") \
    .option("startingOffsets", "latest") \
    .load() \
    .select(from_json(col("value").cast("string"), post_schema).alias("data")) \
    .select("data.*")

# Load pre-trained sentiment analysis model
sentiment_model = PipelineModel.load("/mnt/models/sentiment_model")

# Apply sentiment analysis to streaming data
posts_with_sentiment = sentiment_model.transform(social_stream)

# Extract sentiment score and label
posts_with_sentiment = posts_with_sentiment \
    .withColumn("sentiment_score", col("probability").getItem(1)) \
    .withColumn(
        "sentiment",
        when(col("prediction") == 0, "negative")
        .when(col("prediction") == 1, "positive")
        .otherwise("neutral")
    )

# Load brand and product keywords
brand_keywords = spark.read.format("delta").load("/mnt/data/brand_keywords")
product_keywords = spark.read.format("delta").load("/mnt/data/product_keywords")
campaign_keywords = spark.read.format("delta").load("/mnt/data/campaign_keywords")

# Broadcast the keywords for efficient joins
broadcast_brand_keywords = broadcast(brand_keywords)
broadcast_product_keywords = broadcast(product_keywords)
broadcast_campaign_keywords = broadcast(campaign_keywords)

# Create UDFs to check if text contains keywords
def contains_keywords(text, keywords_list):
    text_lower = text.lower()
    return any(keyword.lower() in text_lower for keyword in keywords_list)

contains_keywords_udf = udf(contains_keywords, BooleanType())

# Apply keyword matching
brand_keywords_list = [row.keyword for row in brand_keywords.collect()]
product_keywords_list = [row.keyword for row in product_keywords.collect()]
campaign_keywords_list = [row.keyword for row in campaign_keywords.collect()]

posts_with_sentiment = posts_with_sentiment \
    .withColumn(
        "mentions_brand",
        contains_keywords_udf(col("text"), array([lit(k) for k in brand_keywords_list]))
    ) \
    .withColumn(
        "mentions_product",
        contains_keywords_udf(col("text"), array([lit(k) for k in product_keywords_list]))
    ) \
    .withColumn(
        "mentions_campaign",
        contains_keywords_udf(col("text"), array([lit(k) for k in campaign_keywords_list]))
    )

# Calculate engagement potential based on follower count
posts_with_sentiment = posts_with_sentiment \
    .withColumn(
        "engagement_potential",
        when(col("followers_count") > 10000, "high")
        .when(col("followers_count") > 1000, "medium")
        .otherwise("low")
    )

# Process hashtags
exploded_hashtags = posts_with_sentiment \
    .withColumn("hashtag", explode(col("hashtags")))

# Analyze sentiment by hashtag
hashtag_sentiment = exploded_hashtags \
    .groupBy("hashtag") \
    .agg(
        count("*").alias("mentions"),
        avg("sentiment_score").alias("avg_sentiment"),
        sum(when(col("sentiment") == "positive", 1).otherwise(0)).alias("positive_count"),
        sum(when(col("sentiment") == "negative", 1).otherwise(0)).alias("negative_count")
    ) \
    .withColumn(
        "sentiment_ratio",
        col("positive_count") / (col("positive_count") + col("negative_count"))
    )

# Analyze sentiment trends over time
sentiment_trends = posts_with_sentiment \
    .withWatermark("timestamp", "1 hour") \
    .groupBy(
        window("timestamp", "15 minutes"),
        "sentiment"
    ) \
    .count()

# Analyze brand mentions
brand_mentions = posts_with_sentiment \
    .filter(col("mentions_brand") == True) \
    .groupBy("platform") \
    .agg(
        count("*").alias("mention_count"),
        avg("sentiment_score").alias("avg_sentiment")
    )

# Identify influential posts (high engagement potential and strong sentiment)
influential_posts = posts_with_sentiment \
    .filter(
        (col("engagement_potential") == "high") &
        ((col("sentiment_score") > 0.8) | (col("sentiment_score") < 0.2))
    ) \
    .select("post_id", "platform", "user_id", "text", "timestamp", "sentiment", "sentiment_score", "followers_count")

# Write results to Delta tables
query1 = hashtag_sentiment \
    .writeStream \
    .format("delta") \
    .outputMode("complete") \
    .option("checkpointLocation", "/mnt/checkpoints/hashtag_sentiment") \
    .start("/mnt/analysis/hashtag_sentiment")

query2 = sentiment_trends \
    .writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/checkpoints/sentiment_trends") \
    .start("/mnt/analysis/sentiment_trends")

query3 = brand_mentions \
    .writeStream \
    .format("delta") \
    .outputMode("complete") \
    .option("checkpointLocation", "/mnt/checkpoints/brand_mentions") \
    .start("/mnt/analysis/brand_mentions")

query4 = influential_posts \
    .writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/checkpoints/influential_posts") \
    .start("/mnt/analysis/influential_posts")

# Wait for termination
spark.streams.awaitAnyTermination()
Explanation
This script implements a real-time social media sentiment analysis pipeline for brand monitoring. It ingests streaming social media posts from Kafka and applies a pre-trained sentiment analysis model to classify posts as positive, negative, or neutral.

The system identifies mentions of brands, products, and campaigns using keyword matching, and calculates engagement potential based on follower count. It analyzes sentiment by hashtag, tracks sentiment trends over time, and monitors brand mentions across platforms.

The script also identifies influential posts with high engagement potential and strong sentiment, which may require immediate attention from the marketing team. The results are written to Delta tables for real-time dashboards and alerts. This comprehensive social media monitoring solution helps marketing teams understand brand perception, track campaign performance, and quickly respond to emerging issues or opportunities.

7. Supply Chain Optimization
Business Scenario
Retail and manufacturing companies need to optimize their supply chain by analyzing inventory levels, demand patterns, and supplier performance.

Production-Grade PySpark Scrip
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, datediff, current_date, lag, avg, stddev, sum as spark_sum, when, rank
from pyspark.sql.window import Window
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Supply Chain Optimization") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.shuffle.partitions", "200") \
    .getOrCreate()

# Load datasets
inventory = spark.read.format("delta").load("/mnt/data/inventory")
orders = spark.read.format("delta").load("/mnt/data/orders")
shipments = spark.read.format("delta").load("/mnt/data/shipments")
products = spark.read.format("delta").load("/mnt/data/products")
suppliers = spark.read.format("delta").load("/mnt/data/suppliers")

# Calculate inventory metrics
inventory_metrics = inventory \
    .groupBy("product_id", "warehouse_id") \
    .agg(
        sum("quantity").alias("current_stock"),
        sum(when(col("status") == "reserved", col("quantity")).otherwise(0)).alias("reserved_stock"),
        sum(when(col("status") == "available", col("quantity")).otherwise(0)).alias("available_stock")
    )

# Join with product information
inventory_metrics = inventory_metrics.join(
    products,
    "product_id"
)

# Calculate days of supply
daily_sales_avg = orders \
    .filter(col("order_date") >= date_sub(current_date(), 90)) \
    .groupBy("product_id") \
    .agg(
        avg(col("quantity")).alias("avg_daily_sales"),
        stddev(col("quantity")).alias("stddev_daily_sales")
    )

inventory_analysis = inventory_metrics.join(
    daily_sales_avg,
    "product_id",
    "left_outer"
)

inventory_analysis = inventory_analysis \
    .withColumn(
        "days_of_supply",
        when(
            col("avg_daily_sales") > 0,
            col("available_stock") / col("avg_daily_sales")
        ).otherwise(null)
    ) \
    .withColumn(
        "safety_stock",
        col("avg_daily_sales") * 2 + (1.96 * col("stddev_daily_sales") * sqrt(col("lead_time")))
    ) \
    .withColumn(
        "reorder_point",
        col("safety_stock") + (col("avg_daily_sales") * col("lead_time"))
    ) \
    .withColumn(
        "inventory_status",
        when(col("available_stock") <= col("reorder_point"), "REORDER")
        .when(col("available_stock") <= col("safety_stock"), "CRITICAL")
        .when(col("days_of_supply") > 90, "OVERSTOCKED")
        .otherwise("OPTIMAL")
    )

# Analyze supplier performance
supplier_performance = shipments \
    .join(suppliers, "supplier_id") \
    .groupBy("supplier_id", "supplier_name") \
    .agg(
        avg(datediff(col("delivery_date"), col("expected_delivery_date"))).alias("avg_delivery_delay"),
        avg(when(col("delivery_date") <= col("expected_delivery_date"), 1).otherwise(0)).alias("on_time_delivery_rate"),
        avg(col("quality_rating")).alias("avg_quality_rating"),
        count("*").alias("total_shipments")
    )

# Rank suppliers by performance
supplier_window = Window.partitionBy("product_category").orderBy(
    col("on_time_delivery_rate").desc(),
    col("avg_quality_rating").desc(),
    col("avg_delivery_delay")
)

supplier_rankings = supplier_performance \
    .join(
        shipments.join(products, "product_id").select("supplier_id", "product_category").distinct(),
        "supplier_id"
    ) \
    .withColumn("rank", rank().over(supplier_window))

# Analyze demand patterns
order_history = orders \
    .join(products, "product_id") \
    .groupBy("product_id", "product_name", "year(order_date)", "month(order_date)") \
    .agg(
        sum("quantity").alias("monthly_demand"),
        count("order_id").alias("order_count")
    )

# Calculate month-over-month growth
window_spec = Window.partitionBy("product_id").orderBy("year", "month")
demand_trends = order_history \
    .withColumn("prev_month_demand", lag("monthly_demand", 1).over(window_spec)) \
    .withColumn(
        "mom_growth",
        when(
            col("prev_month_demand").isNotNull() & (col("prev_month_demand") > 0),
            (col("monthly_demand") - col("prev_month_demand")) / col("prev_month_demand")
        ).otherwise(null)
    )

# Prepare data for demand forecasting
forecast_data = order_history \
    .withColumn("date", make_date(col("year"), col("month"), lit(1)))

# Feature engineering for forecasting
forecast_data = forecast_data \
    .withColumn("month_of_year", month(col("date"))) \
    .withColumn("quarter", quarter(col("date")))

# Add lag features
for i in range(1, 13):
    forecast_data = forecast_data \
        .withColumn(f"demand_lag_{i}", lag("monthly_demand", i).over(window_spec))

# Prepare features for model training
feature_cols = ["month_of_year", "quarter"] + [f"demand_lag_{i}" for i in range(1, 13)]
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
forecast_data = assembler.transform(forecast_data.na.fill(0))

# Train Random Forest model for demand forecasting
rf = RandomForestRegressor(featuresCol="features", labelCol="monthly_demand")
model = rf.fit(forecast_data.filter(col("year") < year(current_date())))

# Make predictions for future months
future_months = forecast_data \
    .filter(col("date") <= add_months(current_date(), 6)) \
    .filter(col("date") >= current_date())

predictions = model.transform(future_months)
demand_forecast = predictions.select(
    "product_id",
    "product_name",
    "date",
    "prediction"
)

# Save results to Delta tables
inventory_analysis.write.format("delta").mode("overwrite").save("/mnt/analysis/inventory_analysis")
supplier_performance.write.format("delta").mode("overwrite").save("/mnt/analysis/supplier_performance")
supplier_rankings.write.format("delta").mode("overwrite").save("/mnt/analysis/supplier_rankings")
demand_trends.write.format("delta").mode("overwrite").save("/mnt/analysis/demand_trends")
demand_forecast.write.format("delta").mode("overwrite").save("/mnt/analysis/demand_forecast")

# Generate reorder recommendations
reorder_recommendations = inventory_analysis \
    .filter(col("inventory_status").isin("REORDER", "CRITICAL")) \
    .join(
        supplier_rankings.filter(col("rank") == 1),
        ["product_category"],
        "left_outer"
    ) \
    .select(
        "product_id",
        "product_name",
        "warehouse_id",
        "current_stock",
        "available_stock",
        "reorder_point",
        "safety_stock",
        "avg_daily_sales",
        "supplier_id",
        "supplier_name"
    ) \
    .withColumn(
        "recommended_order_quantity",
        (col("reorder_point") * 2) - col("available_stock")
    )

reorder_recommendations.write.format("delta").mode("overwrite").save("/mnt/recommendations/reorder_recommendations")
Explanation
This script implements a comprehensive supply chain optimization solution for retail and manufacturing companies. It analyzes inventory levels across warehouses, calculates key metrics like days of supply and reorder points, and identifies products that need replenishment. The system evaluates supplier performance based on delivery timeliness, quality ratings, and other factors, then ranks suppliers by product category to identify the best options for each product type.

It also analyzes historical demand patterns, calculates month-over-month growth, and uses machine learning to forecast future demand for the next six months. The script generates specific reorder recommendations, including the recommended order quantity and preferred supplier for each product that needs replenishment.

This end-to-end solution helps companies optimize inventory levels, reduce stockouts, improve supplier relationships, and ultimately enhance customer satisfaction while minimizing costs.

8. Healthcare Patient Data Analysis
Business Scenario
Healthcare providers need to analyze patient data to identify high-risk patients, optimize treatment plans, and improve outcomes while reducing costs.

Production-Grade PySpark Script
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, datediff, current_date, when, sum as spark_sum, avg, count, explode
from pyspark.sql.window import Window
from pyspark.ml.feature import VectorAssembler, StringIndexer, OneHotEncoder
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml import Pipeline

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Healthcare Patient Data Analysis") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.shuffle.partitions", "100") \
    .getOrCreate()

# Load datasets with appropriate security measures
patients = spark.read.format("delta").load("/mnt/data/patients")
visits = spark.read.format("delta").load("/mnt/data/visits")
diagnoses = spark.read.format("delta").load("/mnt/data/diagnoses")
medications = spark.read.format("delta").load("/mnt/data/medications")
labs = spark.read.format("delta").load("/mnt/data/lab_results")
procedures = spark.read.format("delta").load("/mnt/data/procedures")

# Calculate patient demographics
patient_demographics = patients.groupBy("gender", "age_group", "zip_code").count()

# Analyze diagnosis patterns
diagnosis_patterns = diagnoses \
    .groupBy("diagnosis_code", "diagnosis_description") \
    .agg(
        count("patient_id").alias("patient_count"),
        countDistinct("patient_id").alias("unique_patients")
    ) \
    .orderBy(col("patient_count").desc())

# Identify comorbidities
patient_diagnoses = diagnoses \
    .groupBy("patient_id") \
    .agg(
        collect_set("diagnosis_code").alias("diagnoses")
    )

# Explode diagnoses to find co-occurring conditions
diagnosis_pairs = patient_diagnoses \
    .select(
        "patient_id",
        explode("diagnoses").alias("diagnosis_1")
    ) \
    .join(
        patient_diagnoses.select(
            "patient_id",
            explode("diagnoses").alias("diagnosis_2")
        ),
        "patient_id"
    ) \
    .filter(col("diagnosis_1") < col("diagnosis_2"))  # Avoid duplicates

comorbidities = diagnosis_pairs \
    .groupBy("diagnosis_1", "diagnosis_2") \
    .agg(
        count("patient_id").alias("co_occurrence_count")
    ) \
    .orderBy(col("co_occurrence_count").desc())

# Join with diagnosis descriptions
comorbidities = comorbidities \
    .join(
        diagnoses.select("diagnosis_code", "diagnosis_description").distinct(),
        col("diagnosis_1") == col("diagnosis_code"),
        "left_outer"
    ) \
    .withColumnRenamed("diagnosis_description", "description_1") \
    .join(
        diagnoses.select("diagnosis_code", "diagnosis_description").distinct(),
        col("diagnosis_2") == col("diagnosis_code"),
        "left_outer"
    ) \
    .withColumnRenamed("diagnosis_description", "description_2") \
    .select(
        "diagnosis_1", "description_1",
        "diagnosis_2", "description_2",
        "co_occurrence_count"
    )

# Calculate readmission rates
readmissions = visits \
    .filter(col("visit_type") == "inpatient") \
    .withColumn(
        "discharge_date",
        col("admission_date") + col("length_of_stay")
    ) \
    .withColumn(
        "next_admission",
        lead("admission_date").over(Window.partitionBy("patient_id").orderBy("admission_date"))
    ) \
    .withColumn(
        "days_to_readmission",
        datediff(col("next_admission"), col("discharge_date"))
    ) \
    .withColumn(
        "is_readmission",
        when(col("days_to_readmission") <= 30, 1).otherwise(0)
    )

readmission_rates = readmissions \
    .groupBy("department") \
    .agg(
        count("*").alias("total_discharges"),
        sum(col("is_readmission")).alias("readmissions"),
        (sum(col("is_readmission")) / count("*")).alias("readmission_rate")
    ) \
    .orderBy(col("readmission_rate").desc())

# Analyze medication patterns
medication_patterns = medications \
    .groupBy("medication_code", "medication_name") \
    .agg(
        count("patient_id").alias("prescription_count"),
        countDistinct("patient_id").alias("unique_patients")
    ) \
    .orderBy(col("prescription_count").desc())

# Identify potential medication interactions
patient_medications = medications \
    .groupBy("patient_id") \
    .agg(
        collect_set("medication_code").alias("medications")
    )

medication_pairs = patient_medications \
    .select(
        "patient_id",
        explode("medications").alias("medication_1")
    ) \
    .join(
        patient_medications.select(
            "patient_id",
            explode("medications").alias("medication_2")
        ),
        "patient_id"
    ) \
    .filter(col("medication_1") < col("medication_2"))  # Avoid duplicates

medication_interactions = medication_pairs \
    .groupBy("medication_1", "medication_2") \
    .agg(
        count("patient_id").alias("co_prescription_count")
    ) \
    .orderBy(col("co_prescription_count").desc())

# Join with medication names
medication_interactions = medication_interactions \
    .join(
        medications.select("medication_code", "medication_name").distinct(),
        col("medication_1") == col("medication_code"),
        "left_outer"
    ) \
    .withColumnRenamed("medication_name", "name_1") \
    .join(
        medications.select("medication_code", "medication_name").distinct(),
        col("medication_2") == col("medication_code"),
        "left_outer"
    ) \
    .withColumnRenamed("medication_name", "name_2") \
    .select(
        "medication_1", "name_1",
        "medication_2", "name_2",
        "co_prescription_count"
    )

# Prepare data for readmission risk prediction
# Join patient data with visits, diagnoses, and medications
patient_features = patients \
    .join(
        visits.filter(col("visit_type") == "inpatient"),
        "patient_id"
    ) \
    .join(
        diagnoses,
        diagnoses.visit_id == visits.visit_id,
        "left_outer"
    ) \
    .join(
        medications,
        medications.visit_id == visits.visit_id,
        "left_outer"
    ) \
    .join(
        labs,
        labs.visit_id == visits.visit_id,
        "left_outer"
    )

# Feature engineering
patient_features = patient_features \
    .withColumn("age", floor(datediff(current_date(), col("birth_date")) / 365.25)) \
    .withColumn("has_diabetes", when(array_contains(col("diagnoses"), "E11"), 1).otherwise(0)) \
    .withColumn("has_hypertension", when(array_contains(col("diagnoses"), "I10"), 1).otherwise(0)) \
    .withColumn("has_heart_failure", when(array_contains(col("diagnoses"), "I50"), 1).otherwise(0)) \
    .withColumn("abnormal_lab_count", size(filter(col("lab_results"), lambda x: x.result_flag == "abnormal"))) \
    .withColumn("medication_count", size(col("medications"))) \
    .withColumn("previous_admissions", count("visit_id").over(Window.partitionBy("patient_id").orderBy("admission_date")))

# Prepare features for model training
categorical_cols = ["gender", "insurance_type", "marital_status"]
numeric_cols = ["age", "has_diabetes", "has_hypertension", "has_heart_failure",
                "abnormal_lab_count", "medication_count", "previous_admissions", "length_of_stay"]

# Create pipeline for preprocessing
indexers = [StringIndexer(inputCol=col, outputCol=col+"_index") for col in categorical_cols]
encoders = [OneHotEncoder(inputCol=col+"_index", outputCol=col+"_encoded") for col in categorical_cols]
encoded_cols = [col+"_encoded" for col in categorical_cols]
assembler = VectorAssembler(inputCols=numeric_cols + encoded_cols, outputCol="features")

# Create and train the model
rf = RandomForestClassifier(labelCol="is_readmission", featuresCol="features")
pipeline = Pipeline(stages=indexers + encoders + [assembler, rf])
model = pipeline.fit(patient_features)

# Make predictions
predictions = model.transform(patient_features)

# Evaluate model
evaluator = BinaryClassificationEvaluator(labelCol="is_readmission")
auc = evaluator.evaluate(predictions)
print(f"AUC: {auc}")

# Identify high-risk patients
high_risk_patients = predictions \
    .filter(col("probability").getItem(1) > 0.7) \
    .select(
        "patient_id",
        "patient_name",
        "age",
        "gender",
        "probability",
        "has_diabetes",
        "has_hypertension",
        "has_heart_failure",
        "abnormal_lab_count",
        "medication_count",
        "previous_admissions"
    )

# Save results to Delta tables
patient_demographics.write.format("delta").mode("overwrite").save("/mnt/analysis/patient_demographics")
diagnosis_patterns.write.format("delta").mode("overwrite").save("/mnt/analysis/diagnosis_patterns")
comorbidities.write.format("delta").mode("overwrite").save("/mnt/analysis/comorbidities")
readmission_rates.write.format("delta").mode("overwrite").save("/mnt/analysis/readmission_rates")
medication_patterns.write.format("delta").mode("overwrite").save("/mnt/analysis/medication_patterns")
medication_interactions.write.format("delta").mode("overwrite").save("/mnt/analysis/medication_interactions")
high_risk_patients.write.format("delta").mode("overwrite").save("/mnt/analysis/high_risk_patients")

# Save model for future predictions
model.write().overwrite().save("/mnt/models/readmission_risk_model")
Explanation
This script implements a comprehensive healthcare patient data analysis solution that helps providers identify high-risk patients and improve outcomes. It analyzes patient demographics, diagnosis patterns, and comorbidities to understand the patient population.

The system calculates readmission rates by department to identify areas for improvement and analyzes medication patterns and potential interactions to optimize treatment plans. The script also builds a machine learning model to predict readmission risk based on patient characteristics, diagnoses, medications, and lab results. It identifies high-risk patients who may benefit from additional interventions, enabling proactive care management.

The results are saved to Delta tables for integration with clinical decision support systems and population health management tools. This solution helps healthcare providers reduce readmissions, improve patient outcomes, and optimize resource allocation while maintaining patient privacy and data security.

9. Financial Transaction Processing
Business Scenario
Financial institutions need to process and analyze millions of transactions daily to detect fraud, ensure compliance, and provide insights to customers.

Production-Grade PySpark Script
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, window, count, sum as spark_sum, avg, stddev, when, expr, from_json
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType, IntegerType
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.clustering import KMeans
from pyspark.ml import Pipeline

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Financial Transaction Processing") \
    .config("spark.sql.streaming.checkpointLocation", "/mnt/checkpoints/transaction_processing") \
    .config("spark.sql.shuffle.partitions", "200") \
    .getOrCreate()

# Define schema for transaction data
transaction_schema = StructType([
    StructField("transaction_id", StringType(), True),
    StructField("account_id", StringType(), True),
    StructField("transaction_type", StringType(), True),
    StructField("amount", DoubleType(), True),
    StructField("currency", StringType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("merchant_id", StringType(), True),
    StructField("merchant_category", StringType(), True),
    StructField("location", StringType(), True),
    StructField("device_id", StringType(), True)
])

# Read streaming transaction data from Kafka
transaction_stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "financial_transactions") \
    .option("startingOffsets", "latest") \
    .load() \
    .select(from_json(col("value").cast("string"), transaction_schema).alias("data")) \
    .select("data.*")

# Load account information
accounts = spark.read.format("delta").load("/mnt/data/accounts")
exchange_rates = spark.read.format("delta").load("/mnt/data/exchange_rates")

# Join streaming data with account information
enriched_stream = transaction_stream.join(
    accounts,
    "account_id",
    "left_outer"
)

# Convert all amounts to USD for consistent analysis
enriched_stream = enriched_stream.join(
    exchange_rates,
    enriched_stream.currency == exchange_rates.currency_code,
    "left_outer"
) \
.withColumn(
    "amount_usd",
    col("amount") * col("usd_rate")
)

# Calculate real-time account balances
account_balances = enriched_stream \
    .withColumn(
        "amount_change",
        when(col("transaction_type").isin("deposit", "credit", "refund"), col("amount_usd"))
        .when(col("transaction_type").isin("withdrawal", "debit", "payment"), -col("amount_usd"))
        .otherwise(0)
    ) \
    .withWatermark("timestamp", "10 minutes") \
    .groupBy("account_id") \
    .agg(
        sum("amount_change").alias("balance_change"),
        max("timestamp").alias("last_transaction_time")
    )

# Join with account information to get starting balance
current_balances = account_balances.join(
    accounts.select("account_id", "starting_balance"),
    "account_id",
    "left_outer"
) \
.withColumn(
    "current_balance",
    col("starting_balance") + col("balance_change")
)

# Write current balances to Delta table
balance_query = current_balances \
    .writeStream \
    .format("delta") \
    .outputMode("complete") \
    .option("checkpointLocation", "/mnt/checkpoints/account_balances") \
    .start("/mnt/data/current_account_balances")

# Calculate spending patterns by category
spending_by_category = enriched_stream \
    .filter(col("transaction_type").isin("debit", "payment")) \
    .withWatermark("timestamp", "1 day") \
    .groupBy(
        "account_id",
        "merchant_category",
        window("timestamp", "1 day")
    ) \
    .agg(
        sum("amount_usd").alias("daily_spend"),
        count("transaction_id").alias("transaction_count")
    )

# Write spending patterns to Delta table
spending_query = spending_by_category \
    .writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/checkpoints/spending_patterns") \
    .start("/mnt/data/spending_patterns")

# Detect anomalous transactions using historical patterns
# Load historical transaction statistics
historical_stats = spark.read.format("delta").load("/mnt/data/historical_transaction_stats")

# Join streaming data with historical statistics
anomaly_detection = enriched_stream.join(
    historical_stats,
    ["account_id", "merchant_category"],
    "left_outer"
)

# Flag potentially fraudulent transactions
anomaly_detection = anomaly_detection \
    .withColumn(
        "amount_zscore",
        when(
            col("stddev_amount") > 0,
            (col("amount_usd") - col("avg_amount")) / col("stddev_amount")
        ).otherwise(0)
    ) \
    .withColumn(
        "is_anomalous",
        when(
            col("amount_zscore") > 3 |  # Amount is 3 standard deviations above average
            (col("location") != col("usual_location")) |  # Unusual location
            (col("transaction_count_1d") > col("avg_daily_transactions") * 2),  # Unusual frequency
            1
        ).otherwise(0)
    )

# Write anomalous transactions to Delta table for investigation
anomaly_query = anomaly_detection \
    .filter(col("is_anomalous") == 1) \
    .writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/checkpoints/anomalous_transactions") \
    .start("/mnt/data/anomalous_transactions")

# Generate customer insights
# Calculate monthly spending summaries
monthly_summaries = enriched_stream \
    .filter(col("transaction_type").isin("debit", "payment")) \
    .withColumn("year_month", date_format(col("timestamp"), "yyyy-MM")) \
    .groupBy("account_id", "year_month") \
    .agg(
        sum("amount_usd").alias("total_spend"),
        count("transaction_id").alias("transaction_count"),
        countDistinct("merchant_id").alias("unique_merchants"),
        countDistinct("merchant_category").alias("unique_categories")
    )

# Calculate top spending categories
top_categories = enriched_stream \
    .filter(col("transaction_type").isin("debit", "payment")) \
    .withColumn("year_month", date_format(col("timestamp"), "yyyy-MM")) \
    .groupBy("account_id", "year_month", "merchant_category") \
    .agg(
        sum("amount_usd").alias("category_spend")
    ) \
    .withColumn(
        "rank",
        rank().over(Window.partitionBy("account_id", "year_month").orderBy(desc("category_spend")))
    ) \
    .filter(col("rank") <= 3)

# Write customer insights to Delta tables
monthly_query = monthly_summaries \
    .writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/checkpoints/monthly_summaries") \
    .start("/mnt/data/monthly_spending_summaries")

category_query = top_categories \
    .writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/checkpoints/top_categories") \
    .start("/mnt/data/top_spending_categories")

# Wait for termination
spark.streams.awaitAnyTermination()
Explanation
This script implements a comprehensive financial transaction processing system that handles millions of transactions in real-time. It ingests transaction data from Kafka, enriches it with account information, and converts all amounts to USD for consistent analysis.

The system calculates real-time account balances, tracks spending patterns by category, and detects anomalous transactions that may indicate fraud. It also generates customer insights, including monthly spending summaries and top spending categories, which can be used for personalized financial advice and marketing. The results are written to Delta tables for integration with banking applications, fraud investigation systems, and customer-facing dashboards.

The streaming architecture ensures that transactions are processed as they occur, enabling real-time fraud detection and up-to-date account information. This solution helps financial institutions improve security, enhance customer experience, and gain valuable insights from transaction data.

10. Website User Behavior Analysis
Business Scenario
E-commerce and content websites need to analyze user behavior to optimize the user experience, increase conversions, and personalize content.

Production-Grade PySpark Script
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, split, count, sum as spark_sum, avg, when, window, expr, from_json
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, IntegerType, ArrayType
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans
from pyspark.ml import Pipeline

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Website User Behavior Analysis") \
    .config("spark.sql.streaming.checkpointLocation", "/mnt/checkpoints/user_behavior") \
    .config("spark.sql.shuffle.partitions", "100") \
    .getOrCreate()

# Define schema for clickstream data
clickstream_schema = StructType([
    StructField("session_id", StringType(), True),
    StructField("user_id", StringType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("page_url", StringType(), True),
    StructField("referrer_url", StringType(), True),
    StructField("action", StringType(), True),
    StructField("product_id", StringType(), True),
    StructField("category_id", StringType(), True),
    StructField("time_spent", IntegerType(), True),
    StructField("device_type", StringType(), True),
    StructField("browser", StringType(), True),
    StructField("location", StringType(), True)
])

# Read streaming clickstream data from Kafka
clickstream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "website_clickstream") \
    .option("startingOffsets", "latest") \
    .load() \
    .select(from_json(col("value").cast("string"), clickstream_schema).alias("data")) \
    .select("data.*")

# Load product and user information
products = spark.read.format("delta").load("/mnt/data/products")
users = spark.read.format("delta").load("/mnt/data/users")

# Join with product and user information
enriched_clickstream = clickstream \
    .join(
        products,
        clickstream.product_id == products.product_id,
        "left_outer"
    ) \
    .join(
        users,
        clickstream.user_id == users.user_id,
        "left_outer"
    )

# Analyze page views and engagement
page_analytics = enriched_clickstream \
    .withWatermark("timestamp", "1 hour") \
    .groupBy(
        "page_url",
        window("timestamp", "15 minutes")
    ) \
    .agg(
        count("*").alias("page_views"),
        avg("time_spent").alias("avg_time_spent"),
        countDistinct("session_id").alias("unique_sessions"),
        countDistinct("user_id").alias("unique_users")
    )

# Write page analytics to Delta table
page_query = page_analytics \
    .writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/checkpoints/page_analytics") \
    .start("/mnt/data/page_analytics")

# Analyze user journeys
session_paths = enriched_clickstream \
    .withWatermark("timestamp", "2 hours") \
    .groupBy("session_id") \
    .agg(
        collect_list(
            struct(
                "timestamp",
                "page_url",
                "action"
            )
        ).alias("journey_steps"),
        min("timestamp").alias("session_start"),
        max("timestamp").alias("session_end"),
        first("user_id").alias("user_id"),
        first("device_type").alias("device_type"),
        first("browser").alias("browser"),
        first("location").alias("location")
    ) \
    .withColumn(
        "session_duration_minutes",
        (unix_timestamp("session_end") - unix_timestamp("session_start")) / 60
    )

# Write session paths to Delta table
session_query = session_paths \
    .writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/checkpoints/session_paths") \
    .start("/mnt/data/session_paths")

# Analyze conversion funnel
funnel_stages = enriched_clickstream \
    .withColumn(
        "funnel_stage",
        when(col("action") == "view_product", "product_view")
        .when(col("action") == "add_to_cart", "add_to_cart")
        .when(col("action") == "view_cart", "cart_view")
        .when(col("action") == "checkout", "checkout")
        .when(col("action") == "purchase", "purchase")
        .otherwise(null)
    ) \
    .filter(col("funnel_stage").isNotNull())

funnel_analysis = funnel_stages \
    .withWatermark("timestamp", "1 hour") \
    .groupBy(
        "session_id",
        "funnel_stage",
        window("timestamp", "1 hour")
    ) \
    .agg(
        count("*").alias("stage_count"),
        min("timestamp").alias("first_occurrence")
    ) \
    .groupBy(
        "window",
        "funnel_stage"
    ) \
    .agg(
        countDistinct("session_id").alias("unique_sessions")
    ) \
    .orderBy("window", "funnel_stage")

# Write funnel analysis to Delta table
funnel_query = funnel_analysis \
    .writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/checkpoints/funnel_analysis") \
    .start("/mnt/data/funnel_analysis")

# Analyze product interactions
product_interactions = enriched_clickstream \
    .filter(col("product_id").isNotNull()) \
    .withWatermark("timestamp", "1 hour") \
    .groupBy(
        "product_id",
        "product_name",
        "category_name",
        window("timestamp", "1 hour")
    ) \
    .agg(
        count(when(col("action") == "view_product", 1)).alias("views"),
        count(when(col("action") == "add_to_cart", 1)).alias("add_to_carts"),
        count(when(col("action") == "purchase", 1)).alias("purchases"),
        countDistinct("session_id").alias("unique_sessions")
    ) \
    .withColumn(
        "cart_rate",
        when(col("views") > 0, col("add_to_carts") / col("views")).otherwise(0)
    ) \
    .withColumn(
        "conversion_rate",
        when(col("views") > 0, col("purchases") / col("views")).otherwise(0)
    )

# Write product interactions to Delta table
product_query = product_interactions \
    .writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/checkpoints/product_interactions") \
    .start("/mnt/data/product_interactions")

# Identify user segments based on behavior
# Prepare data for clustering
user_behavior = enriched_clickstream \
    .withWatermark("timestamp", "1 day") \
    .groupBy("user_id") \
    .agg(
        count("*").alias("total_events"),
        countDistinct("session_id").alias("session_count"),
        countDistinct("page_url").alias("unique_pages_visited"),
        avg("time_spent").alias("avg_time_spent"),
        count(when(col("action") == "view_product", 1)).alias("product_views"),
        count(when(col("action") == "add_to_cart", 1)).alias("add_to_carts"),
        count(when(col("action") == "purchase", 1)).alias("purchases"),
        sum(when(col("action") == "purchase", col("price")).otherwise(0)).alias("total_spend")
    ) \
    .withColumn(
        "cart_rate",
        when(col("product_views") > 0, col("add_to_carts") / col("product_views")).otherwise(0)
    ) \
    .withColumn(
        "conversion_rate",
        when(col("product_views") > 0, col("purchases") / col("product_views")).otherwise(0)
    )

# Write user behavior to Delta table for batch processing
behavior_query = user_behavior \
    .writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/checkpoints/user_behavior") \
    .start("/mnt/data/user_behavior")

# Wait for termination
spark.streams.awaitAnyTermination()
Explanation
This script implements a comprehensive website user behavior analysis system that processes clickstream data in real-time. It ingests user interactions from Kafka, enriches them with product and user information, and performs multiple analyses to understand user behavior. The system analyzes page views and engagement metrics, tracks user journeys through the website, and evaluates the conversion funnel to identify drop-off points.

It also analyzes product interactions, calculating key metrics like cart rate and conversion rate for each product. The script identifies user segments based on behavior patterns, which can be used for personalized marketing and content recommendations.

The results are written to Delta tables for integration with analytics dashboards, personalization engines, and marketing automation systems. This solution helps e-commerce and content websites optimize the user experience, increase conversions, and deliver personalized content to different user segments.

11. Data Quality Monitoring
Business Scenario
Organizations need to continuously monitor data quality across their data pipelines to ensure accuracy, completeness, and consistency of data used for business decisions.

Production-Grade PySpark Script
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, when, isnan, isnull, length, expr, to_date, current_timestamp
from pyspark.sql.types import StructType, StringType, IntegerType, DoubleType, DateType, TimestampType
import json
import datetime

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Data Quality Monitoring") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.shuffle.partitions", "100") \
    .getOrCreate()

# Load data quality rules from configuration
with open("/mnt/config/data_quality_rules.json", "r") as f:
    quality_rules = json.load(f)

# Function to apply data quality checks
def apply_data_quality_checks(df, table_name, rules):
    """Apply data quality checks based on rules configuration"""
    if table_name not in rules:
        return None

    table_rules = rules[table_name]
    results = []

    # Get total row count
    total_rows = df.count()

    # Check for null values
    if "null_checks" in table_rules:
        for column in table_rules["null_checks"]:
            null_count = df.filter(col(column).isNull() | isnan(column)).count()
            null_percentage = (null_count / total_rows) * 100 if total_rows > 0 else 0
            threshold = table_rules["null_checks"][column]

            results.append({
                "table_name": table_name,
                "check_type": "null_check",
                "column_name": column,
                "check_timestamp": datetime.datetime.now().isoformat(),
                "failed_count": null_count,
                "total_count": total_rows,
                "failure_percentage": null_percentage,
                "threshold": threshold,
                "status": "FAIL" if null_percentage > threshold else "PASS"
            })

    # Check for uniqueness
    if "uniqueness_checks" in table_rules:
        for column in table_rules["uniqueness_checks"]:
            distinct_count = df.select(column).distinct().count()
            duplicate_count = total_rows - distinct_count
            duplicate_percentage = (duplicate_count / total_rows) * 100 if total_rows > 0 else 0
            threshold = table_rules["uniqueness_checks"][column]

            results.append({
                "table_name": table_name,
                "check_type": "uniqueness_check",
                "column_name": column,
                "check_timestamp": datetime.datetime.now().isoformat(),
                "failed_count": duplicate_count,
                "total_count": total_rows,
                "failure_percentage": duplicate_percentage,
                "threshold": threshold,
                "status": "FAIL" if duplicate_percentage > threshold else "PASS"
            })

    # Check for value ranges
    if "range_checks" in table_rules:
        for column in table_rules["range_checks"]:
            min_val = table_rules["range_checks"][column]["min"]
            max_val = table_rules["range_checks"][column]["max"]

            out_of_range_count = df.filter(
                (col(column) < min_val) | (col(column) > max_val)
            ).count()

            out_of_range_percentage = (out_of_range_count / total_rows) * 100 if total_rows > 0 else 0
            threshold = table_rules["range_checks"][column]["threshold"]

            results.append({
                "table_name": table_name,
                "check_type": "range_check",
                "column_name": column,
                "check_timestamp": datetime.datetime.now().isoformat(),
                "failed_count": out_of_range_count,
                "total_count": total_rows,
                "failure_percentage": out_of_range_percentage,
                "threshold": threshold,
                "status": "FAIL" if out_of_range_percentage > threshold else "PASS"
            })

    # Check for pattern matching
    if "pattern_checks" in table_rules:
        for column in table_rules["pattern_checks"]:
            pattern = table_rules["pattern_checks"][column]["pattern"]

            pattern_mismatch_count = df.filter(
                ~col(column).rlike(pattern)
            ).count()

            pattern_mismatch_percentage = (pattern_mismatch_count / total_rows) * 100 if total_rows > 0 else 0
            threshold = table_rules["pattern_checks"][column]["threshold"]

            results.append({
                "table_name": table_name,
                "check_type": "pattern_check",
                "column_name": column,
                "check_timestamp": datetime.datetime.now().isoformat(),
                "failed_count": pattern_mismatch_count,
                "total_count": total_rows,
                "failure_percentage": pattern_mismatch_percentage,
                "threshold": threshold,
                "status": "FAIL" if pattern_mismatch_percentage > threshold else "PASS"
            })

    # Check for referential integrity
    if "referential_checks" in table_rules:
        for check in table_rules["referential_checks"]:
            source_column = check["source_column"]
            reference_table = check["reference_table"]
            reference_column = check["reference_column"]

            # Load reference table
            ref_df = spark.read.format("delta").load(f"/mnt/data/{reference_table}")

            # Get distinct values from reference table
            ref_values = ref_df.select(reference_column).distinct()

            # Left anti join to find values that don't exist in reference table
            missing_refs = df.join(
                ref_values,
                df[source_column] == ref_values[reference_column],
                "left_anti"
            )

            missing_count = missing_refs.count()
            missing_percentage = (missing_count / total_rows) * 100 if total_rows > 0 else 0
            threshold = check["threshold"]

            results.append({
                "table_name": table_name,
                "check_type": "referential_check",
                "column_name": source_column,
                "reference_table": reference_table,
                "reference_column": reference_column,
                "check_timestamp": datetime.datetime.now().isoformat(),
                "failed_count": missing_count,
                "total_count": total_rows,
                "failure_percentage": missing_percentage,
                "threshold": threshold,
                "status": "FAIL" if missing_percentage > threshold else "PASS"
            })

    # Create DataFrame from results
    if results:
        result_df = spark.createDataFrame(results)
        return result_df
    else:
        return None

# Get list of tables to monitor
tables = quality_rules.keys()

# Initialize empty DataFrame for results
schema = StructType() \
    .add("table_name", StringType()) \
    .add("check_type", StringType()) \
    .add("column_name", StringType()) \
    .add("check_timestamp", StringType()) \
    .add("failed_count", IntegerType()) \
    .add("total_count", IntegerType()) \
    .add("failure_percentage", DoubleType()) \
    .add("threshold", DoubleType()) \
    .add("status", StringType()) \
    .add("reference_table", StringType(), True) \
    .add("reference_column", StringType(), True)

all_results = spark.createDataFrame([], schema)

# Process each table
for table_name in tables:
    # Load table data
    table_path = f"/mnt/data/{table_name}"
    try:
        df = spark.read.format("delta").load(table_path)

        # Apply data quality checks
        results = apply_data_quality_checks(df, table_name, quality_rules)

        if results is not None:
            # Union with all results
            all_results = all_results.union(results)
    except Exception as e:
        # Log error
        print(f"Error processing table {table_name}: {str(e)}")

        # Create error record
        error_data = [{
            "table_name": table_name,
            "check_type": "table_access",
            "column_name": None,
            "check_timestamp": datetime.datetime.now().isoformat(),
            "failed_count": 1,
            "total_count": 1,
            "failure_percentage": 100.0,
            "threshold": 0.0,
            "status": "FAIL",
            "reference_table": None,
            "reference_column": None
        }]
        error_df = spark.createDataFrame(error_data, schema)
        all_results = all_results.union(error_df)

# Add run timestamp
all_results = all_results.withColumn("run_timestamp", current_timestamp())

# Write results to Delta table
all_results.write.format("delta").mode("append").save("/mnt/data/data_quality_results")

# Generate summary report
summary = all_results.groupBy("table_name", "status").count()
summary.write.format("delta").mode("overwrite").save("/mnt/data/data_quality_summary")

# Generate alerts for failed checks
failed_checks = all_results.filter(col("status") == "FAIL")
if failed_checks.count() > 0:
    failed_checks.write.format("delta").mode("overwrite").save("/mnt/alerts/data_quality_failures")

    # Send alert notifications (example)
    critical_failures = failed_checks.filter(col("failure_percentage") > 50)
   Explanation
This script implements a comprehensive data quality monitoring system that continuously checks data across multiple tables. It loads data quality rules from a configuration file, which defines various checks like null value detection, uniqueness constraints, value range validation, pattern matching, and referential integrity. For each table, the script applies the relevant checks and calculates failure percentages, comparing them against defined thresholds. The results are stored in a Delta table for historical tracking and trend analysis. The script also generates a summary report and alerts for failed checks, with special handling for critical failures that might require immediate attention. This solution helps organizations maintain high data quality by proactively identifying issues before they impact business decisions. The modular design allows for easy addition of new quality checks and tables without modifying the core logic.

12. SCD Type 2 Implementation
Business Scenario
Organizations need to track historical changes to dimension data (like customer or product information) while maintaining current values for reporting and analysis.

Production-Grade PySpark Script if critical_failures.count() > 0:
        # In a real system, this would trigger an alert via email, Slack, etc.
        critical_tables = critical_failures.select("table_name").distinct().collect()
        print(f"CRITICAL DATA QUALITY ALERT: Tables with severe issues: {[row.table_name for row in critical_tables]}")
Explanation
This script implements a comprehensive data quality monitoring system that continuously checks data across multiple tables. It loads data quality rules from a configuration file, which defines various checks like null value detection, uniqueness constraints, value range validation, pattern matching, and referential integrity.

For each table, the script applies the relevant checks and calculates failure percentages, comparing them against defined thresholds. The results are stored in a Delta table for historical tracking and trend analysis. The script also generates a summary report and alerts for failed checks, with special handling for critical failures that might require immediate attention.

This solution helps organizations maintain high data quality by proactively identifying issues before they impact business decisions. The modular design allows for easy addition of new quality checks and tables without modifying the core logic.

12. SCD Type 2 Implementation
Business Scenario
Organizations need to track historical changes to dimension data (like customer or product information) while maintaining current values for reporting and analysis.

Production-Grade PySpark Script
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp, lit, when, row_number
from pyspark.sql.window import Window
import datetime

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("SCD Type 2 Implementation") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.shuffle.partitions", "100") \
    .getOrCreate()

# Define configuration
dimension_table = "customer_dimension"
source_table = "customer_updates"
business_keys = ["customer_id"]
track_columns = ["name", "email", "phone", "address", "customer_segment", "credit_score"]
effective_date_col = "effective_date"
end_date_col = "end_date"
current_flag_col = "is_current"
surrogate_key_col = "customer_sk"

# Load current dimension data
try:
    dim_df = spark.read.format("delta").load(f"/mnt/data/{dimension_table}")
    print(f"Loaded existing dimension table: {dimension_table}")
except:
    # If dimension table doesn't exist, create it with empty dataframe
    print(f"Dimension table {dimension_table} does not exist. Creating new table.")

    # Create empty dataframe with schema
    from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType, BooleanType

    schema = StructType([
        StructField(surrogate_key_col, IntegerType(), False),
        StructField(business_keys[0], StringType(), False)
    ])

    # Add tracked columns to schema
    for col_name in track_columns:
        schema.add(StructField(col_name, StringType(), True))

    # Add SCD Type 2 specific columns
    schema.add(StructField(effective_date_col, TimestampType(), False))
    schema.add(StructField(end_date_col, TimestampType(), True))
    schema.add(StructField(current_flag_col, BooleanType(), False))

    # Create empty dataframe
    dim_df = spark.createDataFrame([], schema)

    # Write empty dataframe to Delta table
    dim_df.write.format("delta").mode("overwrite").save(f"/mnt/data/{dimension_table}")

# Load source data with updates
source_df = spark.read.format("delta").load(f"/mnt/data/{source_table}")
print(f"Loaded source data: {source_table} with {source_df.count()} records")

# Filter only current records from dimension table
current_dim_df = dim_df.filter(col(current_flag_col) == True)

# Join source and dimension data to identify changes
joined_df = source_df.alias("source").join(
    current_dim_df.alias("target"),
    [source_df[key] == current_dim_df[key] for key in business_keys],
    "outer"
)

# Identify new records (in source but not in dimension)
new_records = joined_df.filter(col("target." + business_keys[0]).isNull())
new_records = new_records.select("source.*")

# Identify changed records
changed_records_condition = None
for column in track_columns:
    if changed_records_condition is None:
        changed_records_condition = (col("source." + column) != col("target." + column))
    else:
        changed_records_condition = changed_records_condition | (col("source." + column) != col("target." + column))

changed_records = joined_df.filter(
    (col("target." + business_keys[0]).isNotNull()) &
    (col("source." + business_keys[0]).isNotNull()) &
    changed_records_condition
)

# Identify unchanged records (no action needed)
unchanged_records = joined_df.filter(
    (col("target." + business_keys[0]).isNotNull()) &
    (col("source." + business_keys[0]).isNotNull()) &
    ~changed_records_condition
)

# Get records to expire (changed records in dimension table)
records_to_expire = changed_records.select("target.*")

# Prepare new records for insertion
if new_records.count() > 0:
    # Get max surrogate key from dimension table
    max_sk = dim_df.agg({"customer_sk": "max"}).collect()[0][0]
    if max_sk is None:
        max_sk = 0

    # Add SCD Type 2 columns to new records
    new_records_with_metadata = new_records.withColumn(surrogate_key_col, lit(None).cast("integer"))

    # Add window for assigning surrogate keys
    window_spec = Window.orderBy(business_keys[0])
    new_records_with_metadata = new_records_with_metadata.withColumn(
        surrogate_key_col,
        row_number().over(window_spec) + max_sk
    )

    # Add SCD Type 2 metadata
    current_time = datetime.datetime.now()
    new_records_with_metadata = new_records_with_metadata \
        .withColumn(effective_date_col, lit(current_time).cast("timestamp")) \
        .withColumn(end_date_col, lit(None).cast("timestamp")) \
        .withColumn(current_flag_col, lit(True))

    # Select columns in the right order
    new_records_final = new_records_with_metadata.select(
        [surrogate_key_col] + business_keys + track_columns +
        [effective_date_col, end_date_col, current_flag_col]
    )
else:
    new_records_final = spark.createDataFrame([], dim_df.schema)

# Prepare changed records for insertion
if changed_records.count() > 0:
    # Get max surrogate key from dimension table
    max_sk = dim_df.agg({surrogate_key_col: "max"}).collect()[0][0]
    if max_sk is None:
        max_sk = 0

    # Add SCD Type 2 columns to changed records
    changed_records_with_metadata = changed_records.select("source.*")

    # Add window for assigning surrogate keys
    window_spec = Window.orderBy(business_keys[0])
    changed_records_with_metadata = changed_records_with_metadata.withColumn(
        surrogate_key_col,
        row_number().over(window_spec) + max_sk + new_records.count()
    )

    # Add SCD Type 2 metadata
    current_time = datetime.datetime.now()
    changed_records_with_metadata = changed_records_with_metadata \
        .withColumn(effective_date_col, lit(current_time).cast("timestamp")) \
        .withColumn(end_date_col, lit(None).cast("timestamp")) \
        .withColumn(current_flag_col, lit(True))

    # Select columns in the right order
    changed_records_final = changed_records_with_metadata.select(
        [surrogate_key_col] + business_keys + track_columns +
        [effective_date_col, end_date_col, current_flag_col]
    )
else:
    changed_records_final = spark.createDataFrame([], dim_df.schema)

# Update expired records
if records_to_expire.count() > 0:
    current_time = datetime.datetime.now()

    # Create DataFrame with records to update
    records_to_expire_updated = records_to_expire \
        .withColumn(end_date_col, lit(current_time).cast("timestamp")) \
        .withColumn(current_flag_col, lit(False))

    # Create a temporary view for the records to update
    records_to_expire_updated.createOrReplaceTempView("records_to_expire")

    # Use Delta Lake's MERGE to update expired records
    spark.sql(f"""
        MERGE INTO delta.`/mnt/data/{dimension_table}` as target
        USING records_to_expire as source
        ON target.{surrogate_key_col} = source.{surrogate_key_col}
        WHEN MATCHED THEN
          UPDATE SET
            {end_date_col} = source.{end_date_col},
            {current_flag_col} = source.{current_flag_col}
    """)

# Insert new and changed records
records_to_insert = new_records_final.union(changed_records_final)
if records_to_insert.count() > 0:
    records_to_insert.write.format("delta").mode("append").save(f"/mnt/data/{dimension_table}")

# Log the results
print(f"SCD Type 2 processing complete:")
print(f"  New records: {new_records.count()}")
print(f"  Changed records: {changed_records.count()}")
print(f"  Unchanged records: {unchanged_records.count()}")
print(f"  Total records in dimension table: {dim_df.count() + records_to_insert.count()}")

# Optimize the table
spark.sql(f"OPTIMIZE delta.`/mnt/data/{dimension_table}`")
Explanation
This script implements a Slowly Changing Dimension (SCD) Type 2 pattern for tracking historical changes to dimension data. It loads the current dimension table and source data with updates, then identifies new records, changed records, and unchanged records by comparing business keys and tracked columns. For changed records, it expires the current records by setting an end date and changing the current flag to false, then inserts new records with updated values and a new effective date.

For new records, it simply inserts them with appropriate metadata. The script uses Delta Lake’s MERGE operation for atomic updates to expired records, ensuring data consistency even if the job fails midway. It also optimizes the table after processing to improve query performance. This solution enables point-in-time analysis and historical tracking of dimension data changes, which is essential for accurate reporting and compliance requirements.

The modular design allows for easy adaptation to different dimension tables by simply changing the configuration parameters.

13. ETL Pipeline with Delta Lake
Business Scenario
Organizations need to build reliable, scalable ETL (Extract, Transform, Load) pipelines to integrate data from multiple sources into a unified data warehouse for analytics and reporting.

Production-Grade PySpark Script
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp, date_format, to_date, when, coalesce, lit, expr
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, TimestampType, DateType
import datetime
import json
import os

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("ETL Pipeline with Delta Lake") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.shuffle.partitions", "200") \
    .config("spark.databricks.delta.autoCompact.enabled", "true") \
    .config("spark.databricks.delta.optimizeWrite.enabled", "true") \
    .getOrCreate()

# Load pipeline configuration
with open("/mnt/config/etl_pipeline_config.json", "r") as f:
    pipeline_config = json.load(f)

# Create a log table if it doesn't exist
log_schema = StructType([
    StructField("pipeline_id", StringType(), True),
    StructField("stage", StringType(), True),
    StructField("status", StringType(), True),
    StructField("start_time", TimestampType(), True),
    StructField("end_time", TimestampType(), True),
    StructField("records_processed", IntegerType(), True),
    StructField("error_message", StringType(), True)
])

try:
    log_df = spark.read.format("delta").load("/mnt/logs/etl_pipeline_logs")
except:
    empty_log = spark.createDataFrame([], log_schema)
    empty_log.write.format("delta").mode("overwrite").save("/mnt/logs/etl_pipeline_logs")

# Function to log pipeline events
def log_event(pipeline_id, stage, status, start_time, end_time=None, records_processed=0, error_message=None):
    if end_time is None:
        end_time = datetime.datetime.now()

    log_data = [{
        "pipeline_id": pipeline_id,
        "stage": stage,
        "status": status,
        "start_time": start_time,
        "end_time": end_time,
        "records_processed": records_processed,
        "error_message": error_message
    }]

    log_df = spark.createDataFrame(log_data, log_schema)
    log_df.write.format("delta").mode("append").save("/mnt/logs/etl_pipeline_logs")

# Generate pipeline ID
pipeline_id = f"ETL_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
pipeline_start_time = datetime.datetime.now()

# Log pipeline start
log_event(pipeline_id, "pipeline", "STARTED", pipeline_start_time)

try:
    # Extract stage
    extract_start_time = datetime.datetime.now()
    log_event(pipeline_id, "extract", "STARTED", extract_start_time)

    # Process each source
    extracted_data = {}
    for source in pipeline_config["sources"]:
        source_id = source["id"]
        source_type = source["type"]

        try:
            if source_type == "jdbc":
                # Extract from JDBC source (e.g., MySQL, PostgreSQL)
                df = spark.read \
                    .format("jdbc") \
                    .option("url", source["connection_string"]) \
                    .option("dbtable", source["query"]) \
                    .option("user", source["username"]) \
                    .option("password", source["password"]) \
                    .load()

            elif source_type == "csv":
                # Extract from CSV files
                schema = None
                if "schema" in source:
                    # Parse schema from configuration
                    schema_fields = []
                    for field in source["schema"]:
                        data_type = None
                        if field["type"] == "string":
                            data_type = StringType()
                        elif field["type"] == "integer":
                            data_type = IntegerType()
                        elif field["type"] == "double":
                            data_type = DoubleType()
                        elif field["type"] == "timestamp":
                            data_type = TimestampType()
                        elif field["type"] == "date":
                            data_type = DateType()

                        schema_fields.append(StructField(field["name"], data_type, field.get("nullable", True)))

                    schema = StructType(schema_fields)

                df = spark.read \
                    .format("csv") \
                    .option("header", source.get("header", "true")) \
                    .option("inferSchema", "true" if schema is None else "false") \
                    .schema(schema) \
                    .load(source["path"])

            elif source_type == "json":
                # Extract from JSON files
                df = spark.read \
                    .format("json") \
                    .option("multiLine", source.get("multiLine", "false")) \
                    .load(source["path"])

            elif source_type == "delta":
                # Extract from Delta table
                df = spark.read \
                    .format("delta") \
                    .load(source["path"])

            elif source_type == "parquet":
                # Extract from Parquet files
                df = spark.read \
                    .format("parquet") \
                    .load(source["path"])

            else:
                raise ValueError(f"Unsupported source type: {source_type}")

            # Add metadata columns
            df = df.withColumn("source_id", lit(source_id)) \
                   .withColumn("extract_time", current_timestamp())

            # Store extracted data
            extracted_data[source_id] = df

            # Log successful extraction
            log_event(
                pipeline_id,
                f"extract_{source_id}",
                "COMPLETED",
                extract_start_time,
                datetime.datetime.now(),
                df.count()
            )

        except Exception as e:
            # Log extraction error
            log_event(
                pipeline_id,
                f"extract_{source_id}",
                "FAILED",
                extract_start_time,
                datetime.datetime.now(),
                0,
                str(e)
            )
            raise

    # Log extract stage completion
    log_event(
        pipeline_id,
        "extract",
        "COMPLETED",
        extract_start_time,
        datetime.datetime.now(),
        sum([df.count() for df in extracted_data.values()])
    )

    # Transform stage
    transform_start_time = datetime.datetime.now()
    log_event(pipeline_id, "transform", "STARTED", transform_start_time)

    transformed_data = {}
    for transform in pipeline_config["transformations"]:
        transform_id = transform["id"]
        transform_type = transform["type"]
        source_ids = transform["source_ids"]

        try:
            # Get source dataframes
            source_dfs = [extracted_data[source_id] for source_id in source_ids]

            if transform_type == "join":
                # Join multiple sources
                base_df = source_dfs[0]
                for i in range(1, len(source_dfs)):
                    join_type = transform.get("join_type", "inner")
                    join_condition = transform["join_conditions"][i-1]

                    # Parse join condition
                    left_col, right_col = join_condition.split("=")
                    left_col = left_col.strip()
                    right_col = right_col.strip()

                    base_df = base_df.join(
                        source_dfs[i],
                        base_df[left_col] == source_dfs[i][right_col],
                        join_type
                    )

                result_df = base_df

            elif transform_type == "filter":
                # Apply filters
                base_df = source_dfs[0]
                for filter_condition in transform["filter_conditions"]:
                    result_df = base_df.filter(expr(filter_condition))

            elif transform_type == "select":
                # Select columns
                base_df = source_dfs[0]
                result_df = base_df.select(transform["columns"])

            elif transform_type == "aggregate":
                # Perform aggregations
                base_df = source_dfs[0]
                group_by_cols = transform["group_by"]
                agg_expressions = []

                for agg in transform["aggregations"]:
                    agg_func = agg["function"]
                    agg_col = agg["column"]
                    alias = agg["alias"]

                    if agg_func == "sum":
                        agg_expressions.append(sum(col(agg_col)).alias(alias))
                    elif agg_func == "avg":
                        agg_expressions.append(avg(col(agg_col)).alias(alias))
                    elif agg_func == "count":
                        agg_expressions.append(count(col(agg_col)).alias(alias))
                    elif agg_func == "min":
                        agg_expressions.append(min(col(agg_col)).alias(alias))
                    elif agg_func == "max":
                        agg_expressions.append(max(col(agg_col)).alias(alias))

                result_df = base_df.groupBy(group_by_cols).agg(*agg_expressions)

            elif transform_type == "custom_sql":
                # Register source dataframes as temp views
                for i, source_id in enumerate(source_ids):
                    extracted_data[source_id].createOrReplaceTempView(f"source_{i}")

                # Execute custom SQL
                result_df = spark.sql(transform["sql_query"])

            else:
                raise ValueError(f"Unsupported transformation type: {transform_type}")

            # Apply column mappings if specified
            if "column_mappings" in transform:
                for mapping in transform["column_mappings"]:
                    source_col = mapping["source"]
                    target_col = mapping["target"]
                    result_df = result_df.withColumnRenamed(source_col, target_col)

            # Apply data type conversions if specified
            if "type_conversions" in transform:
                for conversion in transform["type_conversions"]:
                    col_name = conversion["column"]
                    data_type = conversion["type"]

                    if data_type == "string":
                        result_df = result_df.withColumn(col_name, col(col_name).cast("string"))
                    elif data_type == "integer":
                        result_df = result_df.withColumn(col_name, col(col_name).cast("integer"))
                    elif data_type == "double":
                        result_df = result_df.withColumn(col_name, col(col_name).cast("double"))
                    elif data_type == "date":
                        result_df = result_df.withColumn(col_name, to_date(col(col_name)))
                    elif data_type == "timestamp":
                        result_df = result_df.withColumn(col_name, col(col_name).cast("timestamp"))

            # Add transformation metadata
            result_df = result_df.withColumn("transform_id", lit(transform_id)) \
                               .withColumn("transform_time", current_timestamp())

            # Store transformed data
            transformed_data[transform_id] = result_df

            # Log successful transformation
            log_event(
                pipeline_id,
                f"transform_{transform_id}",
                "COMPLETED",
                transform_start_time,
                datetime.datetime.now(),
                result_df.count()
            )

        except Exception as e:
            # Log transformation error
            log_event(
                pipeline_id,
                f"transform_{transform_id}",
                "FAILED",
                transform_start_time,
                datetime.datetime.now(),
                0,
                str(e)
            )
            raise

    # Log transform stage completion
    log_event(
        pipeline_id,
        "transform",
        "COMPLETED",
        transform_start_time,
        datetime.datetime.now(),
        sum([df.count() for df in transformed_data.values()])
    )

    # Load stage
    load_start_time = datetime.datetime.now()
    log_event(pipeline_id, "load", "STARTED", load_start_time)

    for target in pipeline_config["targets"]:
        target_id = target["id"]
        target_type = target["type"]
        transform_id = target["transform_id"]

        try:
            # Get transformed dataframe
            df = transformed_data[transform_id]

            # Add load metadata
            df = df.withColumn("load_time", current_timestamp())

            if target_type == "delta":
                # Load to Delta table
                save_mode = target.get("mode", "overwrite")
                partition_by = target.get("partition_by", None)

                writer = df.write.format("delta").mode(save_mode)

                if partition_by:
                    writer = writer.partitionBy(partition_by)

                writer.save(target["path"])

                # Optimize table if specified
                if target.get("optimize", False):
                    spark.sql(f"OPTIMIZE delta.`{target['path']}`")

                # Vacuum old files if specified
                if "vacuum_hours" in target:
                    spark.sql(f"VACUUM delta.`{target['path']}` RETAIN {target['vacuum_hours']} HOURS")

            elif target_type == "jdbc":
                # Write to JDBC target
                df.write \
                    .format("jdbc") \
                    .option("url", target["connection_string"]) \
                    .option("dbtable", target["table"]) \
                    .option("user", target["username"]) \
                    .option("password", target["password"]) \
                    .mode(target.get("mode", "overwrite")) \
                    .save()

            elif target_type == "parquet":
                # Write to Parquet files
                save_mode = target.get("mode", "overwrite")
                partition_by = target.get("partition_by", None)

                writer = df.write.format("parquet").mode(save_mode)

                if partition_by:
                    writer = writer.partitionBy(partition_by)

                writer.save(target["path"])

            else:
                raise ValueError(f"Unsupported target type: {target_type}")

            # Log successful load
            log_event(
                pipeline_id,
                f"load_{target_id}",
                "COMPLETED",
                load_start_time,
                datetime.datetime.now(),
                df.count()
            )

        except Exception as e:
            # Log load error
            log_event(
                pipeline_id,
                f"load_{target_id}",
                "FAILED",
                load_start_time,
                datetime.datetime.now(),
                0,
                str(e)
            )
            raise

    # Log load stage completion
    log_event(
        pipeline_id,
        "load",
        "COMPLETED",
        load_start_time,
        datetime.datetime.now(),
        sum([df.count() for df in transformed_data.values()])
    )

    # Log pipeline completion
    log_event(
        pipeline_id,
        "pipeline",
        "COMPLETED",
        pipeline_start_time,
        datetime.datetime.now(),
        sum([df.count() for df in transformed_data.values()])
    )

except Exception as e:
    # Log pipeline failure
    log_event(
        pipeline_id,
        "pipeline",
        "FAILED",
        pipeline_start_time,
        datetime.datetime.now(),
        0,
        str(e)
    )
    raise
Explanation
This script implements a flexible, configuration-driven ETL pipeline using Delta Lake for reliable data integration. It reads a JSON configuration file that defines sources, transformations, and targets, allowing for easy modification without changing the code.

The pipeline has three main stages: Extract (loading data from various sources like JDBC, CSV, JSON, Delta, or Parquet), Transform (applying operations like joins, filters, aggregations, and custom SQL), and Load (writing data to targets like Delta tables, JDBC databases, or Parquet files).

The script includes comprehensive logging at each stage, recording start and end times, record counts, and any errors. It also adds metadata columns to track data lineage through the pipeline. Delta Lake features like OPTIMIZE and VACUUM are used to maintain performance and manage storage. This solution provides a robust foundation for building scalable data pipelines that can handle diverse data sources and complex transformations while maintaining reliability and auditability.

14. Streaming Data Processing
Business Scenario
Organizations need to process streaming data in real-time to enable immediate insights, alerts, and actions based on incoming data.

Production-Grade PySpark Script
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, window, explode, split, from_json, to_json, struct, current_timestamp
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType, IntegerType
import os

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Streaming Data Processing") \
    .config("spark.sql.streaming.checkpointLocation", "/mnt/checkpoints/streaming") \
    .config("spark.sql.shuffle.partitions", "200") \
    .config("spark.databricks.delta.autoCompact.enabled", "true") \
    .getOrCreate()

# Define schema for incoming IoT sensor data
sensor_schema = StructType([
    StructField("device_id", StringType(), True),
    StructField("sensor_type", StringType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("value", DoubleType(), True),
    StructField("unit", StringType(), True),
    StructField("location", StringType(), True),
    StructField("status", StringType(), True)
])

# Read streaming data from Kafka
kafka_bootstrap_servers = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
kafka_topic = os.environ.get("KAFKA_TOPIC", "sensor_data")

raw_stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic) \
    .option("startingOffsets", "latest") \
    .load()

# Parse JSON data
parsed_stream = raw_stream \
    .select(from_json(col("value").cast("string"), sensor_schema).alias("data")) \
    .select("data.*")

# Add processing timestamp
enriched_stream = parsed_stream \
    .withColumn("processing_time", current_timestamp())

# Write raw data to Delta table for archival
raw_query = enriched_stream \
    .writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/checkpoints/raw_sensor_data") \
    .start("/mnt/data/raw_sensor_data")

# Calculate real-time aggregations
windowed_aggs = enriched_stream \
    .withWatermark("timestamp", "10 minutes") \
    .groupBy(
        "device_id",
        "sensor_type",
        window("timestamp", "5 minutes")
    ) \
    .agg(
        avg("value").alias("avg_value"),
        min("value").alias("min_value"),
        max("value").alias("max_value"),
        count("*").alias("reading_count")
    )

# Write aggregations to Delta table
agg_query = windowed_aggs \
    .writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/checkpoints/aggregated_sensor_data") \
    .start("/mnt/data/aggregated_sensor_data")

# Load reference data for thresholds
thresholds = spark.read.format("delta").load("/mnt/data/sensor_thresholds")

# Join streaming data with thresholds for anomaly detection
joined_stream = enriched_stream.join(
    thresholds,
    (enriched_stream.device_id == thresholds.device_id) &
    (enriched_stream.sensor_type == thresholds.sensor_type),
    "left_outer"
)

# Detect anomalies
anomalies = joined_stream \
    .withColumn(
        "is_anomaly",
        when(
            (col("value") > col("max_threshold")) |
            (col("value") < col("min_threshold")),
            True
        ).otherwise(False)
    ) \
    .filter(col("is_anomaly") == True)

# Write anomalies to Delta table
anomaly_query = anomalies \
    .writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/checkpoints/sensor_anomalies") \
    .start("/mnt/data/sensor_anomalies")

# Send high-priority alerts to Kafka
alerts = anomalies \
    .filter(col("priority") == "high") \
    .select(
        col("device_id"),
        col("sensor_type"),
        col("timestamp"),
        col("value"),
        col("max_threshold"),
        col("min_threshold"),
        current_timestamp().alias("alert_time")
    )

# Convert alerts to JSON for Kafka
alert_json = alerts \
    .select(to_json(struct("*")).alias("value"))

# Write alerts to Kafka
alert_query = alert_json \
    .writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("topic", "sensor_alerts") \
    .option("checkpointLocation", "/mnt/checkpoints/sensor_alerts") \
    .start()

# Calculate device status
device_status = enriched_stream \
    .withWatermark("timestamp", "10 minutes") \
    .groupBy(
        "device_id",
        window("timestamp", "5 minutes", "1 minute")
    ) \
    .agg(
        count("*").alias("reading_count"),
        count(when(col("status") == "error", 1)).alias("error_count")
    ) \
    .withColumn(
        "error_rate",
        col("error_count") / col("reading_count")
    ) \
    .withColumn(
        "device_status",
        when(col("error_rate") > 0.1, "warning")
        .when(col("error_rate") > 0.3, "critical")
        .otherwise("normal")
    )

# Write device status to Delta table
status_query = device_status \
    .writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/checkpoints/device_status") \
    .start("/mnt/data/device_status")

# Create a real-time dashboard view
spark.sql("""
CREATE OR REPLACE VIEW sensor_dashboard AS
SELECT
    d.device_id,
    d.sensor_type,
    d.window.end AS time_window,
    d.avg_value,
    d.min_value,
    d.max_value,
    d.reading_count,
    s.device_status,
    s.error_rate,
    a.anomaly_count
FROM delta.`/mnt/data/aggregated_sensor_data` d
LEFT JOIN (
    SELECT
        device_id,
        window.end AS time_window,
        device_status,
        error_rate
    FROM delta.`/mnt/data/device_status`
) s
ON d.device_id = s.device_id AND d.window.end = s.time_window
LEFT JOIN (
    SELECT
        device_id,
        sensor_type,
        window(timestamp, '5 minutes').end AS time_window,
        count(*) AS anomaly_count
    FROM delta.`/mnt/data/sensor_anomalies`
    GROUP BY device_id, sensor_type, window(timestamp, '5 minutes')
) a
ON d.device_id = a.device_id AND d.sensor_type = a.sensor_type AND d.window.end = a.time_window
""")

# Wait for termination
spark.streams.awaitAnyTermination()
Explanation
This script implements a comprehensive streaming data processing pipeline for IoT sensor data. It ingests data from Kafka, parses the JSON payload, and enriches it with processing timestamps. The pipeline has multiple branches: one writes raw data to a Delta table for archival, another calculates real-time aggregations in 5-minute windows, and a third detects anomalies by comparing sensor values against predefined thresholds.

High-priority anomalies are sent to a Kafka topic for immediate alerting, while all anomalies are stored in a Delta table for analysis. The script also calculates device status based on error rates and creates a real-time dashboard view that combines aggregations, device status, and anomaly counts. The use of watermarking and windowing ensures that late-arriving data is handled correctly, while checkpointing provides fault tolerance.

This solution enables organizations to monitor IoT devices in real-time, detect issues immediately, and maintain a complete history of sensor data for long-term analysis.

15. Recommendation Engine
Business Scenario
E-commerce and content platforms need to provide personalized recommendations to users based on their behavior and preferences to increase engagement and conversions.

Production-Grade PySpark Script
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, split, count, when, rank, row_number, desc, array
from pyspark.sql.window import Window
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.feature import StringIndexer
from pyspark.ml import Pipeline
import datetime

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Recommendation Engine") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.shuffle.partitions", "200") \
    .getOrCreate()

# Load user interaction data
interactions = spark.read.format("delta").load("/mnt/data/user_interactions")

# Load product data
products = spark.read.format("delta").load("/mnt/data/products")

# Load user data
users = spark.read.format("delta").load("/mnt/data/users")

# Prepare data for ALS model
# Convert string IDs to numeric indices
user_indexer = StringIndexer(inputCol="user_id", outputCol="user_idx", handleInvalid="skip")
product_indexer = StringIndexer(inputCol="product_id", outputCol="product_idx", handleInvalid="skip")

# Create pipeline for consistent indexing
indexer_pipeline = Pipeline(stages=[user_indexer, product_indexer])
indexer_model = indexer_pipeline.fit(interactions)
indexed_interactions = indexer_model.transform(interactions)

# Split data into training and test sets
(training, test) = indexed_interactions.randomSplit([0.8, 0.2], seed=42)

# Build ALS model
als = ALS(
    userCol="user_idx",
    itemCol="product_idx",
    ratingCol="rating",
    coldStartStrategy="drop",
    implicitPrefs=True,
    rank=50,
    maxIter=10,
    regParam=0.01,
    alpha=1.0,
    nonnegative=True
)

# Train the model
model = als.fit(training)

# Evaluate the model
predictions = model.transform(test)
evaluator = RegressionEvaluator(
    metricName="rmse",
    labelCol="rating",
    predictionCol="prediction"
)
rmse = evaluator.evaluate(predictions)
print(f"Root-mean-square error = {rmse}")

# Generate recommendations for all users
user_recs = model.recommendForAllUsers(20)

# Convert back to original IDs
# Get the reverse mapping from index to ID
user_mapping = indexer_model.stages[0].labelsArray[0]
product_mapping = indexer_model.stages[1].labelsArray[0]

# Create UDFs to map indices back to IDs
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType, ArrayType

@udf(returnType=StringType())
def map_user_idx_to_id(idx):
    return user_mapping[int(idx)]

@udf(returnType=StringType())
def map_product_idx_to_id(idx):
    return product_mapping[int(idx)]

@udf(returnType=ArrayType(StringType()))
def map_product_indices_to_ids(indices):
    return [product_mapping[int(idx)] for idx in indices]

# Apply the mapping
user_recs = user_recs \
    .withColumn("user_id", map_user_idx_to_id(col("user_idx"))) \
    .withColumn("recommendations",
                explode(col("recommendations"))) \
    .select(
        "user_id",
        map_product_idx_to_id(col("recommendations.product_idx")).alias("product_id"),
        col("recommendations.rating").alias("predicted_rating")
    )

# Join with product information
user_recs_with_products = user_recs.join(
    products,
    user_recs.product_id == products.product_id,
    "inner"
)

# Store recommendations in Delta table
user_recs_with_products \
    .withColumn("generation_time", current_timestamp()) \
    .write \
    .format("delta") \
    .mode("overwrite") \
    .save("/mnt/data/user_recommendations")

# Generate item-based recommendations (similar products)
item_recs = model.recommendForAllItems(20)

# Convert back to original IDs
item_recs = item_recs \
    .withColumn("product_id", map_product_idx_to_id(col("product_idx"))) \
    .withColumn("recommendations",
                explode(col("recommendations"))) \
    .select(
        "product_id",
        map_product_idx_to_id(col("recommendations.product_idx")).alias("similar_product_id"),
        col("recommendations.rating").alias("similarity_score")
    )

# Join with product information
item_recs_with_products = item_recs.join(
    products.alias("p1"),
    item_recs.product_id == col("p1.product_id"),
    "inner"
).join(
    products.alias("p2"),
    item_recs.similar_product_id == col("p2.product_id"),
    "inner"
).select(
    col("p1.product_id"),
    col("p1.product_name"),
    col("p1.category"),
    col("p2.product_id").alias("similar_product_id"),
    col("p2.product_name").alias("similar_product_name"),
    col("p2.category").alias("similar_product_category"),
    col("similarity_score")
)

# Store similar products in Delta table
item_recs_with_products \
    .withColumn("generation_time", current_timestamp()) \
    .write \
    .format("delta") \
    .mode("overwrite") \
    .save("/mnt/data/similar_products")

# Generate real-time personalized recommendations
# Load recent user activity
recent_activity = spark.read.format("delta").load("/mnt/data/recent_user_activity")

# Get user's recently viewed items
recent_views = recent_activity \
    .filter(col("action_type") == "view") \
    .groupBy("user_id") \
    .agg(
        array_sort(collect_list(struct(col("timestamp").desc(), col("product_id")))).alias("recent_views")
    ) \
    .select(
        "user_id",
        slice(col("recent_views.product_id"), 1, 10).alias("recent_product_ids")
    )

# Get similar products for recently viewed items
recent_similar_products = recent_views \
    .withColumn("recent_product_id", explode(col("recent_product_ids"))) \
    .join(
        item_recs,
        col("recent_product_id") == item_recs.product_id,
        "inner"
    ) \
    .select(
        "user_id",
        "recent_product_id",
        "similar_product_id",
        "similarity_score"
    )

# Rank similar products by similarity score
window_spec = Window.partitionBy("user_id").orderBy(desc("similarity_score"))
ranked_similar_products = recent_similar_products \
    .withColumn("rank", row_number().over(window_spec)) \
    .filter(col("rank") <= 20) \
    .select(
        "user_id",
        "similar_product_id",
        "similarity_score"
    )

# Join with product information
real_time_recs = ranked_similar_products.join(
    products,
    ranked_similar_products.similar_product_id == products.product_id,
    "inner"
).select(
    "user_id",
    "product_id",
    "product_name",
    "category",
    "price",
    "similarity_score"
)

# Store real-time recommendations in Delta table
real_time_recs \
    .withColumn("generation_time", current_timestamp()) \
    .write \
    .format("delta") \
    .mode("overwrite") \
    .save("/mnt/data/real_time_recommendations")

# Generate category-based recommendations
category_preferences = interactions \
    .join(
        products,
        interactions.product_id == products.product_id,
        "inner"
    ) \
    .groupBy("user_id", "category") \
    .agg(
        count("*").alias("interaction_count"),
        avg("rating").alias("avg_rating")
    ) \
    .withColumn("preference_score", col("interaction_count") * col("avg_rating"))

# Rank categories by preference score
category_window = Window.partitionBy("user_id").orderBy(desc("preference_score"))
top_categories = category_preferences \
    .withColumn("category_rank", row_number().over(category_window)) \
    .filter(col("category_rank") <= 3)

# Get top-rated products in preferred categories
product_ratings = interactions \
    .join(
        products,
        interactions.product_id == products.product_id,
        "inner"
    ) \
    .groupBy("product_id", "product_name", "category", "price") \
    .agg(
        count("*").alias("rating_count"),
        avg("rating").alias("avg_rating")
    ) \
    .filter(col("rating_count") >= 5)

# Rank products within each category
product_window = Window.partitionBy("category").orderBy(desc("avg_rating"))
top_products = product_ratings \
    .withColumn("product_rank", row_number().over(product_window)) \
    .filter(col("product_rank") <= 10)

# Join user's preferred categories with top products
category_recs = top_categories.join(
    top_products,
    top_categories.category == top_products.category,
    "inner"
).select(
    "user_id",
    "category",
    "category_rank",
    "product_id",
    "product_name",
    "price",
    "avg_rating",
    "product_rank"
)

# Store category-based recommendations in Delta table
category_recs \
    .withColumn("generation_time", current_timestamp()) \
    .write \
    .format("delta") \
    .mode("overwrite") \
    .save("/mnt/data/category_recommendations")

# Create a unified recommendation view
spark.sql("""
CREATE OR REPLACE VIEW unified_recommendations AS
SELECT
    user_id,
    product_id,
    product_name,
    category,
    price,
    'als' AS recommendation_type,
    predicted_rating AS score,
    generation_time
FROM delta.`/mnt/data/user_recommendations`
UNION ALL
SELECT
    user_id,
    product_id,
    product_name,
    category,
    price,
    'real_time' AS recommendation_type,
    similarity_score AS score,
    generation_time
FROM delta.`/mnt/data/real_time_recommendations`
UNION ALL
SELECT
    user_id,
    product_id,
    product_name,
    category,
    price,
    'category_based' AS recommendation_type,
    avg_rating AS score,
    generation_time
FROM delta.`/mnt/data/category_recommendations`
""")

# Log model metrics
model_metrics = [{
    "model_type": "ALS",
    "training_date": datetime.datetime.now().isoformat(),
    "rmse": rmse,
    "rank": 50,
    "max_iter": 10,
    "reg_param": 0.01,
    "alpha": 1.0
}]

spark.createDataFrame(model_metrics).write \
    .format("delta") \
    .mode("append") \
    .save("/mnt/data/recommendation_model_metrics")

print("Recommendation engine processing complete")
Explanation
This script implements a comprehensive recommendation engine using collaborative filtering with Alternating Least Squares (ALS). It processes user interaction data to build a model that captures latent factors influencing user preferences.

The system generates three types of recommendations: user-based recommendations (items a user might like based on their past behavior), item-based recommendations (similar products to ones a user has viewed or purchased), and category-based recommendations (top products in categories a user has shown interest in). The script includes data preparation with StringIndexers to convert IDs to numeric indices, model training and evaluation, and mapping the results back to original IDs. It also incorporates real-time personalization by considering users’ recent activity.

All recommendations are stored in Delta tables and unified in a view that can be queried by applications. The solution helps e-commerce and content platforms increase user engagement and conversions by providing personalized recommendations through multiple complementary approaches.

16. Machine Learning Pipeline
Business Scenario
Organizations need to build end-to-end machine learning pipelines that handle data preparation, model training, evaluation, and deployment for predictive analytics.

Production-Grade PySpark Script
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, count, isnan, isnull, mean, stddev, min, max
from pyspark.ml.feature import VectorAssembler, StandardScaler, StringIndexer, OneHotEncoder, Imputer
from pyspark.ml.classification import RandomForestClassifier, LogisticRegression, GBTClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator, MulticlassClassificationEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.ml import Pipeline
import datetime
import json
import mlflow
import mlflow.spark

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Machine Learning Pipeline") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.shuffle.partitions", "200") \
    .getOrCreate()

# Set MLflow tracking URI
mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/customer_churn_prediction")

# Load configuration
with open("/mnt/config/ml_pipeline_config.json", "r") as f:
    config = json.load(f)

# Load training data
training_data = spark.read.format("delta").load(config["training_data_path"])

# Exploratory Data Analysis
print("Dataset Overview:")
print(f"Number of records: {training_data.count()}")
print(f"Number of features: {len(training_data.columns)}")

# Check for missing values
missing_values = training_data.select([count(when(col(c).isNull() | isnan(c), c)).alias(c) for c in training_data.columns])
missing_values.show()

# Calculate basic statistics
numeric_features = [c for c in training_data.columns if c != config["target_column"] and training_data.select(c).dtypes[0][1] in ["int", "double"]]
stats = training_data.select([mean(c).alias(f"{c}_mean"),
                             stddev(c).alias(f"{c}_stddev"),
                             min(c).alias(f"{c}_min"),
                             max(c).alias(f"{c}_max") for c in numeric_features])
stats.show()

# Class distribution
class_distribution = training_data.groupBy(config["target_column"]).count()
class_distribution.show()

# Start MLflow run
with mlflow.start_run(run_name=f"customer_churn_prediction_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"):
    # Log dataset info
    mlflow.log_param("data_path", config["training_data_path"])
    mlflow.log_param("num_records", training_data.count())
    mlflow.log_param("num_features", len(training_data.columns) - 1)  # Excluding target

    # Data Preparation
    # Handle categorical features
    categorical_features = config["categorical_features"]
    string_indexers = [StringIndexer(inputCol=c, outputCol=f"{c}_idx", handleInvalid="keep") for c in categorical_features]
    one_hot_encoders = [OneHotEncoder(inputCol=f"{c}_idx", outputCol=f"{c}_ohe") for c in categorical_features]

    # Handle numeric features
    numeric_features = config["numeric_features"]
    imputer = Imputer(inputCols=numeric_features, outputCols=[f"{c}_imputed" for c in numeric_features], strategy="mean")

    # Assemble features
    assembler_inputs = [f"{c}_ohe" for c in categorical_features] + [f"{c}_imputed" for c in numeric_features]
    assembler = VectorAssembler(inputCols=assembler_inputs, outputCol="features")

    # Scale features
    scaler = StandardScaler(inputCol="features", outputCol="scaled_features", withStd=True, withMean=True)

    # Define models to evaluate
    models = {
        "RandomForest": RandomForestClassifier(labelCol=config["target_column"], featuresCol="scaled_features",
                                              numTrees=100, maxDepth=10, seed=42),
        "LogisticRegression": LogisticRegression(labelCol=config["target_column"], featuresCol="scaled_features",
                                                maxIter=20, regParam=0.1, elasticNetParam=0.8),
        "GradientBoostedTrees": GBTClassifier(labelCol=config["target_column"], featuresCol="scaled_features",
                                             maxIter=20, maxDepth=5, seed=42)
    }

    # Split data into training and validation sets
    train_data, val_data = training_data.randomSplit([0.8, 0.2], seed=42)

    # Log training and validation set sizes
    mlflow.log_param("train_size", train_data.count())
    mlflow.log_param("validation_size", val_data.count())

    # Train and evaluate each model
    best_model_name = None
    best_model_auc = 0
    best_pipeline = None

    for model_name, model in models.items():
        print(f"Training {model_name}...")

        # Create pipeline
        pipeline = Pipeline(stages=string_indexers + one_hot_encoders + [imputer, assembler, scaler, model])

        # Train model
        pipeline_model = pipeline.fit(train_data)

        # Make predictions
        predictions = pipeline_model.transform(val_data)

        # Evaluate model
        evaluator = BinaryClassificationEvaluator(labelCol=config["target_column"], metricName="areaUnderROC")
        auc = evaluator.evaluate(predictions)

        # Calculate additional metrics
        multi_evaluator = MulticlassClassificationEvaluator(labelCol=config["target_column"], predictionCol="prediction")
        accuracy = multi_evaluator.setMetricName("accuracy").evaluate(predictions)
        precision = multi_evaluator.setMetricName("weightedPrecision").evaluate(predictions)
        recall = multi_evaluator.setMetricName("weightedRecall").evaluate(predictions)
        f1 = multi_evaluator.setMetricName("f1").evaluate(predictions)

        # Log metrics
        mlflow.log_metric(f"{model_name}_auc", auc)
        mlflow.log_metric(f"{model_name}_accuracy", accuracy)
        mlflow.log_metric(f"{model_name}_precision", precision)
        mlflow.log_metric(f"{model_name}_recall", recall)
        mlflow.log_metric(f"{model_name}_f1", f1)

        print(f"{model_name} - AUC: {auc}, Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}, F1: {f1}")

        # Track best model
        if auc > best_model_auc:
            best_model_auc = auc
            best_model_name = model_name
            best_pipeline = pipeline_model

    # Log best model info
    mlflow.log_param("best_model", best_model_name)
    mlflow.log_metric("best_model_auc", best_model_auc)

    # Hyperparameter tuning for best model
    print(f"Performing hyperparameter tuning for {best_model_name}...")

    if best_model_name == "RandomForest":
        model = RandomForestClassifier(labelCol=config["target_column"], featuresCol="scaled_features", seed=42)
        param_grid = ParamGridBuilder() \
            .addGrid(model.numTrees, [50, 100, 200]) \
            .addGrid(model.maxDepth, [5, 10, 15]) \
            .addGrid(model.minInstancesPerNode, [1, 2, 4]) \
            .build()

    elif best_model_name == "LogisticRegression":
        model = LogisticRegression(labelCol=config["target_column"], featuresCol="scaled_features")
        param_grid = ParamGridBuilder() \
            .addGrid(model.regParam, [0.01, 0.1, 0.5]) \
            .addGrid(model.elasticNetParam, [0.0, 0.5, 1.0]) \
            .addGrid(model.maxIter, [10, 20, 50]) \
            .build()

    elif best_model_name == "GradientBoostedTrees":
        model = GBTClassifier(labelCol=config["target_column"], featuresCol="scaled_features", seed=42)
        param_grid = ParamGridBuilder() \
            .addGrid(model.maxDepth, [3, 5, 8]) \
            .addGrid(model.maxIter, [10, 20, 50]) \
            .addGrid(model.stepSize, [0.05, 0.1, 0.2]) \
            .build()

    # Create pipeline for tuning
    tuning_pipeline = Pipeline(stages=string_indexers + one_hot_encoders + [imputer, assembler, scaler, model])

    # Set up cross-validation
    evaluator = BinaryClassificationEvaluator(labelCol=config["target_column"], metricName="areaUnderROC")
    cv = CrossValidator(estimator=tuning_pipeline,
                      estimatorParamMaps=param_grid,
                      evaluator=evaluator,
                      numFolds=3,
                      seed=42)

    # Run cross-validation
    cv_model = cv.fit(train_data)

    # Get best model
    best_tuned_model = cv_model.bestModel

    # Evaluate tuned model
    tuned_predictions = best_tuned_model.transform(val_data)
    tuned_auc = evaluator.evaluate(tuned_predictions)

    # Calculate additional metrics
    multi_evaluator = MulticlassClassificationEvaluator(labelCol=config["target_column"], predictionCol="prediction")
    tuned_accuracy = multi_evaluator.setMetricName("accuracy").evaluate(tuned_predictions)
    tuned_precision = multi_evaluator.setMetricName("weightedPrecision").evaluate(tuned_predictions)
    tuned_recall = multi_evaluator.setMetricName("weightedRecall").evaluate(tuned_predictions)
    tuned_f1 = multi_evaluator.setMetricName("f1").evaluate(tuned_predictions)

    # Log tuned metrics
    mlflow.log_metric("tuned_auc", tuned_auc)
    mlflow.log_metric("tuned_accuracy", tuned_accuracy)
    mlflow.log_metric("tuned_precision", tuned_precision)
    mlflow.log_metric("tuned_recall", tuned_recall)
    mlflow.log_metric("tuned_f1", tuned_f1)

    print(f"Tuned {best_model_name} - AUC: {tuned_auc}, Accuracy: {tuned_accuracy}, Precision: {tuned_precision}, Recall: {tuned_recall}, F1: {tuned_f1}")

    # Log best parameters
    best_params = best_tuned_model.stages[-1].extractParamMap()
    for param, value in best_params.items():
        param_name = param.name
        mlflow.log_param(f"best_{param_name}", value)

    # Save model
    mlflow.spark.log_model(best_tuned_model, "model")

    # Register model in MLflow Model Registry
    model_uri = f"runs:/{mlflow.active_run().info.run_id}/model"
    registered_model = mlflow.register_model(model_uri, "customer_churn_prediction")

    # Save model to Delta table for batch scoring
    best_tuned_model.write().overwrite().save("/mnt/models/customer_churn_prediction")

    # Create feature importance DataFrame
    if best_model_name in ["RandomForest", "GradientBoostedTrees"]:
        feature_importances = best_tuned_model.stages[-1].featureImportances
        feature_names = assembler_inputs
        importance_df = spark.createDataFrame(
            [(feature_names[i], float(feature_importances[i])) for i in range(len(feature_names))],
            ["feature", "importance"]
        )

        # Save feature importance
        importance_df.write.format("delta").mode("overwrite").save("/mnt/data/feature_importance")

    # Create model metadata
    model_metadata = [{
        "model_name": "customer_churn_prediction",
        "model_version": registered_model.version,
        "training_date": datetime.datetime.now().isoformat(),
        "best_algorithm": best_model_name,
        "auc": float(tuned_auc),
        "accuracy": float(tuned_accuracy),
        "precision": float(tuned_precision),
        "recall": float(tuned_recall),
        "f1_score": float(tuned_f1),
        "training_records": train_data.count(),
        "validation_records": val_data.count(),
        "mlflow_run_id": mlflow.active_run().info.run_id
    }]

    # Save model metadata
    spark.createDataFrame(model_metadata).write \
        .format("delta") \
        .mode("append") \
        .save("/mnt/data/model_metadata")

# Create batch scoring function
def score_new_data(data_path, output_path):
    """Score new data using the trained model"""
    # Load model
    loaded_model = Pipeline.load("/mnt/models/customer_churn_prediction")

    # Load data
    new_data = spark.read.format("delta").load(data_path)

    # Make predictions
    predictions = loaded_model.transform(new_data)

    # Select relevant columns
    result = predictions.select(
        "*",
        col("prediction").alias("churn_prediction"),
        col("probability").getItem(1).alias("churn_probability")
    )

    # Save results
    result.write.format("delta").mode("overwrite").save(output_path)

    return result

# Example batch scoring
if config.get("run_batch_scoring", False):
    score_new_data(config["scoring_data_path"], config["scoring_output_path"])

print("Machine Learning Pipeline completed successfully")
Explanation
This script implements a comprehensive machine learning pipeline for customer churn prediction. It handles the entire ML lifecycle, from data preparation to model deployment. The pipeline begins with exploratory data analysis to understand the dataset’s characteristics, including missing values and class distribution. It then prepares the data by handling categorical features through indexing and one-hot encoding, imputing missing values in numeric features, assembling all features into a vector, and scaling them.

The script evaluates multiple models (Random Forest, Logistic Regression, and Gradient Boosted Trees) to identify the best performer based on AUC. For the best model, it performs hyperparameter tuning using cross-validation to further improve performance. The pipeline integrates with MLflow for experiment tracking, logging parameters, metrics, and the model itself. It also registers the model in the MLflow Model Registry for versioning and deployment.

The script saves the model for batch scoring and creates a function to score new data. Additionally, it generates feature importance analysis for tree-based models and stores model metadata for governance and auditing. This solution enables organizations to build, evaluate, and deploy machine learning models in a reproducible and scalable way.

17. Graph Analysis
Business Scenario
Organizations need to analyze complex relationships in their data to identify patterns, communities, and influential entities.

Production-Grade PySpark Script
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, count, sum as spark_sum, desc, row_number, collect_list
from pyspark.sql.window import Window
from graphframes import GraphFrame
import datetime

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Graph Analysis") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.shuffle.partitions", "200") \
    .getOrCreate()

# Load vertices (entities)
vertices = spark.read.format("delta").load("/mnt/data/entities")

# Load edges (relationships)
edges = spark.read.format("delta").load("/mnt/data/relationships")

# Create GraphFrame
g = GraphFrame(vertices, edges)

# Basic graph statistics
print("Graph Statistics:")
print(f"Number of vertices: {g.vertices.count()}")
print(f"Number of edges: {g.edges.count()}")

# Degree distribution
in_degree = g.inDegrees
out_degree = g.outDegrees
degree = g.degrees

# Calculate degree statistics
in_degree_stats = in_degree.summary().collect()[0]
out_degree_stats = out_degree.summary().collect()[0]
degree_stats = degree.summary().collect()[0]

print("Degree Statistics:")
print(f"In-degree: min={in_degree_stats['min']}, max={in_degree_stats['max']}, avg={in_degree_stats['mean']}")
print(f"Out-degree: min={out_degree_stats['min']}, max={out_degree_stats['max']}, avg={out_degree_stats['mean']}")
print(f"Total degree: min={degree_stats['min']}, max={degree_stats['max']}, avg={degree_stats['mean']}")

# Find most connected entities
top_connected = degree.orderBy(desc("degree")).limit(10)
print("Top 10 most connected entities:")
top_connected.show()

# PageRank to find influential entities
pagerank = g.pageRank(resetProbability=0.15, maxIter=10)
influential_entities = pagerank.vertices.orderBy(desc("pagerank")).limit(10)
print("Top 10 influential entities by PageRank:")
influential_entities.show()

# Save PageRank results
pagerank.vertices \
    .withColumn("analysis_date", lit(datetime.datetime.now())) \
    .write \
    .format("delta") \
    .mode("overwrite") \
    .save("/mnt/data/pagerank_results")

# Community detection using Label Propagation
communities = g.labelPropagation(maxIter=5)
community_sizes = communities.groupBy("label").count().orderBy(desc("count"))
print("Community sizes:")
community_sizes.show()

# Save community detection results
communities \
    .withColumn("analysis_date", lit(datetime.datetime.now())) \
    .write \
    .format("delta") \
    .mode("overwrite") \
    .save("/mnt/data/community_results")

# Connected components analysis
connected_components = g.connectedComponents()
component_sizes = connected_components.groupBy("component").count().orderBy(desc("count"))
print("Connected component sizes:")
component_sizes.show()

# Save connected components results
connected_components \
    .withColumn("analysis_date", lit(datetime.datetime.now())) \
    .write \
    .format("delta") \
    .mode("overwrite") \
    .save("/mnt/data/connected_components")

# Triangle count (local clustering)
triangle_counts = g.triangleCount()
avg_triangles = triangle_counts.agg({"count": "avg"}).collect()[0][0]
print(f"Average number of triangles per vertex: {avg_triangles}")

# Save triangle count results
triangle_counts \
    .withColumn("analysis_date", lit(datetime.datetime.now())) \
    .write \
    .format("delta") \
    .mode("overwrite") \
    .save("/mnt/data/triangle_counts")

# Shortest paths analysis
# Select source vertices (e.g., top 10 influential entities)
sources = influential_entities.select("id").limit(10).collect()
source_ids = [row["id"] for row in sources]

# Find shortest paths from each source to all other vertices
all_paths = []
for source_id in source_ids:
    paths = g.shortestPaths(landmarks=[source_id])
    paths = paths.withColumn("source", lit(source_id))
    paths = paths.withColumn("distances", explode(paths.distances))
    paths = paths.select("id", "source", "distances.key", "distances.value")
    paths = paths.withColumnRenamed("key", "destination").withColumnRenamed("value", "distance")
    all_paths.append(paths)

# Union all paths
if all_paths:
    shortest_paths = all_paths[0]
    for i in range(1, len(all_paths)):
        shortest_paths = shortest_paths.union(all_paths[i])

    # Calculate average shortest path length
    avg_path_length = shortest_paths.filter(col("distance") > 0).agg({"distance": "avg"}).collect()[0][0]
    print(f"Average shortest path length: {avg_path_length}")

    # Save shortest paths results
    shortest_paths \
        .withColumn("analysis_date", lit(datetime.datetime.now())) \
        .write \
        .format("delta") \
        .mode("overwrite") \
        .save("/mnt/data/shortest_paths")

# Motif finding (pattern matching)
# Find all triangles
triangles = g.find("(a)-[ab]->(b); (b)-[bc]->(c); (c)-[ca]->(a)")
print(f"Number of triangles: {triangles.count()}")

# Find hub patterns (star topology)
hubs = g.find("(a)-[ab]->(b); (a)-[ac]->(c); (a)-[ad]->(d)")
print(f"Number of hub patterns: {hubs.count()}")

# Save motif results
triangles \
    .withColumn("analysis_date", lit(datetime.datetime.now())) \
    .write \
    .format("delta") \
    .mode("overwrite") \
    .save("/mnt/data/triangle_motifs")

hubs \
    .withColumn("analysis_date", lit(datetime.datetime.now())) \
    .write \
    .format("delta") \
    .mode("overwrite") \
    .save("/mnt/data/hub_motifs")

# Entity similarity based on structural equivalence
# For each pair of vertices, count common neighbors
common_neighbors = g.vertices.alias("v1").crossJoin(g.vertices.alias("v2")) \
    .filter(col("v1.id") != col("v2.id")) \
    .join(g.edges.alias("e1"), col("v1.id") == col("e1.src")) \
    .join(g.edges.alias("e2"), (col("v2.id") == col("e2.src")) & (col("e1.dst") == col("e2.dst"))) \
    .groupBy("v1.id", "v2.id") \
    .agg(count("e1.dst").alias("common_neighbors"))

# Find top similar entity pairs
top_similar = common_neighbors.orderBy(desc("common_neighbors")).limit(100)
print("Top similar entity pairs:")
top_similar.show()

# Save entity similarity results
top_similar \
    .withColumn("analysis_date", lit(datetime.datetime.now())) \
    .write \
    .format("delta") \
    .mode("overwrite") \
    .save("/mnt/data/entity_similarity")

# Create graph analysis dashboard view
spark.sql("""
CREATE OR REPLACE VIEW graph_analysis_dashboard AS
SELECT
    v.id,
    v.name,
    v.type,
    v.properties,
    d.degree,
    pr.pagerank,
    tc.count AS triangle_count,
    cc.label AS community,
    comp.component
FROM delta.`/mnt/data/entities` v
LEFT JOIN (
    SELECT id, degree FROM delta.`/mnt/data/degree_results`
) d ON v.id = d.id
LEFT JOIN (
    SELECT id, pagerank FROM delta.`/mnt/data/pagerank_results`
) pr ON v.id = pr.id
LEFT JOIN (
    SELECT id, count FROM delta.`/mnt/data/triangle_counts`
) tc ON v.id = tc.id
LEFT JOIN (
    SELECT id, label FROM delta.`/mnt/data/community_results`
) cc ON v.id = cc.id
LEFT JOIN (
    SELECT id, component FROM delta.`/mnt/data/connected_components`
) comp ON v.id = comp.id
""")

print("Graph analysis completed successfully")
Explanation
This script implements a comprehensive graph analysis pipeline using GraphFrames, a powerful library for graph processing on top of Apache Spark. It loads entity and relationship data to create a graph representation, then performs various analyses to extract insights about the network structure. The pipeline calculates basic graph statistics, degree distributions, and identifies the most connected entities.

It uses PageRank to find influential entities in the network and applies community detection algorithms to identify groups of closely connected entities. The script also analyzes connected components, triangle counts (which indicate clustering), and shortest paths between important entities. It performs pattern matching to find specific motifs like triangles and hub patterns, and calculates entity similarity based on common neighbors. All analysis results are stored in Delta tables for further exploration and visualization.

This solution helps organizations understand complex relationships in their data, identify key entities and communities, and discover hidden patterns that might not be apparent through traditional analysis methods.

18. Time Series Analysis
Business Scenario
Organizations need to analyze time series data to identify trends, seasonality, and anomalies for forecasting and monitoring.

Production-Grade PySpark Script
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, window, avg, min, max, count, stddev, lag, lead, expr
from pyspark.sql.functions import year, month, dayofmonth, hour, minute, date_format, to_timestamp
from pyspark.sql.window import Window
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator
import datetime

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Time Series Analysis") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.shuffle.partitions", "200") \
    .getOrCreate()

# Load time series data
time_series = spark.read.format("delta").load("/mnt/data/time_series")

# Ensure timestamp column is properly formatted
time_series = time_series.withColumn("timestamp", to_timestamp(col("timestamp")))

# Sort by timestamp
time_series = time_series.orderBy("timestamp")

# Extract time components
time_series = time_series \
    .withColumn("year", year(col("timestamp"))) \
    .withColumn("month", month(col("timestamp"))) \
    .withColumn("day", dayofmonth(col("timestamp"))) \
    .withColumn("hour", hour(col("timestamp"))) \
    .withColumn("minute", minute(col("timestamp"))) \
    .withColumn("day_of_week", date_format(col("timestamp"), "E")) \
    .withColumn("week_of_year", date_format(col("timestamp"), "w"))

# Calculate basic statistics
stats = time_series.groupBy("series_id").agg(
    count("value").alias("count"),
    avg("value").alias("mean"),
    stddev("value").alias("stddev"),
    min("value").alias("min"),
    max("value").alias("max")
)

# Save basic statistics
stats.write.format("delta").mode("overwrite").save("/mnt/data/time_series_stats")

# Calculate moving averages
window_specs = {
    "1h": "1 hour",
    "6h": "6 hours",
    "1d": "1 day",
    "7d": "7 days",
    "30d": "30 days"
}

for window_name, window_duration in window_specs.items():
    # Calculate moving average
    moving_avg = time_series \
        .groupBy("series_id", window(col("timestamp"), window_duration)) \
        .agg(
            avg("value").alias(f"avg_{window_name}"),
            min("value").alias(f"min_{window_name}"),
            max("value").alias(f"max_{window_name}"),
            count("value").alias(f"count_{window_name}")
        ) \
        .select(
            "series_id",
            col("window.start").alias("window_start"),
            col("window.end").alias("window_end"),
            f"avg_{window_name}",
            f"min_{window_name}",
            f"max_{window_name}",
            f"count_{window_name}"
        )

    # Save moving averages
    moving_avg.write.format("delta").mode("overwrite").save(f"/mnt/data/moving_avg_{window_name}")

# Calculate rate of change
window_spec = Window.partitionBy("series_id").orderBy("timestamp")
time_series = time_series \
    .withColumn("prev_value", lag("value", 1).over(window_spec)) \
    .withColumn("next_value", lead("value", 1).over(window_spec)) \
    .withColumn("value_change", col("value") - col("prev_value")) \
    .withColumn("pct_change", when(col("prev_value") != 0, (col("value") - col("prev_value")) / col("prev_value") * 100).otherwise(0))

# Save rate of change data
time_series.write.format("delta").mode("overwrite").save("/mnt/data/time_series_enriched")

# Detect anomalies using Z-score
window_spec = Window.partitionBy("series_id").orderBy("timestamp").rowsBetween(-24, 0)  # 24-hour window
time_series = time_series \
    .withColumn("rolling_mean", avg("value").over(window_spec)) \
    .withColumn("rolling_stddev", stddev("value").over(window_spec)) \
    .withColumn("z_score", when(col("rolling_stddev") != 0, (col("value") - col("rolling_mean")) / col("rolling_stddev")).otherwise(0)) \
    .withColumn("is_anomaly", abs(col("z_score")) > 3)  # Z-score > 3 standard deviations

# Save anomaly detection results
anomalies = time_series.filter(col("is_anomaly") == True)
anomalies.write.format("delta").mode("overwrite").save("/mnt/data/time_series_anomalies")

# Seasonal decomposition
# Group by time components to identify patterns
hourly_pattern = time_series.groupBy("hour").agg(avg("value").alias("hourly_avg"))
daily_pattern = time_series.groupBy("day_of_week").agg(avg("value").alias("daily_avg"))
monthly_pattern = time_series.groupBy("month").agg(avg("value").alias("monthly_avg"))

# Save seasonal patterns
hourly_pattern.write.format("delta").mode("overwrite").save("/mnt/data/hourly_pattern")
daily_pattern.write.format("delta").mode("overwrite").save("/mnt/data/daily_pattern")
monthly_pattern.write.format("delta").mode("overwrite").save("/mnt/data/monthly_pattern")

# Time series forecasting using Random Forest
# Create features for forecasting
for series_id in time_series.select("series_id").distinct().collect():
    series = time_series.filter(col("series_id") == series_id.series_id)

    # Create lag features
    for i in range(1, 25):  # 24 hours of lag features
        series = series.withColumn(f"lag_{i}", lag("value", i).over(window_spec))

    # Add time-based features
    feature_cols = [f"lag_{i}" for i in range(1, 25)] + ["hour", "day_of_week", "month"]

    # Drop rows with nulls (first 24 rows will have null lag values)
    series = series.dropna(subset=feature_cols)

    # Prepare features
    assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
    series = assembler.transform(series)

    # Split data into training and test sets
    train_data = series.filter(col("timestamp") < "2023-01-01")
    test_data = series.filter(col("timestamp") >= "2023-01-01")

    # Train Random Forest model
    rf = RandomForestRegressor(featuresCol="features", labelCol="value", numTrees=100)
    model = rf.fit(train_data)

    # Make predictions
    predictions = model.transform(test_data)

    # Evaluate model
    evaluator = RegressionEvaluator(labelCol="value", predictionCol="prediction", metricName="rmse")
    rmse = evaluator.evaluate(predictions)

    # Calculate additional metrics
    mae = evaluator.setMetricName("mae").evaluate(predictions)
    r2 = evaluator.setMetricName("r2").evaluate(predictions)

    print(f"Series {series_id.series_id} - RMSE: {rmse}, MAE: {mae}, R2: {r2}")

    # Save predictions
    predictions.select(
        "series_id",
        "timestamp",
        "value",
        "prediction",
        (col("value") - col("prediction")).alias("error")
    ).write.format("delta").mode("overwrite").save(f"/mnt/data/forecast_results_{series_id.series_id}")

    # Save model metrics
    metrics = [{
        "series_id": series_id.series_id,
        "model_type": "RandomForest",
        "training_date": datetime.datetime.now().isoformat(),
        "rmse": rmse,
        "mae": mae,
        "r2": r2
    }]

    spark.createDataFrame(metrics).write \
        .format("delta") \
        .mode("append") \
        .save("/mnt/data/forecast_metrics")

    # Generate future forecasts
    # Create a dataframe with future timestamps
    future_dates = spark.sql(f"""
        SELECT
            explode(sequence(to_timestamp('2023-01-01 00:00:00'), to_timestamp('2023-01-31 23:59:59'), interval 1 hour)) as timestamp
    """)

    future_dates = future_dates \
        .withColumn("series_id", lit(series_id.series_id)) \
        .withColumn("year", year(col("timestamp"))) \
        .withColumn("month", month(col("timestamp"))) \
        .withColumn("day", dayofmonth(col("timestamp"))) \
        .withColumn("hour", hour(col("timestamp"))) \
        .withColumn("day_of_week", date_format(col("timestamp"), "E")) \
        .withColumn("week_of_year", date_format(col("timestamp"), "w"))

    # Join with historical data to get lag features
    last_values = series.orderBy(col("timestamp").desc()).limit(24)

    # Create a dataframe with lag values for the first prediction
    lag_values = spark.createDataFrame([(i, float(last_values.collect()[i-1]["value"])) for i in range(1, 25)], ["lag", "value"])

    # Initialize predictions list
    future_predictions = []

    # Iterate through future dates and predict
    for future_row in future_dates.collect():
        # Create feature vector
        features = [lag_values.filter(col("lag") == i).first()["value"] for i in range(1, 25)]
        features.extend([future_row["hour"], future_row["day_of_week"], future_row["month"]])

        # Assemble feature vector
        feature_vector = Vectors.dense(features)

        # Make prediction
        prediction = model.predict(feature_vector)

        # Update lag values for next prediction
        lag_values = lag_values.withColumn("lag", col("lag") + 1).filter(col("lag") <= 24)
        lag_values = lag_values.union(spark.createDataFrame([(1, float(prediction))], ["lag", "value"]))

        # Add to predictions list
        future_predictions.append((
            future_row["series_id"],
            future_row["timestamp"],
            float(prediction)
        ))

    # Create dataframe from predictions
    future_df = spark.createDataFrame(future_predictions, ["series_id", "timestamp", "prediction"])

    # Save future predictions
    future_df.write.format("delta").mode("overwrite").save(f"/mnt/data/future_forecast_{series_id.series_id}")

# Create time series dashboard view
spark.sql("""
CREATE OR REPLACE VIEW time_series_dashboard AS
SELECT
    ts.series_id,
    ts.timestamp,
    ts.value,
    ts.rolling_mean,
    ts.rolling_stddev,
    ts.z_score,
    ts.is_anomaly,
    ma1.avg_1h,
    ma6.avg_6h,
    ma24.avg_1d,
    fr.prediction,
    fr.error
FROM delta.`/mnt/data/time_series_enriched` ts
LEFT JOIN delta.`/mnt/data/moving_avg_1h` ma1
    ON ts.series_id = ma1.series_id AND ts.timestamp >= ma1.window_start AND ts.timestamp < ma1.window_end
LEFT JOIN delta.`/mnt/data/moving_avg_6h` ma6
    ON ts.series_id = ma6.series_id AND ts.timestamp >= ma6.window_start AND ts.timestamp < ma6.window_end
LEFT JOIN delta.`/mnt/data/moving_avg_1d` ma24
    ON ts.series_id = ma24.series_id AND ts.timestamp >= ma24.window_start AND ts.timestamp < ma24.window_end
LEFT JOIN (
    SELECT series_id, timestamp, prediction, error
    FROM delta.`/mnt/data/forecast_results_*`
) fr
    ON ts.series_id = fr.series_id AND ts.timestamp = fr.timestamp
""")

print("Time series analysis completed successfully")
Explanation
This script implements a comprehensive time series analysis pipeline for monitoring, anomaly detection, and forecasting. It processes time series data by extracting temporal components (year, month, day, hour) and calculating basic statistics. The pipeline computes moving averages at different time scales (1 hour, 6 hours, 1 day, 7 days, 30 days) to identify trends and smooth out noise. It calculates rate of change metrics to understand how quickly values are changing over time.

The script detects anomalies using Z-scores, flagging values that deviate significantly from the rolling mean. It performs seasonal decomposition by analyzing patterns at hourly, daily, and monthly levels to identify recurring cycles in the data. For forecasting, the pipeline builds a Random Forest regression model for each time series, using lag features and temporal components as predictors.

It evaluates model performance using RMSE, MAE, and R² metrics, and generates future forecasts for the next month. All analysis results are stored in Delta tables and unified in a dashboard view for visualization. This solution helps organizations understand patterns in their time series data, detect anomalies in real-time, and make data-driven forecasts for future planning.

19. Natural Language Processing
Business Scenario
Organizations need to analyze text data from customer feedback, social media, and other sources to extract insights, sentiment, and topics.

Production-Grade PySpark Script
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf, explode, split, count, desc, array_contains, regexp_replace, lower
from pyspark.sql.types import ArrayType, StringType, FloatType, StructType, StructField
from pyspark.ml.feature import Tokenizer, StopWordsRemover, CountVectorizer, IDF, Word2Vec
from pyspark.ml.clustering import LDA
from pyspark.ml import Pipeline
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import PorterStemmer, WordNetLemmatizer
import datetime

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Natural Language Processing") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.shuffle.partitions", "200") \
    .getOrCreate()

# Download NLTK resources
nltk.download('vader_lexicon')
nltk.download('wordnet')
nltk.download('punkt')

# Load text data
text_data = spark.read.format("delta").load("/mnt/data/text_data")

# Clean text
text_data = text_data \
    .withColumn("cleaned_text", 
                regexp_replace(lower(col("text")), "[^a-zA-Z0-9\\s]", " ")) \
    .withColumn("cleaned_text", 
                regexp_replace(col("cleaned_text"), "\\s+", " "))

# Tokenization
tokenizer = Tokenizer(inputCol="cleaned_text", outputCol="tokens")
tokenized = tokenizer.transform(text_data)

# Remove stop words
remover = StopWordsRemover(inputCol="tokens", outputCol="filtered_tokens")
filtered = remover.transform(tokenized)

# Define stemming UDF
stemmer = PorterStemmer()
@udf(returnType=ArrayType(StringType()))
def stem_tokens(tokens):
    return [stemmer.stem(token) for token in tokens]

# Apply stemming
stemmed = filtered.withColumn("stemmed_tokens", stem_tokens(col("filtered_tokens")))

# Define lemmatization UDF
lemmatizer = WordNetLemmatizer()
@udf(returnType=ArrayType(StringType()))
def lemmatize_tokens(tokens):
    return [lemmatizer.lemmatize(token) for token in tokens]

# Apply lemmatization
processed = stemmed.withColumn("lemmatized_tokens", lemmatize_tokens(col("filtered_tokens")))

# Save processed text
processed.write.format("delta").mode("overwrite").save("/mnt/data/processed_text")

# Sentiment Analysis using VADER
# Define sentiment analysis UDF
sid = SentimentIntensityAnalyzer()
@udf(returnType=StructType([
    StructField("compound", FloatType(), True),
    StructField("positive", FloatType(), True),
    StructField("neutral", FloatType(), True),
    StructField("negative", FloatType(), True)
]))
def analyze_sentiment(text):
    sentiment = sid.polarity_scores(text)
    return (
        sentiment["compound"],
        sentiment["pos"],
        sentiment["neu"],
        sentiment["neg"]
    )

# Apply sentiment analysis
sentiment = processed.withColumn("sentiment", analyze_sentiment(col("text")))
sentiment = sentiment \
    .withColumn("compound_score", col("sentiment.compound")) \
    .withColumn("positive_score", col("sentiment.positive")) \
    .withColumn("neutral_score", col("sentiment.neutral")) \
    .withColumn("negative_score", col("sentiment.negative")) \
    .withColumn("sentiment_label", 
                when(col("compound_score") >= 0.05, "positive")
                .when(col("compound_score") <= -0.05, "negative")
                .otherwise("neutral"))

# Save sentiment analysis results
sentiment.write.format("delta").mode("overwrite").save("/mnt/data/sentiment_analysis")

# Aggregate sentiment by category
sentiment_by_category = sentiment.groupBy("category") \
    .agg(
        count("*").alias("document_count"),
        count(when(col("sentiment_label") == "positive", 1)).alias("positive_count"),
        count(when(col("sentiment_label") == "negative", 1)).alias("negative_count"),
        count(when(col("sentiment_label") == "neutral", 1)).alias("neutral_count"),
        avg("compound_score").alias("avg_compound_score")
    ) \
    .withColumn("positive_percentage", col("positive_count") / col("document_count") * 100) \
    .withColumn("negative_percentage", col("negative_count") / col("document_count") * 100) \
    .withColumn("neutral_percentage", col("neutral_count") / col("document_count") * 100)

# Save sentiment by category
sentiment_by_category.write.format("delta").mode("overwrite").save("/mnt/data/sentiment_by_category")

# Term Frequency-Inverse Document Frequency (TF-IDF)
# Create TF-IDF pipeline
cv = CountVectorizer(inputCol="filtered_tokens", outputCol="tf", vocabSize=10000, minDF=5)
idf = IDF(inputCol="tf", outputCol="tfidf")
tfidf_pipeline = Pipeline(stages=[cv, idf])

# Fit and transform
tfidf_model = tfidf_pipeline.fit(processed)
tfidf_data = tfidf_model.transform(processed)

# Extract vocabulary
vocabulary = cv.fit(processed).vocabulary

# Get top terms by TF-IDF score
from pyspark.ml.functions import vector_to_array
tfidf_data = tfidf_data.withColumn("tfidf_array", vector_to_array(col("tfidf")))

# Create a dataframe with document ID, term, and TF-IDF score
term_scores = tfidf_data.select(
    col("document_id"),
    explode(array_zip(array(*(f"filtered_tokens[{i}]" for i in range(len(vocabulary)))), col("tfidf_array"))).alias("term_score")
)

term_scores = term_scores.select(
    col("document_id"),
    col("term_score._1").alias("term"),
    col("term_score._2").alias("tfidf_score")
)

# Get top terms by document
top_terms_by_document = term_scores \
    .filter(col("tfidf_score") > 0) \
    .orderBy(col("document_id"), col("tfidf_score").desc())

# Save top terms
top_terms_by_document.write.format("delta").mode("overwrite").save("/mnt/data/top_terms")

# Topic Modeling with LDA
# Create LDA model
lda = LDA(k=10, maxIter=10, featuresCol="tf")
lda_model = lda.fit(tfidf_data)

# Transform data
topics_data = lda_model.transform(tfidf_data)

# Extract topics
topics = lda_model.describeTopics(10)
topics_with_terms = topics.withColumn("term", explode(array_zip(col("termIndices"), col("termWeights"))))
topics_with_terms = topics_with_terms.select(
    col("topic"),
    col("term._1").alias("term_index"),
    col("term._2").alias("term_weight")
)

# Map term indices to actual terms
term_mapping = [(i, vocabulary[i]) for i in range(len(vocabulary))]
term_mapping_df = spark.createDataFrame(term_mapping, ["term_index", "term"])

# Join to get terms
topics_with_terms = topics_with_terms.join(term_mapping_df, "term_index")
topics_with_terms = topics_with_terms.orderBy(col("topic"), col("term_weight").desc())

# Save topic model results
topics_with_terms.write.format("delta").mode("overwrite").save("/mnt/data/topic_terms")

# Assign documents to topics
document_topics = topics_data.select(
    col("document_id"),
    col("topicDistribution")
)

# Convert topic distribution to array
document_topics = document_topics.withColumn("topic_dist_array", vector_to_array(col("topicDistribution")))

# Create columns for each topic probability
for i in range(10):
    document_topics = document_topics.withColumn(f"topic_{i}_prob", col("topic_dist_array")[i])

# Determine primary topic
document_topics = document_topics.withColumn(
    "primary_topic",
    array_position(col("topic_dist_array"), array_max(col("topic_dist_array"))) - 1
)

# Save document topics
document_topics.write.format("delta").mode("overwrite").save("/mnt/data/document_topics")

# Word Embeddings with Word2Vec
word2vec = Word2Vec(vectorSize=100, minCount=5, inputCol="filtered_tokens", outputCol="word_embeddings")
word2vec_model = word2vec.fit(processed)
word_embeddings = word2vec_model.transform(processed)

# Save word embeddings
word_embeddings.select("document_id", "word_embeddings").write.format("delta").mode("overwrite").save("/mnt/data/word_embeddings")

# Find similar words
similar_words = {}
for word in vocabulary[:100]:  # Get similar words for top 100 terms
    try:
        similar = word2vec_model.findSynonyms(word, 10)
        similar_words[word] = [(row.word, float(row.similarity)) for row in similar.collect()]
    except:
        pass

# Create dataframe of similar words
similar_words_data = []
for word, similars in similar_words.items():
    for similar_word, similarity in similars:
        similar_words_data.append((word, similar_word, similarity))

similar_words_df = spark.createDataFrame(similar_words_data, ["word", "similar_word", "similarity"])
similar_words_df.write.format("delta").mode("overwrite").save("/mnt/data/similar_words")

# Named Entity Recognition
# Define NER UDF
import spacy
nlp = spacy.load("en_core_web_sm")

@udf(returnType=ArrayType(StructType([
    StructField("text", StringType(), True),
    StructField("label", StringType(), True)
])))
def extract_entities(text):
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))
    return entities

# Apply NER
entities = processed.withColumn("entities", extract_entities(col("text")))
entities = entities.select(
    col("document_id"),
    col("text"),
    explode(col("entities")).alias("entity")
)
entities = entities.select(
    col("document_id"),
    col("text"),
    col("entity.text").alias("entity_text"),
    col("entity.label").alias("entity_type")
)

# Save entities
entities.write.format("delta").mode("overwrite").save("/mnt/data/named_entities")

# Aggregate entities by type
entity_counts = entities.groupBy("entity_type", "entity_text").count().orderBy(desc("count"))
entity_counts.write.format("delta").mode("overwrite").save("/mnt/data/entity_counts")

# Text Classification
# Join with categories
text_with_categories = processed.join(
    sentiment.select("document_id", "category"),
    "document_id"
)

# Create feature vector for classification
from pyspark.ml.feature import HashingTF
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Create TF features
hashingTF = HashingTF(inputCol="filtered_tokens", outputCol="features", numFeatures=10000)
featurized = hashingTF.transform(text_with_categories)

# Split data
train_data, test_data = featurized.randomSplit([0.8, 0.2], seed=42)

# Train classifier
rf = RandomForestClassifier(labelCol="category", featuresCol="features", numTrees=100)
model = rf.fit(train_data)

# Make predictions
predictions = model.transform(test_data)

# Evaluate model
evaluator = MulticlassClassificationEvaluator(labelCol="category", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print(f"Classification Accuracy: {accuracy}")

# Save model and predictions
predictions.write.format("delta").mode("overwrite").save("/mnt/data/text_classification_results")

# Feature importance
feature_importance = model.featureImportances
feature_importance_df = spark.createDataFrame(
    [(i, float(feature_importance[i])) for i in range(len(feature_importance)) if feature_importance[i] > 0],
    ["feature_index", "importance"]
)
feature_importance_df = feature_importance_df.orderBy(desc("importance"))
feature_importance_df.write.format("delta").mode("overwrite").save("/mnt/data/text_feature_importance")

# Create NLP dashboard view
spark.sql("""
CREATE OR REPLACE VIEW nlp_dashboard AS
SELECT
    t.document_id,
    t.text,
    t.category,
    s.sentiment_label,
    s.compound_score,
    s.positive_score,
    s.negative_score,
    s.neutral_score,
    dt.primary_topic,
    e.entities
FROM delta.`/mnt/data/text_data` t
LEFT JOIN (
    SELECT
        document_id,
        sentiment_label,
        compound_score,
        positive_score,
        negative_score,
        neutral_score
    FROM delta.`/mnt/data/sentiment_analysis`
) s ON t.document_id = s.document_id
LEFT JOIN (
    SELECT
        document_id,
        primary_topic
    FROM delta.`/mnt/data/document_topics`
) dt ON t.document_id = dt.document_id
LEFT JOIN (
    SELECT
        document_id,
        collect_list(struct(entity_text, entity_type)) as entities
    FROM delta.`/mnt/data/named_entities`
    GROUP BY document_id
) e ON t.document_id = e.document_id
""")

print("Natural Language Processing completed successfully")
Explanation
This script implements a comprehensive natural language processing pipeline for analyzing text data. It begins with text preprocessing, including cleaning, tokenization, stop word removal, stemming, and lemmatization to prepare the text for analysis.

The pipeline then performs sentiment analysis using VADER, assigning positive, negative, or neutral labels to each document and calculating sentiment scores. It aggregates sentiment by category to identify trends across different segments. The script creates TF-IDF vectors to identify important terms in each document and implements topic modeling using Latent Dirichlet Allocation (LDA) to discover hidden themes in the corpus.

It generates word embeddings using Word2Vec, enabling semantic similarity analysis between words. The pipeline also performs named entity recognition to extract and categorize entities like people, organizations, and locations. Additionally, it builds a text classification model using Random Forest to categorize documents based on their content. All analysis results are stored in Delta tables and unified in a dashboard view for exploration. This solution helps organizations extract valuable insights from unstructured text data, understand customer sentiment, identify important topics, and classify documents automatically.

20. Image Processing Pipeline
Business Scenario
Organizations need to process and analyze large volumes of images for tasks like classification, object detection, and feature extraction.

Production-Grade PySpark Script
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf, lit, array, struct, explode
from pyspark.sql.types import StringType, ArrayType, StructType, StructField, FloatType, IntegerType, BinaryType
from pyspark.ml.image import ImageSchema
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.applications import ResNet50, MobileNetV2
from tensorflow.keras.applications.resnet50 import preprocess_input as resnet_preprocess
from tensorflow.keras.preprocessing import image
from io import BytesIO
import datetime

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Image Processing Pipeline") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.shuffle.partitions", "200") \
    .config("spark.driver.memory", "16g") \
    .config("spark.executor.memory", "16g") \
    .getOrCreate()

# Load pre-trained models
resnet_model = ResNet50(weights='imagenet', include_top=False, pooling='avg')
mobilenet_model = MobileNetV2(weights='imagenet', include_top=False, pooling='avg')

# Define schema for image metadata
metadata_schema = StructType([
    StructField("image_id", StringType(), True),
    StructField("path", StringType(), True),
    StructField("label", StringType(), True),
    StructField("width", IntegerType(), True),
    StructField("height", IntegerType(), True),
    StructField("channels", IntegerType(), True),
    StructField("format", StringType(), True),
    StructField("date_captured", StringType(), True)
])

# Load image metadata
image_metadata = spark.read.format("delta").schema(metadata_schema).load("/mnt/data/image_metadata")

# Load images
images = spark.read.format("binaryFile") \
    .option("pathGlobFilter", "*.jpg,*.jpeg,*.png") \
    .option("recursiveFileLookup", "true") \
    .load("/mnt/data/images")

# Join metadata with images
images_with_metadata = images.join(
    image_metadata,
    images.path == image_metadata.path,
    "inner"
)

# Basic image processing functions
@udf(returnType=BinaryType())
def resize_image(content, target_size=224):
    """Resize image to target size"""
    try:
        # Convert binary content to numpy array
        file_bytes = np.asarray(bytearray(content), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        # Resize image
        img_resized = cv2.resize(img, (target_size, target_size))

        # Encode back to binary
        _, buffer = cv2.imencode('.jpg', img_resized)
        return bytes(buffer)
    except Exception as e:
        return None

@udf(returnType=ArrayType(FloatType()))
def extract_resnet_features(content):
    """Extract features using ResNet50"""
    try:
        # Convert binary content to numpy array
        file_bytes = np.asarray(bytearray(content), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        # Resize and preprocess for ResNet
        img = cv2.resize(img, (224, 224))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = np.expand_dims(img, axis=0)
        img = resnet_preprocess(img)

        # Extract features
        features = resnet_model.predict(img)
        return features[0].tolist()
    except Exception as e:
        return None

@udf(returnType=ArrayType(FloatType()))
def extract_mobilenet_features(content):
    """Extract features using MobileNetV2"""
    try:
        # Convert binary content to numpy array
        file_bytes = np.asarray(bytearray(content), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        # Resize and preprocess for MobileNet
        img = cv2.resize(img, (224, 224))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = np.expand_dims(img, axis=0)
        img = tf.keras.applications.mobilenet_v2.preprocess_input(img)

        # Extract features
        features = mobilenet_model.predict(img)
        return features[0].tolist()
    except Exception as e:
        return None

@udf(returnType=StructType([
    StructField("mean_r", FloatType(), True),
    StructField("mean_g", FloatType(), True),
    StructField("mean_b", FloatType(), True),
    StructField("std_r", FloatType(), True),
    StructField("std_g", FloatType(), True),
    StructField("std_b", FloatType(), True)
]))
def extract_color_stats(content):
    """Extract color statistics"""
    try:
        # Convert binary content to numpy array
        file_bytes = np.asarray(bytearray(content), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        # Calculate mean and std for each channel
        means = cv2.mean(img)
        stds = cv2.meanStdDev(img)[1].flatten()

        return (
            float(means[2]),  # R
            float(means[1]),  # G
            float(means[0]),  # B
            float(stds[2]),   # R std
            float(stds[1]),   # G std
            float(stds[0])    # B std
        )
    except Exception as e:
        return None

@udf(returnType=ArrayType(StructType([
    StructField("x", IntegerType(), True),
    StructField("y", IntegerType(), True),
    StructField("width", IntegerType(), True),
    StructField("height", IntegerType(), True),
    StructField("class", StringType(), True),
    StructField("confidence", FloatType(), True)
])))
def detect_objects(content):
    """Detect objects using pre-trained model"""
    try:
        # This is a placeholder for actual object detection
        # In a real implementation, you would use a model like YOLO, SSD, or Faster R-CNN

        # For demonstration, return dummy detections
        return [
            (100, 100, 200, 200, "person", 0.95),
            (300, 300, 100, 100, "car", 0.85)
        ]
    except Exception as e:
        return None

# Process images
processed_images = images_with_metadata \
    .withColumn("resized_image", resize_image(col("content"))) \
    .withColumn("resnet_features", extract_resnet_features(col("content"))) \
    .withColumn("mobilenet_features", extract_mobilenet_features(col("content"))) \
    .withColumn("color_stats", extract_color_stats(col("content"))) \
    .withColumn("detected_objects", detect_objects(col("content")))

# Save processed images
processed_images.select(
    "image_id",
    "path",
    "label",
    "width",
    "height",
    "channels",
    "format",
    "date_captured",
    "resized_image",
    "resnet_features",
    "mobilenet_features",
    "color_stats",
    "detected_objects"
).write.format("delta").mode("overwrite").save("/mnt/data/processed_images")

# Explode detected objects for analysis
object_detections = processed_images.select(
    "image_id",
    "path",
    "label",
    explode(col("detected_objects")).alias("detection")
)

object_detections = object_detections.select(
    "image_id",
    "path",
    "label",
    col("detection.x").alias("x"),
    col("detection.y").alias("y"),
    col("detection.width").alias("width"),
    col("detection.height").alias("height"),
    col("detection.class").alias("object_class"),
    col("detection.confidence").alias("confidence")
)

# Save object detections
object_detections.write.format("delta").mode("overwrite").save("/mnt/data/object_detections")

# Aggregate object detections by class
object_counts = object_detections.groupBy("object_class").count().orderBy(desc("count"))
object_counts.write.format("delta").mode("overwrite").save("/mnt/data/object_counts")

# Image classification using extracted features
# Prepare data for classification
classification_data = processed_images.select(
    "image_id",
    "resnet_features",
    "label"
)

# Convert label to numeric
from pyspark.ml.feature import StringIndexer
label_indexer = StringIndexer(inputCol="label", outputCol="label_idx")
indexed_data = label_indexer.fit(classification_data).transform(classification_data)

# Assemble features
assembler = VectorAssembler(inputCol="resnet_features", outputCol="features")
assembled_data = assembler.transform(indexed_data)

# Split data
train_data, test_data = assembled_data.randomSplit([0.8, 0.2], seed=42)

# Train classifier
rf = RandomForestClassifier(labelCol="label_idx", featuresCol="features", numTrees=100)
model = rf.fit(train_data)

# Make predictions
predictions = model.transform(test_data)

# Evaluate model
evaluator = MulticlassClassificationEvaluator(labelCol="label_idx", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print(f"Classification Accuracy: {accuracy}")

# Save classification results
predictions.select(
    "image_id",
    "label",
    "label_idx",
    "prediction",
    "probability"
).write.format("delta").mode("overwrite").save("/mnt/data/image_classification_results")

# Save model metrics
model_metrics = [{
    "model_type": "RandomForest",
    "feature_type": "ResNet50",
    "training_date": datetime.datetime.now().isoformat(),
    "accuracy": accuracy,
    "num_classes": label_indexer.labels.size,
    "num_trees": 100
}]

spark.createDataFrame(model_metrics).write \
    .format("delta") \
    .mode("append") \
    .save("/mnt/data/image_model_metrics")

# Image similarity analysis
# Calculate pairwise similarity between images
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import BucketedRandomProjectionLSH

# Convert features to vectors
feature_vectors = processed_images.select(
    "image_id",
    udf(lambda x: Vectors.dense(x), VectorUDT())(col("resnet_features")).alias("feature_vector")
)

# Apply LSH for approximate nearest neighbor search
brp = BucketedRandomProjectionLSH(inputCol="feature_vector", outputCol="hashes", numHashTables=10)
model = brp.fit(feature_vectors)
transformed = model.transform(feature_vectors)

# Find similar images for a sample of images
sample_images = feature_vectors.limit(10)
similar_images = model.approxSimilarityJoin(sample_images, transformed, 0.1, "distance")

# Format results
similar_images = similar_images.select(
    col("datasetA.image_id").alias("query_image"),
    col("datasetB.image_id").alias("similar_image"),
    col("distance")
)

# Save similarity results
similar_images.write.format("delta").mode("overwrite").save("/mnt/data/image_similarity")

# Create image analysis dashboard view
spark.sql("""
CREATE OR REPLACE VIEW image_analysis_dashboard AS
SELECT
    i.image_id,
    i.path,
    i.label,
    i.width,
    i.height,
    i.format,
    i.date_captured,
    cs.mean_r,
    cs.mean_g,
    cs.mean_b,
    od.object_counts,
    cr.prediction_label,
    cr.confidence
FROM delta.`/mnt/data/image_metadata` i
LEFT JOIN (
    SELECT
        image_id,
        color_stats.mean_r,
        color_stats.mean_g,
        color_stats.mean_b
    FROM delta.`/mnt/data/processed_images`
) cs ON i.image_id = cs.image_id
LEFT JOIN (
    SELECT
        image_id,
        collect_list(struct(object_class, count)) as object_counts
    FROM (
        SELECT
            image_id,
            object_class,
            count(*) as count
        FROM delta.`/mnt/data/object_detections`
        GROUP BY image_id, object_class
    )
    GROUP BY image_id
) od ON i.image_id = od.image_id
LEFT JOIN (
    SELECT
        image_id,
        label as prediction_label,
        max(probability) as confidence
    FROM delta.`/mnt/data/image_classification_results`
    GROUP BY image_id, label
) cr ON i.image_id = cr.image_id
""")

print("Image Processing Pipeline completed successfully")
Explanation
This script implements a comprehensive image processing pipeline for analyzing large volumes of images. It loads image data and metadata, then performs multiple types of analysis in parallel. The pipeline resizes images for consistent processing and extracts features using pre-trained deep learning models (ResNet50 and MobileNetV2), which capture high-level visual characteristics. It calculates color statistics to understand the visual composition of each image and performs object detection to identify and locate objects within images.

The script builds an image classification model using the extracted features, enabling automatic categorization of images. It also implements image similarity analysis using locality-sensitive hashing (LSH) to find visually similar images efficiently. All processing results are stored in Delta tables and unified in a dashboard view for exploration.

This solution helps organizations extract valuable insights from image data, automate image categorization, detect objects, and find similar images across large collections. The use of pre-trained models enables high-quality analysis without requiring extensive labeled training data.

