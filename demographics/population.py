import os
import wget
import urllib
import pandas as pd
from collections import OrderedDict
from fuzzywuzzy import process
import numpy as np
from pandarallel import pandarallel

pandarallel.initialize(progress_bar=True)

MANILA_DISTRICTS = {
        "TONDO I/II",
        "BINONDO",
        "QUIAPO",
        "SAN NICOLAS",
        "SANTA CRUZ",
        "SAMPALOC",
        "SAN MIGUEL",
        "ERMITA",
        "INTRAMUROS",
        "MALATE",
        "PACO",
        "PANDACAN",
        "PORT AREA"
        "SANTA ANA"
}

RAW_DATASET_URLS = [
    "https://psa.gov.ph/system/files/phcd/2022-12/NCR.xlsx",
    "https://psa.gov.ph/system/files/phcd/2022-12/CAR.xlsx",
    "https://psa.gov.ph/system/files/phcd/2022-12/Region%25201.xlsx",
    "https://psa.gov.ph/system/files/phcd/2022-12/Region%25202.xlsx",
    "https://psa.gov.ph/system/files/phcd/2022-12/Region%25203.xlsx",
    "https://psa.gov.ph/system/files/phcd/2022-12/Region%25205.xlsx",
    "https://psa.gov.ph/system/files/phcd/2022-12/%25281%2529%2520Region%25206_final.xlsx",
    "https://psa.gov.ph/system/files/phcd/2022-12/Region%25207.xlsx",
    "https://psa.gov.ph/system/files/phcd/2022-12/Region%25208.xlsx",
    "https://psa.gov.ph/system/files/phcd/2022-12/Region%25209.xlsx",
    "https://psa.gov.ph/system/files/phcd/2022-12/Region%252010.xlsx",
    "https://psa.gov.ph/system/files/phcd/2022-12/Region%252011.xlsx",
    "https://psa.gov.ph/system/files/phcd/2022-12/Region%252012.xlsx",
    "https://psa.gov.ph/system/files/phcd/2022-12/Caraga.xlsx",
    "https://psa.gov.ph/system/files/phcd/2022-12/BARMM.xlsx",
    "https://psa.gov.ph/system/files/phcd/2022-12/Region%25204A.xlsx",
    "https://psa.gov.ph/system/files/phcd/2022-12/MIMAROPA.xlsx"
]

RAW_DATA_DIRECTORY = "raw/locations"

population_dict = []
location_data = pd.DataFrame()
def extractFiles():
    raw_files = []
    for url in RAW_DATASET_URLS:
        try:
            decodedURL = urllib.parse.unquote(url)
            fileName = decodedURL.split("/")[-1]
            raw_files.append(fileName)
            if not os.path.exists(f"{RAW_DATA_DIRECTORY}/{fileName}"):
                print(f"Downloading url {url}")
                print(decodedURL)
                wget.download(decodedURL, out=f"{os.getcwd()}/{RAW_DATA_DIRECTORY}")
            else:
                print(f"File {fileName} already exists")
        except urllib.error.HTTPError as e:
            print(f"An error has occurred while downloading url {url}: {e}") 
    return raw_files

def appendRow(province : str, municipality : str, brgy_name : str, brgy_pop : str):
    global population_dict
    population_dict.append({'Province': province, 'Municipality' : municipality, 'Barangay' : brgy_name , '2020 Population' : brgy_pop})
  
def sanitizeString(s: str):
    s = s.replace("*",'')
    s = s.replace("(Pob.)",'')
    s = s.replace("(Capital)",'')
    s = s.strip()
    return s

def obtainRaw():
    global population_dict
    raw_files = extractFiles()
    
    for file in raw_files:
        df_dictionary = OrderedDict(pd.read_excel(f"{RAW_DATA_DIRECTORY}/{file}", sheet_name = None))
        df_dictionary.popitem(last=False) # Removes the first sheet

        print(f"Reading file {file}")
        column_idenifier = 'Total Population by Province, City, Municipality, and Barangay:'

        #Special Cases:
        if file == "Region%2012.xlsx": # for region 12
            df_dictionary.popitem(last=False)
        if file == "BARMM.xlsx" or file == "NCR.xlsx": # for BARMM and NCR
            column_idenifier = 'Total Population by Province, City, and Municipality:'

        for df_key in df_dictionary:
            df = df_dictionary[df_key]

            province_name : str =''
            municipality_name : str = ''
            barangay_name: str = ''
            barangay_population : int = 0

            name_col_index = df_dictionary[df_key].columns.get_loc(column_idenifier)
            pop_col_index = name_col_index+1

            for index, row in df.iterrows():
                name = sanitizeString(str(row.iloc[name_col_index]))
                if index < 5: 
                    continue
                if str(name) == 'nan' :
                    continue
                if str(name) in ["Note:","Source:","Notes:"]:
                    break

                if index == 5:
                    province_name = name.title()
                elif str(df.iloc[index-1][name_col_index]) == 'nan':
                    #SPECIAL CASES FOR Manila
                    if name in MANILA_DISTRICTS and province_name == "National Capital Region":
                        # print(f"Found a district in Manila: {name}")
                        municipality_name = name + ", Manila"
                    else:
                        municipality_name = name.title()
                else:
                    try:
                        barangay_name = name.title()
                        barangay_population = int(row[name_col_index+1])
                        # print(province_name, municipality_name, barangay_name, barangay_population)
                        appendRow(province_name, municipality_name, barangay_name, barangay_population)
                    except ValueError:
                        print(f"{barangay_name} doesn't have a population count.  Removing from the database.")


    return pd.DataFrame(population_dict, columns = ['Province','Municipality','Barangay','2020 Population'])

def find_match(row, location_data):
    # import numpy as np
    # import pandas as pd
    from fuzzywuzzy import process

    # global location_data

    # print(row["combined__cleaned"])
    # print(location_data["combined__cleaned"])

    print("Finding match for: ", row.combined__cleaned)
    prov_muni_keys = {} # key = location, value = popu
    filter = ''
    if row["combined__cleaned"] not in prov_muni_keys.keys():
        key, score = process.extractOne(row["combined__cleaned"], location_data["combined__cleaned"].unique())
        prov_muni_keys[row["combined__cleaned"]] = key
        filter = key
    else:
        filter = prov_muni_keys[row["combined__cleaned"]]
    location_data_filtered = location_data[location_data["combined__cleaned"] == filter]
    key1, score1, index1  = process.extractOne(row["Barangay"], location_data_filtered["ADM4_EN"])
    

    return location_data.iloc[index1]["ADM4_PCODE"]

def get(_location_data) -> pd.DataFrame:
    global location_data
    location_data = _location_data

    population_data = obtainRaw()
    location_data["combined__cleaned"] = (location_data["ADM3_EN"] + ", " + location_data["ADM2_EN"])\
                        .str.replace("City of ","")\
                        .str.replace("City","")\
                        .str.replace("NCR", "National Capital Region")\
                        .str.replace("First District","")\
                        .str.replace("Second District","")\
                        .str.replace("Third District","")\
                        .str.replace("Fourth District","")

    population_data["combined__cleaned"]  = (population_data["Municipality"] + ", " + population_data["Province"])\
                            .str.replace("City of ","")\
                            .str.replace("City","")\
                            .str.replace("Of ","")\
                            .tolist()
    display(population_data)

    population_data["brgy_code"] = population_data.parallel_apply(find_match, axis =1, location_data=location_data)

    # Post processing
    population_data["2020 Population"] = population_data["2020 Population"]/1000
    population_data.drop(columns=["combined__cleaned"], axis =1, inplace=True)
    location_data.drop(columns=["combined__cleaned"], axis =1, inplace=True)

    population_data.to_csv('final/demographics/population.csv', index=False)
    return population_data