DROP TABLE IF EXISTS poverty_income_gap;

CREATE TABLE IF NOT EXISTS poverty_income_gap (
        pcode TEXT,
        AttributeID INTEGER NOT NULL,
        "2015",
        "2018",
        "2021p",
        FOREIGN KEY(pcode) REFERENCES location(pcode),
        FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
    );

INSERT INTO poverty_income_gap(pcode, AttributeID, "2015", "2018", "2021p")
    SELECT
        "ADM2_CODE" as pcode,
        (SELECT AttributeID FROM AttributeDIM WHERE AttributeDesc = 'Income Gap'),
        "2015",
        "2018",
        "2021p"
    FROM stg_poverty_income_gap;