import pandas as pd
from fuzzywuzzy import process

RAW_DATA_DIRECTORY = "raw/demographics"
FINAL_DATA_DIRECTORY = "final/demographics"

location_data = pd.DataFrame()
def getRegionalId(row):
       # inconsistent data cases:
       if "MIMAROPA" in row:
              row = "Region IV-B"
       elif "National Capital Region" in row:
              return "PH133900000,PH137400000,PH137500000,PH137600000"
  
       key, _ = process.extractOne(row, location_data["ADM1_EN"].unique())
       return location_data.loc[location_data["ADM1_EN"] == key]["ADM1_PCODE"].values[0]

def get(_location_data):
    global location_data
    location_data = _location_data
    grdp = pd.read_csv(f"{RAW_DATA_DIRECTORY}/2B5CPGD1.csv", skiprows=[0,1])
    grdp["region_id"] = grdp["Region"].apply(getRegionalId)

    grdp["region_id"] = grdp["region_id"].str.split(",")
    grdp = grdp.explode("region_id").drop("Region", axis=1)

    grdp.to_csv(f'{FINAL_DATA_DIRECTORY}/grdp.csv', index=False)
    return grdp
    # display(grdp.head(5))