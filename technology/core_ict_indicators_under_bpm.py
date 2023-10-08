import pandas as pd


RAW_DATA_DIRECTORY = "raw/technology"
FINAL_DATA_DIRECTORY = "final/technology"

from .mappings import REGIONAL_MAPPING

def get():
    data = pd.read_csv(RAW_DATA_DIRECTORY + "/core_ict_indicators_under_bpm.csv", na_values=["s",".."], skiprows=2)

    data["Geolocation"] = data["Geolocation"].str\
                                .replace(r'^\.+', "", regex=True)\
                                .replace(r',', "", regex=True)\
                                .replace(r'(\w|\d)/', "", regex=True)\
                                .str.strip()

    data["Industry Description"] = data["Industry Description"].str\
                            .replace(r'^\.+', "", regex=True)\
                            .replace(r',', "", regex=True)\
                            .replace(r'(\w|\d)/', "", regex=True)\
                            .str.strip()

    # data["Industry Description"]

        
    data = pd.melt(data, id_vars=["Geolocation","Industry Description"], var_name="Year and Metric", value_name="Value")


    data["Year"] = data["Year and Metric"].apply(lambda x: x.split(" ")[-1])
    data["Metric"] = data["Year and Metric"].apply(lambda x: " ".join(x.split(" ")[0:-1]))

    del data["Year and Metric"]
    data = data.pivot(index=["Geolocation","Industry Description","Metric"], columns="Year", values="Value").reset_index()

    data["ADM1_CODE"] = data["Geolocation"].apply(lambda x: REGIONAL_MAPPING[x])
    data.to_csv(FINAL_DATA_DIRECTORY + "/core_ict_indicators_under_bpm.csv", index=False)

    return data