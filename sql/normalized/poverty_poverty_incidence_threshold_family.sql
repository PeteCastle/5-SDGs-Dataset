DROP TABLE IF EXISTS poverty_poverty_incidence_threshold_family;

CREATE TABLE IF NOT EXISTS poverty_poverty_incidence_threshold_family (
        pcode TEXT,
        AttributeID INTEGER NOT NULL,
        "2015",
        "2018",
        "2021p",
        FOREIGN KEY(pcode) REFERENCES location(pcode),
        FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
    );

INSERT INTO poverty_poverty_incidence_threshold_family(pcode, AttributeID, "2015", "2018", "2021p")
    SELECT
        "ADM2_CODE" as pcode,
        (SELECT AttributeID FROM AttributeDIM WHERE AttributeDesc = 'Poverty Incidence Threshold'),
        "2015",
        "2018",
        "2021p"
    FROM stg_poverty_poverty_incidence_threshold_family
