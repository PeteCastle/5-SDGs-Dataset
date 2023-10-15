DROP TABLE IF EXISTS poverty_food_threshold_subsistence_family;

CREATE TABLE IF NOT EXISTS poverty_food_threshold_subsistence_family (
        pcode TEXT,
        AttributeID INTEGER NOT NULL,
        "2015",
        "2018",
        "2021p",
        FOREIGN KEY(pcode) REFERENCES location(pcode),
        FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
    );

INSERT INTO poverty_food_threshold_subsistence_family(pcode, AttributeID, "2015", "2018", "2021p")
    SELECT
        "ADM2_CODE" as pcode,
        (SELECT AttributeID FROM AttributeDIM WHERE AttributeDesc = 'Food Threshold Subsistence') AS AttributeID,
        "2015",
        "2018",
        "2021p"
    FROM stg_poverty_food_threshold_subsistence_family    
