DROP TABLE IF EXISTS drrm_evacuation_center;

CREATE TABLE IF NOT EXISTS drrm_evacuation_center (
        pcode TEXT,
        AttributeID INTEGER NOT NULL,
        "2019",
        FOREIGN KEY(pcode) REFERENCES location(pcode),
        FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
);

INSERT INTO drrm_evacuation_center(pcode, AttributeID, "2019")
    SELECT
        "ADM3_PCODE" as pcode,
        AttributeDIM."AttributeID",
        "2019"
    FROM stg_drrm_evacuation_center
    LEFT JOIN AttributeDIM
    ON stg_drrm_evacuation_center."Indicator" = AttributeDIM.AttributeDesc
