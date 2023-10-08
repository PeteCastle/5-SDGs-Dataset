import pandas as pd
import re

from poverty.mappings import PROVINCIAL_MAPPINGS

RAW_DATA_DIRECTORY = "raw/poverty"
FINAL_DATA_DIRECTORY = "final/poverty"

def get():
    poverty_incidence_threshold_pop = pd.read_csv(f"{RAW_DATA_DIRECTORY}/poverty_incidence_threshold_pop.csv", skiprows=2, sep=";")

    poverty_incidence_threshold_pop["Geolocation"] = poverty_incidence_threshold_pop["Geolocation"].str\
                            .replace(r'^\.+', "", regex=True)\
                            .replace(r',', "", regex=True)\
                            .replace(r'(\w|\d)/', "", regex=True)\
                            .str.strip()

    poverty_incidence_threshold_pop["ADM2_CODE"] = poverty_incidence_threshold_pop["Geolocation"].apply(lambda x: PROVINCIAL_MAPPINGS[x])


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
            "Annual Per Capita Poverty Threshold (in PhP) 2015":"Poverty Threshold 2015",
            "Annual Per Capita Poverty Threshold (in PhP) 2018":"Poverty Threshold 2018",
            "Annual Per Capita Poverty Threshold (in PhP) 2021p":"Poverty Threshold 2021p",
            "Poverty Incidence among Population (%) 2015":"Poverty Incidence 2015",
            "Poverty Incidence among Population (%) 2018":"Poverty Incidence 2018",
            "Poverty Incidence among Population (%) 2021p":"Poverty Incidence 2021p",
    }

    poverty_incidence_threshold_pop = poverty_incidence_threshold_pop.drop(columns=irrelevant_columns)\
                                                    .rename(columns=rename_columns)
    
    poverty_incidence_threshold_pop = poverty_incidence_threshold_pop.melt(id_vars=["ADM2_CODE", "Geolocation"], var_name="Attribute Year", value_name="Value")
    poverty_incidence_threshold_pop["Year"] = poverty_incidence_threshold_pop["Attribute Year"].str.split(" ").str[-1]
    poverty_incidence_threshold_pop["Attribute"] = poverty_incidence_threshold_pop["Attribute Year"].str.split(" ").str[:-1].str.join(" ")
    del poverty_incidence_threshold_pop["Attribute Year"]
    poverty_incidence_threshold_pop = poverty_incidence_threshold_pop.pivot_table(index=["ADM2_CODE", "Geolocation", "Attribute"], columns="Year", values="Value", aggfunc='sum').reset_index()


    poverty_incidence_threshold_pop.to_csv(f"{FINAL_DATA_DIRECTORY}/poverty_incidence_threshold_pop.csv", index=False)
    return poverty_incidence_threshold_pop                      
