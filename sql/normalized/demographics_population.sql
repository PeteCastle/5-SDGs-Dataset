DROP TABLE IF EXISTS demographics_population;

CREATE TABLE IF NOT EXISTS demographics_population (
        pcode TEXT,
        "2020" REAL,
        AttributeID INTEGER NOT NULL,
        FOREIGN KEY(pcode) REFERENCES location(pcode),
        FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
    );

INSERT INTO demographics_population(pcode, "2020", AttributeID)
    SELECT
        brgy_code,
        "2020 Population",
        (SELECT AttributeID FROM AttributeDIM WHERE AttributeDesc = 'Population')
    FROM stg_demographics_population