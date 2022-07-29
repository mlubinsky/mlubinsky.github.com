### CSV

```
from pyspark.sql.types import *

csv_schema = StructType(
   [   
       StructField('id', IntegerType(), True),
       StructField('genre_id', LongType(), True),
       StructField('downloads_weight', DoubleType(), True),
       StructField('mps_total_downloads_weight', DoubleType(), True),
       StructField('revenue_weight', DoubleType(), True),
       StructField('mps_total_revenue_weight', DoubleType(), True),
       StructField('mps_monetization_sov_weight', DoubleType(), True),
       StructField('rau_weight', DoubleType(), True),
       StructField('afu_weight', DoubleType(), True),
       StructField('adu_weight', DoubleType(), True),
       StructField('atu_weight', DoubleType(), True),
       StructField('ris_weight', DoubleType(), True),
       StructField('incremental_ratings_average_weight', DoubleType(), True),
       StructField('cumulative_ratings_average_weight', DoubleType(), True),
       StructField('cumulative_rating_count_weight', DoubleType(), True),
       StructField('incremental_rating_count_weight', DoubleType(), True)
   ]
)      
fname="file:/dbfs/FileStore/uploads/mlubinsky/20220728_mps_weights.csv"

df = spark.read.option("header",True).option("delimiter",",").schema(csv_schema).csv(fname)

df_ordered=df.select("genre_id","downloads_weight","mps_total_downloads_weight","revenue_weight","mps_total_revenue_weight","mps_monetization_sov_weight","rau_weight","afu_weight","adu_weight","atu_weight","ris_weight","cumulative_rating_count_weight","incremental_rating_count_weight","cumulative_ratings_average_weight","incremental_ratings_average_weight")
```

### CLEAR

aws s3 rm --recursive s3://aardvark-prod-dca-data/oss/MPS_APPIQ_TAXONOMY_WEIGHTS

### DELTA
```
### WRITE
import pyspark.sql.functions as F
path = "s3://aardvark-prod-dca-data/oss/MPS_APPIQ_TAXONOMY_WEIGHTS/"
df_ordered.withColumn("version", F.lit("1.0.0")).write.partitionBy("version").format("delta").save(path)

###   READ
from bdp.common.spark.spark_utils import load_as_spark_df
genre_params={"version":"1.0.0"}
df_genre_weights = load_as_spark_df(spark, "MPS_APPIQ_TAXONOMY_WEIGHTS_O", genre_params)


```
