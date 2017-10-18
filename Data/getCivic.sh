#!/bin/bash
#script to get data from api and convert to csv
curl https://civic.genome.wustl.edu/api/genes?count=5000 >genes.json
in2csv genes.json >  genes.csv -k 'records'
