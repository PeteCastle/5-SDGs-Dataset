DROP TABLE IF EXISTS drrm_vulnerable_groups;

CREATE TABLE IF NOT EXISTS drrm_vulnerable_groups (
        pcode TEXT,
        AttributeID INTEGER NOT NULL,
        "2018",
        FOREIGN KEY(pcode) REFERENCES location(pcode),
        FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
    );    

INSERT INTO drrm_vulnerable_groups(pcode, AttributeID, "2018")
    SELECT
        "ADM3_PCODE" as pcode,
        AttributeDIM."AttributeID",
        "2018"
    FROM stg_drrm_vulnerable_groups 
    LEFT JOIN AttributeDIM
    ON stg_drrm_vulnerable_groups."Indicator" = AttributeDIM.AttributeDesc