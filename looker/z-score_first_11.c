coalesce(
if(row()=1, 0, null),
if(row()=2, 0, null),

if(row()=3,  ( index(${derived_trc_amoeba_kpi.mean_Total},1) - 
   pivot_where(contains(${derived_trc_amoeba_kpi.bucket}, "#Control"), index(${derived_trc_amoeba_kpi.mean_Total},1))
)/
sqrt(index(${derived_trc_amoeba_kpi.std2_Total_cnt},1) +
pivot_where(contains(${derived_trc_amoeba_kpi.bucket}, "#Control"), index(${derived_trc_amoeba_kpi.std2_Total_cnt},1))
), null),
# --- AVOD  
if(row()=4,  ( index(${derived_trc_amoeba_kpi.mean_AVOD},1) - 
   pivot_where(contains(${derived_trc_amoeba_kpi.bucket}, "#Control"), index(${derived_trc_amoeba_kpi.mean_AVOD},1))
)/
sqrt(index(${derived_trc_amoeba_kpi.std2_AVOD_cnt},1) +
pivot_where(contains(${derived_trc_amoeba_kpi.bucket}, "#Control"), index(${derived_trc_amoeba_kpi.std2_AVOD_cnt},1))
), null),
# --- AVOD movies
if(row()=5,  ( index(${derived_trc_amoeba_kpi.mean_AVOD_movies},1) - 
   pivot_where(contains(${derived_trc_amoeba_kpi.bucket}, "#Control"), index(${derived_trc_amoeba_kpi.mean_AVOD_movies},1))
)/
sqrt(index(${derived_trc_amoeba_kpi.std2_AVOD_movies_cnt},1) +
pivot_where(contains(${derived_trc_amoeba_kpi.bucket}, "#Control"), index(${derived_trc_amoeba_kpi.std2_AVOD_movies_cnt},1))
), null),
# --- AVOD series
if(row()=6,  ( index(${derived_trc_amoeba_kpi.mean_AVOD_series},1) - 
   pivot_where(contains(${derived_trc_amoeba_kpi.bucket}, "#Control"), index(${derived_trc_amoeba_kpi.mean_AVOD_series},1))
)/
sqrt(index(${derived_trc_amoeba_kpi.std2_AVOD_series_cnt},1) +
pivot_where(contains(${derived_trc_amoeba_kpi.bucket}, "#Control"), index(${derived_trc_amoeba_kpi.std2_AVOD_series_cnt},1))
), null),
# --- SVOD  
if(row()=7,  ( index(${derived_trc_amoeba_kpi.mean_SVOD},1) - 
   pivot_where(contains(${derived_trc_amoeba_kpi.bucket}, "#Control"), index(${derived_trc_amoeba_kpi.mean_SVOD},1))
)/
sqrt(index(${derived_trc_amoeba_kpi.std2_SVOD_cnt},1) +
pivot_where(contains(${derived_trc_amoeba_kpi.bucket}, "#Control"), index(${derived_trc_amoeba_kpi.std2_SVOD_cnt},1))
), null),
# --- SVOD movies
if(row()=8,  ( index(${derived_trc_amoeba_kpi.mean_SVOD_movies},1) - 
   pivot_where(contains(${derived_trc_amoeba_kpi.bucket}, "#Control"), index(${derived_trc_amoeba_kpi.mean_SVOD_movies},1))
)/
sqrt(index(${derived_trc_amoeba_kpi.std2_SVOD_movies_cnt},1) +
pivot_where(contains(${derived_trc_amoeba_kpi.bucket}, "#Control"), index(${derived_trc_amoeba_kpi.std2_SVOD_movies_cnt},1))
), null),
# --- SVOD series
if(row()=9,  ( index(${derived_trc_amoeba_kpi.mean_SVOD_series},1) - 
   pivot_where(contains(${derived_trc_amoeba_kpi.bucket}, "#Control"), index(${derived_trc_amoeba_kpi.mean_SVOD_series},1))
)/
sqrt(index(${derived_trc_amoeba_kpi.std2_SVOD_series_cnt},1) +
pivot_where(contains(${derived_trc_amoeba_kpi.bucket}, "#Control"), index(${derived_trc_amoeba_kpi.std2_SVOD_series_cnt},1))
), null),
# --- Live
if(row()=10,  ( index(${derived_trc_amoeba_kpi.mean_Live},1) - 
   pivot_where(contains(${derived_trc_amoeba_kpi.bucket}, "#Control"), index(${derived_trc_amoeba_kpi.mean_Live},1))
)/
sqrt(index(${derived_trc_amoeba_kpi.std2_Live_cnt},1) +
pivot_where(contains(${derived_trc_amoeba_kpi.bucket}, "#Control"), index(${derived_trc_amoeba_kpi.std2_Live_cnt},1))
), null),
# --- Kids
if(row()=11,  ( index(${derived_trc_amoeba_kpi.mean_Kids},1) - 
   pivot_where(contains(${derived_trc_amoeba_kpi.bucket}, "#Control"), index(${derived_trc_amoeba_kpi.mean_Kids},1))
)/
sqrt(index(${derived_trc_amoeba_kpi.std2_Kids_cnt},1) +
pivot_where(contains(${derived_trc_amoeba_kpi.bucket}, "#Control"), index(${derived_trc_amoeba_kpi.std2_Kids_cnt},1))
), null),