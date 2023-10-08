import pandas as pd

RAW_DATA_DIRECTORY = "raw/economic"
FINAL_DATA_DIRECTORY = "final/economic"

NEW_MAPPING = {
    "Central Mindanao": "Region XII (SOCCSKSARGEN)",
    "Southern Tagalog":[
        'Region IV-A (CALABARZON)',
        "MIMAROPA Region",
    ],
    "Southern Mindanao": "Region XI (Davao Region)",
    "Western Mindanao": "Region IX (Zamboanga Peninsula)",
}
REGIONAL_MAPPING = {
    'Cordillera Administrative Region (CAR)':"PH140000000",
    'Region I (Ilocos Region)':"PH010000000", 
    'Region II (Cagayan Valley)':"PH020000000",
    'Region III (Central Luzon)':"PH030000000", 
    'Region IV-A (CALABARZON)':"PH040000000", 
    'MIMAROPA Region':"PH170000000",
    'Region V (Bicol Region)':"PH050000000", 
    'Region VI (Western Visayas)':"PH060000000",
    'Region VII (Central Visayas)':"PH070000000", 
    'Region VIII (Eastern Visayas)':"PH080000000",
    'Region IX (Zamboanga Peninsula)':"PH090000000",
    'Region X (Northern Mindanao)':"PH100000000", 
    'Region XI (Davao Region)':"PH110000000", 
    'Region XII (SOCCSKSARGEN)':"PH120000000", 
    'Region XIII (Caraga)':"PH160000000",
    'Autonomous Region in Muslim Mindanao (ARMM)':"PH150000000"
}

def get():
    labor = pd.read_csv(f"{RAW_DATA_DIRECTORY}/agricultural_wage_rate.csv", sep=",", skiprows=2, na_values=[".",".."])

    # No data before 1994
    columns_to_keep = ['Type of Wages', 'Type of Farm Workers', 'Geolocation'] + [str(year) + ' ..Male' for year in range(1994, 2020)] + [str(year) + ' ..Female' for year in range(1994, 2020)]
    labor = labor[columns_to_keep]


    labor["Geolocation"] = labor["Geolocation"].str\
                            .replace(r'^\.+', "", regex=True)\
                            .replace(r',', "", regex=True)\
                            .replace(r'(\w|\d)/', "", regex=True)\
                            .str.strip()

    labor["Type of Farm Workers"] = labor["Type of Farm Workers"].str\
                            .replace(r'^\.+', "", regex=True)\
                            .replace(r',', "", regex=True)\
                            .replace(r'(\w|\d)/', "", regex=True)\
                            .str.strip()

    for old_region in NEW_MAPPING.keys():
        new_region = NEW_MAPPING[old_region]
        if isinstance(new_region, list):
            for region in new_region:
                labor["Geolocation"] = labor["Geolocation"].str.replace(old_region, region)
        else:
            labor["Geolocation"] = labor["Geolocation"].str.replace(old_region, new_region)

    # merge vertically
    labor = labor.groupby(["Geolocation", "Type of Farm Workers","Type of Wages"]).first().reset_index()
    labor = pd.melt(labor, id_vars=["Type of Wages", "Type of Farm Workers", "Geolocation"], var_name="Year and Gender", value_name="Value")
    labor[["Year", "Gender"]] = labor["Year and Gender"].str.split(" ..", expand=True)
    labor.drop("Year and Gender", axis=1, inplace=True)
    labor = labor.pivot(index=["Type of Wages", "Type of Farm Workers", "Geolocation","Gender"], columns="Year", values="Value").reset_index()
    labor["ADM1_CODE"] = labor["Geolocation"].apply(lambda x: REGIONAL_MAPPING[x])

    labor.to_csv(f"{FINAL_DATA_DIRECTORY}/agricultural_wage_rate.csv", index=False)
    return labor

