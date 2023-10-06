import pandas as pd
import re

from poverty.mappings import PROVINCIAL_MAPPINGS

RAW_DATA_DIRECTORY = "raw/poverty"
FINAL_DATA_DIRECTORY = "final/poverty"

def get():
    poverty_incidence_threshold_family = pd.read_csv(f"{RAW_DATA_DIRECTORY}/poverty_incidence_threshold_family.csv", skiprows=2, sep=";")

    poverty_incidence_threshold_family["Geolocation"] = poverty_incidence_threshold_family["Geolocation"].str\
                            .replace(r'^\.+', "", regex=True)\
                            .replace(r',', "", regex=True)\
                            .replace(r'(\w|\d)/', "", regex=True)\
                            .str.strip()

    poverty_incidence_threshold_family["ADM2_CODE"] = poverty_incidence_threshold_family["Geolocation"].apply(lambda x: PROVINCIAL_MAPPINGS[x])

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
            "Annual Per Capita Poverty Threshold  (in PhP) 2015":"Poverty Threshold 2015",
            "Annual Per Capita Poverty Threshold  (in PhP) 2018":"Poverty Threshold 2018",
            "Annual Per Capita Poverty Threshold  (in PhP) 2021p":"Poverty Threshold 2021p",
            "Poverty Incidence among Families (%) 2015":"Poverty Incidence 2015",
            "Poverty Incidence among Families (%) 2018":"Poverty Incidence 2018",
            "Poverty Incidence among Families (%) 2021p":"Poverty Incidence 2021p",
    }

    poverty_incidence_threshold_family = poverty_incidence_threshold_family.drop(columns=irrelevant_columns)\
                                                    .rename(columns=rename_columns)
    poverty_incidence_threshold_family.to_csv(f"{FINAL_DATA_DIRECTORY}/poverty_incidence_threshold_family.csv", index=False)

    return poverty_incidence_threshold_family                              
