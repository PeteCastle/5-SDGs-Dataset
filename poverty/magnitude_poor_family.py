import pandas as pd
import re

from .mappings import PROVINCIAL_MAPPINGS

RAW_DATA_DIRECTORY = "raw/poverty"
FINAL_DATA_DIRECTORY = "final/poverty"

def get():
    magnitude_poor_family = pd.read_csv(f"{RAW_DATA_DIRECTORY}/magnitude_poor_family.csv", skiprows=2, sep=";")
    magnitude_poor_family["Geolocation"] = magnitude_poor_family["Geolocation"].str\
                            .replace(r'^\.+', "", regex=True)\
                            .replace(r',', "", regex=True)\
                            .replace(r'(\w|\d)/', "", regex=True)\
                            .str.strip()
    magnitude_poor_family["ADM2_CODE"] = magnitude_poor_family["Geolocation"].apply(lambda x: PROVINCIAL_MAPPINGS[x])

    irrelevant_columns = [
        "Coefficient of Variation 2015",
        "Coefficient of Variation 2018",
        "Coefficient of Variation 2021p",
        "Standard Error 2015",
        "Standard Error 2018",
        "Standard Error 2021p",
        "90% Confidence Interval (Lower Limit) 2015",
        "90% Confidence Interval (Lower Limit) 2018",
        "90% Confidence Interval (Lower Limit) 2021p",
        "90% Confidence Interval (Upper Limit) 2015",
        "90% Confidence Interval (Upper Limit) 2018",
        "90% Confidence Interval (Upper Limit) 2021p",
    ]
    rename_columns = {
            "Estimate ('000) 2015":"2015",
            "Estimate ('000) 2018":"2018",
            "Estimate ('000) 2021p":"2021p",
    }

    magnitude_poor_family = magnitude_poor_family.drop(columns=irrelevant_columns)\
                                                    .rename(columns=rename_columns)

    magnitude_poor_family.to_csv(f"{FINAL_DATA_DIRECTORY}/magnitude_poor_family.csv", index=False)
    return magnitude_poor_family
                                                
