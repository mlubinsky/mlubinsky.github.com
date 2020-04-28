<https://training.looker.com/> mlubinsky@ho / LeVe>

![look](Looker_terms.png)

### Model
<https://dashboards.bdp.roku.com/projects/dea-foundation-prod/files/account_device_channel_related.model.lkml>

```
connection: "dea_redshift_-_analytics_prod"   => dea_redshift_-_analytics_dev

explore: dim_experiment{
  label: "Amoeba experiment"
  description: "Amoeba A/B experiments"
  join: another_table {
    sql_on:
    type:
    relationship: many_to_one . | one_to_one
  }
  join:  {
  } ...
  always_filter {
       filters: {
                field:
                value:
                }
       filters: {
                field:
                value:
                }
                
  }
  
}
```
### View:

<https://dashboards.bdp.roku.com/projects/dea-foundation-prod/files/agg_amoeba_reports.view.lkml>

<https://dashboards.bdp.roku.com/projects/dea-foundation-prod/files/agg_amoeba_allocation_events_daily.view.lkml>

<https://dashboards.bdp.roku.com/projects/dea-foundation-prod/files/agg_amoeba_allocation_events.view.lkml>

Example:
```
view: agg_amoeba_allocation_events {
  sql_table_name: dea.agg_amoeba_allocation_events ;;

  dimension: account_id {
    type: string
    sql: ${TABLE}.account_id ;;
  }
```
  
Defines:
```
- derived table
- measure, 
- dimensions, 
- filters
```

<https://docs.looker.com/exploring-data/creating-looker-expressions/looker-functions-and-operators>

<https://docs.looker.com/data-modeling/learning-lookml/lookml-terms-and-concepts>

<https://docs.looker.com/data-modeling/learning-lookml/lookml-terms-and-concepts#derived-table> Derived table

<https://looker.com/guide>

<https://discourse.looker.com/>

<https://github.com/looker-open-source>

<https://github.com/alison985/awesome-looker>

<https://docs.looker.com/reference/field-reference/dimension-type-reference>

In Looker, queries are grouped by the model to which they belong. Your users see models listed under the Explore menu:

```
model: (.model.lkml)  which tables to use and how they should be joined together and Explores

explore:  defined within a model file, but if you’re working with native derived tables you might make it its own file.
 Each Explore declaration includes join logic to join any view that Looker can determine is related to the Explore.
An Explore is a view that users can query.
 
view: (.view.lkml) define the view, its dimensions and measures, and its field sets.

join: lets you combine data from multiple views

dimension - is a groupable field (inside view)  and can be used to filter query results.

dimension_group:   example -  duration dimension,  dimension group specify diffrent units of measure

measure -  is a field that uses a SQL aggregate function, such as COUNT, SUM, AVG, MIN, or MAX. Any field computed based on the values of other measure values is also a measure. Measures can be used to filter grouped values. For example, measures for a Sales view might include total items sold (a count), total sale price (a sum), and average sale price (an average).

set . ???

Parameters in Looker increase interactivity for users and provide flexibility from the front end perspective without having to write custom code for each and every field the user asks for.
```
### Liquid variables
<https://docs.looker.com/reference/liquid-variables>

<https://blog.redpillanalytics.com/how-to-create-a-basic-parameter-in-looker-using-a-liquid-variable-e97d2b9b4669>

### Filters
<https://docs.looker.com/reference/filter-expressions>

<https://redpillanalytics.com/combining-advanced-and-custom-filters-in-looker/>

<https://blog.redpillanalytics.com/combining-advanced-and-custom-filters-in-looker-2c45590d1129>

### Custom dimentions

<https://docs.looker.com/data-modeling/learning-lookml/templated-filters>

<https://help.looker.com/hc/en-us/articles/360001285847-Timeframe-vs-Timeframe-Analysis-Using-Templated-Filters>

### Looker API

https://docs.looker.com/reference/api-and-integration/api-getting-started



https://www.youtube.com/watch?v=OEbttXD17lA A/B testing with looker


SQL block
<https://docs.looker.com/data-modeling/learning-lookml/sql-and-referring-to-lookml#sql_block> 

<https://docs.looker.com/video-library/data-modeling>

<https://docs.looker.com/data-modeling/learning-lookml/extends>  Looker has the option to extend Explores, views, and LookML dashboards so that you can reuse the code

<https://www.youtube.com/user/LookerData>




<https://docs.looker.com/data-modeling/learning-lookml/caching> Caching Queries

<https://looker.com/blog/data-science-with-looker-and-python-part-two> . Data Science with looker


<https://looker.com/blog>


### Lookml-tools
<https://discourse.looker.com/t/lookml-tools-better-looker-code-user-experience-and-data-governance/12877>
<https://ww-tech.github.io/lookml-tools/> 

### Programmatic LookML Generation
<https://www.youtube.com/watch?v=cdyn-KLwyfc> .   
<https://github.com/llooker/lookmlscript>

## Extension framework
<https://looker.com/blog/empowering-developers-to-create-powerful-custom-data-experiences>

## Snowflake

<https://blog.redpillanalytics.com/managing-snowflake-data-warehouse-compute-in-looker-e445543987b2>

<https://looker.com/blog/using-snowflake-mvs-in-looker>

