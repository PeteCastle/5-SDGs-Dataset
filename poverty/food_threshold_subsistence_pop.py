import pandas as pd
import re

from .mappings import PROVINCIAL_MAPPINGS

RAW_DATA_DIRECTORY = "raw/poverty"
FINAL_DATA_DIRECTORY = "final/poverty"

def get():
    food_threshold_subsistence_pop = pd.read_csv(f"{RAW_DATA_DIRECTORY}/food_threshold_subsistence_pop.csv", skiprows=2, sep=";")

    food_threshold_subsistence_pop["Geolocation"] = food_threshold_subsistence_pop["Geolocation"].str\
                            .replace(r'^\.+', "", regex=True)\
                            .replace(r',', "", regex=True)\
                            .replace(r'(\w|\d)/', "", regex=True)\
                            .str.strip()

    # special case for LAGUNA due to typo
    # food_threshold_subsistence_pop.loc[food_threshold_subsistence_pop["Geolocation"] == "Nueva Ecija b", "Geolocation"] = "Nueva Ecija"

    food_threshold_subsistence_pop["ADM2_CODE"] = food_threshold_subsistence_pop["Geolocation"].apply(lambda x: PROVINCIAL_MAPPINGS[x])


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
            "Annual Per Capita Food Threshold  (in PhP) 2015":"Per Capita Food Threshold 2015",
            "Annual Per Capita Food Threshold  (in PhP) 2018":"Per Capita Food Threshold 2018",
            "Annual Per Capita Food Threshold  (in PhP) 2021p":"Per Capita Food Threshold 2021p",
            "Estimates (%) 2015":"Subsistence Incidence 2015",
            "Estimates (%) 2018":"Subsistence Incidence 2018",
            "Estimates (%) 2021p":"Subsistence Incidence 2021p",
    }

    food_threshold_subsistence_pop = food_threshold_subsistence_pop.drop(columns=irrelevant_columns)\
                                                    .rename(columns=rename_columns)
    
    
    food_threshold_subsistence_pop = food_threshold_subsistence_pop.melt(id_vars=["ADM2_CODE", "Geolocation"], var_name="Attribute Year", value_name="Value")
    food_threshold_subsistence_pop["Year"] = food_threshold_subsistence_pop["Attribute Year"].str.split(" ").str[-1]
    food_threshold_subsistence_pop["Attribute"] = food_threshold_subsistence_pop["Attribute Year"].str.split(" ").str[:-1].str.join(" ")
    del food_threshold_subsistence_pop["Attribute Year"]
    food_threshold_subsistence_pop = food_threshold_subsistence_pop.pivot_table(index=["ADM2_CODE", "Geolocation", "Attribute"], columns="Year", values="Value", aggfunc='sum').reset_index()


    food_threshold_subsistence_pop.to_csv(f"{FINAL_DATA_DIRECTORY}/food_threshold_subsistence_pop.csv", index=False)

    return food_threshold_subsistence_pop                        
