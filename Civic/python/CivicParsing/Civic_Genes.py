import csv
import io
import requests
import json
from requests.exceptions import ConnectionError
import pandas as pd
from pandas.io.json import json_normalize





def getJson(CivicField):
    response=requests.get("https://civic.genome.wustl.edu/api/"+CivicField+"?count=50000")
    data = response.json()


    return data

def pandasJson(CivicField):
    df = json.loads(requests.get("https://civic.genome.wustl.edu/api/"+CivicField+"?count=50000").text)
   # data = df.json()
    data = pd.io.json.json_normalize(df)
    print (data)




df = pd.read_csv('genes.csv')


dfmelted=pd.melt(df, id_vars=['id','name','entrez_id','description'], value_vars=['"variants/"[0-9]*"/name”, "variants/"[0-9]*"/id”, ”variants/"[0-9]*"/evidence_items/accepted_count”, “variants/"[0-9]*"/evidence_items/rejected_count” ,”variants/"[0-9]*"/evidence_items/submitted_count”'])
#print(dfmelted)

df.set_index('id', inplace=True)
df.columns=df.columns.str.split("/", expand=True)
teststack=df.stack(level=0).rename_axis(['id', 'variant']).reset_index()
print(teststack)