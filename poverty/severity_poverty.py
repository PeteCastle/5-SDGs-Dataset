import pandas as pd
import re

from poverty.mappings import PROVINCIAL_MAPPINGS

RAW_DATA_DIRECTORY = "raw/poverty"
FINAL_DATA_DIRECTORY = "final/poverty"

def get():
    severity_poverty = pd.read_csv(f"{RAW_DATA_DIRECTORY}/severity_poverty.csv", skiprows=2, sep=";")

    severity_poverty["Geolocation"] = severity_poverty["Geolocation"].str\
                            .replace(r'^\.+', "", regex=True)\
                            .replace(r',', "", regex=True)\
                            .replace(r'(\w|\d)/', "", regex=True)\
                            .str.strip()

    severity_poverty["ADM2_CODE"] = severity_poverty["Geolocation"].apply(lambda x: PROVINCIAL_MAPPINGS[x])


    irrelevant_columns = [
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
            "Severity of Poverty (%) 2015":"Poverty Severity 2015",
            "Severity of Poverty (%) 2018":"Poverty Severity 2018",
            "Severity of Poverty (%) 2021p":"Poverty Severity 2021p",
    }

    severity_poverty = severity_poverty.drop(columns=irrelevant_columns)\
                                                    .rename(columns=rename_columns)

    severity_poverty.to_csv(f"{FINAL_DATA_DIRECTORY}/severity_poverty.csv", index=False)
                                                
    return severity_poverty