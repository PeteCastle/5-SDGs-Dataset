DROP TABLE IF EXISTS poverty_poverty_severity;

CREATE TABLE IF NOT EXISTS poverty_poverty_severity (
        pcode TEXT,
        AttributeID INTEGER NOT NULL,
        "2015",
        "2018",
        "2021p",
        FOREIGN KEY(pcode) REFERENCES location(pcode),
        FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
    );
    
INSERT INTO poverty_poverty_severity(pcode, AttributeID, "2015", "2018", "2021p")
    SELECT
        "ADM2_CODE" as pcode,
        (SELECT AttributeID FROM AttributeDIM WHERE AttributeDesc = 'Poverty Severity'),
        "Poverty Severity 2015",
        "Poverty Severity 2018",
        "Poverty Severity 2021p"
    FROM stg_poverty_severity_poverty;