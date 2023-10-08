import pandas as pd

from .mappings import REGIONAL_MAPPING

RAW_DATA_DIRECTORY = "raw/technology"
FINAL_DATA_DIRECTORY = "final/technology"

def get():
    data = pd.read_csv(RAW_DATA_DIRECTORY + "/core_ict_indicators_under_information_economy.csv", sep=";", na_values=["s",".."], skiprows=2)

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
    
    data = pd.melt(data, id_vars=["Geolocation","Industry Description"], var_name="Year and Metric", value_name="Value")


    data["Year"] = data["Year and Metric"].apply(lambda x: x.split(" ")[-1])
    data["Metric"] = data["Year and Metric"].apply(lambda x: " ".join(x.split(" ")[0:-1]))

    del data["Year and Metric"]
    data = data.pivot(index=["Geolocation","Industry Description","Metric"], columns="Year", values="Value").reset_index()
    data[["2010", "2013", "2015", "2017"]] = data[["2010", "2013", "2015", "2017"]].astype(float)

    # Special Case for Negros Region (existed only in 2015)
    # Since Negros Region is part of Western and Central Visayas, the best way is to divide by two.

    mask = data["Geolocation"] == "Negros Island Region"
    negros_region = data[mask].copy()
    negros_region["Geolocation"] = "Region VII (Central Visayas)"
    negros_region[["2010","2013","2015","2017"]] = negros_region[["2010","2013","2015","2017"]] /2

    data = pd.concat([data, negros_region], ignore_index=True)
    negros_region["Geolocation"] = "Region VIII (Eastern Visayas)"
    data = pd.concat([data, negros_region], ignore_index=True)

    # remove negros island region
    data = data[data["Geolocation"] != "Negros Island Region"]

    # Merge Vertically
    data = data.groupby(["Geolocation", "Industry Description","Metric"]).sum(numeric_only=True).reset_index()
        
    data["ADM1_CODE"] = data["Geolocation"].apply(lambda x: REGIONAL_MAPPING[x])

    data.to_csv(FINAL_DATA_DIRECTORY + "/core_ict_indicators_information_economy.csv", index=False)
    return data

