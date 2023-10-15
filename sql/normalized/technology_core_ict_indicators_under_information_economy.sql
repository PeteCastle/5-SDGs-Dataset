DROP TABLE IF EXISTS technology_core_ict_indicators_under_information_economy;

CREATE TABLE IF NOT EXISTS technology_core_ict_indicators_under_information_economy (
        pcode TEXT,
        AttributeID INTEGER NOT NULL,
        "2010",
        "2013",
        "2015",
        "2017",
        FOREIGN KEY(pcode) REFERENCES location(pcode),
        FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
    );

INSERT INTO technology_core_ict_indicators_under_information_economy(pcode, AttributeID,"2010", "2013", "2015", "2017")
    SELECT
        ADM1_CODE as pcode,
        AttributeDIM."AttributeID",
        "2010",
        "2013",
        "2015",
        "2017"
    FROM stg_technology_core_ict_indicators_under_information_economy
    LEFT JOIN AttributeDIM
    ON stg_technology_core_ict_indicators_under_information_economy."Industry Description" = AttributeDIM.Industry
        AND stg_technology_core_ict_indicators_under_information_economy."Metric" = AttributeDIM.AttributeDesc