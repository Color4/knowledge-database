#!/bin/bash
#script to get data from api and convert to csv for onko kb


#get oncotree mainTypes
curl -X GET --header "Accept: application/json" "http://oncotree.mskcc.org/oncotree/api/mainTypes" >oncotree_maintypes.json
in2csv oncotree_maintypes.json >  oncotree_maintypes.csv -k 'data'


# tumor types .txt files
wget http://oncotree.mskcc.org/oncotree/api/tumor_types.txt

# get genes
curl http://oncokb.org/api/v1/genes >onco_genes.json
in2csv onco_genes.json >  onco_genes.csv

#get oncokb evidences
curl http://oncokb.org/api/v1/evidences/lookup?source=oncotree >onco_evidences.json
in2csv onco_evidences.json >  onco_evidences.csv

#get oncokb evidences
curl http://oncokb.org/api/v1/variants >onco_variants.json
in2csv onco_variants.json >  onco_variants.csv

#get oncokb levels
curl http://oncokb.org/api/v1/levels >onco_levels.json
in2csv onco_levels.json >  onco_levels.csv

#get oncokb all actionable variants
curl http://oncokb.org/api/v1/utils/allActionableVariants >onco_actionableVariants.json
in2csv onco_actionableVariants.json >  onco_actionableVariants.csv

#get oncokb all annotated variants
curl http://oncokb.org/api/v1/utils/allActionableVariants >onco_all_annotated_variants.json
in2csv onco_all_annotated_variants.json >  onco_all_annotated_variants.csv



# delete un-needed json files
rm *.json

eCollection=( $(cut -d ',' -f1 onco_genes.csv ) )
for i in  "${eCollection[@]}"; do  curl http://oncokb.org/api/v1/genes/$i/evidences > $i.json; done
for i in  "${eCollection[@]}"; do in2csv $i.json >  $i.csv; done
rm *.json
