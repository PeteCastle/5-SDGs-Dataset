DROP TABLE IF EXISTS poverty_magnitude_poor_pop;

CREATE TABLE IF NOT EXISTS poverty_magnitude_poor_pop (
        pcode TEXT,
        AttributeID INTEGER NOT NULL,
        "2015",
        "2018",
        "2021p",
        FOREIGN KEY(pcode) REFERENCES location(pcode),
        FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
    );

INSERT INTO poverty_magnitude_poor_pop(pcode, AttributeID, "2015", "2018", "2021p")
    SELECT
        "ADM2_CODE" as pcode,
        (SELECT AttributeID FROM AttributeDIM WHERE AttributeDesc = 'Magnitude of Poor'),
        "2015",
        "2018",
        "2021p"
    FROM stg_poverty_magnitude_poor_pop;