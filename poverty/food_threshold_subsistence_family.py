import pandas as pd
import re

from .mappings import PROVINCIAL_MAPPINGS

RAW_DATA_DIRECTORY = "raw/poverty"
FINAL_DATA_DIRECTORY = "final/poverty"

def get():
    food_threshold_subsistence_families = pd.read_csv(f"{RAW_DATA_DIRECTORY}/food_threshold_subsistence_families.csv", skiprows=2, sep=";")

    food_threshold_subsistence_families["Geolocation"] = food_threshold_subsistence_families["Geolocation"].str\
                            .replace(r'^\.+', "", regex=True)\
                            .replace(r',', "", regex=True)\
                            .replace(r'(\w|\d)/', "", regex=True)\
                            .str.strip()

    food_threshold_subsistence_families["ADM2_CODE"] = food_threshold_subsistence_families["Geolocation"].apply(lambda x: PROVINCIAL_MAPPINGS[x])

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
            "Annual Per Capita Food Threshold (in PhP) 2015":"Per Capita Food Threshold 2015",
            "Annual Per Capita Food Threshold (in PhP) 2018":"Per Capita Food Threshold 2018",
            "Annual Per Capita Food Threshold (in PhP) 2021p":"Per Capita Food Threshold 2021p",
            "Subsistence Incidence among Families (%) 2015":"Subsistence Incidence 2015",
            "Subsistence Incidence among Families (%) 2018":"Subsistence Incidence 2018",
            "Subsistence Incidence among Families (%) 2021p":"Subsistence Incidence 2021p",
    }

    food_threshold_subsistence_families = food_threshold_subsistence_families.drop(columns=irrelevant_columns)\
                                                    .rename(columns=rename_columns)

    food_threshold_subsistence_families.to_csv(f"{FINAL_DATA_DIRECTORY}/food_threshold_subsistence_families.csv", index=False)
    return food_threshold_subsistence_families              
