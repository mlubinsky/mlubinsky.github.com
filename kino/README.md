поэтом можешь ты не быть, а композитором не можешь.


https://val000.livejournal.com/2408208.html?view=comments#comments Detectives

```
 src/main/python/eue/left_nav_agg/hql/agg_left_hand_nav_time_grain.hql                                                                      |   10 +-
 src/main/python/eue/left_nav_agg/hql/agg_left_hand_nav_time_grain_local.hql                                                                |   10 +-
 src/main/python/eue/left_nav_agg/left_nav_agg_dag.py                                                                                       |   14 +-
 src/main/python/fact/fact_google_alexa_linked_accounts/BUILD                                                                               |   14 +
 src/main/python/fact/fact_google_alexa_linked_accounts/__init__.py                                                                         |    0
 src/main/python/fact/fact_google_alexa_linked_accounts/api.py                                                                              |   11 +
 src/main/python/fact/fact_google_alexa_linked_accounts/fact_google_alexa_linked_accounts_dag.py                                            |  297 ++++++++++++
 src/main/python/fact/fact_google_alexa_linked_accounts/fact_join_linked_account_device_detail.hql                                          |   26 ++
 src/main/python/finance/finance_dsp_data.hql                                                                                               |    1 +
 src/main/python/finance/finance_dsp_data_dag.py                                                                                            |    2 +-
 src/main/python/infra/peppet/adi_conf/spark_jobs.json                                                                                      |    6 +
 src/main/python/infra/peppet/conf/spark_jobs.json                                                                                          |    6 -
 src/main/python/infra/servicemon/api.py                                                                                                    |   19 +-
 src/main/python/mlp_v3/delta_model_dag.py                                                                                                  |    4 +-
 src/main/python/mlp_v3/mlpy/delta_gendata.py                                                                                               |    2 +-
 src/main/python/mlp_v3/mlpy/docker/delta_ctr_model/test/test_ctr_model_image.py                                                            |  135 ++++--
 src/main/python/mlp_v3/mlpy/features/delta_ctrmodel.py                                                                                     |   13 +-
 src/main/python/mlp_v3/mlpy/features/makefeat.py                                                                                           |    2 +-
 src/main/python/mlp_v3/mlpy/libs/encode_and_score.py                                                                                       |    6 +-
 src/main/python/mlp_v3/mlpy/libs/encoder.py                                                                                                |    8 +-
 src/main/python/mlp_v3/mlpy/po_score.py                                                                                                    |    1 +
 src/main/python/mlp_v3/mlpy/{dev => prod}/RUM_UID.txt                                                                                      |    0
 src/main/python/mlp_v3/mlpy/{dev => prod}/repo/rum_real.schema                                                                             |    0
 src/main/python/mlp_v3/mlpy/{dev => prod}/rum/features_ad_rum.list                                                                         |    0
 src/main/python/mlp_v3/mlpy/{dev => prod}/rum/features_interests.list                                                                      |    0
 src/main/python/mlp_v3/mlpy/prod/rum/model_install.json                                                                                    |   15 +
 src/main/python/mlp_v3/mlpy/prod/rum/model_template.json                                                                                   |   35 ++
 src/main/python/mlp_v3/mlpy/{dev => prod}/rum/virtual_ad_rum.config                                                                        |    0
 src/main/python/mlp_v3/mlpy/{dev => prod}/rum/virtual_rum.config                                                                           |    0
 src/main/python/mlp_v3/mlpy/prod/rum_master.json                                                                                           |   26 ++
 src/main/python/mlp_v3/mlpy/prod/rum_tiny.json                                                                                             |   11 +
 src/main/python/mlp_v3/mlpy/rum_score.py                                                                                                   |   48 +-
 src/main/python/mlp_v3/mlpy/testloc/debug_delta.py                                                                                         |    2 +-
 src/main/python/mo/hql/in_demo_calculations.hql                                                                                            |    7 +-
 src/main/python/mo/mo_calculations.py                                                                                                      |   34 --
 src/main/python/mo/mo_daily.py                                                                                                             |    6 +-
 src/main/python/mo/mo_data_fetcher.py                                                                                                      |    6 +-
 src/main/python/mo/mo_objects.py                                                                                                           |   30 +-
 src/main/python/mo/test/mo_objects_test.py                                                                                                 |    3 +-
 src/main/python/mo/update_r.py                                                                                                             |   15 +-
 src/main/python/pmm/pmm_hourly/BUILD                                                                                                       |    2 +-
 src/main/python/pmm/pmm_hourly/agg_device_build_metrics_daily.hql                                                                          |   77 ++--
 src/main/python/pmm/pmm_hourly/agg_device_build_metrics_daily_old.hql                                                                      |  177 ++++++++
 src/main/python/pmm/pmm_hourly/agg_diff_in_diff_model_input_daily_normalized.hql                                                           |   81 ++--
 src/main/python/pmm/pmm_hourly/pmm_ai_model.conf                                                                                           |   22 +
 src/main/python/pmm/pmm_hourly/pmm_ai_model.py                                                                                             |  231 ++++++++++
 src/main/python/pmm/pmm_hourly/pmm_feature_generation.hql                                                                                  |   38 ++
 src/main/python/pmm/pmm_hourly/pmm_hourly.py                                                                                               |  166 ++++++-
 src/main/python/pmm/pmm_hourly/pmm_model.py                                                                                                |  334 ++++++++++++--
 src/main/python/pmm/rpay_pmm/BUILD                                                                                                         |   15 +
 src/main/python/pmm/rpay_pmm/__init__.py                                                                                                   |    0
 src/main/python/pmm/rpay_pmm/agg_rpay_pmm_metrics_daily.hql                                                                                |   85 ++++
 src/main/python/pmm/rpay_pmm/rpay_pmm.py                                                                                                   |  145 ++++++
 src/main/python/pmm/rpay_pmm/rpay_pmm_ai_model.conf                                                                                        |   23 +
 src/main/python/pmm/rpay_pmm/rpay_pmm_ai_model.py                                                                                          |  252 +++++++++++
 src/main/python/po/abTestAndPercentile/po_ab_percentile_dag.py                                                                             |    4 +-
 src/main/python/po/campaign_automation/DisplayAdsPacingUpdater.py                                                                          |  322 +++++++++++++
 src/main/python/po/campaign_automation/LineItemsManagerUACpm.py                                                                            |  109 -----
 src/main/python/po/campaign_automation/global_field_name.py                                                                                |    2 +-
 src/main/python/po/campaign_automation/po_campaign_automation_hourly_dag.py                                                                |   27 +-
 src/main/python/po/diagnosis_tool/checks.py                                                                                                |    2 +-
 src/main/python/po/po_utils/DFPClient.py                                                                                                   |    6 +
 src/main/python/rams_dag_bag.py                                                                                                            |    2 +
 src/main/python/roku_dag_bag.py                                                                                                            |   11 +
 src/main/python/rum/BUILD                                                                                                                  |    8 +-
 src/main/python/rum/eligible_offers.py                                                                                                     |   23 +-
 src/main/python/rum/rum_eligible_offers_dag.py                                                                                             |    4 +-
 src/main/python/sboxedresource/hive_udf.py                                                                                                 |   33 +-
 src/main/python/sim_avails/avails_data_diff.py                                                                                             |  545 ++++++++++++++++++++++
 src/main/python/solutions/BUILD                                                                                                            |   13 +
 src/main/python/solutions/__init__.py                                                                                                      |    0
 src/main/python/solutions/hulu_rejection_data_dag.py                                                                                       |   66 +++
 src/main/python/solutions/load_hulu_rejection_data.hql                                                                                     |   12 +
 src/main/python/third_party/pii/pii_api.py                                                                                                 |   10 +-
 src/main/python/third_party/pii/tpd_dim_pii_match_export.py                                                                                |   23 +-
 src/main/python/userprofile/userprofile_api.py                                                                                             |    4 +
 src/main/scala/com/roku/adcloud/spark/avails/AvailsPerMinRAMS.scala                                                                        |    2 +
 src/main/scala/com/roku/adcloud/spark/avails/sellthrough/AvailsLineItems.scala                                                             |    2 +-
 src/main/scala/com/roku/adcloud/spark/avails2/AvailsIndexerApp.scala                                                                       |    2 +-
 src/main/scala/com/roku/adcloud/spark/avails2/FetchBookingData.scala                                                                       |   20 +-
 src/main/scala/com/roku/adcloud/spark/avails2/GenerateRequestOrUserSamples.scala                                                           |   12 +-
 src/main/scala/com/roku/adcloud/spark/avails2/indexer/AvailsIndexAggregator.scala                                                          |    9 +-
 src/main/scala/com/roku/adcloud/spark/avails2/indexer/AvailsIndexOutput.scala                                                              |   12 +-
 src/main/scala/com/roku/adcloud/spark/avails2/loaders/ChannelCategoriesAndIsKidsDatasetProvider.scala                                      |   46 ++
 src/main/scala/com/roku/adcloud/spark/avails2/loaders/TagMetaDataLoader.scala                                                              |   13 +-
 src/main/scala/com/roku/adcloud/spark/avails2/loaders/TrcGenreProvider.scala                                                               |   64 +++
 src/main/scala/com/roku/adcloud/spark/avails2/util/BannerSamplesUtil.scala                                                                 |   32 +-
 src/main/scala/com/roku/adcloud/spark/avails2/util/SamplesUtil.scala                                                                       |    2 +
 src/main/scala/com/roku/adcloud/spark/avails2/util/VideoSamplesUtil.scala                                                                  |  242 +++++++---
 src/main/scala/com/roku/adcloud/spark/insights/BUILD                                                                                       |    3 +-
 src/main/scala/com/roku/adcloud/spark/insights/acr/AcrInsightsHelper.scala                                                                 |  225 ----------
 src/main/scala/com/roku/adcloud/spark/insights/acr/AggAdiAcrApp.scala                                                                      |  189 --------
 src/main/scala/com/roku/adcloud/spark/insights/acr/AggAdiAcrEducationApp.scala                                                             |  181 --------
 src/main/scala/com/roku/adcloud/spark/insights/acr/AggAdiAcrIncomeApp.scala                                                                |  180 --------
 src/main/scala/com/roku/adcloud/spark/insights/acr/loaders/AdiFactAcrDataLoader.scala                                                      |   44 --
 src/main/scala/com/roku/adcloud/spark/insights/acr/loaders/AdiFactAcrEducationDataLoader.scala                                             |   41 --
 src/main/scala/com/roku/adcloud/spark/insights/acr/loaders/AdiFactAcrIncomeDataLoader.scala                                                |   41 --
 src/main/scala/com/roku/adcloud/spark/insights/acr/objects/AdiAcrEducationPreAggDimension.scala                                            |   16 -
 src/main/scala/com/roku/adcloud/spark/insights/acr/objects/AdiAcrEducationPreAggRecord.scala                                               |   54 ---
 src/main/scala/com/roku/adcloud/spark/insights/acr/objects/AdiAcrIncomePreAggDimension.scala                                               |   16 -
 src/main/scala/com/roku/adcloud/spark/insights/acr/objects/AdiAcrIncomePreAggRecord.scala                                                  |   54 ---
 src/main/scala/com/roku/adcloud/spark/insights/acr/objects/AdiAcrPreAggDimension.scala                                                     |   19 -
 src/main/scala/com/roku/adcloud/spark/insights/acr/objects/AdiAcrPreAggRecord.scala                                                        |   60 ---
 src/main/scala/com/roku/adcloud/spark/insights/acr/objects/AggAdiAcrEducationRecord.scala                                                  |   24 -
 src/main/scala/com/roku/adcloud/spark/insights/acr/objects/AggAdiAcrIncomeRecord.scala                                                     |   24 -
 src/main/scala/com/roku/adcloud/spark/insights/acr/objects/AggAdiAcrRecord.scala                                                           |   27 --
 src/main/scala/com/roku/adcloud/spark/insights/acr/objects/Implicits.scala                                                                 |   16 -
 src/main/scala/com/roku/adcloud/spark/insights/campaign/CampaignInsightsHelper.scala                                                       |  190 ++++++--
 src/main/scala/com/roku/adcloud/spark/insights/campaign/CampaignUtils.scala                                                                |    2 +-
 src/main/scala/com/roku/adcloud/spark/insights/campaign/FactCampaignInsightsApp.scala                                                      |   12 +-
 src/main/scala/com/roku/adcloud/spark/insights/campaign/loaders/AdiDimSfMetadataLoader.scala                                               |   52 +++
 src/main/scala/com/roku/adcloud/spark/insights/campaign/loaders/DspDataLoader.scala                                                        |   50 +--
 src/main/scala/com/roku/adcloud/spark/insights/campaign/loaders/RamsLiveTrcTagsDataLoader.scala                                            |   11 +-
 src/main/scala/com/roku/adcloud/spark/insights/common/Utils.scala                                                                          |  276 +++++++-----
 src/main/scala/com/roku/adcloud/spark/insights/data_toolkit/BUILD                                                                          |    2 +-
 src/main/scala/com/roku/adcloud/spark/insights/data_toolkit/DimAdiAcrPanelApp.scala                                                        |  306 +++++++++++++
 src/main/scala/com/roku/adcloud/spark/insights/data_toolkit/FillMissingAccountDemoUsingDAROApp.scala                                       |   46 +-
 src/main/scala/com/roku/adcloud/spark/insights/data_toolkit/InsightsAccountAttributesApp.scala                                             |   22 +-
 src/main/scala/com/roku/adcloud/spark/insights/data_toolkit/OneviewHouseholdMapApp.scala                                                   |   87 ++--
 src/main/scala/com/roku/adcloud/spark/insights/data_toolkit/TargetingSpecificDemoPopulatorApp.scala                                        |  278 ++++++++++++
 src/main/scala/com/roku/adcloud/spark/insights/data_toolkit/ToolkitHelper.scala                                                            |  425 +++++++++++++++---
 src/main/scala/com/roku/adcloud/spark/insights/data_toolkit/loaders/DimAccountAttributesLoader.scala                                       |   42 ++
 src/main/scala/com/roku/adcloud/spark/insights/data_toolkit/loaders/DimAdIdentityHistoryLoader.scala                                       |   10 +-
 src/main/scala/com/roku/adcloud/spark/insights/data_toolkit/loaders/DimAliasMappingsLoader.scala                                           |   10 +-
 src/main/scala/com/roku/adcloud/spark/insights/data_toolkit/loaders/DimHouseholdMapLoader.scala                                            |    7 +-
 src/main/scala/com/roku/adcloud/spark/insights/data_toolkit/loaders/DimRokuPiiLoader.scala                                                 |   44 ++
 src/main/scala/com/roku/adcloud/spark/insights/data_toolkit/objects/AccountRidaDevice.scala                                                |    4 +-
 src/main/scala/com/roku/adcloud/spark/insights/data_toolkit/objects/OneviewHouseholdMap.scala                                              |    3 +-
 src/main/scala/com/roku/adcloud/spark/insights/dataloader/AccountAttributesDataLoader.scala                                                |    2 +-
 src/main/scala/com/roku/adcloud/spark/insights/dataloader/DimSearchCapMediaDataLoader.scala                                                |   16 +-
 src/main/scala/com/roku/adcloud/spark/insights/dataloader/RokuLinearViewershipDataLoader.scala                                             |  133 ++----
 src/main/scala/com/roku/adcloud/spark/insights/dspcordcutter/BUILD                                                                         |   15 +-
 src/main/scala/com/roku/adcloud/spark/insights/dspcordcutter/Utils.scala                                                                   |  307 +++++++------
 src/main/scala/com/roku/adcloud/spark/insights/dspcordcutter/dataprep/DailyFeaturesFromDSPCTVTrans.scala                                   |   48 +-
 src/main/scala/com/roku/adcloud/spark/insights/dspcordcutter/dataprep/DailyFeaturesFromDSPCTVTrans.scala.bkup                              |  492 --------------------
 src/main/scala/com/roku/adcloud/spark/insights/dspcordcutter/dataprep/DailyFeaturesFromDSPImpressions.scala                                |   13 +-
 src/main/scala/com/roku/adcloud/spark/insights/dspcordcutter/dataprep/Discretizer.scala                                                    |  189 ++++++++
 src/main/scala/com/roku/adcloud/spark/insights/dspcordcutter/dataprep/agg/AggDailyFeaturesFromCTVTrans.scala                               |  302 +++++++------
 src/main/scala/com/roku/adcloud/spark/insights/dspcordcutter/dataprep/agg/AggDailyFeaturesFromDSPImpressions.scala                         | 1874 +++++++++++++++++++++++++++++++++++++++-------------------------------------
 src/main/scala/com/roku/adcloud/spark/insights/dspcordcutter/glue/Controller.scala                                                         |   93 ++--
 src/main/scala/com/roku/adcloud/spark/insights/dspcordcutter/glue/RequestFactory.scala                                                     |   53 ++-
 src/main/scala/com/roku/adcloud/spark/insights/dspcordcutter/labelling/ModellingData.scala                                                 | 1325 +++++++++++++++++++++++++++++++++---------------------
 src/main/scala/com/roku/adcloud/spark/insights/dspcordcutter/schema.txt                                                                    |   30 +-
 src/main/scala/com/roku/adcloud/spark/insights/reach/AdiPersonReachHelper.scala                                                            |   21 +-
 src/main/scala/com/roku/adcloud/spark/insights/reach/AggAdiPersonDemoDmaDimensionsApp.scala                                                |    1 +
 src/main/scala/com/roku/adcloud/spark/insights/reach/AggAdiReachApp.scala                                                                  |  165 +++----
 src/main/scala/com/roku/adcloud/spark/insights/ump/AggAdiUmpBidWinDensityApp.scala                                                         |  144 ++++++
 src/main/scala/com/roku/adcloud/spark/insights/ump/AggAdiUmpFlightAudienceApp.scala                                                        |    4 +-
 src/main/scala/com/roku/adcloud/spark/insights/ump/AggAdiUmpFlightGeoApp.scala                                                             |    4 +-
 src/main/scala/com/roku/adcloud/spark/insights/ump/AggAdiUmpFlightInventoryApp.scala                                                       |    4 +-
 src/main/scala/com/roku/adcloud/spark/insights/ump/AggAdiUmpFlightPixelCpaApp.scala                                                        |  137 +++---
 src/main/scala/com/roku/adcloud/spark/insights/ump/AggAdiUmpPixelFiresApp.scala                                                            |    4 +-
 src/main/scala/com/roku/adcloud/spark/insights/ump/FactAdiUmpAttributionsApp.scala                                                         |   12 +-
 src/main/scala/com/roku/adcloud/spark/insights/ump/FactAdiUmpBidsApp.scala                                                                 |  239 ++++++++++
 src/main/scala/com/roku/adcloud/spark/insights/ump/FactAdiUmpImpressionsApp.scala                                                          |   14 +-
 src/main/scala/com/roku/adcloud/spark/insights/ump/UMPHelper.scala                                                                         |  185 ++++++--
 src/main/scala/com/roku/adcloud/spark/insights/ump/loaders/DspBidTransactionsDataLoader.scala                                              |   42 ++
 src/main/scala/com/roku/adcloud/spark/insights/ump/loaders/DxCurrencyRatesDataLoader.scala                                                 |   34 ++
 src/main/scala/com/roku/adcloud/spark/insights/ump/loaders/FactAdiUmpAttributionsDataLoader.scala                                          |    5 +
 src/main/scala/com/roku/adcloud/spark/insights/ump/loaders/FactAdiUmpBidsAndImpressionsDataLoader.scala                                    |   76 ++++
 src/main/scala/com/roku/adcloud/spark/insights/ump/loaders/FactAdiUmpImpressionsDataLoader.scala                                           |    8 +-
 src/main/scala/com/roku/adcloud/spark/insights/ump/loaders/RwhAttributionsDataLoader.scala                                                 |    6 +-
 src/main/scala/com/roku/adcloud/spark/insights/ump/loaders/RwhImpressionsDataLoader.scala                                                  |    6 +-
 src/main/scala/com/roku/adcloud/spark/insights/ump/objects/AggAdiUmpBidWinDensityRecord.scala                                              |   10 +
 src/main/scala/com/roku/adcloud/spark/insights/ump/objects/FactAdiUmpBidRecord.scala                                                       |    9 +
 src/main/scala/com/roku/adcloud/spark/insights/viewability/AggAdiDVViewabilityApp.scala                                                    |  110 +++++
 src/main/scala/com/roku/adcloud/spark/insights/viewability/AggAdiIASViewabilityApp.scala                                                   |  109 +++++
 src/main/scala/com/roku/adcloud/spark/insights/viewability/AggAdiMOATViewabilityApp.scala                                                  |  122 +++++
 src/main/scala/com/roku/adcloud/spark/insights/viewability/BUILD                                                                           |   32 ++
 src/main/scala/com/roku/adcloud/spark/insights/viewability/ViewabilityHelper.scala                                                         |  356 +++++++++++++++
 src/main/scala/com/roku/adcloud/spark/insights/viewability/objects/FactViewabilityRecord.scala                                             |   18 +
 src/main/scala/com/roku/adcloud/spark/supplyreport/AggTxnCnfSketchRecord.scala                                                             |   49 +-
 src/main/scala/com/roku/adcloud/spark/supplyreport/DimensionRecord.scala                                                                   |   38 +-
 src/main/scala/com/roku/adcloud/spark/supplyreport/MetricRecord.scala                                                                      |   24 +-
 src/main/scala/com/roku/adcloud/spark/supplyreport/SupplyReportApp.scala                                                                   |    4 +-
 src/main/scala/com/roku/adcloud/spark/supplyreport/TxnCnfDatasetAggregator.scala                                                           |   67 ++-
 src/main/scala/com/roku/adcloud/spark/supplyreport/TxnCnfRecord.scala                                                                      |    2 +
 src/main/scala/com/roku/adcloud/spark/unifiedavails/RokuUnifiedAttrApp.scala                                                               |   30 +-
 src/main/scala/com/roku/adcloud/spark/unifiedavails/RokuUnifiedAvailsIndexerApp.scala                                                      |   86 ++--
 src/main/scala/com/roku/adcloud/spark/unifiedavails/config/RokuUnifiedAttrConfigManager.scala                                              |   17 +-
 src/main/scala/com/roku/adcloud/spark/unifiedavails/config/VideoUnifiedAttributeConfigurations.scala                                       |   16 +
 src/main/scala/com/roku/adcloud/spark/unifiedavails/features/ChannelGenreFeatures.scala                                                    |   24 +
 src/main/scala/com/roku/adcloud/spark/unifiedavails/features/IsKidsFeatures.scala                                                          |   29 ++
 src/main/scala/com/roku/adcloud/spark/unifiedavails/features/TrcContentTypeFeatures.scala                                                  |   17 +
 src/main/scala/com/roku/adcloud/spark/unifiedavails/features/TrcGenreFeatures.scala                                                        |   16 +
 src/main/scala/com/roku/adcloud/spark/unifiedavails/features/UnifiedAvailsFeatures.scala                                                   |    3 +
 src/main/scala/com/roku/adcloud/spark/unifiedavails/loaders/RokuSampleLoader.scala                                                         |   87 +++-
 src/main/scala/com/roku/adcloud/spark/unifiedavails/loaders/RokuUnifiedAvailsAttrLoader.scala                                              |   20 +-
 src/main/scala/com/roku/ads/services/rams/backend/common/Constants.scala                                                                   |    1 +
 src/main/scala/com/roku/ads/services/rams/backend/dao/DealDao.scala                                                                        |  229 ++++------
 src/main/scala/com/roku/ads/services/rams/backend/dao/InventoryPackageDao.scala                                                            |   13 +-
 src/main/scala/com/roku/ads/services/rams/backend/dao/PriorityMapDao.scala                                                                 |   10 +-
 src/main/scala/com/roku/ads/services/rams/backend/dao/SystemDao.scala                                                                      |    7 +
 src/main/scala/com/roku/ads/services/rams/backend/dao/TagDao.scala                                                                         |   31 +-
 src/main/scala/com/roku/ads/services/rams/backend/graphql/CustomFromInputs.scala                                                           |    7 +-
 src/main/scala/com/roku/ads/services/rams/backend/graphql/CustomInputTypes.scala                                                           |    4 +-
 src/main/scala/com/roku/ads/services/rams/backend/graphql/CustomTypes.scala                                                                |    4 +-
 src/main/scala/com/roku/ads/services/rams/backend/graphql/GraphQLSchema.scala                                                              |   20 +-
 src/main/scala/com/roku/ads/services/rams/backend/inventorypackage/InventoryPackageObject.scala                                            |    3 +-
 src/main/scala/com/roku/ads/services/rams/backend/models/DealModel.scala                                                                   |   32 +-
 src/main/scala/com/roku/ads/services/rams/backend/models/InventoryPackageModel.scala                                                       |    9 +-
 src/main/scala/com/roku/ads/services/rams/backend/models/PriorityMapModel.scala                                                            |   17 +-
 src/main/scala/com/roku/ads/services/rams/backend/models/ddl/bootstrap_data.sql                                                            |    6 +-
 src/main/scala/com/roku/ads/spark/rams/impression/RamsPixelEventsDataLoader.scala                                                          |    1 +
 src/main/scala/com/roku/common/deequ/core/LocationDataLoader.scala                                                                         |   33 ++
 src/main/scala/com/roku/common/deequ/deequ-consumer.sh                                                                                     |    1 +
 src/main/scala/com/roku/common/deequ/deequ-runner.sh                                                                                       |    1 +
 src/main/scala/com/roku/common/deequ/validators/BUILD                                                                                      |    1 +
 src/main/scala/com/roku/common/deequ/validators/DataCollabValidator.scala                                                                  |  198 ++++++++
 src/main/scala/com/roku/common/deequ/validators/GenericValueOccurrenceValidator.scala                                                      |   62 +++
 src/main/scala/com/roku/common/deequ/validators/RamsAggGranularValidator.scala                                                             |    1 +
 src/main/scala/com/roku/daro/spark/DemoProbabilitiesLoader.scala                                                                           |    3 +-
 src/main/scala/com/roku/daro/spark/DemoProbabilitiesResolverV2.scala                                                                       |   55 ++-
 src/main/scala/com/roku/daro/spark/DemoProbabilitiesValidator.scala                                                                        |    2 +-
 src/main/scala/com/roku/dea/nosql/userprofile/DisplayAdsProfileAerospikeLoader.scala                                                       |   47 +-
 src/main/scala/com/roku/dea/nosql/userprofile/coppa/CoppaProfileUtil.scala                                                                 |   67 ++-
 src/main/scala/com/roku/dea/spark/log_query/ETLProcessor.scala                                                                             |    6 +-
 src/main/scala/com/roku/dea/spark/streaming/device/BUILD                                                                                   |    3 -
 src/main/scala/com/roku/dea/spark/streaming/device/resources/monitor_streaming_lag.py                                                      |   96 ++++
 src/main/scala/com/roku/dea/spark/streaming/device/resources/submit_utils.sh                                                               |   22 +
 src/main/scala/com/roku/dea/spark/streaming/device_log_validator/BUILD                                                                     |    3 -
 src/main/scala/com/roku/dea/spark/streaming/device_log_validator/resources/monitor_streaming_lag.py                                        |   96 ++++
 src/main/scala/com/roku/dea/spark/streaming/device_log_validator/resources/submit_utils.sh                                                 |   22 +
 src/main/scala/com/roku/dea/spark/streaming/device_ux/BUILD                                                                                |    3 -
 src/main/scala/com/roku/dea/spark/streaming/device_ux/resources/monitor_streaming_lag.py                                                   |   96 ++++
 src/main/scala/com/roku/dea/spark/streaming/device_ux/resources/submit_utils.sh                                                            |   22 +
 src/main/scala/com/roku/dea/spark/streaming/lego/BUILD                                                                                     |    3 -
 src/main/scala/com/roku/dea/spark/streaming/lego/resources/monitor_streaming_lag.py                                                        |   96 ++++
 src/main/scala/com/roku/dea/spark/streaming/lego/resources/submit_utils.sh                                                                 |   22 +
 src/main/scala/com/roku/dea/spark/streaming/lego_commons/BUILD                                                                             |    3 -
 src/main/scala/com/roku/dea/spark/streaming/lego_commons/resources/monitor_streaming_lag.py                                                |   96 ++++
 src/main/scala/com/roku/dea/spark/streaming/lego_commons/resources/submit_utils.sh                                                         |   22 +
 src/main/scala/com/roku/dea/spark/streaming/lego_gc/BUILD                                                                                  |    7 +-
 src/main/scala/com/roku/dea/spark/streaming/lego_gc/LegoGcStreaming.scala                                                                  |   12 +-
 src/main/scala/com/roku/dea/spark/streaming/lego_gc/LegoGcStreamingConf.scala                                                              |   13 +-
 src/main/scala/com/roku/dea/spark/streaming/lego_gc/resources/conf/lego_gc_streaming_dev.conf                                              |   28 +-
 src/main/scala/com/roku/dea/spark/streaming/lego_gc/resources/conf/lego_gc_streaming_prod.conf                                             |   29 +-
 src/main/scala/com/roku/dea/spark/streaming/lego_gc/resources/conf/lego_gc_streaming_prod_v2.conf                                          |   92 ++++
 src/main/scala/com/roku/dea/spark/streaming/lego_gc/resources/monitor_streaming_lag.py                                                     |   96 ++++
 src/main/scala/com/roku/dea/spark/streaming/lego_gc/resources/setup_db.sql                                                                 |   10 +-
 src/main/scala/com/roku/dea/spark/streaming/lego_gc/resources/submit_lego_gc_v2.sh                                                         |   66 +++
 src/main/scala/com/roku/dea/spark/streaming/lego_gc/resources/submit_utils.sh                                                              |   22 +
 src/main/scala/com/roku/dea/spark/streaming/lego_generic/BUILD                                                                             |    3 -
 src/main/scala/com/roku/dea/spark/streaming/lego_generic/resources/monitor_streaming_lag.py                                                |   96 ++++
 src/main/scala/com/roku/dea/spark/streaming/lego_generic/resources/submit_utils.sh                                                         |   22 +
 src/main/scala/com/roku/dea/spark/streaming/metrics/Utils/BUILD                                                                            |    3 -
 src/main/scala/com/roku/dea/spark/streaming/metrics/Utils/resources/monitor_streaming_lag.py                                               |   96 ++++
 src/main/scala/com/roku/dea/spark/streaming/metrics/Utils/resources/submit_utils.sh                                                        |   22 +
 src/main/scala/com/roku/dea/spark/streaming/metrics/raf/BUILD                                                                              |    4 -
 src/main/scala/com/roku/dea/spark/streaming/metrics/raf/resources/monitor_streaming_lag.py                                                 |   96 ++++
 src/main/scala/com/roku/dea/spark/streaming/metrics/raf/resources/streaming.conf                                                           |   50 +++
 src/main/scala/com/roku/dea/spark/streaming/metrics/raf/resources/submit_utils.sh                                                          |   22 +
 src/main/scala/com/roku/dea/spark/streaming/metrics/ramsv2/BUILD                                                                           |    3 -
 src/main/scala/com/roku/dea/spark/streaming/metrics/ramsv2/resources/monitor_streaming_lag.py                                              |   96 ++++
 src/main/scala/com/roku/dea/spark/streaming/metrics/ramsv2/resources/submit_utils.sh                                                       |   22 +
 src/main/scala/com/roku/dea/spark/streaming/po/conversions/BUILD                                                                           |    3 -
 src/main/scala/com/roku/dea/spark/streaming/po/conversions/resources/monitor_streaming_lag.py                                              |   96 ++++
 src/main/scala/com/roku/dea/spark/streaming/po/conversions/resources/submit_utils.sh                                                       |   22 +
 src/main/scala/com/roku/dea/spark/streaming/roku_pixel/BUILD                                                                               |    3 -
 src/main/scala/com/roku/dea/spark/streaming/roku_pixel/resources/monitor_streaming_lag.py                                                  |   96 ++++
 src/main/scala/com/roku/dea/spark/streaming/roku_pixel/resources/submit_utils.sh                                                           |   22 +
 src/main/scala/com/roku/dea/spark/streaming/tclogs/BUILD                                                                                   |    1 -
 src/main/scala/com/roku/dea/spark/streaming/tclogs/resources/submit_utils.sh                                                               |   22 +
 src/main/scala/com/roku/delta/direct_license/CategoryContents2AeroSpike.scala                                                              |    8 +-
 src/main/scala/com/roku/delta/logs/BUILD                                                                                                   |   22 -
 src/main/scala/com/roku/delta/logs/SummarizePredictions.scala                                                                              |  178 --------
 src/main/scala/com/roku/delta/mock_traffic/MockTraffic2NormalizationService.scala                                                          |    2 +-
 src/main/scala/com/roku/dmp/data_collab/DataCollabMaintenance.scala                                                                        |   96 ++++
 src/main/scala/com/roku/dmp/data_collab/DataCollabPrepare.scala                                                                            |   35 +-
 src/main/scala/com/roku/dmp/data_collab/Dataset.scala                                                                                      |    9 +
 src/main/scala/com/roku/dmp/data_collab/DatasetQueries.scala                                                                               |  390 ++++++++++------
 src/main/scala/com/roku/dmp/data_collab/IdType.scala                                                                                       |    9 +
 src/main/scala/com/roku/dmp/data_collab/PiiHash.scala                                                                                      |   14 +
 src/main/scala/com/roku/dmp/models/ddl/patches/2021/09/Add-New-DSP-OneView-Category-DMP-8173.sql                                           |    7 +
 src/main/scala/com/roku/dmp/sideloading/GenericAccountSideloading.scala                                                                    |    2 +-
 src/main/scala/com/roku/dmp/uibackend/metadata/ChannelLoader.scala                                                                         |   11 +-
 src/main/scala/com/roku/dmp/userprofile/load/AccountSubscriptionSummaryLoader.scala                                                        |    1 +
 src/main/scala/com/roku/dmp/userprofile/load/AccountSummaryLoader.scala                                                                    |   16 +-
 src/main/scala/com/roku/dmp/userprofile/load/AdInsightsPersonSummaryLoader.scala                                                           |    8 +-
 src/main/scala/com/roku/dmp/userprofile/load/CurrentSubscriptionStatusLoader.scala                                                         |    1 +
 src/main/scala/com/roku/mlp/utils/BUILD                                                                                                    |    2 +-
 src/main/scala/com/roku/mlp/utils/resources/MlpEventsSchema.json                                                                           |  307 +++++++++++++
 src/main/scala/com/roku/mlp/utils/resources/daro/daro_usermodel_request_template.json                                                      |  428 ++++++++++++++++++
 src/main/scala/com/roku/mlp/utils/resources/daro/daro_usermodel_request_template_global_no_gd.json                                         |  432 ++++++++++++++++++
 src/main/scala/com/roku/mlp/utils/resources/daro/pushRequest.sh                                                                            |   18 +
 src/main/scala/com/roku/mlp/utils/resources/daro/submit_user_model.sh                                                                      |   90 ++++
 src/main/scala/com/roku/mlp/utils/resources/log4j.properties                                                                               |   47 ++
 src/main/scala/com/roku/mlp/utils/resources/mlp.conf                                                                                       |  233 ++++++++++
 src/main/scala/com/roku/mlp/v2/BUILD                                                                                                       |    2 +-
 src/main/scala/com/roku/mlp/v2/features/BUILD                                                                                              |    2 +-
 src/main/scala/com/roku/mlp/v2/features/resources/MlpEventsSchema.json                                                                     |  307 +++++++++++++
 src/main/scala/com/roku/mlp/v2/features/resources/daro/daro_usermodel_request_template.json                                                |  428 ++++++++++++++++++
 src/main/scala/com/roku/mlp/v2/features/resources/daro/daro_usermodel_request_template_global_no_gd.json                                   |  432 ++++++++++++++++++
 src/main/scala/com/roku/mlp/v2/features/resources/daro/pushRequest.sh                                                                      |   18 +
 src/main/scala/com/roku/mlp/v2/features/resources/daro/submit_user_model.sh                                                                |   90 ++++
 src/main/scala/com/roku/mlp/v2/features/resources/log4j.properties                                                                         |   47 ++
 src/main/scala/com/roku/mlp/v2/features/resources/mlp.conf                                                                                 |  233 ++++++++++
 src/main/scala/com/roku/mlp/v2/resources/MlpEventsSchema.json                                                                              |  307 +++++++++++++
 src/main/scala/com/roku/mlp/v2/resources/daro/daro_usermodel_request_template.json                                                         |  428 ++++++++++++++++++
 src/main/scala/com/roku/mlp/v2/resources/daro/daro_usermodel_request_template_global_no_gd.json                                            |  432 ++++++++++++++++++
 src/main/scala/com/roku/mlp/v2/resources/daro/pushRequest.sh                                                                               |   18 +
 src/main/scala/com/roku/mlp/v2/resources/daro/submit_user_model.sh                                                                         |   90 ++++
 src/main/scala/com/roku/mlp/v2/resources/log4j.properties                                                                                  |   47 ++
 src/main/scala/com/roku/mlp/v2/resources/mlp.conf                                                                                          |  233 ++++++++++
 src/main/scala/com/roku/mlp/v3/BUILD                                                                                                       |    2 +-
 src/main/scala/com/roku/mlp/v3/resources/MlpEventsSchema.json                                                                              |  307 +++++++++++++
 src/main/scala/com/roku/mlp/v3/resources/daro/daro_usermodel_request_template.json                                                         |  428 ++++++++++++++++++
 src/main/scala/com/roku/mlp/v3/resources/daro/daro_usermodel_request_template_global_no_gd.json                                            |  432 ++++++++++++++++++
 src/main/scala/com/roku/mlp/v3/resources/daro/pushRequest.sh                                                                               |   18 +
 src/main/scala/com/roku/mlp/v3/resources/daro/submit_user_model.sh                                                                         |   90 ++++
 src/main/scala/com/roku/mlp/v3/resources/log4j.properties                                                                                  |   47 ++
 src/main/scala/com/roku/mlp/v3/resources/mlp.conf                                                                                          |  233 ++++++++++
 src/main/scala/com/roku/mo/MoExperimentReporterApp.scala                                                                                   |    6 +-
 src/main/scala/com/roku/rome/metadata-loader/SfdcLoader.scala                                                                              |  238 +++++-----
 src/main/scala/com/roku/rome/models/ddl/patches/ROME-1.15.1.sql                                                                            |    3 +
 src/main/scala/com/roku/rome/models/ddl/patches/ROME-1.15.sql                                                                              |    2 +-
 src/main/scala/com/roku/rome/models/ddl/patches/ROME-1.16.sql                                                                              |   44 ++
 src/main/scala/com/roku/rome/models/ddl/patches/ROME-1.6.sql                                                                               |    1 +
 src/main/scala/com/roku/rome/models/generated/AppTables.scala                                                                              |  186 +++++---
 src/main/scala/com/roku/rome/models/generated/ChangelogTables.scala                                                                        |  302 +++++++------
 src/main/scala/com/roku/rome/uibackend/controllers/BUILD                                                                                   |    3 +-
 src/main/scala/com/roku/rome/uibackend/controllers/BalanceSheetController.scala                                                            |   18 +-
 src/main/scala/com/roku/rome/uibackend/controllers/InsertionOrderController.scala                                                          |    2 +-
 src/main/scala/com/roku/rome/uibackend/controllers/InvoiceController.scala                                                                 |   21 +-
 src/main/scala/com/roku/rome/uibackend/controllers/IoSnapshotController.scala                                                              |    7 +-
 src/main/scala/com/roku/rome/uibackend/controllers/LineItemController.scala                                                                |   37 +-
 src/main/scala/com/roku/rome/uibackend/controllers/PeriodCloseController.scala                                                             |    6 +-
 src/main/scala/com/roku/rome/uibackend/controllers/SspController.scala                                                                     |   93 ++--
 src/main/scala/com/roku/rome/uibackend/core/InsertionOrderManager.scala                                                                    |   70 ++-
 src/main/scala/com/roku/rome/uibackend/core/LineItemManager.scala                                                                          |  111 +++--
 src/main/scala/com/roku/rome/uibackend/core/RevRecManager.scala                                                                            |    6 +-
 src/main/scala/com/roku/rome/uibackend/core/SspManager.scala                                                                               |   12 +-
 src/main/scala/com/roku/rome/uibackend/core/ValidationManager.scala                                                                        |    2 +-
 src/main/scala/com/roku/rome/uibackend/core/changelog/InsertionOrderChangelogManager.scala                                                 |   15 +-
 src/main/scala/com/roku/rome/uibackend/core/sfdc_boomi/OneLoginAccessToken.scala                                                           |   51 ---
 src/main/scala/com/roku/rome/uibackend/core/sfdc_boomi/SFDCBoomiServiceApi.scala                                                           |   16 +-
 src/main/scala/com/roku/rome/uibackend/rest/BalanceSheetRest.scala                                                                         |    2 +-
 src/main/scala/com/roku/rome/uibackend/rest/InvoiceRest.scala                                                                              |    4 +-
 src/main/scala/com/roku/rome/uibackend/rest/IoSnapshotRest.scala                                                                           |    3 +-
 src/main/scala/com/roku/rome/uibackend/rest/PeriodCloseRest.scala                                                                          |    3 +-
 src/main/scala/com/roku/rome/uibackend/rest/ReportRest.scala                                                                               |   18 +-
 src/main/scala/com/roku/rome/uibackend/rest/UserRest.scala                                                                                 |   55 ++-
 src/main/scala/com/roku/rome/uibackend/tasks/InvoiceStateUpdateSchedulerTask.scala                                                         |   57 +--
 src/main/scala/com/roku/rome/uibackend/utils/Utils.scala                                                                                   |   22 +
 src/main/scala/com/roku/rum/RumServingMetadataDump.scala                                                                                   |    1 +
 src/main/scripts/agg_device_streaming_hourly.sql                                                                                           |  173 -------
 src/main/scripts/shell-scripts/PROGDE-1098_avro.sh                                                                                         |    2 +
 src/test/java/com/roku/ads/lambdas/lat/LatSetterLambdaTest.java                                                                            |   23 +-
 src/test/java/com/roku/ads/pixelserver/scribe/BUILD                                                                                        |    1 +
 src/test/java/com/roku/ads/pixelserver/scribe/ScribeWriterServiceTest.java                                                                 |   56 +--
 src/test/java/com/roku/ads/pixelserver/util/BUILD                                                                                          |    2 +-
 src/test/java/com/roku/ads/pixelserver/util/HttpUtilsTest.java                                                                             |   86 ++++
 src/test/java/com/roku/ads/pixelserver/util/PropertiesReaderTest.java                                                                      |   33 +-
 src/test/java/com/roku/ads/rams/eventbackup/BUILD                                                                                          |   18 +
 src/test/java/com/roku/ads/rams/eventbackup/EventBackupTest.java                                                                           |   38 ++
 src/test/java/com/roku/ads/rams/module/ads/margin/BUILD                                                                                    |    3 +-
 src/test/java/com/roku/ads/rams/module/ads/margin/MarginOptimizerModuleTest.java                                                           |  229 ++++++++--
 src/test/java/com/roku/ads/rams/module/ads/pricing/BUILD                                                                                   |    4 +-
 src/test/java/com/roku/ads/rams/module/ads/pricing/VariablePricingModuleTest.java                                                          |   63 ++-
 src/test/java/com/roku/ads/rams/module/ads/scoring/BUILD                                                                                   |   45 +-
 src/test/java/com/roku/ads/rams/module/ads/scoring/BucketTest.java                                                                         |   46 ++
 src/test/java/com/roku/ads/rams/module/ads/scoring/DisplayAdScoringModuleTest.java                                                         |    6 +-
 src/test/java/com/roku/ads/rams/module/ads/scoring/staging/application.properties                                                          |    5 +-
 src/test/java/com/roku/ads/rams/module/common/RamsEventGenTest.java                                                                        |    4 +-
 src/test/java/com/roku/ads/rams/service/cache/cacheloader/DfpMetaDataLoaderTest.java                                                       |    2 +
 src/test/java/com/roku/ads/tam/event/TamEventGenTest.java                                                                                  |    2 +
 src/test/java/com/roku/ads/tam/module/requestparse/TamRequestParseModuleTest.java                                                          |    7 +-
 src/test/java/com/roku/ads/tam/module/response/TamResponseModuleTest.java                                                                  |  112 +++++
 src/test/java/com/roku/ads/tam/service/cache/AdPolicyCacheTest.java                                                                        |   10 +-
 src/test/java/com/roku/ads/test/integration/admedia/adservices/config/config.json                                                          |    2 +-
 src/test/java/com/roku/ads/test/integration/admedia/adservices/testdata/ramsV2TestData/createPriorityMappingData.csv                       |    2 +-
 src/test/java/com/roku/ads/test/integration/admedia/adservices/tests/DealsIT.java                                                          |  223 +++++++--
 src/test/java/com/roku/ads/test/integration/admedia/adservices/tests/InventoryPackageIT.java                                               |  613 +++++++++++++++----------
 src/test/java/com/roku/ads/test/integration/admedia/adservices/tests/RamsServicesBaseTest.java                                             |  111 ++++-
 src/test/java/com/roku/ads/test/integration/admedia/adservices/tests/TagCreateIT.java                                                      |   12 -
 src/test/java/com/roku/ads/test/integration/admedia/constants/MethodConstants.java                                                         |    3 +
 src/test/java/com/roku/ads/test/integration/admedia/graphqlqueries/dealqueries/createDeal.graphql                                          |    6 +-
 src/test/java/com/roku/ads/test/integration/admedia/graphqlqueries/dealqueries/deleteDeal.graphql                                          |    2 +-
 src/test/java/com/roku/ads/test/integration/admedia/graphqlqueries/dealqueries/editDeal.graphql                                            |    6 +-
 src/test/java/com/roku/ads/test/integration/admedia/graphqlqueries/dealqueries/findDeals.graphql                                           |    2 +
 src/test/java/com/roku/ads/test/integration/admedia/graphqlqueries/dealqueries/findTags.graphql                                            |    5 +
 src/test/java/com/roku/ads/test/integration/admedia/graphqlqueries/inventoryPackageQueries/getInventoryPackages.graphql                    |   11 +
 src/test/java/com/roku/ads/test/integration/admedia/rams/config/config.json                                                                |    6 +-
 src/test/java/com/roku/ads/test/integration/admedia/rams/testdata/{dev-mgupta => dev-mgupta1}/application.properties                       |    4 +-
 src/test/java/com/roku/ads/test/integration/admedia/rams/testdata/{dev-mgupta => dev-mgupta1}/channelOnlyOrTagOnlyRuleSsoSecapdsp.json     |    0
 src/test/java/com/roku/ads/test/integration/admedia/rams/testdata/{dev-mgupta => dev-mgupta1}/ip_ridas.csv                                 |    0
 src/test/java/com/roku/ads/test/integration/admedia/rams/testdata/{dev-mgupta => dev-mgupta1}/ip_ridas_10k.csv                             |    0
 src/test/java/com/roku/ads/test/integration/admedia/rams/testdata/dev-wweiss/application.properties                                        |    2 +-
 src/test/java/com/roku/ads/test/integration/admedia/rams/tests/display/DisplayAdsIT.java                                                   |   36 +-
 src/test/java/com/roku/ads/test/integration/admedia/rams/tests/event/EventBackupIT.java                                                    |   37 +-
 src/test/java/com/roku/ads/test/integration/admedia/rams/tests/hb/HbHoIT.java                                                              |    3 +-
 src/test/java/com/roku/ads/test/integration/admedia/rams/tests/hb/HbIT.java                                                                |    3 -
 src/test/java/com/roku/ads/test/integration/admedia/rams/tests/hb/VariablePriceIT.java                                                     |    1 -
 src/test/java/com/roku/ads/test/integration/admedia/tam/config/config.json                                                                 |   17 +-
 src/test/java/com/roku/ads/test/integration/admedia/tam/testdata/adPolicyEmptyPreRollUrlsWithAdBreaks.json                                 |   35 ++
 src/test/java/com/roku/ads/test/integration/admedia/tam/testdata/adPolicyPreRollWithUrlsWithAdBreaks.json                                  |   34 ++
 src/test/java/com/roku/ads/test/integration/admedia/tam/tests/TamEpisodeNewSessionAdPolicyIT.java                                          |   77 ++++
 src/test/java/com/roku/ads/test/integration/admedia/tam/tests/constants/TamConstants.java                                                  |    1 +
 src/test/java/com/roku/ads/test/integration/admedia/tam/tests/datamodel/AdPolicyContent.java                                               |    3 +
 src/test/java/com/roku/ads/test/integration/admedia/tam/tests/datamodel/PreRollData.java                                                   |    1 +
 src/test/java/com/roku/ads/test/integration/admedia/tam/utils/TamTestUtils.java                                                            |    1 +
 src/test/java/com/roku/ads/test/integration/admedia/utils/ServiceV2Utils.java                                                              |    6 +-
 src/test/java/com/roku/ads/test/integration/common/BaseTest.java                                                                           |    2 +-
 src/test/java/com/roku/ads/test/integration/common/Constants.java                                                                          |    2 +-
 src/test/java/com/roku/ads/test/integration/rome/datamodel/io/InsertionOrder.java                                                          |    4 +
 src/test/java/com/roku/ads/test/integration/rome/sql/create_active_test_insertion_order.sql                                                |    2 +-
 src/test/java/com/roku/ads/test/integration/rome/sql/create_test_insertion_order_io_holding.sql                                            |    2 +-
 src/test/java/com/roku/ads/test/integration/rome/sql/create_test_insertion_order_io_holding_delivery_cap_on.sql                            |    1 +
 src/test/java/com/roku/ads/test/integration/rome/sql/create_test_insertion_order_io_holding_sfdc_line_add_and_delete_op.sql                |    2 +-
 src/test/java/com/roku/ads/test/integration/rome/sql/invoice-credit-rebill/create_io_multiple_line_actuals.sql                             |    1 +
 src/test/java/com/roku/ads/test/integration/rome/sql/invoice-credit-rebill/create_io_multiple_line_actuals_cap_on.sql                      |    1 +
 src/test/java/com/roku/ads/test/integration/rome/sql/invoice-credit-rebill/create_io_multiple_line_fixed.sql                               |    1 +
 src/test/java/com/roku/ads/test/integration/rome/sql/invoice-credit-rebill/create_io_multiple_line_fixed_cap_on.sql                        |    1 +
 src/test/java/com/roku/ads/test/integration/rome/sql/invoice-credit-rebill/create_io_single_line_actuals.sql                               |    1 +
 src/test/java/com/roku/ads/test/integration/rome/sql/invoice-credit-rebill/create_io_single_line_fixed.sql                                 |    1 +
 src/test/java/com/roku/ads/test/integration/rome/sql/remove_test_insertion_order.sql                                                       |    4 +-
 src/test/java/com/roku/ads/test/integration/rome/sql/revisions/create_test_insertion_order_io_holding_invalid_revisions.sql                |    2 +-
 src/test/java/com/roku/ads/test/integration/rome/sql/revisions/create_test_insertion_order_io_holding_no_revisions.sql                     |    2 +-
 src/test/java/com/roku/ads/test/integration/rome/sql/revisions/create_test_insertion_order_io_holding_valid_revisions.sql                  |    2 +-
 src/test/java/com/roku/ads/test/integration/rome/test/balancesheet/BalanceSheetAdjustmentsTest.java                                        |   94 ++++
 src/test/java/com/roku/ads/test/integration/rome/test/balancesheet/BalanceSheetBaseTest.java                                               |   21 +-
 src/test/java/com/roku/ads/test/integration/rome/test/balancesheet/BalanceSheetTest.java                                                   |    2 -
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0010786.sql                                               |    4 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0015907.sql                                               |    4 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0016650.sql                                               |    4 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0024960.sql                                               |    4 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0025003.sql                                               |    4 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0025444.sql                                               |    4 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0025505.sql                                               |    4 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0025559.sql                                               |    4 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0025560.sql                                               |    4 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0025567.sql                                               |    4 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0025785.sql                                               |    4 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0025921.sql                                               |    4 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0026594.sql                                               |    4 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0026780.sql                                               |    4 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0028404.sql                                               |    4 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0029002.sql                                               |    8 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0029012.sql                                               |   12 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0032346.sql                                               |   12 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0033772.sql                                               |    4 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0034403.sql                                               |    8 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0038343.sql                                               |    7 +-
 src/test/java/com/roku/ads/test/integration/rome/testdata/io-data-simulation-sql/0039162.sql                                               |    8 +-
 src/test/java/com/roku/dea/hive/udfs/DecodePathPartUdfTest.java                                                                            |   63 +++
 src/test/java/com/roku/pub/cms/service/CreativeServiceTest.java                                                                            |    6 +-
 src/test/java/com/roku/pub/cms/service/StorageServiceTest.java                                                                             |   23 +-
 src/test/java/com/roku/pub/cms/service/VastServiceTest.java                                                                                |    4 +-
 src/test/java/com/roku/pub/cms/vertx/GetCreativeBatchHandlerTest.java                                                                      |    4 +-
 src/test/java/com/roku/pub/cms/vertx/GetCreativeHandlerTest.java                                                                           |    4 +-
 src/test/java/com/roku/pub/cms/vertx/PutCreativeHandlerTest.java                                                                           |    2 +-
 src/test/java/com/roku/pub/server/BUILD                                                                                                    |    4 +-
 src/test/java/com/roku/pub/server/handlers/BUILD                                                                                           |    2 +-
 src/test/java/com/roku/pub/server/hbhandlers/BUILD                                                                                         |    2 +-
 src/test/java/com/roku/pub/server/hbhandlers/RapsUtilTest.java                                                                             |   12 +
 src/test/java/com/roku/pub/server/util/BUILD                                                                                               |    2 +-
 src/test/scala/com/roku/adcloud/spark/insights/common/BUILD                                                                                |   24 +-
 src/test/scala/com/roku/adcloud/spark/insights/common/SparkTestBase.scala                                                                  |  208 ++++++++-
 src/test/scala/com/roku/adcloud/spark/insights/common/SparkTestBaseTest.scala                                                              |  202 +++++++++
 src/test/scala/com/roku/adcloud/spark/insights/dspcordcutter/dataprep/BUILD                                                                |    8 +
 src/test/scala/com/roku/adcloud/spark/insights/dspcordcutter/dataprep/DailyFeaturesFromDSPImpressionsTest.scala                            |   35 ++
 src/test/scala/com/roku/ads/services/rams/backend/dao/ChannelActionValueDaoTest.scala                                                      |    2 +-
 src/test/scala/com/roku/ads/services/rams/backend/dao/DealDaoTest.scala                                                                    |   25 +-
 src/test/scala/com/roku/ads/services/rams/backend/dao/PriorityMapDaoTest.scala                                                             |   10 +-
 src/test/scala/com/roku/ads/services/rams/backend/inventorypackage/InventoryPackageObjectTests.scala                                       |   17 +-
 tools/build_rules/common.bzl                                                                                                               |   30 +-
 tools/build_rules/jar_library.bzl                                                                                                          |   33 +-
 tools/build_rules/java_library.bzl                                                                                                         |    4 +-
 tools/build_rules/junit_tests.bzl                                                                                                          |    9 +-
 tools/build_rules/jvm_binary.bzl                                                                                                           |   79 ++--
 tools/build_rules/resources.bzl                                                                                                            |    5 -
 tools/build_rules/scala_library.bzl                                                                                                        |   14 +-
 1211 files changed, 53174 insertions(+), 12691 deletions(-)
 create mode 100644 3rdparty/java/springboot/BUILD
 create mode 100644 idea.bazelproject
 create mode 100644 roku_dea_style.xml
 create mode 100644 src/main/ddls/avro_schemas/roku/dim_content_library_status_history.avsc
 create mode 100644 src/main/ddls/hive_ddls/ads/delta/migrations/2021_09_13.hql
 create mode 100644 src/main/ddls/hive_ddls/ads/dmp/create_custom_acr_linear_segments_tables.hql
 create mode 100644 src/main/ddls/hive_ddls/ads/dmp/graph/create_rida_graph.hql
 create mode 100644 src/main/ddls/hive_ddls/ads/insights/thirdparty_viewability.hql
 create mode 100644 src/main/ddls/hive_ddls/ads/insights/thirdparty_viewability_dev.hql
 create mode 100644 src/main/ddls/hive_ddls/ads/insights/ump_facts.hql
 create mode 100644 src/main/ddls/hive_ddls/ads/migrations/0086_RAPSCS-163.hql
 create mode 100644 src/main/ddls/hive_ddls/ads/migrations/DATACOLAB-59-deequ-validation.hql
 create mode 100644 src/main/ddls/hive_ddls/ads/migrations/DATACOLLAB-57-hourly-dag-perf.hql
 create mode 100644 src/main/ddls/hive_ddls/ads/rams/migrations/0043-RAMS-5583.hql
 create mode 100644 src/main/ddls/hive_ddls/ads/rams/migrations/0043_RAMS-5579.hql
 create mode 100644 src/main/ddls/hive_ddls/ads/rams/migrations/0044-RAMS-5619.hql
 create mode 100644 src/main/ddls/hive_ddls/ads/rams/migrations/RAMS_4507.hql
 create mode 100644 src/main/ddls/hive_ddls/ads/rams/migrations/RAMS_5694.hql
 create mode 100644 src/main/ddls/hive_ddls/dsp/als_tables_create.hql
 create mode 100644 src/main/ddls/hive_ddls/dsp/dsp-dmp-internal-tables.hql
 create mode 100644 src/main/ddls/hive_ddls/dsp/dsp-dmp-tables.hql
 create mode 100644 src/main/ddls/hive_ddls/dsp/dsp-graph-tables.hql
 create mode 100644 src/main/ddls/hive_ddls/dsp/dsp_daz_tables.hql
 create mode 100644 src/main/ddls/hive_ddls/dsp/solutions/ADDEV-17281-hulu_rejected_creative_tables.hql
 create mode 100644 src/main/ddls/hive_ddls/pmp/migrations/0038_PMP_5383_ddl.hql
 create mode 100644 src/main/ddls/hive_ddls/rum/APERF-290-rum-scores-and-qualified-offers.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/06/DE-37.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/07/ADI-599.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/07/DEA-13533.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/07/DMP-8125.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/31/ADDEV-17393.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/ACRDATA-161.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/ADDEV-14356.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/ADI-665.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/ADI-677.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/ADI-689.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/ADI-705.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/APERF-277.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/APERF-292.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/CDE-24.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/CDE-30.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/DE-21.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/DE-21_partitions.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/DE-609.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/DE-7.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/DMP-8196.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/EUEDE-323.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/MLP-325.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/PROGDE-1098.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/PROGDE-1365.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/PROGDE-1382.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/PROGDE-1414_device_ux_serde.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/RAPSCS-162.sql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/08/SAM-16495.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/ACRDATA-143.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/ADCLOUD-1793.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/ADDEV-16896.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/ADI-668.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/ADI-701.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/ADI-708.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/ADI-711.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/ADI-713.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/ADI-713_1.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/ADI-716.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/CDE-34.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/CDE-41.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/CDE-45.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/CDE-46.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/CDE-47-2.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/CDE-47.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/DE-370.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/DE-544.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/DE-550.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/DE-588.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/DE-679.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/DE-717.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/DE-729.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/EUEDE-277.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/EUEDE-317-1.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/EUEDE-317.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/EUEDE-349_Insert.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/EUEDE-349_create_table.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/EUEDE-364.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/PROGDE-1405.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/PROGDE-1430.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/PROGDE-1436.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/PROGDE-1443.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/2021/09/addev-17565.hql
 create mode 100644 src/main/ddls/hive_ddls/schema_changes/ADSPLN-1818.hql
 create mode 100644 src/main/ddls/mysql_ddls/ads/migrations/DATACOLLAB-71-pii_hash_salt_remove.sql
 create mode 100644 src/main/ddls/mysql_ddls/ads/migrations/DATACOLLAB-73-snowflake-retention.sql
 create mode 100644 src/main/ddls/mysql_ddls/ads/rams/migrations/RAMS-5737.sql
 create mode 100644 src/main/ddls/redshift_ddls/rams/migrations/044-RAMS-5619.sql
 create mode 100644 src/main/ddls/redshift_ddls/rams/migrations/045-RAMS-5754.sql
 create mode 100644 src/main/ddls/redshift_ddls/schema_changes/2021/08/EUEDE-323.sql
 create mode 100644 src/main/ddls/redshift_ddls/schema_changes/2021/08/PROGDE-1098.sql
 create mode 100644 src/main/ddls/redshift_ddls/schema_changes/2021/09/ADCLOUD-1793.sql
 create mode 100644 src/main/ddls/redshift_ddls/schema_changes/2021/09/AIF-154.sql
 create mode 100644 src/main/ddls/redshift_ddls/schema_changes/2021/09/DE-573.sql
 create mode 100644 src/main/ddls/redshift_ddls/schema_changes/2021/09/DE-717.sql
 create mode 100644 src/main/ddls/redshift_ddls/schema_changes/2021/09/PROGDE-1405.sql
 create mode 100644 src/main/ddls/redshift_ddls/schema_changes/2021/09/PROGDE-1419.sql
 create mode 100644 src/main/ddls/redshift_ddls/schema_changes/2021/09/PROGDE-1455.sql
 create mode 100644 src/main/ddls/redshift_ddls/schema_changes/ADSPLN-1818.sql
 rename src/main/deployment_automations/avails/{Jenkinsfile-nightly => Jenkinsfile-master} (99%)
 create mode 100644 src/main/deployment_automations/avails/avails-dev-deploy/Jenkinsfile
 create mode 100644 src/main/deployment_automations/avails/avails-dev-deploy/deployment.json
 create mode 100644 src/main/deployment_automations/avails/avails-dev-deploy/qa_config.ini
 create mode 100644 src/main/deployment_automations/data-processing-roku-dag-bag/master-build/Jenkinsfile
 create mode 100644 src/main/deployment_automations/dmp/liquibase/Jenkinsfile
 create mode 100644 src/main/deployment_automations/dmp/liquibase/users.json
 delete mode 100644 src/main/deployment_automations/rams-data-pipeline/Jenkinsfile
 rename src/main/deployment_automations/rams-nrt-pipeline/{Jenkinsfile => JenkinsfileProd} (98%)
 delete mode 100644 src/main/deployment_automations/rome/ui-rest-server-stg/users.json
 create mode 100644 src/main/dmls/hive_dmls/AIF-199-add-pod-ads.hql
 rename src/main/go/src/avails/testdata/banner/user_2020-07-20/{user_2020-07-20 => }/2020-07-20/local/attr/data/part_0.csv.gz (100%)
 rename src/main/go/src/avails/testdata/banner/user_2020-07-20/{user_2020-07-20 => }/2020-07-20/local/attr/header/header.txt (100%)
 create mode 100644 src/main/installers/aerospike-enterprise/rsei_installer/target_root/etc/aerospike/templates/features.conf
 create mode 100644 src/main/installers/aerospike-enterprise/rsei_installer/target_root/etc/aerospike/templates/logrotate
 create mode 100644 src/main/installers/aerospike-enterprise/rsei_installer/target_root/etc/aerospike/templates/rams_aero56.template
 create mode 100755 src/main/installers/marketing-service/rsei_installer/INSTALL_SCRIPT
 create mode 100644 src/main/installers/marketing-service/rsei_installer/target_root/etc/dd-agent/conf.d/marketing-service-server.yaml
 create mode 100644 src/main/installers/marketing-service/rsei_installer/target_root/etc/sv/marketing-service-server/log/main/config
 create mode 100644 src/main/installers/marketing-service/rsei_installer/target_root/etc/sv/marketing-service-server/log/run
 create mode 100644 src/main/installers/marketing-service/rsei_installer/target_root/etc/sv/marketing-service-server/run
 create mode 100644 src/main/installers/marketing-service/rsei_installer/target_root/opt/marketing-service-server/conf/.donotdelete
 create mode 100755 src/main/installers/marketing-service/rsei_installer/target_root/opt/marketing-service-server/marketing-service-server.sh
 create mode 100755 src/main/installers/marketing-service/setup_installer.sh
 create mode 100644 src/main/java/BUILD.bazel
 create mode 100644 src/main/java/com/roku/ads/email/common/service/User.java
 create mode 100644 src/main/java/com/roku/ads/email/common/service/UserServiceClient.java
 create mode 100644 src/main/java/com/roku/ads/email/common/service/UserServiceClientImpl.java
 create mode 100644 src/main/java/com/roku/ads/email/common/service/UserServiceConfig.java
 create mode 100644 src/main/java/com/roku/ads/marketing/marketingservice/BUILD
 create mode 100644 src/main/java/com/roku/ads/marketing/marketingservice/MarketingServiceApplication.java
 create mode 100644 src/main/java/com/roku/ads/marketing/marketingservice/config/ApplicationConfig.java
 create mode 100644 src/main/java/com/roku/ads/marketing/marketingservice/config/BUILD
 create mode 100644 src/main/java/com/roku/ads/marketing/marketingservice/handlers/BUILD
 create mode 100644 src/main/java/com/roku/ads/marketing/marketingservice/handlers/HealthHandler.java
 create mode 100644 src/main/java/com/roku/ads/marketing/marketingservice/resources/BOOT-INF/classes/META-INF/spring.factories
 create mode 100644 src/main/java/com/roku/ads/marketing/marketingservice/resources/META-INF/spring.factories
 create mode 100644 src/main/java/com/roku/ads/marketing/marketingservice/resources/application.properties
 create mode 100644 src/main/java/com/roku/ads/marketing/marketingservice/resources/logback.xml
 create mode 100644 src/main/java/com/roku/ads/marketing/marketingservice/routers/BUILD
 create mode 100644 src/main/java/com/roku/ads/marketing/marketingservice/routers/HealthRouter.java
 create mode 100644 src/main/java/com/roku/ads/pixelserver/util/EventIdGenerator.java
 create mode 100644 src/main/java/com/roku/ads/pixelserver/util/UniqueIdSequenceGenerator.java
 create mode 100644 src/main/java/com/roku/ads/rams/module/pixel/ridaprofile/BUILD
 create mode 100644 src/main/java/com/roku/ads/rams/module/pixel/ridaprofile/RidaProfileUpdaterModule.java
 create mode 100644 src/main/java/com/roku/ads/rams/rsei_installer/resources/module_conf/RidaProfileUpdaterModule.conf
 create mode 100644 src/main/java/com/roku/ads/rams/service/ratelimiter/RequestLimiterByEndPoint.java
 create mode 100644 src/main/java/com/roku/dea/hive/udfs/DecodePathPartUdf.java
 create mode 100644 src/main/java/com/roku/pub/aerospike/FutureDeleteListener.java
 create mode 100644 src/main/java/com/roku/pub/cms/data/BUILD
 create mode 100644 src/main/java/com/roku/pub/cms/data/CreativeMetadataParser.java
 rename src/main/java/com/roku/pub/{server/eventschema/single => cms/data}/cms_event.proto (97%)
 create mode 100644 src/main/java/com/roku/pub/cms/vertx/DeleteCreativeHandler.java
 create mode 100644 src/main/liquibase/mysql/dmp/Jenkinsfile
 create mode 100644 src/main/liquibase/mysql/dmp/Jenkinsfile_drop_db
 rename src/main/liquibase/mysql/dmp/{sql => sample_liquibase_sql}/2021-07-20_14-03-12.sql (100%)
 create mode 100644 src/main/liquibase/mysql/dmp/sample_liquibase_sql/2021-09-01_16-00-25.sql
 create mode 100644 src/main/liquibase/mysql/dmp/sample_liquibase_sql/2021-09-07_13-33-55.sql
 create mode 100755 src/main/liquibase/mysql/dmp/scripts/jenkins/checkCommitSet.sh
 create mode 100755 src/main/liquibase/mysql/dmp/scripts/jenkins/deleteDB.sh
 create mode 100755 src/main/liquibase/mysql/dmp/scripts/jenkins/liquibaseDeployment.sh
 create mode 100644 src/main/python/ADS/avails/sql/avails_usage_analytics.sql
 delete mode 100644 src/main/python/ADS/insights/acr/agg_adi_acr_education_tasks_helper.py
 delete mode 100644 src/main/python/ADS/insights/acr/agg_adi_acr_income_tasks_helper.py
 delete mode 100644 src/main/python/ADS/insights/acr/conf/agg_adi_acr_druid_ingest.json
 delete mode 100644 src/main/python/ADS/insights/acr/conf/agg_adi_acr_education_druid_ingest.json
 delete mode 100644 src/main/python/ADS/insights/acr/conf/agg_adi_acr_education_spark_job.conf
 delete mode 100644 src/main/python/ADS/insights/acr/conf/agg_adi_acr_income_spark_job.conf
 create mode 100644 src/main/python/ADS/insights/customer_journey/customer_journey_dmt_helper.py
 create mode 100644 src/main/python/ADS/insights/customer_journey/sql/customer_journey_trend_check.sql
 create mode 100644 src/main/python/ADS/insights/data_toolkit/conf/acr_panel.conf
 create mode 100644 src/main/python/ADS/insights/data_toolkit/conf/adi_household_panel_druid_ingest.json
 create mode 100644 src/main/python/ADS/insights/data_toolkit/conf/adi_oneview_household_map_druid_ingest.json
 create mode 100644 src/main/python/ADS/insights/data_toolkit/conf/targeting_specific_demo_inference.conf
 create mode 100644 src/main/python/ADS/insights/dspcordcutter/BUILD
 create mode 100644 src/main/python/ADS/insights/dspcordcutter/conf/agg_ctv_trans_spark_job.conf
 create mode 100644 src/main/python/ADS/insights/dspcordcutter/conf/agg_ump_imps_spark_job.conf
 create mode 100644 src/main/python/ADS/insights/dspcordcutter/conf/ctv_trans_snapshot_spark_job.conf
 create mode 100644 src/main/python/ADS/insights/dspcordcutter/conf/feature_discretization_spark_job.conf
 create mode 100644 src/main/python/ADS/insights/dspcordcutter/conf/feature_gen_spark_job.conf
 create mode 100644 src/main/python/ADS/insights/dspcordcutter/conf/ump_imps_snapshot_spark_job.conf
 create mode 100644 src/main/python/ADS/insights/dspcordcutter/dsp_cordcutter_feature_gen_dag.py
 create mode 100644 src/main/python/ADS/insights/dspcordcutter/dsp_cordcutter_helper.py
 create mode 100644 src/main/python/ADS/insights/dspcordcutter/dsp_cordcutter_snapshot_dag.py
 delete mode 100644 src/main/python/ADS/insights/linear_insights/hql/exclusive_reach.hql
 delete mode 100644 src/main/python/ADS/insights/linear_insights/hql/frequency_distribution.hql
 delete mode 100644 src/main/python/ADS/insights/linear_insights/hql/total_channel_reach.hql
 create mode 100644 src/main/python/ADS/insights/sam/adi_sam_dmt_helper.py
 create mode 100644 src/main/python/ADS/insights/sam/sql/agg_adi_sam_segment_reach_trend_check.sql
 create mode 100644 src/main/python/ADS/insights/sam/sql/agg_adi_sam_universe_reach_trend_check.sql
 create mode 100644 src/main/python/ADS/insights/sam/sql/dim_adi_sam_segment_correction_factor_trend_check.sql
 create mode 100644 src/main/python/ADS/insights/sam/sql/dim_adi_sam_segment_map_null_count_check.sql
 create mode 100644 src/main/python/ADS/insights/sam/sql/dim_adi_sam_segment_reverse_map_null_count_check.sql
 create mode 100644 src/main/python/ADS/insights/sam/sql/segment_ratio_check.sql
 create mode 100644 src/main/python/ADS/insights/sam/sql/universe_ratio_check.sql
 create mode 100644 src/main/python/ADS/insights/ump/conf/agg_adi_ump_bid_win_density_druid_ingest.json
 create mode 100644 src/main/python/ADS/insights/ump/conf/agg_adi_ump_bid_win_density_index_parallel_druid_ingest.json
 create mode 100644 src/main/python/ADS/insights/ump/conf/agg_adi_ump_bid_win_density_spark_job.conf
 create mode 100644 src/main/python/ADS/insights/ump/conf/fact_adi_ump_bids_spark_job.conf
 create mode 100644 src/main/python/ADS/insights/viewability/BUILD
 create mode 100644 src/main/python/ADS/insights/viewability/__init__.py
 create mode 100644 src/main/python/ADS/insights/viewability/conf/dv_viewability_spark_job.conf
 create mode 100644 src/main/python/ADS/insights/viewability/conf/ias_viewability_spark_job.conf
 create mode 100644 src/main/python/ADS/insights/viewability/conf/moat_viewability_spark_job.conf
 rename src/main/python/ADS/insights/{acr/conf/agg_adi_acr_income_druid_ingest.json => viewability/conf/third_party_viewability_druid_injest.json} (53%)
 create mode 100644 src/main/python/ADS/insights/viewability/sql/viewability_metrics_daily.sql
 create mode 100644 src/main/python/ADS/insights/viewability/viewability_dag.py
 create mode 100644 src/main/python/ADS/insights/viewability/viewability_helper.py
 create mode 100644 src/main/python/ADS/nielsen_ad/fact_game_hourly_detections.hql
 create mode 100644 src/main/python/ADS/nielsen_ad/fact_nielsen_tv_off_and_on.hql
 create mode 100644 src/main/python/ADS/nielsen_ad/nielsen_game_data_dag.py
 create mode 100644 src/main/python/ADS/nielsen_ad/nielsen_tv_off_and_on_dag.py
 create mode 100644 src/main/python/CDM/conf/cdm_spark_conf_intermediate.conf
 create mode 100644 src/main/python/CDM/conf/cdm_spark_conf_intermediate_x.conf
 create mode 100644 src/main/python/CDM/hql/agg_cdm_device_metrics.hql
 create mode 100644 src/main/python/CDM/hql/fact_device_intermediate_logs_final.hql
 create mode 100644 src/main/python/CDM/hql/fact_device_intermediate_logs_install.hql
 create mode 100644 src/main/python/CDM/hql/fact_device_intermediate_logs_launch.hql
 create mode 100644 src/main/python/CDM/hql/fact_device_intermediate_logs_stg_recreation.hql
 create mode 100644 src/main/python/CDM/hql/fact_device_intermediate_logs_ui_events.hql
 create mode 100644 src/main/python/CDM/hql/fact_device_intermediate_logs_ui_play.hql
 create mode 100644 src/main/python/CDM/hql/fact_device_log_launch_events_stg.hql
 create mode 100644 src/main/python/CDM/hql/fact_device_log_launch_events_stg_recreation.hql
 create mode 100644 src/main/python/CDM/hql/fact_device_ux_logs_dedup_orc_stg.hql
 create mode 100644 src/main/python/CON/CON_search_agg/search/agg_search_business_metrics.hql
 create mode 100644 src/main/python/CON/CON_traffic_attribution_agg/hql/fact_conversion_window_stg.hql
 create mode 100644 src/main/python/CON/CON_ux_grid_agg/hive_merge_files_util.py
 create mode 100644 src/main/python/CON/CON_ux_grid_agg/hql/agg_trc_partner_content_internal.hql
 create mode 100644 src/main/python/CON/CON_ux_grid_agg/hql/agg_trc_partner_external_agg_daily.hql
 create mode 100644 src/main/python/CON/CON_ux_grid_agg/hql/agg_trc_partner_live_external_daily.hql
 create mode 100644 src/main/python/CON/CON_ux_grid_agg/hql/agg_trc_partner_vod_external_daily.hql
 create mode 100644 src/main/python/CON/sr_cap/hql/add_beehive_stg_partition.hql
 create mode 100644 src/main/python/CON/sr_cap/hql/dim_content_library_status.hql
 create mode 100644 src/main/python/CON/sr_cap/hql/dim_content_library_status_history.hql
 create mode 100644 src/main/python/RAMS/agg/ads_pixel_event_metrics_daily/BUILD
 create mode 100644 src/main/python/RAMS/agg/ads_pixel_event_metrics_daily/agg_dag_pixel_event.py
 create mode 100644 src/main/python/RAMS/agg/ads_pixel_event_metrics_daily/hql/ads_events_metrics_daily.hql
 create mode 100644 src/main/python/RAMS/agg/ads_pixel_event_metrics_daily/hql/get_granular_video_ad_events.hql
 create mode 100644 src/main/python/RAMS/agg/ads_pixel_event_metrics_daily/hql/load_partition_ads_events_metrics_daily.hql
 create mode 100644 src/main/python/RPAY/RPAY_import_from_s3/dim_account_purchase_hist_merged.hql
 create mode 100644 src/main/python/RPAY/RPAY_import_from_s3/fact_billing_transaction_invoice_merged.hql
 create mode 100644 src/main/python/RPAY/RPAY_je_aggregate_file_generation/BUILD
 create mode 100644 src/main/python/RPAY/RPAY_je_aggregate_file_generation/__init__.py
 create mode 100644 src/main/python/RPAY/RPAY_je_aggregate_file_generation/agg_journal_entry_deferred_revenue.hql
 create mode 100644 src/main/python/RPAY/RPAY_je_aggregate_file_generation/agg_journal_entry_pii.hql
 create mode 100644 src/main/python/RPAY/RPAY_je_aggregate_file_generation/agg_trc_deferred_revenue.hql
 create mode 100644 src/main/python/RPAY/RPAY_je_aggregate_file_generation/fact_trc_deferred_revenue.hql
 create mode 100644 src/main/python/RPAY/RPAY_je_aggregate_file_generation/fact_trc_deferred_revenue_stg.hql
 create mode 100644 src/main/python/RPAY/RPAY_je_aggregate_file_generation/rpay_je_aggregate_file_generation_dag.py
 create mode 100644 src/main/python/RPAY/RPAY_je_aggregate_file_generation/rpay_je_file_generation_util.py
 delete mode 100644 src/main/python/agg/agg_daily/agg_device_streaming_hourly.hql
 create mode 100644 src/main/python/agg/backfills/DE-640/README.md
 create mode 100644 src/main/python/agg/backfills/DE-640/backfill_dea_agg_channel_streaming_metrics_daily.hql
 create mode 100644 src/main/python/agg/backfills/DE-640/backfill_roku_agg_device_streaming_hourly.hql
 create mode 100644 src/main/python/agg/backfills/DE-640/backfill_roku_agg_device_streaming_metrics_daily.hql
 create mode 100644 src/main/python/agg/backfills/DE-640/backup_roku_agg_device_streaming_hourly.hql
 create mode 100644 src/main/python/agg/backfills/DE-640/script.sh
 create mode 100644 src/main/python/amoeba/amoeba_hourly/fact_amoeba_allocation_events_v2_virtual_yesterday.hql
 create mode 100644 src/main/python/attribution/san_events/BUILD
 create mode 100644 src/main/python/attribution/san_events/README.md
 create mode 100644 src/main/python/attribution/san_events/__init__.py
 create mode 100644 src/main/python/attribution/san_events/hql/agg_san_events_daily.hql
 create mode 100644 src/main/python/attribution/san_events/san_events_dag.py
 create mode 100644 src/main/python/attribution/san_events/san_tasks.py
 create mode 100644 src/main/python/bazel_py3_example/dummy.hql
 create mode 100644 src/main/python/bazel_py3_example/dummy_utils.py
 create mode 100644 src/main/python/cms/__init__.py
 create mode 100644 src/main/python/cms/client/BUILD
 create mode 100644 src/main/python/cms/client/__init__.py
 create mode 100644 src/main/python/cms/client/cms_client.py
 create mode 100644 src/main/python/cms/client/test_cms_client.py
 create mode 100644 src/main/python/custom_utils/airflow/dynamodb_to_s3.py
 create mode 100644 src/main/python/daro/oneview_campaign_automation/BUILD
 create mode 100644 src/main/python/daro/oneview_campaign_automation/__init__.py
 create mode 100644 src/main/python/daro/oneview_campaign_automation/daro_oneview_calculations.py
 create mode 100644 src/main/python/daro/oneview_campaign_automation/daro_oneview_campaign_automation.py
 create mode 100644 src/main/python/daro/oneview_campaign_automation/daro_oneview_cms_update.py
 create mode 100644 src/main/python/daro/oneview_campaign_automation/daro_oneview_config.py
 create mode 100644 src/main/python/daro/oneview_campaign_automation/daro_oneview_data_fetch.py
 create mode 100644 src/main/python/daro/oneview_campaign_automation/daro_oneview_pacing_opt.py
 create mode 100644 src/main/python/daro/oneview_campaign_automation/daro_oneview_utils.py
 create mode 100644 src/main/python/daro/oneview_campaign_automation/hql/register_date_partition.hql
 create mode 100644 src/main/python/dmp/data_collab/maintenance_dag.py
 create mode 100644 src/main/python/dmp/data_collab/rotate_dce_secret_operator.py
 create mode 100644 src/main/python/dmp/data_collab/rotate_partner_salt_operator.py
 create mode 100644 src/main/python/dmp/data_collab/sql/snowflake_ddl_public_EXPIRED_IDS.sql
 create mode 100644 src/main/python/dmp/data_collab/sql/snowflake_ddl_public_PII_SALT.sql
 create mode 100644 src/main/python/dmp/data_collab/sql/snowflake_delete_expired_from_ACCOUNTS.sql
 create mode 100644 src/main/python/dmp/data_collab/sql/snowflake_delete_expired_from_ONE_VIEW_IMPRESSIONS.sql
 create mode 100644 src/main/python/dmp/data_collab/sql/snowflake_load_EXPIRED_IDS.sql
 create mode 100644 src/main/python/dmp/data_collab/sql/spark_dim_adv_inet.hql
 create mode 100644 src/main/python/dmp/data_collab/sql/spark_rida_graph.hql
 create mode 100644 src/main/python/dsp/graph/blend_graph/BUILD
 create mode 100644 src/main/python/dsp/graph/blend_graph/__init__.py
 create mode 100644 src/main/python/dsp/graph/blend_graph/blend_graph_conf.py
 create mode 100644 src/main/python/dsp/graph/blend_graph/blend_graph_dag.py
 create mode 100644 src/main/python/dsp/graph/blend_graph/hql/blender-graph-metrics.hql
 create mode 100644 src/main/python/dsp/graph/blend_graph/hql/control-graph-metrics.hql
 create mode 100644 src/main/python/dsp/graph/blend_graph/hql/treatment-graph-metrics.hql
 create mode 100644 src/main/python/dsp/graph/graph_blender/BUILD
 create mode 100644 src/main/python/dsp/graph/graph_blender/__init__.py
 create mode 100644 src/main/python/dsp/graph/graph_blender/graph-blender-bdcs.json
 create mode 100644 src/main/python/dsp/graph/graph_blender/graph_blender_task.py
 create mode 100644 src/main/python/dsp/graph/graph_file_formatting/BUILD
 create mode 100644 src/main/python/dsp/graph/graph_file_formatting/__init__.py
 create mode 100644 src/main/python/dsp/graph/graph_file_formatting/graph_file_formatting_task.py
 delete mode 100644 src/main/python/dsp/graph/oneview_household_graph/add_dx_household_partitions_config.py
 create mode 100644 src/main/python/dsp/graph/opt_out_exporter/BUILD
 create mode 100644 src/main/python/dsp/graph/opt_out_exporter/__init__.py
 create mode 100644 src/main/python/dsp/graph/opt_out_exporter/opt_out_exporter_tasks.py
 create mode 100644 src/main/python/fact/fact_google_alexa_linked_accounts/BUILD
 create mode 100644 src/main/python/fact/fact_google_alexa_linked_accounts/__init__.py
 create mode 100644 src/main/python/fact/fact_google_alexa_linked_accounts/api.py
 create mode 100644 src/main/python/fact/fact_google_alexa_linked_accounts/fact_google_alexa_linked_accounts_dag.py
 create mode 100644 src/main/python/fact/fact_google_alexa_linked_accounts/fact_join_linked_account_device_detail.hql
 rename src/main/python/mlp_v3/mlpy/{dev => prod}/RUM_UID.txt (100%)
 rename src/main/python/mlp_v3/mlpy/{dev => prod}/repo/rum_real.schema (100%)
 rename src/main/python/mlp_v3/mlpy/{dev => prod}/rum/features_ad_rum.list (100%)
 rename src/main/python/mlp_v3/mlpy/{dev => prod}/rum/features_interests.list (100%)
 create mode 100644 src/main/python/mlp_v3/mlpy/prod/rum/model_install.json
 create mode 100644 src/main/python/mlp_v3/mlpy/prod/rum/model_template.json
 rename src/main/python/mlp_v3/mlpy/{dev => prod}/rum/virtual_ad_rum.config (100%)
 rename src/main/python/mlp_v3/mlpy/{dev => prod}/rum/virtual_rum.config (100%)
 create mode 100644 src/main/python/mlp_v3/mlpy/prod/rum_master.json
 create mode 100644 src/main/python/mlp_v3/mlpy/prod/rum_tiny.json
 delete mode 100644 src/main/python/mo/mo_calculations.py
 create mode 100644 src/main/python/pmm/pmm_hourly/agg_device_build_metrics_daily_old.hql
 create mode 100644 src/main/python/pmm/pmm_hourly/pmm_ai_model.conf
 create mode 100644 src/main/python/pmm/pmm_hourly/pmm_ai_model.py
 create mode 100644 src/main/python/pmm/pmm_hourly/pmm_feature_generation.hql
 create mode 100644 src/main/python/pmm/rpay_pmm/BUILD
 create mode 100644 src/main/python/pmm/rpay_pmm/__init__.py
 create mode 100644 src/main/python/pmm/rpay_pmm/agg_rpay_pmm_metrics_daily.hql
 create mode 100644 src/main/python/pmm/rpay_pmm/rpay_pmm.py
 create mode 100644 src/main/python/pmm/rpay_pmm/rpay_pmm_ai_model.conf
 create mode 100644 src/main/python/pmm/rpay_pmm/rpay_pmm_ai_model.py
 create mode 100644 src/main/python/po/campaign_automation/DisplayAdsPacingUpdater.py
 delete mode 100644 src/main/python/po/campaign_automation/LineItemsManagerUACpm.py
 create mode 100644 src/main/python/sim_avails/avails_data_diff.py
 create mode 100644 src/main/python/solutions/BUILD
 create mode 100644 src/main/python/solutions/__init__.py
 create mode 100644 src/main/python/solutions/hulu_rejection_data_dag.py
 create mode 100644 src/main/python/solutions/load_hulu_rejection_data.hql
 create mode 100644 src/main/scala/com/roku/adcloud/spark/avails2/loaders/ChannelCategoriesAndIsKidsDatasetProvider.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/avails2/loaders/TrcGenreProvider.scala
 delete mode 100644 src/main/scala/com/roku/adcloud/spark/insights/acr/AggAdiAcrApp.scala
 delete mode 100644 src/main/scala/com/roku/adcloud/spark/insights/acr/AggAdiAcrEducationApp.scala
 delete mode 100644 src/main/scala/com/roku/adcloud/spark/insights/acr/AggAdiAcrIncomeApp.scala
 delete mode 100644 src/main/scala/com/roku/adcloud/spark/insights/acr/loaders/AdiFactAcrDataLoader.scala
 delete mode 100644 src/main/scala/com/roku/adcloud/spark/insights/acr/loaders/AdiFactAcrEducationDataLoader.scala
 delete mode 100644 src/main/scala/com/roku/adcloud/spark/insights/acr/loaders/AdiFactAcrIncomeDataLoader.scala
 delete mode 100644 src/main/scala/com/roku/adcloud/spark/insights/acr/objects/AdiAcrEducationPreAggDimension.scala
 delete mode 100644 src/main/scala/com/roku/adcloud/spark/insights/acr/objects/AdiAcrEducationPreAggRecord.scala
 delete mode 100644 src/main/scala/com/roku/adcloud/spark/insights/acr/objects/AdiAcrIncomePreAggDimension.scala
 delete mode 100644 src/main/scala/com/roku/adcloud/spark/insights/acr/objects/AdiAcrIncomePreAggRecord.scala
 delete mode 100644 src/main/scala/com/roku/adcloud/spark/insights/acr/objects/AdiAcrPreAggDimension.scala
 delete mode 100644 src/main/scala/com/roku/adcloud/spark/insights/acr/objects/AdiAcrPreAggRecord.scala
 delete mode 100644 src/main/scala/com/roku/adcloud/spark/insights/acr/objects/AggAdiAcrEducationRecord.scala
 delete mode 100644 src/main/scala/com/roku/adcloud/spark/insights/acr/objects/AggAdiAcrIncomeRecord.scala
 delete mode 100644 src/main/scala/com/roku/adcloud/spark/insights/acr/objects/AggAdiAcrRecord.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/insights/campaign/loaders/AdiDimSfMetadataLoader.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/insights/data_toolkit/DimAdiAcrPanelApp.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/insights/data_toolkit/TargetingSpecificDemoPopulatorApp.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/insights/data_toolkit/loaders/DimAccountAttributesLoader.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/insights/data_toolkit/loaders/DimRokuPiiLoader.scala
 delete mode 100644 src/main/scala/com/roku/adcloud/spark/insights/dspcordcutter/dataprep/DailyFeaturesFromDSPCTVTrans.scala.bkup
 create mode 100644 src/main/scala/com/roku/adcloud/spark/insights/dspcordcutter/dataprep/Discretizer.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/insights/ump/AggAdiUmpBidWinDensityApp.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/insights/ump/FactAdiUmpBidsApp.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/insights/ump/loaders/DspBidTransactionsDataLoader.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/insights/ump/loaders/DxCurrencyRatesDataLoader.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/insights/ump/loaders/FactAdiUmpBidsAndImpressionsDataLoader.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/insights/ump/objects/AggAdiUmpBidWinDensityRecord.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/insights/ump/objects/FactAdiUmpBidRecord.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/insights/viewability/AggAdiDVViewabilityApp.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/insights/viewability/AggAdiIASViewabilityApp.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/insights/viewability/AggAdiMOATViewabilityApp.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/insights/viewability/BUILD
 create mode 100644 src/main/scala/com/roku/adcloud/spark/insights/viewability/ViewabilityHelper.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/insights/viewability/objects/FactViewabilityRecord.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/unifiedavails/config/VideoUnifiedAttributeConfigurations.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/unifiedavails/features/ChannelGenreFeatures.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/unifiedavails/features/IsKidsFeatures.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/unifiedavails/features/TrcContentTypeFeatures.scala
 create mode 100644 src/main/scala/com/roku/adcloud/spark/unifiedavails/features/TrcGenreFeatures.scala
 create mode 100644 src/main/scala/com/roku/common/deequ/core/LocationDataLoader.scala
 create mode 100644 src/main/scala/com/roku/common/deequ/validators/DataCollabValidator.scala
 create mode 100644 src/main/scala/com/roku/common/deequ/validators/GenericValueOccurrenceValidator.scala
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/device/resources/monitor_streaming_lag.py
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/device/resources/submit_utils.sh
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/device_log_validator/resources/monitor_streaming_lag.py
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/device_log_validator/resources/submit_utils.sh
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/device_ux/resources/monitor_streaming_lag.py
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/device_ux/resources/submit_utils.sh
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/lego/resources/monitor_streaming_lag.py
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/lego/resources/submit_utils.sh
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/lego_commons/resources/monitor_streaming_lag.py
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/lego_commons/resources/submit_utils.sh
 create mode 100644 src/main/scala/com/roku/dea/spark/streaming/lego_gc/resources/conf/lego_gc_streaming_prod_v2.conf
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/lego_gc/resources/monitor_streaming_lag.py
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/lego_gc/resources/submit_lego_gc_v2.sh
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/lego_gc/resources/submit_utils.sh
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/lego_generic/resources/monitor_streaming_lag.py
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/lego_generic/resources/submit_utils.sh
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/metrics/Utils/resources/monitor_streaming_lag.py
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/metrics/Utils/resources/submit_utils.sh
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/metrics/raf/resources/monitor_streaming_lag.py
 create mode 100644 src/main/scala/com/roku/dea/spark/streaming/metrics/raf/resources/streaming.conf
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/metrics/raf/resources/submit_utils.sh
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/metrics/ramsv2/resources/monitor_streaming_lag.py
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/metrics/ramsv2/resources/submit_utils.sh
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/po/conversions/resources/monitor_streaming_lag.py
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/po/conversions/resources/submit_utils.sh
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/roku_pixel/resources/monitor_streaming_lag.py
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/roku_pixel/resources/submit_utils.sh
 create mode 100755 src/main/scala/com/roku/dea/spark/streaming/tclogs/resources/submit_utils.sh
 delete mode 100644 src/main/scala/com/roku/delta/logs/BUILD
 delete mode 100644 src/main/scala/com/roku/delta/logs/SummarizePredictions.scala
 create mode 100644 src/main/scala/com/roku/dmp/data_collab/DataCollabMaintenance.scala
 create mode 100644 src/main/scala/com/roku/dmp/data_collab/Dataset.scala
 create mode 100644 src/main/scala/com/roku/dmp/data_collab/IdType.scala
 create mode 100644 src/main/scala/com/roku/dmp/data_collab/PiiHash.scala
 create mode 100644 src/main/scala/com/roku/dmp/models/ddl/patches/2021/09/Add-New-DSP-OneView-Category-DMP-8173.sql
 create mode 100644 src/main/scala/com/roku/mlp/utils/resources/MlpEventsSchema.json
 create mode 100644 src/main/scala/com/roku/mlp/utils/resources/daro/daro_usermodel_request_template.json
 create mode 100644 src/main/scala/com/roku/mlp/utils/resources/daro/daro_usermodel_request_template_global_no_gd.json
 create mode 100755 src/main/scala/com/roku/mlp/utils/resources/daro/pushRequest.sh
 create mode 100755 src/main/scala/com/roku/mlp/utils/resources/daro/submit_user_model.sh
 create mode 100644 src/main/scala/com/roku/mlp/utils/resources/log4j.properties
 create mode 100644 src/main/scala/com/roku/mlp/utils/resources/mlp.conf
 create mode 100644 src/main/scala/com/roku/mlp/v2/features/resources/MlpEventsSchema.json
 create mode 100644 src/main/scala/com/roku/mlp/v2/features/resources/daro/daro_usermodel_request_template.json
 create mode 100644 src/main/scala/com/roku/mlp/v2/features/resources/daro/daro_usermodel_request_template_global_no_gd.json
 create mode 100755 src/main/scala/com/roku/mlp/v2/features/resources/daro/pushRequest.sh
 create mode 100755 src/main/scala/com/roku/mlp/v2/features/resources/daro/submit_user_model.sh
 create mode 100644 src/main/scala/com/roku/mlp/v2/features/resources/log4j.properties
 create mode 100644 src/main/scala/com/roku/mlp/v2/features/resources/mlp.conf
 create mode 100644 src/main/scala/com/roku/mlp/v2/resources/MlpEventsSchema.json
 create mode 100644 src/main/scala/com/roku/mlp/v2/resources/daro/daro_usermodel_request_template.json
 create mode 100644 src/main/scala/com/roku/mlp/v2/resources/daro/daro_usermodel_request_template_global_no_gd.json
 create mode 100755 src/main/scala/com/roku/mlp/v2/resources/daro/pushRequest.sh
 create mode 100755 src/main/scala/com/roku/mlp/v2/resources/daro/submit_user_model.sh
 create mode 100644 src/main/scala/com/roku/mlp/v2/resources/log4j.properties
 create mode 100644 src/main/scala/com/roku/mlp/v2/resources/mlp.conf
 create mode 100644 src/main/scala/com/roku/mlp/v3/resources/MlpEventsSchema.json
 create mode 100644 src/main/scala/com/roku/mlp/v3/resources/daro/daro_usermodel_request_template.json
 create mode 100644 src/main/scala/com/roku/mlp/v3/resources/daro/daro_usermodel_request_template_global_no_gd.json
 create mode 100755 src/main/scala/com/roku/mlp/v3/resources/daro/pushRequest.sh
 create mode 100755 src/main/scala/com/roku/mlp/v3/resources/daro/submit_user_model.sh
 create mode 100644 src/main/scala/com/roku/mlp/v3/resources/log4j.properties
 create mode 100644 src/main/scala/com/roku/mlp/v3/resources/mlp.conf
 create mode 100644 src/main/scala/com/roku/rome/models/ddl/patches/ROME-1.15.1.sql
 create mode 100644 src/main/scala/com/roku/rome/models/ddl/patches/ROME-1.16.sql
 delete mode 100644 src/main/scala/com/roku/rome/uibackend/core/sfdc_boomi/OneLoginAccessToken.scala
 delete mode 100644 src/main/scripts/agg_device_streaming_hourly.sql
 create mode 100644 src/main/scripts/shell-scripts/PROGDE-1098_avro.sh
 create mode 100644 src/test/java/com/roku/ads/rams/eventbackup/BUILD
 create mode 100644 src/test/java/com/roku/ads/rams/eventbackup/EventBackupTest.java
 create mode 100644 src/test/java/com/roku/ads/rams/module/ads/scoring/BucketTest.java
 create mode 100644 src/test/java/com/roku/ads/test/integration/admedia/graphqlqueries/dealqueries/findTags.graphql
 create mode 100644 src/test/java/com/roku/ads/test/integration/admedia/graphqlqueries/inventoryPackageQueries/getInventoryPackages.graphql
 rename src/test/java/com/roku/ads/test/integration/admedia/rams/testdata/{dev-mgupta => dev-mgupta1}/application.properties (95%)
 rename src/test/java/com/roku/ads/test/integration/admedia/rams/testdata/{dev-mgupta => dev-mgupta1}/channelOnlyOrTagOnlyRuleSsoSecapdsp.json (100%)
 rename src/test/java/com/roku/ads/test/integration/admedia/rams/testdata/{dev-mgupta => dev-mgupta1}/ip_ridas.csv (100%)
 rename src/test/java/com/roku/ads/test/integration/admedia/rams/testdata/{dev-mgupta => dev-mgupta1}/ip_ridas_10k.csv (100%)
Professor T (British remake, we didn't see the original)
Das boot (based on the great film with the same name — если не видели, то обязательно посмотрите)

Mare of Easttown,

Следствие по телу Детектив США, 2011, 3 сезона
Доктор Меган Хант была ведущим нейрохирургом, пока из-за автомобильной аварии ее карьера не оборвалась. И теперь, раз уж живым помочь она больше не в силах, она стала судмедэкспертом

Вечность Драма США, 2016, 1 сезон
У доктора Генри Моргана, звездного судебно-медицинского эксперта Нью-Йорка, есть секрет. Он изучает мертвых не только, чтобы раскрывать уголовные дела. Он это делает, чтобы раскрыть...

https://top-reyting.ru/kino/30-luchshich-novich-detektivnich-serialov-2021-goda.html

"Большая секунда"
Вызов (Россия) — все 4 сезона 2006 — 2009
:set nonu
Professor T (British remake, we didn't see the original)
Das boot (based on the great film with the same name — если не видели, то обязательно посмотрите)

Mare of Easttown,

Следствие по телу Детектив США, 2011, 3 сезона
Доктор Меган Хант была ведущим нейрохирургом, пока из-за автомобильной аварии ее карьера не оборвалась. И теперь, раз уж живым помочь она больше не в силах, она стала судмедэкспертом

Вечность Драма США, 2016, 1 сезон
У доктора Генри Моргана, звездного судебно-медицинского эксперта Нью-Йорка, есть секрет. Он изучает мертвых не только, чтобы раскрывать уголовные дела. Он это делает, чтобы раскрыть...

https://top-reyting.ru/kino/30-luchshich-novich-detektivnich-serialov-2021-goda.html

"Большая секунда"
Вызов (Россия) — все 4 сезона 2006 — 2009
"Смерть в раю" Он детектив в агатокристиевском стиле
Professor T (British remake, we didn't see the original)
Das boot (based on the great film with the same name — если не видели, то обязательно посмотрите)

Mare of Easttown,

Следствие по телу Детектив США, 2011, 3 сезона
Доктор Меган Хант была ведущим нейрохирургом, пока из-за автомобильной аварии ее карьера не оборвалась. И теперь, раз уж живым помочь она больше не в силах, она стала судмедэкспертом

Вечность Драма США, 2016, 1 сезон
У доктора Генри Моргана, звездного судебно-медицинского эксперта Нью-Йорка, есть секрет. Он изучает мертвых не только, чтобы раскрывать уголовные дела. Он это делает, чтобы раскрыть...

https://top-reyting.ru/kino/30-luchshich-novich-detektivnich-serialov-2021-goda.html

"Большая секунда"
Вызов (Россия) — все 4 сезона 2006 — 2009
"Смерть в раю" Он детектив в агатокристиевском стиле
«След»
Обычная женщина Россия)
психологический детектив "Откровения", российский, 22 серии, 1 сезон. Серии короткие, около получаса.
C.S.I. Место преступления и C.S.I. Место преступления Нью-Йорк
Лютер
Касл
Дефективный детектив / Детектив Монк
"Зло"
Хилл стрит блюз.
Мини сериал, последний фильм Соломина, "Пан или пропал" по роману Хмелевской "Всё красное"
Блудный сын
Чёрный список
Кандис Ренуар
Элементарно
Метод Крекера
Закон и порядок
Мистериум, правда, он не длинный и скорее серия из четырёх фильмов.
"Начало",
"Послание в бутылке",
"Охота на фазанов",
"Журнал 69"
Белый воротичок
Гаваи 5О
Испанские сериалы неплохие: "Изабелла-королева Кастилии" и "Карл 5-король и император"
Psych
Leverage
Murdoch Mysteries
Monk
Colombo
X-Files ;)
Supernatural;) ;)
Lucifer ;) ;) ;)
Buffy The Vampire Slayer
Burn Notice
Bones
24
Brooklyn 99!
```



<https://soap.d3.ru/post-vopros-kollektivnomu-razumu-gde-smotret-filmy-onlain-bez-registratsii-i-sms-1867574/>

## Movies

https://soap.d3.ru/porekomenduite-pozhaluista-detektivnyi-serial-1990105/?sorting=rating

https://obsudim-serialy.livejournal.com/

https://irin-v.livejournal.com/tag/%D0%9A%D0%B8%D0%BD%D0%BE%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%D1%8B

https://zbzkino.d3.ru/

https://ahiin.livejournal.com/293907.html

https://ahiin.livejournal.com/294595.html

https://ahiin.livejournal.com/302541.html

## Music

<https://www.youtube.com/watch?v=_TeyBKMITqs> . Egorov

<https://youtu.be/8DRRyAh9OnQ> Blues

<https://www.youtube.com/watch?v=g5wlBqWSgxk> Vysotsky

## Soaps
<https://soap.d3.ru/kakie-otnositelno-sovremennye-serialy-mozhno-tak-ili-inache-schitat-kultovymi-1663894/>

  Bosch | Босх (USA, 2014–...) <https://www.imdb.com/title/tt3502248/>

Trial and Error | Методом проб и ошибок (USA, 2017–..., 2S) <https://www.imdb.com/title/tt5511512/>

The Guest Book | Гостевая книга (USA, 2017–...) <https://www.imdb.com/title/tt5990096/>

<https://www.imdb.com/title/tt7366338/> Chernobyl

<https://www.imdb.com/title/tt8064302/> Dead to me

True Detective (USA, 2014–2019)

Here and Now | Здесь и сейчас (USA, 2018, 1S)

<https://www.imdb.com/title/tt7134194/> The Truth About the Harry Quebert Affair | Правда о деле Гарри Квеберта (USA, 2018)

<https://www.imdb.com/title/tt7587890> Новичок / Rookie

Bodyguard | Телохранитель (UK, 2018) <https://www.imdb.com/title/tt7493974/>

<https://www.imdb.com/title/tt2699110/> The Affair

## Kino

<https://filmzonyoutube.d3.ru/> . youtube

<https://youtube.d3.ru/>

https://www.youtube.com/channel/UC608azSGWiQYi5ImYgOZgdg Epic Media
<https://green-fr.livejournal.com/826791.html>

<https://www.youtube.com/watch?v=QJz1GsMs0Wk> . Подкидыш

<https://www.youtube.com/watch?v=KZRoMKFDj58> Пепел

<https://www.youtube.com/watch?v=8e5DHqIrgrQ> ГУРЗУФ - Детектив

<https://www.youtube.com/results?search_query=%23epicmediachannel> . russian movies

«Оттепель» Валерия Тодоровского 
«Метод» Юрия Быкова (Habensky and Paulina Andreeva).

Домашний арест (сериал) <https://www.kinopoisk.ru/film/1044487/>

Упражнения в прекрасном
<https://www.youtube.com/watch?v=P-Y86m02n10>    

Со мною вот что происходит
<https://www.youtube.com/watch?v=OhS7pU_ZgvU>    or 
<https://www.youtube.com/watch?v=-wAS8sp7Z4A>

Год культуры (сериал) <https://www.kinopoisk.ru/film/1206901/>


<https://d3.ru/tag/%D0%BA%D0%B8%D0%BD%D0%BE/>

<https://soamo.livejournal.com/4862662.html#comments>

<https://soap.d3.ru/kto-chto-peresmotrel-v-ukhodiashchem-godu-1713813/>

<https://soap.d3.ru/ianvar-2019-1713588/?sorting=rating>

<https://reviews.d3.ru/>

<https://kino.d3.ru/>

<https://cinema.d3.ru/>

<https://soap.d3.ru/>

<https://posmotrel.d3.ru/>

<https://recommend.d3.ru/>

<https://kinokakto.d3.ru/>

<https://movies.d3.ru/>

```
100 ЛУЧШИХ ФИЛЬМОВ  
1 Ирония судьбы, или С легким паром! 1975 СССР Эльдар Рязанов
2 Сталкер 1979 СССР Андрей Тарковский
3 Танцующая в темноте Dancer in the Dark 2000 Дания Ларс фон Триер
4 Малхолланд Драйв Mulholland Dr. 2001 Франция, США Дэвид Линч
5 Декалог Dekalog 1988 Польша, Германия (ФРГ) Кшиштоф Кесьлёвский
6 Рождённые в СССР 1991 Великобритания Сергей Мирошниченко
7 Шапито-шоу 2011 Россия Сергей Лобан
8 Криминальное чтиво Pulp Fiction 1994 США Квентин Тарантино
9 Потец 1992 Россия Александр Федулов
10 Кин-дза-дза! 1986 СССР Георгий Данелия
11 Моя любовь 2006 Россия, Япония Александр Петров
12 Сто дней после детства 1975 СССР Сергей Соловьев
13 Заводной апельсин A Clockwork Orange 1971 Великобритания, США Стэнли Кубрик
14 Исчезновение Spoorloos 1988 Нидерланды, Франция, Германия (ФРГ) Джордж Слёйзер
15 Время цыган Dom za vesanje 1988 Югославия, Великобритания, Италия Эмир Кустурица
16 Гараж 1979 СССР Эльдар Рязанов
17 За двумя зайцами 1961 СССР Виктор Иванов
18 Бриллиантовая рука 1968 СССР Леонид Гайдай
19 Убить дракона 1988 Германия (ФРГ), СССР Марк Захаров
20 Про Красную Шапочку 1977 СССР Леонид Нечаев
21 Андеграунд Underground 1995 Сербия Эмир Кустурица
22 Ищите женщину 1982 СССР Алла Сурикова
23 Крокодил Гена 1969 СССР Роман Качанов
24 В моей смерти прошу винить Клаву К. 1979 СССР Николай Лебедев, Эрнест Ясан
25 12 стульев 1976 СССР Марк Захаров
26 Пятая печать Az otodik pecset 1976 Венгрия Золтан Фабри
27 Унесённые призраками Sen to Chihiro no kamikakushi 2001 Япония Хаяо Миядзаки
28 Догвилль Dogville 2003 Нидерланды, Дания, Великобритания Ларс фон Триер
29 Король Лев The Lion King 1994 США Роджер Аллерс, Роб Минкофф
30 ...А зори здесь тихие 1972 СССР Станислав Ростоцкий
31 Семь самураев Shichinin no samurai 1954 Япония Акира Куросава
32 Возвращение 2003 Россия Андрей Звягинцев
33 Отец и дочь Father and Daughter 2000 Великобритания, Бельгия, Нидерланды Майкл Дадок де Уит
34 Услышьте мой крик Uslyszcie moj krzyk 1991 Польша Мацей Дрыгас
35 Жить 2011 Россия Василий Сигарев
36 Ух ты, говорящая рыба! 1983 СССР Роберт Саакянц
37 Он вам не Димон 2017 Россия
38 Скромное обаяние буржуазии Le charme discret de la bourgeoisie 1972 Франция Луис Бунюэль
39 Моя прекрасная леди My Fair Lady 1964 США Джордж Кьюкор
40 Жил-был пёс 1982 СССР Эдуард Назаров
41 Могила светлячков Hotaru no haka 1988 Япония Исао Такахата
42 Приключения Буратино 1975 СССР Леонид Нечаев
43 Служебный роман 1977 СССР Эльдар Рязанов
44 Воспоминания в тумане Kalpurush 2005 Индия Буддхадев Дасгупта
45 Бесконечный дождь Mungaru Male 2006 Индия Yograj Bhat
46 Допрос Visaaranai 2015 Индия Ветримааран
47 Закон Жизни 1940 СССР Борис Иванов
48 Отель «Гранд Будапешт» The Grand Budapest Hotel 2014 США, Германия Уэс Андерсон
49 Собачье сердце 1988 СССР Владимир Бортко
50 Омерзительная восьмерка The Hateful Eight 2015 США Квентин Тарантино
51 Непохищенная невеста Dilwale Dulhania Le Jayenge 1995 Индия Адитья Чопра
52 Золотой теленок 1968 СССР Михаил Швейцер
53 Видимость Drishyam 2015 Индия Нишикант Камат
54 Хороший, плохой, злой Il buono, il brutto, il cattivo 1966 Италия, Испания, Германия (ФРГ) Серджио Леоне
55 Доктор Стрейнджлав, или Как я научился не волноваться и полюбил атомную бомбу Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb 1963 США, Великобритания Стэнли Кубрик
56 Вальс с Баширом Vals Im Bashir 2008 Израиль, Франция, Германия Ари Фольман
57 Окраина 1998 Россия Петр Луцик
58 Покровские ворота 1982 СССР Михаил Козаков
59 Визонтеле Vizontele 2001 Турция Йылмаз Эрдоган, Омер Фарук Сорак
60 Шум в сердце Le souffle au coeur 1971 Франция, Италия, Германия (ФРГ) Луи Маль
61 Добро пожаловать, или Посторонним вход воспрещен 1964 СССР Элем Климов
62 Мимино 1977 СССР Георгий Данелия
63 Пластилиновая ворона 1981 СССР Александр Татарский
64 Операция «Ы» и другие приключения Шурика 1965 СССР Леонид Гайдай
65 Приключения капитана Врунгеля 1976 – 1979 СССР Давид Черкасский
66 Ну, погоди! 1969– 2006 СССР Вячеслав Котёночкин, Юрий Бутырин, Владимир Тарасов
67 Машенька 1942 СССР Юлий Райзман
68 Самая грустная музыка в мире The Saddest Music in the World 2003 Канада Гай Мэддин
69 Слово Ordet 1955 Дания Карл Теодор Дрейер
70 Это безумный, безумный, безумный, безумный мир It's a Mad Mad Mad Mad World 1963 США Стэнли Крамер
71 Тони Эрдманн Toni Erdmann 2016 Германия, Австрия Марен Аде
72 Фантазии Фарятьева 1979 СССР Илья Авербах
73 Сын Саула Saul fia 2015 Венгрия Ласло Немеш
74 Покаяние 1984 СССР Тенгиз Абуладзе
75 Однажды человек купил дом Huset pa Kampen 1998 Норвегия Петр Сапегин
76 2001 год: Космическая одиссея 2001: A Space Odyssey 1968 Великобритания, США Стэнли Кубрик
77 История Элли Darbareye Elly 2009 Иран, Франция Асгар Фархади
78 Ученик 2016 Россия Кирилл Серебренников
79 Нимфоманка: Часть 1 Nymphomaniac: Vol. I 2013 Дания, Германия, Франция Ларс фон Триер
80 Падал прошлогодний снег 1983 СССР Александр Татарский
81 Пролетая над гнездом кукушки One Flew Over the Cuckoo's Nest 1975 США Милош Форман
82 Дикая собака динго 1962 СССР Юлий Карасик
83 Сжигая мосты Quemar las naves 2007 Мексика Франциско Франко
84 Цвет рая Rang-e khoda 1999 Иран Маджид Маджиди
85 Головоломка Inside Out 2015 США Пит Доктер, Роналдо Дель Кармен
86 Неожиданный день Anukokunda Oka Roju 2005 Индия Чандра Шекхар Йелети
87 Отель 'Устад' Ustad Hotel 2012 Индия Анвар Рашид
88 Остров сокровищ 1988 СССР Давид Черкасский
89 Вам и не снилось... 1980 СССР Илья Фрэз
90 Облако-рай 1990 СССР Николай Досталь
91 Этот смутный объект желания Cet obscur objet du desir 1977 Франция, Испания Луис Бунюэль
92 Охота Jagten 2012 Дания, Швеция Томас Винтерберг
93 Орфей Orphee 1950 Франция Жан Кокто
94 Жестокий романс 1984 СССР Эльдар Рязанов
95 Не так, как в первый раз! Aldrig som forsta gangen! 2006 Швеция Йонас Оделл
96 Изгнание 2007 Россия Андрей Звягинцев
97 Дом. История путешествия Home 2009 Франция Янн Артюс-Бертран
98 Курьер 1986 СССР Карен Шахназаров
99 Сладкая жизнь La dolce vita 1960 Италия Федерико Феллини
100 Джентльмены удачи 1971 СССР Александр Серый
```
