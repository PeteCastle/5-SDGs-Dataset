 CREATE TABLE IF NOT EXISTS demographics_cpi (
        pcode TEXT,
        AttributeID INTEGER,
        "2018" REAL,
        "2019" REAL,
        "2020" REAL,
        "2021" REAL,
        "2022" REAL,
        FOREIGN KEY(pcode) REFERENCES location(pcode),
        FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
    );

INSERT INTO demographics_cpi(pcode, AttributeID, "2018", "2019", "2020", "2021", "2022")
    SELECT stg_demographics_cpi.ADM2_PCODE,
        AttributeDIM."AttributeID",
        stg_demographics_cpi."2018",
        stg_demographics_cpi."2019",
        stg_demographics_cpi."2020",
        stg_demographics_cpi."2021",
        stg_demographics_cpi."2022"
    FROM stg_demographics_cpi
    LEFT JOIN AttributeDIM
    ON stg_demographics_cpi."Commodity Description" = AttributeDIM.AttributeDesc;

    