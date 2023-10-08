import pandas as pd
import os
import wget

LANGUAGES_LIST = [
    "Adasen",
    "Agta",
    "Agta-Dumagat",
    "Agusan Manobo",
    "Agutaynen",
    "Akeanon",
    "Alangan",
    "Ata",
    "Ata-Manobo",
    "Ayangan Ifugao",
    "Ayta language group",
    "Bagobo/Tagabawa",
    "Balangao",
    "Baliwon/Ga'dang",
    "Banao",
    "Bantoanon",
    "Belwang (N.Bontok dialect)",
    "Bikol",
    "Binongan",
    "Binukid",
    "Bisaya/Binisaya",
    "B'laan/Blaan language group",
    "Bontok",
    "Bugkalot/Ilongot",
    "Buhid",
    "Cagayanen",
    "Capizeño",
    "Cebuano",
    "Chavacano",
    "Cuyonon/Cuyonen",
    "Davaweño",
    "Dibabawon",
    "Dumagat/Remontado",
    "English",
    "Gaddang",
    "Giangan",
    "Hanunuo",
    "Higaonon",
    "Hiligaynon Ilonggo",
    "Ibaloi/Ibaloy",
    "Ibanag",
    "Ibatan",
    "Ilianen Manobo",
    "Ilocano",
    "Iranun",
    "Iraya",
    "Isinai",
    "Isnag",
    "Itawis",
    "Ivatan",
    "Iwak/Iowak/Owak/I-wak",
    "Jama Mapun",
    "Kalagan",
    "Kalanguya",
    "Kalibugan/Kolibugan",
    "Kalinga language group",
    "Kamiguin",
    "Kankanaey",
    "Kapampangan",
    "Karao",
    "Karay-a",
    "Kirenteken",
    "Mabaka",
    "Maeng",
    "Maguindanao",
    "Majokayong",
    "Mamanwa",
    "Mandaya",
    "Manobo",
    "Manobo-Cotabato",
    "Mansaka",
    "Maranao",
    "Masadiit",
    "Masbateño/Masbatenon",
    "Matigsalog/Matigsalug",
    "Molbog",
    "Muyadan",
    "Obo Manobo",
    "Unspecified Sama language",
    "Palawani",
    "Palawano language group",
    "Pangasinan/Panggalato",
    "Paranan",
    "Romblomanon",
    "Sama Bangingi",
    "Sama Laut",
    "Sangil",
    "Subanen/Subanon/Subanun",
    "Surigaonon",
    "Tadyawan",
    "Tagakaulo",
    "Tagalog",
    "Tagbanua",
    "Tagbanua Calamian",
    "Tau-buid",
    "Tausug",
    "Tboli",
    "Teduray",
    "Tuwali",
    "Waray",
    "Yakan",
    "Yogad",
    "Zambal",
    "Other languages"
]

RAW_DATA_DIRECTORY = "raw/demographics"
FINAL_DATA_DIRECTORY = "final/demographics"

def n_largest_prct(agg,n):
    # display(agg)
    return agg["percent_share"].nlargest(n).iloc[-1]

def n_largest_lang(agg,n):
    # print(agg["percent_share"].nlargest(n).iloc[-1])
    # print(agg[ agg["percent_share"] == agg["percent_share"].nlargest(n).iloc[-1] ] )
    return agg[ agg["percent_share"] == agg["percent_share"].nlargest(n).iloc[-1] ]["Language"].values[0]

def get(location_data):
    if not os.path.exists(f"{RAW_DATA_DIRECTORY}/ph_lang_admin2_v01.csv"):
        url = "https://data.humdata.org/dataset/4383caa9-b4e0-4608-80f6-2b74482fe8bd/resource/fb35553c-e3bc-4044-9729-8351ad4650f5/download/ph_lang_admin2_v01.csv"
        print(f"Downloading url {url}")
        wget.download(url, out=f"{os.getcwd()}/{RAW_DATA_DIRECTORY}")

    languages = pd.read_csv(f"{RAW_DATA_DIRECTORY}/ph_lang_admin2_v01.csv",encoding='latin-1', skiprows=[1])
    languages_unpivot = pd.melt(languages, id_vars = ["admin2_name","admin2_pcode"], value_vars = LANGUAGES_LIST, var_name="Language", value_name="percent_share")
    

    languages_top = languages_unpivot.groupby(["admin2_name","admin2_pcode"]).apply(lambda agg: pd.Series({
        ("primary_language"):n_largest_lang(agg,1),
        ("primary_language_share"):n_largest_prct(agg,1),
        ("secondary_language"):n_largest_lang(agg,2),
        ("secondary_language_share"):n_largest_prct(agg,2),
        ("tertiary_language"):n_largest_lang(agg,3),
        ("tertiary_language_share"):n_largest_prct(agg,3),
    })).reset_index()

    languages_combined = languages_top\
                        .merge(languages[["admin2_name","literacy_all","literacy_male","literacy_female"]], on="admin2_name", how="left")\
                        .drop("admin2_pcode", axis=1)
    languages_combined = languages_combined.melt(id_vars=["admin2_name"], var_name="Attribute", value_name="Value")
    
    languages_unpivot["Attribute"] = languages_unpivot["Language"] + "_Lang_Percent_Share"
    languages_unpivot.drop(["admin2_pcode","Language"], axis=1, inplace=True)
    languages_unpivot.rename(columns={"percent_share":"Value"}, inplace=True)

    language = pd.concat([languages_unpivot, languages_combined])
    language.to_csv(f'{FINAL_DATA_DIRECTORY}/languages.csv', index=False)
    return language
