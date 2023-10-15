DROP TABLE IF EXISTS technology_core_ict_indicators_under_bpm;

CREATE TABLE IF NOT EXISTS technology_core_ict_indicators_under_bpm (
        pcode TEXT,
        AttributeID INTEGER NOT NULL,
        "2013",
        "2015",
        "2017",
        FOREIGN KEY(pcode) REFERENCES location(pcode),
        FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
    );

INSERT INTO technology_core_ict_indicators_under_bpm(pcode, AttributeID, "2013", "2015", "2017")
    SELECT
        ADM1_CODE as pcode,
        AttributeDIM."AttributeID",
        "2013",
        "2015",
        "2017"
            
    FROM stg_technology_core_ict_indicators_under_bpm   
    LEFT JOIN AttributeDIM
    ON stg_technology_core_ict_indicators_under_bpm."Industry Description" = AttributeDIM.Industry
        AND stg_technology_core_ict_indicators_under_bpm."Metric" = AttributeDIM.AttributeDesc
        