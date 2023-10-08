import pandas as pd   

RAW_DATA_DIRECTORY = "raw/drrm"
FINAL_DATA_DIRECTORY = "final/drrm"

def get():
    data = pd.read_excel(f"{RAW_DATA_DIRECTORY}/180814_number-of-evacuation-center_by-city_municipality.xlsx")
    data["Indicator"] = "Number of Evacuation Centers"
    data["2018"] = data["Number of Evacuation Center"]
    data["ADM3_PCODE"] = data["Municipality_City Code"]
    data.drop(["Municipality_City","Number of Evacuation Center", "Municipality_City Code","Province Code","Province","Region Code","Region"], axis=1, inplace=True)
    data.to_csv(f"{FINAL_DATA_DIRECTORY}/evacuation_center.csv", index=False)
    return data