DROP TABLE IF EXISTS economic_farmer_wage;

CREATE TABLE IF NOT EXISTS economic_farmer_wage (
    pcode TEXT,
    AttributeID INTEGER NOT NULL,
    "1994" REAL, "1995" REAL, "1996" REAL, "1997" REAL, "1998" REAL, "1999" REAL, "2000" REAL, "2001" REAL, "2002" REAL, "2003" REAL, "2004" REAL, "2005" REAL, "2006" REAL, "2007" REAL, "2008" REAL, "2009" REAL, "2010" REAL, "2011" REAL, "2012" REAL, "2013" REAL, "2014" REAL, "2015" REAL, "2016" REAL, "2017" REAL, "2018" REAL, "2019" REAL,
    FOREIGN KEY(pcode) REFERENCES location(pcode),
    FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
);

WITH concatenated AS (
        SELECT
            *,
            stg_economic_farmer_wage."Type of Wages" || " of " || stg_economic_farmer_wage."Gender" || " " || stg_economic_farmer_wage."Gender" || stg_economic_farmer_wage."Type of Farm Workers"  AS "Indicator Name"
        FROM stg_economic_farmer_wage
    )   
            
    INSERT INTO economic_farmer_wage(pcode, AttributeID, "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019")
    SELECT
        concatenated.ADM1_CODE,
        AttributeDIM."AttributeID",
        "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"
    FROM concatenated
    LEFT JOIN AttributeDIM
    ON concatenated."Indicator Name" = AttributeDIM.AttributeDesc
