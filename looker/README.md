<https://docs.looker.com/reference/explore-params/cancel_grouping_fields>


So, for example, we might have this filter field defined:
```
  filter: order_region {
    type: string
  }
```

And, we might also have this dimension defined in the same view file:
```
dimension: region {
    type: string
    sql: ${TABLE}.region ;;
}
```
Then, we could reference both of these in the `WHERE` clause of the derived table:
```
view: customer_facts {
  derived_table: {
    sql:
      SELECT
        customer_id,
        SUM(sale_price) AS lifetime_spend
      FROM
        order
      WHERE
        {\% condition order_region \%} order.region {\% endcondition \%}
    ;;
  }
 
This uses the Liquid `{\% condition filter_name \%} sql_or_lookml_reference {\% endcondition \%}` variable.  This variable returns the value of the filter you ask for with `filter_name`, applied to the `sql_or_lookml_reference` as SQL.
The templated filter tags are always transformed into a logical expression. For example, if the user entered “Northeast” into the `order_region` filter, Looker would turn the Liquid into: 
 
order.region = 'Northeast'
```

<https://discourse.looker.com/t/how-to-create-dynamic-date-filter-for-user/14370/3>

<https://docs.looker.com/data-modeling/learning-lookml/templated-filters>


<https://dashboards.bdp.roku.com/folders/1477> . dashboards

<https://help.looker.com/hc/en-us/articles/360001286007-Creating-Filtered-Measures->

<https://docs.looker.com/exploring-data/exploring-data>

<https://docs.looker.com/video-library/exploring-data> . Video

```
1) create a parameter as outlined here 
<https://docs.looker.com/reference/field-params/parameter>
, which is what the user will interact with, notice that we can limit user input to particular values you specify via "allowed values" 

2) We'll tie that parameter to conditional logic in a dimension that will dynamically change the underlying sql query based on the user input



So the first part is we'd create a parameter like this: 

 parameter: limited_date_filter {
    type: string
    allowed_value: { value: "Is in the past 7 Days" }
    allowed_value: { value: "Is in the past 30 Days" }
    allowed_value: { value: "All Dates" }
  }
  
and I'm seeing what we can do to link that to SQL logic that sums based on the selected value  

measure: total_sales {
    type: number
    sql: 
    {% if limited_date_filter._parameter_value == "'Is in the past 7 Days'" %}
    SUM(CASE WHEN ${your_date} BETWEEN GETDATE() AND Date >= CAST(DATEADD(day, -7, GETDATE())) THEN ${sale_price} END)
    {% elsif limited_date_filter._parameter_value == "'Is in the past 30 Days'" %}
    SUM(CASE WHEN ${your_date} BETWEEN GETDATE() AND Date >= CAST(DATEADD(day, -30, GETDATE())) THEN ${sale_price} END)
    
    and so on... ;;
  }
  
  
  measure: runningTotal{
     type: sum
     sql: ${TABLE}.“runningTotal” ;;
}
  
  Would recommend creating a dashboard with two tiles. One tile will be with a single-record chart () that will show experiment_id, start date, end date, etc
 ``` 
 
 <https://docs.looker.com/exploring-data/visualizing-query-results/single-record-options>
  
<https://training.looker.com/> mlubinsky@ho / LeVe>

![look](Looker_terms.png)

### Model
Model files define Explores and their relationships to other views.

<https://dashboards.bdp.roku.com/projects/dea-foundation-prod/files/account_device_channel_related.model.lkml>

### Explore
<https://docs.looker.com/reference/explore-reference>
An Explore is a view that users can query. You can think of the Explore as a starting point for a query, or in SQL terms, as the FROM in a SQL statement. Not all views are Explores, because not all views describe an entity of interest.

An Explore serves as the starting point for a query in the Looker application. Explores reference views and each Explore can contain joins to other views. Explores should typically be declared in a model file.

```
connection: "dea_redshift_-_analytics_prod"   => dea_redshift_-_analytics_dev

explore: dim_experiment{
  label: "Amoeba experiment"
  description: "Amoeba A/B experiments"
  =>! view_name: agg_channel_subscription_metrics_time_grain
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
A view is stored in a .view.lkml file.

A view declaration defines a list of fields (dimensions or measures) and their linkage to an underlying table or ```derived table```.

 GUI: Create View from Table
 <https://dashboards.bdp.roku.com/projects/dea-foundation-prod/files/agg_amoeba_trc_kpi_daily.view.lkml>

<https://docs.looker.com/reference/view-reference>

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
  
  set: first_set {
    fields: [field_one, field_two]
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

### Derived table
<https://docs.looker.com/data-modeling/learning-lookml/derived-tables>

<https://docs.looker.com/data-modeling/learning-lookml/lookml-terms-and-concepts#derived-table> 

### Dimension_group

<https://docs.looker.com/reference/field-params/dimension_group>

```
  dimension_group: created {
    type: time
    timeframes: [date, week]
    sql: ${TABLE}.created_at ;;
  }
```
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

<https://discourse.looker.com/t/how-to-create-dynamic-date-filter-for-user/14370/3>
Attributes:
  - allow_multiple_values: true | false
  - required: true | false

If You Want Filters A User Can Change, But Not Remove, Consider always_filter
If you want to force users to use a specific set of filters, but where the default value can be changed, try always_filter instead.

Example: 
the filter is given a numeric value. 
The measure will add only orders that have a price of more than 100:
```
measure: sales_18_to_25 {
  type: sum
  filters: [customers.age: ">=18 AND <=25"]
  sql: ${orders.price} ;;
}
```

<https://docs.looker.com/reference/filter-expressions>

<https://redpillanalytics.com/combining-advanced-and-custom-filters-in-looker/>

<https://blog.redpillanalytics.com/combining-advanced-and-custom-filters-in-looker-2c45590d1129>

Range filter

<https://discourse.looker.com/t/date-range-filter-with-relative-dates/11507/5>

### Custom dimentions templetated filters

<https://docs.looker.com/data-modeling/learning-lookml/templated-filters>
```
view: customer_facts {
  derived_table: {
    sql:
      SELECT
        customer_id,
        SUM(sale_price) AS lifetime_spend
      FROM
        order
      WHERE
        {\% condition order_region \%} order.region {\% endcondition \%}
    ;;
  }
·
  filter: order_region {
    type: string
  }
}
```
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

