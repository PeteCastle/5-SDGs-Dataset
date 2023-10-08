import pandas as pd   

RAW_DATA_DIRECTORY = "raw/drrm"
FINAL_DATA_DIRECTORY = "final/drrm"

REGIONAL_MAPPING = {
    'National Capital Region (NCR)':"PH130000000",
    'Cordillera Administrative Region (CAR)':"PH140000000",
    'Region I':"PH010000000", 
    'Region II':"PH020000000",
    'Region III':"PH030000000", 
    'Region IV-A':"PH040000000", 
    'MIMAROPA':"PH170000000",
    'Region V':"PH050000000", 
    'Region VI':"PH060000000",
    'Region VII':"PH070000000", 
    'Region VIII':"PH080000000",
    'Region IX':"PH090000000",
    'Region X':"PH100000000", 
    'Region XI':"PH110000000", 
    'Region XII':"PH120000000", 
    'Caraga':"PH160000000",
    'Autonomous Region in Muslim Mindanao (ARMM)/Bangsamoro Autonomous Region in Muslim Mindanao (BARMM)':"PH150000000"
}

def get():
    data = pd.read_csv(f"{RAW_DATA_DIRECTORY}/drr_implementation.csv", skiprows=2, na_values="..")
    data["ADM1_PCODE"] = data["Geolocation"].map(REGIONAL_MAPPING)
    data["Indicator"] = "Proportion of local governments units that adopt and implement local disaster risk reduction strategies in line with national disaster risk reduction strategies"
    data.to_csv(f"{FINAL_DATA_DIRECTORY}/drr_implementation.csv", index=False)
    return data