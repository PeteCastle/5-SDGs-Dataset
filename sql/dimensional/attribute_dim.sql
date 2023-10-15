CREATE TABLE IF NOT EXISTS AttributeDIM (
        AttributeID INTEGER PRIMARY KEY,
        AttributeDesc TEXT,
        Industry TEXT,
        UNIQUE(Industry, AttributeDesc)
    );

INSERT INTO AttributeDIM(AttributeDesc)
SELECT DISTINCT "Commodity Description" FROM stg_demographics_cpi;

INSERT INTO AttributeDIM(AttributeDesc)
SELECT DISTINCT "Attribute" FROM stg_demographics_grdp;

INSERT INTO AttributeDIM(AttributeDesc)
SELECT DISTINCT "Attribute" FROM stg_demographics_languages;

INSERT INTO AttributeDIM(AttributeDesc)
VALUES('Population');

INSERT INTO AttributeDIM(AttributeDesc)
SELECT DISTINCT "Attribute" FROM stg_demographics_transportation;

INSERT INTO AttributeDIM(AttributeDesc)
SELECT DISTINCT "Indicator" FROM stg_drrm_drr_implementation ;

INSERT INTO AttributeDIM(AttributeDesc)
SELECT DISTINCT "Indicator" FROM stg_drrm_evacuation_center;

INSERT INTO AttributeDIM(AttributeDesc)
SELECT DISTINCT "Indicator" FROM stg_drrm_vulnerable_groups;

INSERT INTO AttributeDIM(AttributeDesc)
SELECT DISTINCT "Indicator" FROM stg_drrm_vulnerable_groups;

INSERT INTO AttributeDIM(AttributeDesc)
SELECT DISTINCT "Indicator Name" FROM stg_economic_all_indicators;

WITH concatenated AS (
        SELECT
            stg_economic_farmer_wage."Type of Wages" || " of " || stg_economic_farmer_wage."Gender" || " " || stg_economic_farmer_wage."Gender" || stg_economic_farmer_wage."Type of Farm Workers"  AS "Indicator Name"
        FROM stg_economic_farmer_wage
    )   
INSERT INTO AttributeDIM(AttributeDesc)
SELECT DISTINCT "Indicator Name" FROM concatenated;

INSERT INTO AttributeDIM(AttributeDesc)
SELECT DISTINCT "Indicator Name" FROM stg_economic_external_debt;

INSERT OR IGNORE INTO AttributeDIM(AttributeDesc)
VALUES("Food Threshold Subsistence");

INSERT OR IGNORE INTO AttributeDIM(AttributeDesc)
VALUES('Income Gap');

INSERT OR IGNORE INTO AttributeDIM(AttributeDesc)
VALUES('Magnitude of Poor');

INSERT OR IGNORE INTO AttributeDIM(AttributeDesc)
VALUES('Magnitude of Subsistence Poor');

INSERT OR IGNORE INTO AttributeDIM(AttributeDesc)
VALUES('Poverty Incidence Threshold');

INSERT OR IGNORE INTO AttributeDIM(AttributeDesc)
VALUES('Poverty Severity');

INSERT INTO AttributeDIM(Industry,AttributeDesc)
SELECT DISTINCT "Industry Description", "Metric" FROM stg_technology_core_ict_indicators_under_bpm;

INSERT OR IGNORE INTO AttributeDIM(Industry,AttributeDesc)
SELECT DISTINCT "Industry Description", "Metric" FROM stg_technology_core_ict_indicators_under_information_economy;
