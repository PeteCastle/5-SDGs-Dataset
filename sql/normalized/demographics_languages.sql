DROP TABLE IF EXISTS demographics_languages;
CREATE TABLE IF NOT EXISTS demographics_languages (
        pcode TEXT,
        "2010" REAL,
        AttributeID INTEGER NOT NULL,
        FOREIGN KEY(pcode) REFERENCES location(pcode),
        FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
    );
    
WITH languages_only AS (
    SELECT admin2_name AS pcode,
        "Value",
        "Attribute"
    FROM stg_demographics_languages
    WHERE "Attribute" IN (
        "primary_language","secondary_language","tertiary_language"
    )
), language_metrics AS (
    SELECT admin2_name AS pcode,
        "Value",
        "Attribute"
    FROM stg_demographics_languages
    WHERE "Attribute" NOT IN (
        "primary_language","secondary_language","tertiary_language"
    )
)
INSERT INTO demographics_languages(pcode, "2010", AttributeID)    
SELECT
    pcode,
    languages_list.languageId AS "Value",
    AttributeDIM."AttributeID"
FROM languages_only
LEFT JOIN languages_list
ON languages_only."Value" = languages_list.languageName
LEFT JOIN AttributeDIM
ON languages_only."Attribute" = AttributeDIM.AttributeDesc
UNION ALL
SELECT
    pcode,
    Value,
    AttributeDIM."AttributeID"
FROM language_metrics
LEFT JOIN AttributeDIM
ON language_metrics."Attribute" = AttributeDIM.AttributeDesc