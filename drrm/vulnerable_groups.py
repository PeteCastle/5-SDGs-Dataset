import pandas as pd   

RAW_DATA_DIRECTORY = "raw/drrm"
FINAL_DATA_DIRECTORY = "final/drrm"

def get():
    data = pd.read_excel(f"{RAW_DATA_DIRECTORY}/180814_vulnerable-groups_by-city_municipality.xlsx")
    data.melt()
    data["ADM3_PCODE"] = data["Municipality_City Code"]
    data.drop(["Municipality_City", "Municipality_City Code","Province Code","Province","Region Code","Region"], axis=1, inplace=True)
    data = data.melt(id_vars=["ADM3_PCODE"], var_name="Indicator", value_name="2018")
    data["Indicator"] = "Number of " + data["Indicator"]
    data.to_csv(f"{FINAL_DATA_DIRECTORY}/vulnerable_groups.csv", index=False)
    return data