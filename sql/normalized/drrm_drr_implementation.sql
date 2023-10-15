DROP TABLE IF EXISTS drrm_drr_implementation;

CREATE TABLE IF NOT EXISTS drrm_drr_implementation (
        pcode TEXT,
        AttributeID INTEGER NOT NULL,
        "2016",
        "2017",
        "2018",
        "2019",
        "2020",
        "2021",
        FOREIGN KEY(pcode) REFERENCES location(pcode),
        FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
    );

INSERT INTO drrm_drr_implementation(pcode, AttributeID, "2016", "2017", "2018", "2019", "2020", "2021")
    SELECT
        "ADM1_PCODE" as pcode,
        AttributeDIM."AttributeID",
        "2016",
        "2017",
        "2018",
        "2019",
        "2020",
        "2021"
    FROM stg_drrm_drr_implementation
    LEFT JOIN AttributeDIM
    ON stg_drrm_drr_implementation."Indicator" = AttributeDIM.AttributeDesc