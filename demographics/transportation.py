
from .grdp import getRegionalId
import numpy as np
import pandas as pd

TRANSPO_REGION_MAPPINGS = {
    "Autonomous Region in Muslim Mindanao":"BARMM",
    "Eastern Visayas":"Region VIII",
    "Ilocos Region":"Region I",
    "Cagayan Valley":"Region II",
    "Central Luzon":"Region III",
    "National Capital Region":"National Capital Region",
    "CALABARZON":"Region IV-A",
    "MIMAROPA Region":"Region IV-B",
    "Bicol Region":"Region V",
    "Western Visayas":"Region VI",
    "Central Visayas":"Region VII",
    "Zamboanga Peninsula":"Region IX",
    "Northern Mindanao":"Region X",
    "Davao Region":"Region XI",
    "SOCCSKSARGEN":"Region XII",
    "Caraga":"Region XIII",
    "Cordillera Administrative Region":"Cordillera Administrative Region (CAR) ",
}

RAW_DATA_DIRECTORY = "raw/demographics"
FINAL_DATA_DIRECTORY = "final/demographics"

def get():
    transpo = pd.read_csv(f"{RAW_DATA_DIRECTORY}/2D4BAH00.csv", skiprows=[0,1])

    transpo["adm_level"] = transpo["Geolocation"].apply(lambda x: x.count('.'))
    transpo["indu_hierarchy"] = transpo["Industry Description"].apply(lambda x: x.count('.'))
    transpo = transpo[((transpo["adm_level"] == 2) & (transpo["indu_hierarchy"] == 2)) | (transpo["Geolocation"] == "..National Capital Region (NCR)")]
    transpo = transpo[["Geolocation","Industry Description","2019 Number of Establishments"]]

    transpo["Geolocation"] = transpo["Geolocation"].str.replace(".","", regex=False)
    transpo["Industry Description"] = transpo["Industry Description"].str.replace(".","", regex=False)
    transpo["2019 Number of Establishments"] = transpo["2019 Number of Establishments"].replace(r"s|c", np.nan, regex=True).astype(float)

    transpo_unpivot = transpo.pivot(index = ["Geolocation"], columns = "Industry Description", values="2019 Number of Establishments").reset_index()

    transpo_unpivot["region_id"] = transpo_unpivot["Geolocation"].map(TRANSPO_REGION_MAPPINGS).apply(getRegionalId)
    transpo_unpivot = transpo_unpivot[[
                                "region_id",
                                "Inland water transport",
                                "Passenger air transport",
                                "Sea and coastal water transport",
                                "Transport via buses",
                                "Transport via railways"]]

    transpo_unpivot.rename(
        {"Inland water transport":"regional_inland_water_transport_count",
        "Passenger air transport":"regional_air_transport_count",
        "Sea and coastal water transport":"regional_coastal_water_transport_count",
        "Transport via buses":"regional_bus_transport_count",
        "Transport via railways":"regional_railway_transport_count"},
        axis=1, inplace=True
    )

    transpo_unpivot["region_id"] = transpo_unpivot["region_id"].str.split(",")
    transpo_unpivot = transpo_unpivot.explode("region_id")

    transpo_unpivot.to_csv(f'{FINAL_DATA_DIRECTORY}/transpo_unpivot.csv', index=False)
    return transpo_unpivot