DROP TABLE IF EXISTS demographics_transportation;

CREATE TABLE IF NOT EXISTS demographics_transportation (
        pcode TEXT,
        AttributeID INTEGER NOT NULL,
        "2019",
        FOREIGN KEY(pcode) REFERENCES location(pcode),
        FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
    );

INSERT INTO demographics_transportation(pcode, AttributeID, "2019")
    SELECT
        stg_demographics_transportation.ADM1_PCODE,
        AttributeDIM."AttributeID",
        stg_demographics_transportation."2019"
    FROM stg_demographics_transportation
    LEFT JOIN AttributeDIM
    ON stg_demographics_transportation."Attribute" = AttributeDIM.AttributeDesc