library(jsonlite)
library(plyr)
# data download from http://oncokb.org/#/dataAccess
# didnt need to use this because it works better in bash using in2csv

# get data and convert to dataframe
onco_genes <- jsonlite::fromJSON("http://oncokb.org/api/v1/genes")
onco_evidences_lookup  <- jsonlite::fromJSON("http://oncokb.org/api/v1/evidences/lookup?source=oncotree")
onco_variants  <- jsonlite::fromJSON("http://oncokb.org/api/v1/variants")
onco_levels  <- jsonlite::fromJSON("http://oncokb.org/api/v1/levels")
onco_all_actionable_variants  <- jsonlite::fromJSON("http://oncokb.org/api/v1/utils/allActionableVariants")
onco_all_annotated_variants  <- jsonlite::fromJSON("http://oncokb.org/api/v1/utils/allAnnotatedVariants")

#write to csv
write.csv(onco_genes, file = "oncokb_genes.csv")
write.csv(onco_evidences_lookup, file = "oncokb_evidences_lookup.csv")
write.csv(onco_variants, file = "oncokb_variants.csv")
write.csv(onco_levels, file = "oncokb_levels.csv")
write.csv(onco_all_actionable_variants, file = "oncokb_all_actionable_variants.csv")
write.csv(onco_all_annotated_variants, file = "oncokb_all_annotated_variants.csv")

