import pandas as pd
import re

from .mappings import PROVINCIAL_MAPPINGS

RAW_DATA_DIRECTORY = "raw/poverty"
FINAL_DATA_DIRECTORY = "final/poverty"

def get():
    income_gap = pd.read_csv(f"{RAW_DATA_DIRECTORY}/income_gap.csv", skiprows=2, sep=";")

    income_gap["Geolocation"] = income_gap["Geolocation"].str\
                            .replace(r'^\.+', "", regex=True)\
                            .replace(r',', "", regex=True)\
                            .replace(r'(\w|\d)/', "", regex=True)\
                            .str.strip()

    income_gap["ADM2_CODE"] = income_gap["Geolocation"].apply(lambda x: PROVINCIAL_MAPPINGS[x])

    irrelevant_columns = [
        "Standard Error 2015",
        "Standard Error 2018",
        "Standard Error 2021p",
        '90% Confidence Interval (Lower Limit) 2015',
        '90% Confidence Interval (Lower Limit) 2018',
        '90% Confidence Interval (Lower Limit) 2021p',
        '90% Confidence Interval (Upper Limit) 2015',
        '90% Confidence Interval (Upper Limit) 2018',
        '90% Confidence Interval (Upper Limit) 2021p',
    ]
    rename_columns = {
        "Income Gap (%) 2015":"2015",
        "Income Gap (%) 2018":"2018",
        "Income Gap (%) 2021p":"2021",
    }
    income_gap.drop(columns=irrelevant_columns, inplace=True, axis=1)
    income_gap.rename(columns=rename_columns, inplace=True)

    income_gap.to_csv(f"{FINAL_DATA_DIRECTORY}/income_gap.csv", index=False)
    return income_gap
