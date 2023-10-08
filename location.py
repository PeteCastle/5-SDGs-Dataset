import pandas as pd
import os
import wget

RAW_LOCATION_DIRECTORY = "raw/locations"
FINAL_LOCATION_DIRECTORY = "final/locations"
LOCATION_URL = "https://data.humdata.org/dataset/caf116df-f984-4deb-85ca-41b349d3f313/resource/e74fd350-3728-427f-8b4c-0589dc563c87/download/phl_admgz_adm01234.xlsx"


def get() -> pd.DataFrame:
    if not os.path.exists(f"{RAW_LOCATION_DIRECTORY}/phl_admgz_adm01234.xlsx"):
        print(f"Downloading url {LOCATION_URL}")
        wget.download(LOCATION_URL, out=f"{os.getcwd()}/{RAW_LOCATION_DIRECTORY}")

    location_data = pd.read_excel(f"{RAW_LOCATION_DIRECTORY}/phl_admgz_adm01234.xlsx")
    location_data = location_data[["ADM4_PCODE","ADM3_PCODE","ADM2_PCODE","ADM1_PCODE","ADM4_EN","ADM3_EN","ADM2_EN","ADM1_EN","ADM0_PCODE","ADM0_EN"]]
    location_data.to_csv('final/location.csv', index=False)

    return location_data
