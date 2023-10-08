import pandas as pd
from fuzzywuzzy import process

RAW_DATA_DIRECTORY = "raw/demographics"
FINAL_DATA_DIRECTORY = "final/demographics"
# location_data = pd.DataFrame()
def getRegionalId(row,location_data):
       # inconsistent data cases:
       if "MIMAROPA" in row:
              row = "Region IV-B"
       elif "National Capital Region (NCR)" in row or "National Capital Region" in row:
              return "PH133900000,PH137400000,PH137500000,PH137600000"

       key, _ = process.extractOne(row, location_data["ADM1_EN"].unique())
       return location_data.loc[location_data["ADM1_EN"] == key]["ADM1_PCODE"].values[0]

def get(location_data):

       grdp = pd.read_csv(f"{RAW_DATA_DIRECTORY}/2B5CPGD1.csv", skiprows=[0,1], sep=";")
       grdp["ADM2_PCODE"] = grdp["Region"].apply(getRegionalId,location_data=location_data)

       grdp["ADM2_PCODE"] = grdp["ADM2_PCODE"].str.split(",")
       grdp = grdp.explode("ADM2_PCODE").drop("Region", axis=1)
       grdp = grdp.melt(id_vars=["ADM2_PCODE"], var_name="Attribute Year", value_name="Value")
       grdp["Year"] = grdp["Attribute Year"].str.split(" ").str[-1]
       grdp["Attribute"] = "GRDP " + grdp["Attribute Year"].str.split(" ").str[:-1].str.join(" ")
       grdp = grdp.drop("Attribute Year", axis=1)
       grdp = grdp.pivot_table(index=["ADM2_PCODE", "Attribute"], columns="Year", values="Value").reset_index()
       # display(grdp)
       grdp.to_csv(f'{FINAL_DATA_DIRECTORY}/grdp.csv', index=False)
       return grdp
    # display(grdp.head(5))