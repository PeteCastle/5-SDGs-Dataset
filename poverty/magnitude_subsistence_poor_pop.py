import pandas as pd
import re

from .mappings import PROVINCIAL_MAPPINGS

RAW_DATA_DIRECTORY = "raw/poverty"
FINAL_DATA_DIRECTORY = "final/poverty"

def get():
    magnitude_subsistence_poor_pop = pd.read_csv(f"{RAW_DATA_DIRECTORY}/magnitude_subsistence_poor_pop.csv", skiprows=2, sep=";")

    magnitude_subsistence_poor_pop["Geolocation"] = magnitude_subsistence_poor_pop["Geolocation"].str\
                            .replace(r'^\.+', "", regex=True)\
                            .replace(r',', "", regex=True)\
                            .replace(r'(\w|\d)/', "", regex=True)\
                            .str.strip()

    # special case for NUEVA ECIJA due to typo
    magnitude_subsistence_poor_pop.loc[magnitude_subsistence_poor_pop["Geolocation"] == "Nueva Ecija b", "Geolocation"] = "Nueva Ecija"

    magnitude_subsistence_poor_pop["ADM2_CODE"] = magnitude_subsistence_poor_pop["Geolocation"].apply(lambda x: PROVINCIAL_MAPPINGS[x])


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
            "Magnitude of Subsistence Poor Population ('000) 2015":"2015",
            "Magnitude of Subsistence Poor Population ('000) 2018":"2018",
            "Magnitude of Subsistence Poor Population ('000) 2021p":"2021p",
    }

    magnitude_subsistence_poor_pop = magnitude_subsistence_poor_pop.drop(columns=irrelevant_columns)\
                                                    .rename(columns=rename_columns)

    magnitude_subsistence_poor_pop.to_csv(f"{FINAL_DATA_DIRECTORY}/magnitude_subsistence_poor_pop.csv", index=False)
                                                
    return magnitude_subsistence_poor_pop