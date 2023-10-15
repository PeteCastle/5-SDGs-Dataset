DROP TABLE IF EXISTS location;
CREATE TABLE IF NOT EXISTS location (
        pcode TEXT PRIMARY KEY,
        name TEXT,
        hierarchy TEXT,
        parent_pcode TEXT
);

WITH AD3_UNIQUE AS (
        SELECT ADM3_PCODE AS pcode,
            ADM3_EN AS name,
            ADM2_PCODE AS parent_pcode
        FROM stg_location
        GROUP BY ADM3_PCODE, ADM3_EN
    ),
    AD2_UNIQUE AS (
        SELECT ADM2_PCODE AS pcode,
            ADM2_EN AS name,
            ADM1_PCODE AS parent_pcode
        FROM stg_location
        GROUP BY ADM2_PCODE, ADM2_EN
    ),
    AD1_UNIQUE AS (
        SELECT ADM1_PCODE AS pcode,
            ADM1_EN AS name,
            "PH" AS parent_pcode
        FROM stg_location
        GROUP BY ADM1_PCODE, ADM1_EN
    )
        
INSERT INTO location(pcode, name, hierarchy, parent_pcode)
SELECT ADM4_PCODE AS pcode,
    ADM4_EN AS name,
    "ASM4" AS hierarchy,
    ADM3_PCODE AS parent_pcode
FROM stg_location
UNION ALL
SELECT *, 
        "ADM3" AS hierarchy
FROM AD3_UNIQUE
UNION ALL
SELECT *, 
        "ADM2" AS hierarchy
FROM AD2_UNIQUE
UNION ALL
SELECT *, 
        "ADM1" AS hierarchy
FROM AD1_UNIQUE
UNION ALL
SELECT "PH" AS pcode,
    "Philippines" AS name,
    "PH" AS hierarchy,
    NULL AS parent_pcode