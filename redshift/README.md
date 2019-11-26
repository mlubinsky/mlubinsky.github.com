
Both Snowflake and Redshift Spectrum allow queries on ORC files as external files located in Amazon S3. However, Snowflake edged out Redshift Spectrum for its ability to also load and transform ORC data files directly into Snowflake.


## RedShift
<http://www.sqlhaven.com/>

You can create primary key constraint while creating tables in Redshift database but 
*it will not be enforced while loading Redshift tables*. 
Redshift query planner uses these constraints to create better query execution plan. |
If Primary key is set at the column level, it must be on a single column

<https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_TABLE_examples.html>

<https://docs.aws.amazon.com/redshift/latest/dg/t_Defining_constraints.html>

<https://docs.aws.amazon.com/redshift/latest/dg/c_redshift_system_overview.html>

<https://github.com/JefClaes/amazon-redshift-fundamentals>

<https://blog.panoply.io/aws-redshift-tutorial>

<https://www.intermix.io/blog/short-query-acceleration/>

<https://medium.com/teads-engineering/give-meaning-to-100-billion-events-a-day-part-ii-how-we-use-and-abuse-redshift-to-serve-our-data-bc23d2ed3e07>

<https://www.intermix.io/blog/14-data-pipelines-amazon-redshift/>

<https://epiphany.pub/post?refId=a362fd3bffdc7eecde1838916fb8f4c267f5672b3774bd86dd23dce9dac72bee> hate log

<https://www.intermix.io/blog/modern-etl-tools-for-amazon-redshift/> 



### Litvinchik
<https://tech.marksblogg.com/billion-nyc-taxi-rides-redshift-large-cluster.html>

<https://tech.marksblogg.com/all-billion-nyc-taxi-rides-redshift.html>

<https://tech.marksblogg.com/importing-data-from-s3-into-redshift.html>

<https://tech.marksblogg.com/billion-nyc-taxi-rides-redshift.html>

### Spectrum 

Amazon Redshift Spectrum to query data directly from files on Amazon S3.
<https://docs.aws.amazon.com/redshift/latest/dg/c-getting-started-using-spectrum.html>

<https://tech.iheart.com/how-we-leveraged-redshift-spectrum-for-elt-in-our-land-of-etl-cf01edb485c0>

<https://medium.com/@thejaravi/how-we-leveraged-redshift-spectrum-for-elt-in-our-land-of-etl-cf01edb485c0>

Redshift Spectrum is new add-on service for Redshift that Amazon introduced mid-2017. 
It allows you to leverage Redshift to query data directly on S3. 
Redshift Spectrum is a good option for those who already have/work with Redshift. 
For those who do not, take a look at Athena. 

Athena is much like Redshift Spectrum with the exception of the chosen execution engine (Athena uses Presto) 
whereas Spectrum uses Redshift. It should be noted that Spectrum also follows pay-per-query pricing model like Athena.
Let’s look at how Redshift and Spectrum communicate with each other, 
how tables are created on top of stores such as S3 and just how much interoperability is provided.
Spectrum needs an external meta store for the data catalog to maintain table definitions; 
we used a Hive meta store for this purpose. Our Hive/Spectrum meta store is simply a RDS instance running MariaDB.
Once we setup Spectrum to talk with our Redshift cluster and use the newly created schema space in the Hive meta store,
any external table created in this schema using Hive is visible and usable immediately from Redshift.
You can query these tables directly from Redshift and Redshift/Spectrum will automatically move the required
portion of data (based on the query) on to Redshift cluster and execute it there.



## SnowFlake

<https://medium.com/hashmapinc/snowflakes-cloud-data-warehouse-what-i-learned-and-why-i-m-rethinking-the-data-warehouse-75a5daad271c>

<https://medium.com/@richiebachala/snowflake-redshift-bigquery-b84d2cb60168>
<https://www.alooma.com/answers/why-did-you-choose-snowflake-over-amazon-redshift-for-your-cloud-data-warehouse>

<https://www.alooma.com/blog/a-guide-to-selecting-the-right-cloud-data-warehouse>

<https://www.periscopedata.com/blog/interactive-analytics-redshift-bigquery-snowflake>

<https://hevodata.com/blog/snowflake-vs-redshift/>


