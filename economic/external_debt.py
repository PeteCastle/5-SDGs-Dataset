import pandas as pd


RAW_DATA_DIRECTORY = "raw/economic"
FINAL_DATA_DIRECTORY = "final/economic"


def get():
    data = pd.read_csv(f"{RAW_DATA_DIRECTORY}/external-debt_phl.csv")
    data = data.drop(0, axis = 0)
    data = data.drop(["Country ISO3"], axis = 1)
    data = data.pivot_table(index=["Country Name","Indicator Name","Indicator Code"], columns="Year", values="Value", aggfunc='first').reset_index()
    data["ADM0_PCODE"] = "PH" 
    # display(data)
    data.to_csv(f"{FINAL_DATA_DIRECTORY}/external-debt_phl.csv", index=False)
    return data