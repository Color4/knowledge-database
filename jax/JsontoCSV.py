import csv

import requests
from requests.exceptions import ConnectionError
import pandas as pd
from pandas.io.json import json_normalize


#get list from jackson JAX-Clinical Knowledgebase (CKB) using the api and multiple requests
def getList(keyName):

    offset =0
    parameters = {"offset": 0, "max": 500}
    response = requests.get("https://ckb.jax.org/ckb-api/api/v1/"+keyName,params=parameters)
    data = response.json()
    count= data["totalCount"]
    w=[]


    while  offset < count:

        parameters = {"offset": offset, "max": 500}
        response = requests.get("https://ckb.jax.org/ckb-api/api/v1/"+keyName,params=parameters)
        dat = response.json()
        x= dat[keyName]
        w.extend(x)
        offset= offset+ 500
    return w

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

def saveInfotoCsv(filename,function, id, list):


    f = open(filename, "w+",encoding="utf8")
    f.close()

    with open(filename, 'a' ,encoding="utf8") as f:



          try:
               datatoprint = json_normalize(function(list[0]))
               datatoprint[id] = (list[0])
               datatoprint.to_csv(f)
          except IndexError as e:    # This is the correct syntax
                print (e)

          for x in list[1:]:

           try:
               datatoprint = json_normalize(function(x))
               datatoprint[id] = x
               datatoprint.to_csv(f, header=False,encoding="utf8" )
           except IndexError as e:    # This is the correct syntax
                print (e)


def getClinicalInfo(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/clinicalTrials/"+idNumber, timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getDrugsInfo(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/drugs/"+str(idNumber), timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getDrugsClinicalInfo(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/drugs/"+str(idNumber)+"/clinicalTrials", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getDrugsEvidencesInfo(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/drugs/"+str(idNumber)+"/evidences", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getDrugsTherapiesInfo(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/drugs/"+str(idNumber)+"/therapies", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getDrugsClassInfo(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/drugClasses/"+str(idNumber), timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getDrugsClassDrugs(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/drugClasses/"+str(idNumber)+"/drugs", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getDrugsClassTreatment(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/drugClasses/"+str(idNumber)+"/treatmentApproaches", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getGenesInfo(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/genes/"+str(idNumber), timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getGenesLevelEvidences(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/genes/"+str(idNumber)+"/evidence", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getGenesVariants(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/genes/"+str(idNumber)+"/geneVariants", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getGenesMolecularProfiles(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/genes/"+str(idNumber)+"/molecularProfiles", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getIndicationsInfo(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/indications/"+str(idNumber), timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getIndicationsAssociatedEvidences(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/indications/"+str(idNumber)+"/associatedEvidences", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data


def getIndicationsClinicalTrials(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/indications/"+str(idNumber)+"/clinicalTrials", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getMolecularProfilesInfo(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/molecularProfiles/"+str(idNumber), timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getComplexMolecularProfileEvidence(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/molecularProfiles/"+str(idNumber)+"/complexMolecularProfileEvidence", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getGeneAssociatedClinicalTrials(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/molecularProfiles/"+str(idNumber)+"/geneAssociatedClinicalTrials", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data


def getGeneLevelEvidence(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/molecularProfiles/"+str(idNumber)+"/geneLevelEvidence", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getTreatmentApproachEvidence(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/molecularProfiles/"+str(idNumber)+"/treatmentApproachEvidence", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getVariantAssociatedClinicalTrials(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/molecularProfiles/"+str(idNumber)+"/variantAssociatedClinicalTrials", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getVariantLevelEvidence(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/molecularProfiles/"+str(idNumber)+"/variantLevelEvidence", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data


def getReferencesInfo(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/references/"+str(idNumber), timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getReferencesDrugs(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/references/"+str(idNumber)+"/drugs", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getReferencesGenes(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/references/"+str(idNumber)+"/genes", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getReferencesProfileResponses(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/references/"+str(idNumber)+"/profileResponses", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getReferencesTherapies(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/references/"+str(idNumber)+"/therapies", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getReferencesTreatmentApproaches(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/references/"+str(idNumber)+"/treatmentApproaches", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data


def getReferencesVariants(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/references/"+str(idNumber)+"/variants", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data



def getTherapiesInfo(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/therapies/"+str(idNumber), timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getTherapiesAssociatedEvidences(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/therapies/"+str(idNumber)+"/associatedEvidences", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getTherapiesClinicalTrials(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/therapies/"+str(idNumber)+"/clinicalTrials", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getTherapiesDrugs(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/therapies/"+str(idNumber)+"/drugs", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getTreatmentApproachesInfo(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/treatmentApproaches/"+str(idNumber), timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data


def getTreatmentApproachesReferences(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/treatmentApproaches/"+str(idNumber)+"/references", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getVariantsInfo(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/variants/"+str(idNumber), timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getVariantsEvidence(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/variants/"+str(idNumber)+"/evidence", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data

def getVariantMolecularProfiles(idNumber):
    global data

    try:
        response = requests.get("https://ckb.jax.org:443/ckb-api/api/v1/variants/"+str(idNumber)+"/molecularProfiles", timeout=1000)
        data = response.json()
       # data= flatten_json(data)
    except ConnectionError as e:    # This is the correct syntax
        print (e)
        r = "No response"
    return data






#get Clinical trial id and titles from Jackson ckb
def getClinicalTrials(keyName):

    parsed_in= getList(keyName)
    nctIDlist=[]
    for x in parsed_in:
        nctIDlist.append(x['nctId'])

    with open(keyName+".csv", "w", newline= '',  encoding='utf-8' )as r:
         f = csv.writer(r)
         f.writerow(['nctId', 'title'])
         for x in parsed_in:
             f.writerow([x['nctId'], x['title']])

    filename = "ClinicaltrialsID.csv"
    # opening the file with w+ mode truncates the file
    f = open(filename, "w+" ,encoding="utf8")
    f.close()



    with open("ClinicaltrialsID.csv", 'a' ,encoding="utf8") as f:
          datatoprint = json_normalize(getClinicalInfo(nctIDlist[0]))

          datatoprint.to_csv(f )
          for x in nctIDlist:

            datatoprint = json_normalize(getClinicalInfo(x))

            datatoprint.to_csv(f, header=False,encoding="utf8")
        #data.to_csv("temp.csv", sep=',', encoding='utf-8')
        #df.to_csv('results.csv')











#get drugs id, drugnames and terms from Jackson ckb
def getDrugs(keyName):

    parsed_in= getList(keyName)
    IDlist=[]
    for x in parsed_in:
        IDlist.append(x['id'])

    with open(keyName+".csv", "w", newline= '',  encoding='utf-8' )as r:
        f = csv.writer(r)
        f.writerow(['Id', 'drugName','terms'])
        for x in parsed_in:
             f.writerow([x["id"], x["drugName"],x["terms"]])


    filename = "DrugsID.csv"
    # opening the file with w+ mode truncates the file
    f = open(filename, "w+",encoding="utf8")
    f.close()



    with open("DrugsID.csv", 'a' ,encoding="utf8") as f:
          datatoprint = json_normalize(getDrugsInfo(IDlist[0]))

          datatoprint.to_csv(f)
          for x in IDlist[1:]:

            datatoprint = json_normalize(getDrugsInfo(x))

            datatoprint.to_csv(f, header=False,encoding="utf8" )
        #data.to_csv("temp.csv", sep=',', encoding='utf-8')
        #df.to_csv('results.csv')


    saveInfotoCsv("DrugsID_Clinical.csv",getDrugsClinicalInfo, 'Drug_id', IDlist)
    saveInfotoCsv("DrugsID_Evidence.csv",getDrugsEvidencesInfo, 'Drug_id', IDlist)
    saveInfotoCsv("DrugsID_Therapies.csv",getDrugsTherapiesInfo, 'Drug_id', IDlist)



#getClinicalTrials("clinicalTrials")



#get drug class info id and drugclass from Jackson ckb





def getDrugClasses( keyName):
    parsed_in= getList(keyName)
    IDlist=[]
    for x in parsed_in:
        IDlist.append(x['id'])

    with open(keyName+".csv", "w", newline= '',  encoding='utf-8' )as r:
        f = csv.writer(r)
        f.writerow(['id', 'drugClass'])
        for x in parsed_in:
            f.writerow([x["id"], x["drugClass"]])

    filename = "DrugClassID.csv"
    # opening the file with w+ mode truncates the file
    f = open(filename, "w+",encoding="utf8")
    f.close()



    with open("DrugClassID.csv", 'a' ,encoding="utf8") as f:
          datatoprint = json_normalize(getDrugsClassInfo(IDlist[0]))

          datatoprint.to_csv(f)
          for x in IDlist[1:]:

            datatoprint = json_normalize(getDrugsClassInfo(x))

            datatoprint.to_csv(f, header=False,encoding="utf8" )


    saveInfotoCsv("DrugClass_drugs.csv",getDrugsClassDrugs, 'DrugClass_id', IDlist)
    saveInfotoCsv("DrugClass_Treatment.csv",getDrugsClassTreatment, 'DrugClass_id', IDlist)




#get genes  id, genesymbol and terms  from Jackson ckb
def getGenes( keyName):
    parsed_in= getList(keyName)
    IDlist=[]
    for x in parsed_in:
        IDlist.append(x['id'])

    with open(keyName+".csv", "w", newline= '',  encoding='utf-8' )as r:
        f = csv.writer(r)
        f.writerow(['id', 'geneSymbol', 'terms'])
        for x in parsed_in:
         f.writerow([x["id"], x["geneSymbol"],x["terms"]])

    filename = "GenesID.csv"
    # opening the file with w+ mode truncates the file
    f = open(filename, "w+",encoding="utf8")
    f.close()



    with open("GenesID.csv", 'a' ,encoding="utf8") as f:
          datatoprint = json_normalize(getGenesInfo(IDlist[0]))

          datatoprint.to_csv(f)
          for x in IDlist[1:]:

            datatoprint = json_normalize(getGenesInfo(x))

            datatoprint.to_csv(f, header=False,encoding="utf8" )

    saveInfotoCsv("Gene_Level_Evidences.csv",getGenesLevelEvidences, 'Gene_id', IDlist)
    saveInfotoCsv("Gene_Variants.csv",getGenesVariants, 'Gene_id', IDlist)
    saveInfotoCsv("Gene_Molecular_Profiles.csv",getGenesMolecularProfiles, 'Gene_id', IDlist)



#get Clinical trial id and titles from Jackson ckb
def getIndications( keyName):
    parsed_in= getList(keyName)
    IDlist=[]
    for x in parsed_in:
        IDlist.append(x['id'])

    with open(keyName+".csv", "w", newline= '',  encoding='utf-8' )as r:
        f = csv.writer(r)
        f.writerow(['id', 'name', 'source'])
        for x in parsed_in:
            f.writerow([x["id"], x["name"],x["source"]])

    filename = "IndicationsID.csv"
    # opening the file with w+ mode truncates the file
    f = open(filename, "w+",encoding="utf8")
    f.close()



    with open("IndicationsID.csv", 'a' ,encoding="utf8") as f:
          datatoprint = json_normalize(getIndicationsInfo(IDlist[0]))

          datatoprint.to_csv(f)
          for x in IDlist[1:]:

            datatoprint = json_normalize(getIndicationsInfo(x))

            datatoprint.to_csv(f, header=False,encoding="utf8" )

    saveInfotoCsv("Indications_Associated_Evidences.csv",getIndicationsAssociatedEvidences, 'Indications_id', IDlist)
    saveInfotoCsv("Indications_Clinical_Trials.csv",getIndicationsClinicalTrials, 'Indications_id', IDlist)







#get molecular profile info, id and profile name from Jackson ckb
def getMolecularProfiles( keyName):
    parsed_in= getList(keyName)
    IDlist=[]
    for x in parsed_in:
        IDlist.append(x['id'])


    with open(keyName+".csv", "w", newline= '',  encoding='utf-8' )as r:
        f = csv.writer(r)
        f.writerow(['id', 'profileName'])
        for x in parsed_in:
            f.writerow([x["id"], x["profileName"]])

    filename = "MolecularProfileID.csv"
    # opening the file with w+ mode truncates the file
    f = open(filename, "w+",encoding="utf8")
    f.close()



    with open("MolecularProfileID.csv", 'a' ,encoding="utf8") as f:
          datatoprint = json_normalize(getMolecularProfilesInfo(IDlist[0]))

          datatoprint.to_csv(f)
          for x in IDlist[1:]:

            datatoprint = json_normalize(getMolecularProfilesInfo(x))

            datatoprint.to_csv(f, header=False,encoding="utf8" )

    #saveInfotoCsv("Molecular_Profile_Complex_Evidences.csv",getComplexMolecularProfileEvidence, 'MolecularProfile_id', IDlist)
   # saveInfotoCsv("Molecular_Profile_Gene_Associated_Clinical_Trials.csv",getGeneAssociatedClinicalTrials, 'MolecularProfile_id', IDlist)
    saveInfotoCsv("Molecular_Profile_Gene_Level_Evidences.csv",getGeneLevelEvidence, 'MolecularProfile_id', IDlist)
    saveInfotoCsv("Molecular_Profile_Treatment_Associated_Evidences.csv",getGeneAssociatedClinicalTrials, 'MolecularProfile_id', IDlist)
    saveInfotoCsv("Molecular_Profile_Variant_Associated_Clinical_Trials.csv",getVariantAssociatedClinicalTrials, 'MolecularProfile_id', IDlist)
    saveInfotoCsv("Molecular_Profile_Variant_Level_Evidences.csv",getVariantLevelEvidence, 'MolecularProfile_id', IDlist)














#get references info id, pebmedId, title and url from jacksoon ckb
def getReferences( keyName):
    parsed_in= getList(keyName)
    IDlist=[]
    for x in parsed_in:
        IDlist.append(x['id'])


    with open(keyName+".csv", "w", newline= '',  encoding='utf-8' )as r:
        f = csv.writer(r)
        f.writerow(['id', 'pubMedId','title','url'])
        for x in parsed_in:
            f.writerow([x["id"], x["pubMedId"],x["title"], x["url"]])


    filename = "ReferencesID.csv"
    # opening the file with w+ mode truncates the file
    f = open(filename, "w+",encoding="utf8")
    f.close()



    with open("ReferencesID.csv", 'a' ,encoding="utf8") as f:
          datatoprint = json_normalize(getReferencesInfo(IDlist[0]))

          datatoprint.to_csv(f)
          for x in IDlist[1:]:

            datatoprint = json_normalize(getReferencesInfo(x))

            datatoprint.to_csv(f, header=False,encoding="utf8" )

    saveInfotoCsv("References_Drugs.csv",getReferencesDrugs, 'References_id', IDlist)
    saveInfotoCsv("References_Genes.csv",getReferencesGenes, 'References_id', IDlist)
    saveInfotoCsv("References_Profile_Responses.csv",getReferencesProfileResponses, 'References_id', IDlist)
    saveInfotoCsv("References_Therapies.csv",getReferencesTherapies, 'References_id', IDlist)
    saveInfotoCsv("References_Treatment_Approaches.csv",getReferencesTreatmentApproaches, 'References_id', IDlist)
    saveInfotoCsv("References_Variants.csv",getReferencesVariants, 'References_id', IDlist)









#get therapies id and therapyname from Jackson ckb
def getTherapies( keyName):
    parsed_in= getList(keyName)
    IDlist=[]
    for x in parsed_in:
        IDlist.append(x['id'])

    with open(keyName+".csv", "w", newline= '',  encoding='utf-8' )as r:
        f = csv.writer(r)
        f.writerow(['id', 'therapyName'])
        for x in parsed_in:
            f.writerow([x["id"], x["therapyName"]])


    filename = "TherapyID.csv"
    # opening the file with w+ mode truncates the file
    f = open(filename, "w+",encoding="utf8")
    f.close()



    with open("TherapyID.csv", 'a' ,encoding="utf8") as f:
          datatoprint = json_normalize(getTherapiesInfo(IDlist[0]))

          datatoprint.to_csv(f)
          for x in IDlist[1:]:

            datatoprint = json_normalize(getTherapiesInfo(x))

            datatoprint.to_csv(f, header=False,encoding="utf8" )


    saveInfotoCsv("Therapies_Associated_Evidences.csv",getReferencesTherapies, 'Therapies_id', IDlist)
    saveInfotoCsv("Therapies_Clinical_Trials.csv",getTherapiesClinicalTrials, 'Therapies_id', IDlist)
    saveInfotoCsv("Therapies_Drugs.csv",getTherapiesDrugs, 'Therapies_id', IDlist)






#get treatment approach info ,  id, name and profilename from Jackson ckb
def getTreatmentApproach( keyName):
    parsed_in= getList(keyName)
    IDlist=[]
    for x in parsed_in:
        IDlist.append(x['id'])


    with open(keyName+".csv", "w", newline= '',  encoding='utf-8' )as r:
        f = csv.writer(r)
        f.writerow(['id', 'name', 'profileName'])
        for x in parsed_in:
            f.writerow([x["id"], x["name"],x["profileName"]])

    filename = "TreatmentApproachID.csv"
    # opening the file with w+ mode truncates the file
    f = open(filename, "w+",encoding="utf8")
    f.close()



    with open("TreatmentApproachID.csv", 'a' ,encoding="utf8") as f:
          datatoprint = json_normalize( getTreatmentApproachesInfo(IDlist[0]))

          datatoprint.to_csv(f)
          for x in IDlist[1:]:

            datatoprint = json_normalize( getTreatmentApproachesInfo(x))

            datatoprint.to_csv(f, header=False,encoding="utf8" )

    saveInfotoCsv("TreatmentApproach_References.csv", getTreatmentApproachesReferences, 'Treatment_id', IDlist)






#get variants, fullname impact and protein effect from Jackson ckb
def getVariants( keyName):
    parsed_in= getList(keyName)
    IDlist=[]
    for x in parsed_in:
        IDlist.append(x['id'])

    with open(keyName+".csv", "w", newline= '',  encoding='utf-8' )as r:
        f = csv.writer(r)
        f.writerow(['id', 'fullName', 'impact', 'proteinEffect'])
        for x in parsed_in:
            f.writerow([x["id"], x["fullName"],x["impact"],x["proteinEffect"]])







    # opening the file with w+ mode truncates the file


    datatoprint = ( getVariantsInfo(IDlist[0]))
    gv=datatoprint['geneVariantDescriptions']
    y=flatten_json(gv)
    for key, value in y.items() :
          print (key, value)
    datatoprint ={'references': [{'id': 275, 'title': '', 'url': 'http://www.ncbi.nlm.nih.gov/pubmed/10', 'pubMedId': 10}], 'description': 'Wild-type BRAF indicates that no mutation has been detected within the BRAF gene.'}
    data=flatten_json(datatoprint)
    #print(data)

    #cols = data.columns.tolist()
    #print(cols)
    #cols=['createDate', 'fullName',  'id', 'impact', 'proteinEffect', 'updateDate', 'variant','gene.geneSymbol', 'gene.id', 'gene.terms', 'geneVariantDescriptions']
    #data=data[cols]
    #print(data)
    #g=(data[['geneVariantDescriptions']])






   # print(cols)



    filename = "VariantID.csv"

    f = open(filename, "w+",encoding="utf8")
    f.close()
    filename = "gvc.csv"

    f = open(filename, "w+",encoding="utf8")
    f.close()

    with open("gvc.csv", 'a' ,newline='',encoding="utf8") as f:

            for x in IDlist:

                   datatoprint = (getVariantsInfo(x))
                   #cols = datatoprint.columns.tolist()
                   gv=datatoprint['geneVariantDescriptions']
                   y=flatten_json(gv)
                   y["VARid"] = x
                   print(y)
                   w = csv.DictWriter(f, y.keys())
                   w.writerow(y)

                   #y.to_csv(f, line_terminator=',', index=False, header=False,encoding="utf8" )



    with open("VariantID.csv", 'a' ,encoding="utf8") as f:
            datatoprint = json_normalize( getVariantsInfo(IDlist[0]))
            #cols = datatoprint.columns.tolist()
            cols=['createDate', 'fullName',  'id', 'impact', 'proteinEffect', 'updateDate', 'variant','gene.geneSymbol', 'gene.id', 'gene.terms', 'geneVariantDescriptions']
            datatoprint=datatoprint[cols]


            datatoprint.to_csv(f)
            for x in IDlist[1:]:

                   datatoprint = json_normalize(getVariantsInfo(x))
                   #cols = datatoprint.columns.tolist()
                   cols=['createDate', 'fullName',  'id', 'impact', 'proteinEffect', 'updateDate', 'variant','gene.geneSymbol', 'gene.id', 'gene.terms', 'geneVariantDescriptions']
                   datatoprint=datatoprint[cols]

                   datatoprint.to_csv(f, header=False,encoding="utf8" )


    with open("gvc.csv", 'a' ,encoding="utf8") as f:

            for x in IDlist:

                   datatoprint = json_normalize(getVariantsInfo(x))
                   #cols = datatoprint.columns.tolist()
                   gv=datatoprint['geneVariantDescriptions']

                   y=flatten_json(gv)

                   y.to_csv(f, line_terminator=',', index=False, header=False,encoding="utf8" )



    #saveInfotoCsv("Variant_Evidence.csv", getVariantsEvidence, 'Variant_id', IDlist)
    #saveInfotoCsv("Variant_Molecular_Profiles.csv", getVariantMolecularProfiles, 'Variant_id', IDlist)








#run functions to get all the data from jackson






#getClinicalTrials("clinicalTrials" )
#getDrugs("drugs")


#getDrugClasses(("drugClasses"))
getGenes(("genes"))
#getIndications("indications")

#getReferences("references")
#getTherapies("therapies")
#getTreatmentApproach("treatmentApproaches")
#getVariants("variants")
#getMolecularProfiles("molecularProfiles")

exit()









