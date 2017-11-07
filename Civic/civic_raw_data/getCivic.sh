#!/bin/bash
#script to get data from api and convert to csv


curl https://civic.genome.wustl.edu/api/genes?count=5000 > civic_genes.json
in2csv civic_genes.json >  civic_genes.csv -k 'records'

curl https://civic.genome.wustl.edu/api/variants?count=10000 > civic_variants.json
in2csv civic_variants.json >  civic_variants.csv -k 'records'


curl https://civic.genome.wustl.edu/api/variant_groups?count=50000 > civic_vargroups.json
in2csv civic_vargroups.json >  civic_vargroups.csv -k 'records'

curl https://civic.genome.wustl.edu/api/evidence_items?count=10000 > civic_evidence_items.json
in2csv civic_evidence_items.json >  civic_evidence_items.csv -k 'records'


rm *.json
