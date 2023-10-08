
from .grdp import getRegionalId
import numpy as np
import pandas as pd

TRANSPO_REGION_MAPPINGS = {
    "Autonomous Region in Muslim Mindanao":"BARMM",
    "Eastern Visayas":"Region VIII",
    "Ilocos Region":"Region I",
    "Cagayan Valley":"Region II",
    "Central Luzon":"Region III",
    "National Capital Region":"National Capital Region",
    "CALABARZON":"Region IV-A",
    "MIMAROPA Region":"Region IV-B",
    "Bicol Region":"Region V",
    "Western Visayas":"Region VI",
    "Central Visayas":"Region VII",
    "Zamboanga Peninsula":"Region IX",
    "Northern Mindanao":"Region X",
    "Davao Region":"Region XI",
    "SOCCSKSARGEN":"Region XII",
    "Caraga":"Region XIII",
    "Cordillera Administrative Region":"Cordillera Administrative Region (CAR) ",
}

RAW_DATA_DIRECTORY = "raw/demographics"
FINAL_DATA_DIRECTORY = "final/demographics"

def get(location_data):
    transpo = pd.read_csv(f"{RAW_DATA_DIRECTORY}/2D4BAH00.csv", skiprows=[0,1], na_values=["s","-","N/A"])
    transpo["Geolocation"] = transpo["Geolocation"].str.replace(".","", regex=False)
    transpo["Industry Description"] = transpo["Industry Description"].str.replace(".","", regex=False)

    transpo = transpo.melt(id_vars= ["Geolocation","Industry Description"],var_name="Attribute Year", value_name="Value").reset_index()
    transpo["Attribute"] = transpo["Attribute Year"].str.split(" ").str[1:].str.join(" ").replace("a/","",regex=True).str.strip()
    transpo["Year"] = transpo["Attribute Year"].str.split(" ").str[0]
    del transpo["Attribute Year"]
    
    transpo = pd.pivot_table(transpo, index=["Geolocation","Attribute"], columns=["Year"], values="Value", aggfunc="first").reset_index()
    transpo["ADM1_PCODE"] = transpo["Geolocation"].map(TRANSPO_REGION_MAPPINGS).apply(getRegionalId,location_data=location_data)

    transpo["ADM1_PCODE"] = transpo["ADM1_PCODE"].str.split(",")
    transpo = transpo.explode("ADM1_PCODE")
    
    transpo.to_csv(f'{FINAL_DATA_DIRECTORY}/transpo.csv', index=False)
    return transpo