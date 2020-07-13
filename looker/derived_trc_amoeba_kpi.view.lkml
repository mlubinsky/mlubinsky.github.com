view: derived_trc_amoeba_kpi {

 derived_table: {
    sql:
       SELECT
       exp_id,
       bucket,
       date_key,
      'sec_streamed_dim' as dummy_dim,
       device_segment,
       content_type,
       profile_type,
       device_id,
       seconds_streamed  as seconds,
       0 as bounced10min,
       CASE
              WHEN content_provider_id IN
               ('epix_live',  'showtime', 'showtime_film',  'starz_live', 'hiya', 'acorn_tv',
                'fandor', 'showtime_live',  'epix', 'starz',  'shout_factory',  'pantaya',  'hbo_live', 'cinemax_live', 'upff')
              THEN  'SVOD'
              WHEN content_id like  '%svod%'              THEN  'SVOD'
              WHEN content_provider_id like  '%svod%'     THEN  'SVOD'
              WHEN provider_id like  '%svod%'             THEN  'SVOD'
              WHEN provider_id =  'hbo'                   THEN  'SVOD'
             ELSE 'AVOD' END
        AS economic_model,
        0 as distinct_7days,
        DATE(NULL) as start_date
        FROM roku.agg_amoeba_trc_device_ux_grid_metrics_daily
        WHERE date_key > '2020-05-01'
        AND {% condition f_date %} date_key {% endcondition %}
        AND {% condition f_exp_id %} exp_id {% endcondition %}

      UNION  ALL  -- allocation events
      SELECT distinct
      experiment_id as exp_id,
      bucket_name as bucket,
      dt_key as date_key,
      'allocated_dim' as dummy_dim,
      NULL as device_segment,
      NULL as content_type,
      NULL as profile_type,
      device_id,
      0 as seconds,
      0 as bounced10min,
      NULL as economic_model,
      0 as distinct_7days,
      DATE(NULL) as start_date
      FROM dea.agg_amoeba_allocation_events B
      WHERE dt_key > '2020-05-01'
      AND {% condition f_date %} dt_key {% endcondition %}
      AND {% condition f_exp_id %} exp_id {% endcondition %}
/*
      UNION ALL --  bounced10min
      SELECT
      exp_id,
      bucket,
      date_key,
      'bounce_rate' as dummy_dim,
      NULL as device_segment,
      NULL as content_type,
      NULL as profile_type,
      device_id,
      0 as seconds,
      CASE
        WHEN SUM(seconds_streamed) < 600 THEN 0
        ELSE 1
      END as bounced10min,

      NULL as economic_model,
      0 as distinct_7days,
      DATE(NULL) as start_date
      FROM roku.agg_amoeba_trc_device_ux_grid_metrics_daily
      WHERE date_key > '2020-05-01'
      AND {% condition f_date %} date_key {% endcondition %}
      AND {% condition f_exp_id %} exp_id {% endcondition %}
      GROUP BY exp_id, bucket, date_key,       device_id


      UNION ALL   -- distinct_7days
      SELECT
      exp_id,
      bucket,
      date_key,
      'distinct_days' as dummy_dim,
      NULL as device_segment,
      NULL as content_type,
      NULL as profile_type,
      device_id,
      0 as seconds,
      0 as bounced10min,
      NULL as economic_model,
      count(distinct date_key)  as distinct_7days,
      start_date
      FROM roku.agg_amoeba_trc_device_ux_grid_metrics_daily
      WHERE date_key > '2020-05-01'
      AND {% condition f_exp_id %} exp_id {% endcondition %}
      AND date_key BETWEEN start_date and start_date+6 -- in Redshift between in inclusive
      GROUP BY exp_id, bucket, date_key, device_id, start_date
*/

       ;;
   }

  filter: f_exp_id {
    type: string
  }

  filter: f_date {
    type: date
  }

  # https://dashboards.bdp.roku.com/dashboards/3666
  # https://dashboards.bdp.roku.com/explore/device_usage_related/agg_device_livetv_usage_metrics_tz?qid=1vQjAHoYqiGaJ4EzOwoGwu&origin_space=2156&toggle=vis
  # https://dashboards.bdp.roku.com/explore/account_device_channel_related/derived_trc_amoeba_kpi?toggle=fil,vis&qid=pUGZ6Gd6VG4JuBXJrQzQ4R

  dimension: seconds {
    type: number
    hidden: yes
    sql: ${TABLE}.seconds ;;
  }

  dimension: bucket {
    type: string
    sql: ${TABLE}.bucket ;;
  }

  dimension:bounced10min {
    type: number
    sql: ${TABLE}.bounced10min ;;
  }
  dimension: device_segment {
    type: string
    sql: ${TABLE}.device_segment ;;
  }
  dimension: dummy_dim { # bounce_rate, allocated_dim, streamed_dim
    type: string
    sql: ${TABLE}.dummy_dim ;;
  }

  dimension: exp_id {
    type: string
    sql: ${TABLE}.exp_id ;;
  }

  dimension: content_type {
    type: string
    sql: ${TABLE}.content_type ;;
  }

  dimension: profile_type {
    type: string
    sql: ${TABLE}.profile_type ;;
  }

  dimension_group: date_key {
    type: time
    timeframes: [
      raw,
      date,
      week,
      month,
      quarter,
      year
    ]
    convert_tz: no
    datatype: date
    sql: ${TABLE}.date_key ;;
  }

  dimension: device_id {
    type: string
    sql: ${TABLE}.device_id ;;
  }


  dimension: economic_model {
    description: "SVOD or AVOD"
    type: string
    sql: ${TABLE}.economic_model;;
  }


#  ------   ABSOLUTE MEASURES  ------------

  measure: allocated_devices { #1
    label: "Allocated Devices"
    description: "Allocated Devices"
    type: count_distinct
    sql: ${TABLE}.device_id;;
    filters:  [ dummy_dim  : "allocated_dim"]
  }

  measure: devices_on_trc { #2
    label: "Devices Active on TRC"
    description: "Devices Active on TRC"
    type: count_distinct
    sql: ${TABLE}.device_id;;
    filters:  [ dummy_dim  : "sec_streamed_dim"]
  }
#-----------------------------------
  measure: Total_hours { #3
    label: "Total Hours"
    type: sum
    value_format: "#,##0.00"
    sql: COALESCE (${TABLE}.seconds, 0)  / 3600.00 ;;
    filters:  [ dummy_dim  : "sec_streamed_dim"]
  }

  measure: count_Total {
    label: "count Total "
    type: count
    #sql: ${TABLE}.device_id;;
    filters: [ dummy_dim  : "sec_streamed_dim" ]
  }

  measure: mean_Total {
    label: "mean Total "
    type: average
    sql: COALESCE (${TABLE}.seconds, 0)    ;;
    filters:  [ dummy_dim  : "sec_streamed_dim"]
  }

  dimension: seconds_Total {
     label: "seconds Total"
     type: number
     sql: CASE  WHEN dummy_dim='sec_streamed_dim' THEN ${seconds} ELSE NULL END;;
  }

  measure: std2_Total_cnt {
     label: "std Total"
     type: number
     sql:  STDDEV(${seconds_Total})^2 / ${count_Total};;
  }
#--------------------------------------

  measure: AVOD_hours { #4
    label: "AVOD Hours"
    type: sum
    value_format: "#,##0.00"
    sql:  CASE WHEN  ${TABLE}.economic_model = 'AVOD'  THEN  COALESCE(${TABLE}.seconds,0)/3600.00 ELSE 0 END;;
    filters:  [ dummy_dim  : "sec_streamed_dim"]
  }

  measure: count_AVOD {
    label: "count AVOD"
    type: count
    #sql: ${TABLE}.device_id;;
    filters: [economic_model : "AVOD", dummy_dim  : "sec_streamed_dim" ]
  }

  measure: mean_AVOD {
    label: "mean AVOD "
    type: average
    sql: COALESCE (${TABLE}.seconds, 0)    ;;
    filters:  [economic_model : "AVOD", dummy_dim  : "sec_streamed_dim"]
  }

  dimension: seconds_AVOD {
    label: "seconds AVOD"
    type: number
    sql: CASE  WHEN dummy_dim='sec_streamed_dim' AND economic_model='AVOD' THEN ${seconds} ELSE NULL END;;
  }

  measure: std2_AVOD_cnt {
    label: "std AVOD"
    type: number
    sql:  STDDEV(${seconds_AVOD})^2 / ${count_AVOD};;
  }
#-----------------------------------------
  measure: AVOD_movies_hours { #5
    label: "AVOD Movies Hours"
    type: sum
    value_format: "#,##0.00"
    sql:  CASE WHEN  ${TABLE}.economic_model = 'AVOD' AND ${TABLE}.content_type = 'movie' THEN COALESCE(${TABLE}.seconds,0)/3600.00 ELSE 0 END;;
    filters:  [ dummy_dim  : "sec_streamed_dim"]
  }

  measure: count_AVOD_movies {
    label: "count AVOD Movies"
    type: count
    #sql: ${TABLE}.device_id;;
    filters: [economic_model : "AVOD", content_type: "movie", dummy_dim  : "sec_streamed_dim" ]
  }

  measure: mean_AVOD_movies {
    label: "mean AVOD movies "
    type: average
    sql: COALESCE (${TABLE}.seconds, 0)    ;;
    filters:  [economic_model : "AVOD", content_type: "movie", dummy_dim  : "sec_streamed_dim"]
  }

  dimension: seconds_AVOD_movies {
    label: "seconds AVOD movies"
    type: number
    sql: CASE  WHEN
          dummy_dim='sec_streamed_dim'
          AND economic_model='AVOD'
          AND content_type = 'movie'
          THEN ${seconds}
          ELSE NULL END;;
  }

  measure: std2_AVOD_movies_cnt {
    label: "std AVOD movies"
    type: number
    sql:  STDDEV(${seconds_AVOD_movies})^2 / ${count_AVOD_movies};;
  }
#-----------------------------------------
  measure: AVOD_series_hours { #6
    label: "AVOD TV Series Hours"
    type: sum
    value_format: "#,##0.00"
    sql:  CASE WHEN  ${TABLE}.economic_model = 'AVOD' AND ${TABLE}.content_type IN ('series','episode') THEN COALESCE(${TABLE}.seconds,0)/3600.00 ELSE 0 END ;;
    filters:  [ dummy_dim  : "sec_streamed_dim"]
  }

  measure: count_AVOD_series {
    label: "count AVOD Series"
    type: count
    #sql: ${TABLE}.device_id;;
    filters: [economic_model : "AVOD", content_type: "series,'episode", dummy_dim  : "sec_streamed_dim" ]
  }

  measure: mean_AVOD_series {
    label: "mean AVOD series "
    type: average
    sql: COALESCE (${TABLE}.seconds, 0)    ;;
    filters:  [economic_model : "AVOD", content_type: "series,'episode", dummy_dim  : "sec_streamed_dim"]
  }

  dimension: seconds_AVOD_series {
    label: "seconds AVOD series"
    type: number
    sql: CASE  WHEN
          dummy_dim='sec_streamed_dim'
          AND economic_model='AVOD'
          AND content_type IN ( 'series', 'episode')
          THEN ${seconds}
          ELSE NULL END;;
  }

  measure: std2_AVOD_series_cnt {
    label: "std AVOD series"
    type: number
    sql:  STDDEV(${seconds_AVOD_series})^2 / ${count_AVOD_series};;
  }
#--------------------------------------
  measure: SVOD_hours { #7
    label: "SVOD Hours"
    type: sum
    value_format: "#,##0.00"
    sql: CASE WHEN  ${TABLE}.economic_model = 'SVOD' THEN COALESCE(${TABLE}.seconds,0)/3600.00 ELSE 0 END;;
    filters:  [ dummy_dim  : "sec_streamed_dim"]
 }



  measure: count_SVOD {
    label: "count SVOD"
    type: count
    #sql: ${TABLE}.device_id;;
    filters: [economic_model : "SVOD", dummy_dim  : "sec_streamed_dim" ]
  }

  measure: mean_SVOD {
    label: "mean SVOD "
    type: average
    sql: COALESCE (${TABLE}.seconds, 0)    ;;
    filters:  [economic_model : "SVOD", dummy_dim  : "sec_streamed_dim"]
  }

  dimension: seconds_SVOD {
    label: "seconds AVOD"
    type: number
    sql: CASE  WHEN dummy_dim='sec_streamed_dim' AND economic_model='SVOD' THEN ${seconds} ELSE NULL END;;
  }

  measure: std2_SVOD_cnt {
    label: "std SVOD"
    type: number
    sql:  STDDEV(${seconds_SVOD})^2 / ${count_SVOD};;
  }


#---------------------------------------
  measure: SVOD_movies_hours { #8
    label: "SVOD Movies Hours"
    type: sum
    value_format: "#,##0.00"
    sql:   CASE WHEN  ${TABLE}.economic_model = 'SVOD' AND ${TABLE}.content_type = 'movie' THEN COALESCE(${TABLE}.seconds,0)/3600.00 ELSE 0 END;;
    filters:  [ dummy_dim  : "sec_streamed_dim"]
 }

  measure: count_SVOD_movies {
    label: "count SVOD Movies"
    type: count
    #sql: ${TABLE}.device_id;;
    filters: [economic_model : "SVOD", content_type: "movie", dummy_dim  : "sec_streamed_dim" ]
  }

  measure: mean_SVOD_movies {
    label: "mean SVOD movies "
    type: average
    sql: COALESCE (${TABLE}.seconds, 0)    ;;
    filters:  [economic_model : "SVOD", content_type: "movie", dummy_dim  : "sec_streamed_dim"]
  }

  dimension: seconds_SVOD_movies {
    label: "seconds SVOD movies"
    type: number
    sql: CASE  WHEN
          dummy_dim='sec_streamed_dim'
          AND economic_model='SVOD'
          AND content_type = 'movie'
          THEN ${seconds}
          ELSE NULL END;;
  }

  measure: std2_SVOD_movies_cnt {
    label: "std SVOD movies"
    type: number
    sql:  STDDEV(${seconds_SVOD_movies})^2 / ${count_SVOD_movies};;
  }

#--------------------------------------
  measure: SVOD_series_hours { #9
    label: "SVOD TV Series Hours"
    type: sum
    value_format: "#,##0.00"
    sql:  CASE WHEN  ${TABLE}.economic_model = 'SVOD' AND ${TABLE}.content_type IN ('series','episode') THEN COALESCE(${TABLE}.seconds,0)/3600.00 ELSE 0 END;;
  }

  measure: count_SVOD_series {
    label: "count SVOD Series"
    type: count
    #sql: ${TABLE}.device_id;;
    filters: [economic_model : "SVOD", content_type: "series,episode", dummy_dim  : "sec_streamed_dim" ]
  }

  measure: mean_SVOD_series {
    label: "mean SVOD series "
    type: average
    sql: COALESCE (${TABLE}.seconds, 0)    ;;
    filters:  [economic_model : "SVOD", content_type: "series,'episode", dummy_dim  : "sec_streamed_dim"]
  }

  dimension: seconds_SVOD_series {
    label: "seconds SVOD series"
    type: number
    sql: CASE  WHEN
          dummy_dim='sec_streamed_dim'
          AND economic_model='SVOD'
          AND content_type IN ( 'series', 'episode')
          THEN ${seconds}
          ELSE NULL END;;
  }

  measure: std2_SVOD_series_cnt {
    label: "std SVOD series"
    type: number
    sql:  STDDEV(${seconds_SVOD_series})^2 / ${count_SVOD_series};;
  }
#--------------------------------------
  measure: Livefeed_hours { #10
    label: "Livefeed Hours"
    type: sum
    value_format: "#,##0.00"
    sql:  CASE WHEN ${TABLE}.content_type = 'livefeed' THEN COALESCE(${TABLE}.seconds,0)/3600.00 ELSE 0 END;;
    filters:  [ dummy_dim  : "sec_streamed_dim"]
  }

  measure: count_Live {
    label: "count Live"
    type: count
    #sql: ${TABLE}.device_id;;
    filters: [ content_type: "livefeed", dummy_dim  : "sec_streamed_dim" ]
  }

  measure: mean_Live {
    label: "mean Live "
    type: average
    sql: COALESCE (${TABLE}.seconds, 0)    ;;
    filters:  [content_type: "livefeed", dummy_dim  : "sec_streamed_dim"]
  }

  dimension: seconds_Live {
    label: "seconds Live"
    type: number
    sql: CASE  WHEN dummy_dim='sec_streamed_dim' AND content_type='livefeed' THEN ${seconds} ELSE NULL END;;
  }

  measure: std2_Live_cnt {
    label: "std Live"
    type: number
    sql:  STDDEV(${seconds_Live})^2 / ${count_Live};;
  }
#--------------------------------------
  measure: Kids_hours { #11
    label: "Kids Hours"
    type: sum
    value_format: "#,##0.00"
    sql: CASE WHEN ${TABLE}.profile_type = 'kids' THEN COALESCE(${TABLE}.seconds,0)/3600.00 ELSE 0 END ;;
    filters:  [ dummy_dim  : "sec_streamed_dim"]
  }

  measure: count_Kids {
    label: "count Kids"
    type: count
    #sql: ${TABLE}.device_id;;
    filters: [ content_type: "kids", dummy_dim  : "sec_streamed_dim" ]
  }

  measure: mean_Kids {
    label: "mean Kids "
    type: average
    sql: COALESCE (${TABLE}.seconds, 0)    ;;
    filters:  [content_type: "kids", dummy_dim  : "sec_streamed_dim"]
  }

  dimension: seconds_Kids  {
    label: "seconds Kids"
    type: number
    sql: CASE  WHEN dummy_dim='sec_streamed_dim' AND content_type='kids' THEN ${seconds} ELSE NULL END;;
  }

  measure: std2_Kids_cnt {
    label: "std Kids"
    type: number
    sql:  STDDEV(${seconds_Kids})^2 / ${count_Kids};;
  }
#--------------------------------------
  measure: count_bounce_rate_10_min { # does not work
    label: "count devices streamed < 10 min"
    description: "count devices streamed  < 10 min"
    #type: sum
    type:  number
    #filters: [dummy_dim: "bounce_rate"]
    #sql: CASE WHEN ${TABLE}.bounced10min = 0  THEN 1 ELSE 0 END;;
    sql: 1;;
 }

  measure: bounce_rate_10_min { #
    label: "Bounce Rate for Streamed  < 10 min"
    description: "Bounce Rate for Streamed  < 10 min"
    type: number
    sql:  100.0 * 1;;
    # sql:  100.0 *   ${count_bounce_rate_10_min}   / ${devices_on_trc} ;;
  }

  measure: mean_bounce {
    label: "mean bounce "
    type: average
    sql: COALESCE (${TABLE}.bounced10min, 0)    ;;
    filters:  [ dummy_dim  : "bounce_rate"]
  }

  measure: seconds_bounce {
    label: "seconds bounce"
    type: number
    sql: CASE  WHEN dummy_dim='bounce_rate'   THEN ${count_bounce_rate_10_min} ELSE NULL END;;
  }

  measure: std2_bounce_cnt {
    label: "std bounce"
    type: number
    sql:  STDDEV(${seconds_bounce})^2 / ${count_bounce_rate_10_min};;
  }

#---------   Relative measures  --------

  measure: Active_on_TRC_percentage { #12
    label: "% Devices Active on TRC"
    type: number
    value_format: "#,##0.00"
    sql:  CASE WHEN ${allocated_devices} = 0 THEN 0 ELSE  100 * ${devices_on_trc} / ${allocated_devices} END;;
  }

  measure: Avg_Total_hours { #13
    label: "Avg Total Hours"
    type: number
    value_format: "#,##0.00"
    sql: CASE WHEN ${allocated_devices} = 0 THEN 0 ELSE ${Total_hours} / ${allocated_devices}  END;;
  }

  measure: Avg_AVOD_hours { #14
    label: "Avg AVOD Hours"
    type: number
    value_format: "#,##0.00"
    sql: CASE WHEN ${allocated_devices} = 0 THEN 0 ELSE   ${AVOD_hours} / ${allocated_devices}  END;;
  }

  measure: Avg_AVOD_movies_hours { #15
    label: "Avg AVOD Movies Hours"
    type: number
    value_format: "#,##0.00"
    sql: CASE WHEN ${allocated_devices} = 0 THEN 0 ELSE ${AVOD_movies_hours} / ${allocated_devices}  END;;
  }

  measure: Avg_AVOD_series_hours { #16
    label: "Avg AVOD TV Series Hours"
    type: number
    value_format: "#,##0.00"
    sql: CASE WHEN ${allocated_devices} = 0 THEN 0 ELSE ${AVOD_series_hours} /  ${allocated_devices}  END;;
  }

  measure: Avg_SVOD_hours { #17
    label: "Avg SVOD Hours"
    type: number
    value_format: "#,##0.00"
    sql: CASE WHEN ${allocated_devices} = 0 THEN 0 ELSE ${SVOD_hours} / ${allocated_devices}  END;;
  }

  measure: Avg_SVOD_movies_hours { #18
    label: "Avg SVOD Movies Hours"
    type: number
    value_format: "#,##0.00"
    sql:  CASE WHEN ${allocated_devices} = 0 THEN 0 ELSE  ${SVOD_movies_hours} / ${allocated_devices}  END;;
  }

  measure: Avg_SVOD_series_hours { #19
    label: "Avg SVOD TV Series Hours"
    type: number
    value_format: "#,##0.00"
    sql: CASE WHEN ${allocated_devices} = 0 THEN 0 ELSE   ${SVOD_series_hours} /  ${allocated_devices}  END;;
  }

  measure: Avg_Livefeed_hours { #20
    label: "Avg Livefeed Hours"
    type: number
    value_format: "#,##0.00"
    sql: CASE WHEN ${allocated_devices} = 0 THEN 0 ELSE ${Livefeed_hours} / ${allocated_devices}   END;;
  }

  measure: Avg_Kids_hours { #21
    label: "Avg Kids Hours"
    type: number
    value_format: "#,##0.00"
    sql: CASE WHEN ${allocated_devices} = 0 THEN 0 ELSE ${Kids_hours} / ${allocated_devices}  END;;
  }

# --------------------------------------
# following is based on
# https://help.looker.com/hc/en-us/articles/360023862233-Transpose-Table-Display-Measures-as-Rows-
# -------------------------------------
  dimension: aux {
    case: {

      when: { # 1
        label: "Allocated Devices"
        sql: 1=1 ;;
      }
      when: { # 2
        label: "Devices on TRC"
        sql: 1=1 ;;
      }
      when: {   # 3
        label: "Total Hours"
        sql: 1=1 ;;
      }

      # --------   AVOD  ------------
      when: {  #4
        label: "AVOD Hours"
        sql: 1=1 ;;
      }
      when: {  #5
        label: "AVOD Movies Hours"
        sql: 1=1 ;;
      }
      when: { #6
        label: "AVOD TV Series Hours"
        sql: 1=1 ;;
      }
      # ------- start  SVOD  -----------
      when: {  #7
        label: "SVOD  Hours"
        sql: 1=1 ;;
      }
      when: {  # 8
        label: "SVOD Movies Hours"
        sql: 1=1 ;;
      }
      when: { #9
        label: "SVOD TV Series Hours"
        sql: 1=1 ;;
      }
      #---------end SVOD ----------
      when: { # 10
        label: "Livefeed Hours"
        sql: 1=1 ;;
      }
      when: { #11
        label: "Kids Hours"
        sql: 1=1 ;;
      }
      #--------   Relative

      when: { #12
        label: "% Devices Active on TRC"
        sql: 1=1  ;;
      }

      when: { #13
        label: "Avg Total Hours"
        sql: 1=1 ;;
      }

      when: { #14
        label: "Avg AVOD Hours"
        sql:  1=1  ;;
      }

      when: { #15
        label: "Avg AVOD Movies Hours"
        sql:  1=1;;
      }

      when: { #16
        label: "Avg AVOD TV Series Hours"
        sql:  1=1 ;;
      }

      when: { #17
        label: "Avg SVOD Hours"
        sql:  1=1;;
      }

      when: { #18
        label: "Avg SVOD Movies Hours"
        sql:  1=1;;
      }

      when: { #19
        label: "Avg SVOD TV Series Hours"
        sql:  1=1  ;;
      }

      when: { #20
        label: "Avg Livefeed Hours"
        sql: 1=1  ;;
      }

      when: { #21
        label: "Avg Kids Hours"
        sql: 1=1 ;;
      }

      when: { #22
        label: "% Bounce rate < 10 min"
        sql: 1=1 ;;
      }


    } # end case
  }   # end aux dimension

  }

