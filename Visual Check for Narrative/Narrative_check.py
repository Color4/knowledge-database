import csv
import pandas as pd
import numpy as np

df = pd.read_excel("CVC_Viewer_original.xls", sheetname=0)
CGV= pd.read_excel("CVC_CGV_original.xls", sheetname=1)
#print((df.ix[:,'report_style':]))

#print(np.where(df['report_style'].isnull())[0])





df['reportcheck'] = np.where(df['report_style'].isnull(),0,1)
df['narrativecheck'] = np.where(df['narrative'].isnull(),0,1)


# use this to check if all the files in viewer are in  cancer gene var table
# merged =pd.merge(df,CGV, on=['cancer', 'gene','variant'])
merged =pd.merge(df,CGV, on=['cancer', 'gene','variant'], how='right')


merged = merged.drop('varID', axis=1)
merged = merged.drop('narrative', axis=1)
merged = merged.drop('date_view', axis=1)
merged = merged.drop('report_style', axis=1)
merged = merged.drop('curator', axis=1)
merged = merged.drop('narrative_long', axis=1)





merged =merged.fillna(0)





def f(x):
  if x['reportcheck'] == 0 and x['narrativecheck'] == 1: return 1
  elif x['reportcheck'] == 1 and x['narrativecheck'] == 0: return 2
  elif x['reportcheck'] == 1 and x['narrativecheck'] == 1: return 3
  else: return 0

merged['points'] = merged.apply(f, axis=1)
merged = merged.drop('reportcheck', axis=1)
merged = merged.drop('narrativecheck', axis=1)


merged.to_csv('merged.csv', sep=',')

#for i in (df.ix[:,'report_style':]):
 #   if (df.ix[:,'report_style':]).isnull().values.any():
  #      print(i)




#with open("CVC_VIEWER_original.tsv") as tsv:
 #   for line in csv.reader(tsv, dialect="excel-tab"):
  #      print(line)


#with open("CVC_VIEWER_original.txt") as tsv:
 #   for column in zip(*[line for line in csv.reader(tsv, dialect="excel-tab")]):
  #      print(column)