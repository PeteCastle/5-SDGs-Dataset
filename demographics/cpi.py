from fuzzywuzzy import process
import pandas as pd

RAW_DATA_DIRECTORY = "raw/demographics"
FINAL_DATA_DIRECTORY = "final/demographics"

commodities = ['01 - FOOD AND NON-ALCOHOLIC BEVERAGES',
       '02 - ALCOHOLIC BEVERAGES AND TOBACCO',
       '03 - CLOTHING AND FOOTWEAR',
       '04 - HOUSING, WATER, ELECTRICITY, GAS, AND OTHER FUELS',
       '05 - FURNISHINGS, HOUSEHOLD EQUIPMENT AND ROUTINE HOUSEHOLD MAINTENANCE',
       '06 - HEALTH', '07 - TRANSPORT',
       '08 - INFORMATION AND COMMUNICATION',
       '09 - RECREATION, SPORT AND CULTURE', '10 - EDUCATION SERVICES',
       '11 - RESTAURANTS AND ACCOMMODATION SERVICES',
       '12 - FINANCIAL SERVICES',
       '13 - PERSONAL CARE, AND MISCELLANEOUS GOODS AND SERVICES']

def get(location_data):
    cpi = pd.read_csv(f"{RAW_DATA_DIRECTORY}/2M4ACP09.csv", skiprows=[0,1])
    cpi["adm_level"] = cpi["Geolocation"].apply(lambda x: x.count('.'))
    cpi = cpi[(cpi["adm_level"] == 4) | (cpi["Geolocation"] == "..National Capital Region (NCR)")]

    cpi["Geolocation"] = cpi["Geolocation"].str.replace(".","", regex=False)
    cpi = cpi[cpi["Geolocation"].str.startswith("City of") == False] # Removed component cities

    cpi["Commodity Description"] = cpi["Commodity Description"].str.replace(r'\d{2} - ', '',regex=True)
    cpi["Commodity Description"] = "CPI " + cpi["Commodity Description"]
    cpi["Commodity Description"] = cpi["Commodity Description"].str.replace("AND ","").str.replace(" ","_").str.replace(",","").str.lower()
    cpi_unpivot = cpi.pivot(index = ["Geolocation"], columns = "Commodity Description", values="2022 Ave").reset_index()

    def getProvinceId(row):
        # special cases:
        if row == "Davao de Oro":
                row = "Compostela Valley"
        elif row == "National Capital Region (NCR)":
                return "PH133900000,PH137400000,PH137500000,PH137600000"
        key, _ = process.extractOne(row, location_data["ADM2_EN"].unique())
        return location_data.loc[location_data["ADM2_EN"] == key]["ADM2_PCODE"].values[0]

    cpi_unpivot["province_id"] = cpi_unpivot["Geolocation"].apply(getProvinceId)
    cpi_unpivot.to_csv(f'{FINAL_DATA_DIRECTORY}/cpi_unpivot.csv', index=False)
    return cpi_unpivot