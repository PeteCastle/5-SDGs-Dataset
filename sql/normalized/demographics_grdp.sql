DROP TABLE IF EXISTS demographics_grdp;

CREATE TABLE IF NOT EXISTS demographics_grdp (
        pcode TEXT,
        AttributeID INTEGER,
        "2000" REAL, "2001" REAL, "2002" REAL, "2003" REAL, "2004" REAL, "2005" REAL, "2006" REAL, "2007" REAL, "2008" REAL, "2009" REAL, "2010" REAL, "2011" REAL, "2012" REAL, "2013" REAL, "2014" REAL, "2015" REAL, "2016" REAL, "2017" REAL, "2018" REAL, "2019" REAL, "2020" REAL, "2021" REAL, "2022" REAL,
        FOREIGN KEY(pcode) REFERENCES location(pcode),
        FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
    );

INSERT INTO demographics_grdp(pcode, AttributeID, "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022")
    SELECT stg_demographics_grdp.ADM2_PCODE,
        AttributeDIM."AttributeID",
        stg_demographics_grdp."2000", stg_demographics_grdp."2001", stg_demographics_grdp."2002", stg_demographics_grdp."2003", stg_demographics_grdp."2004", stg_demographics_grdp."2005", stg_demographics_grdp."2006", stg_demographics_grdp."2007", stg_demographics_grdp."2008", stg_demographics_grdp."2009", stg_demographics_grdp."2010", stg_demographics_grdp."2011", stg_demographics_grdp."2012", stg_demographics_grdp."2013", stg_demographics_grdp."2014", stg_demographics_grdp."2015", stg_demographics_grdp."2016", stg_demographics_grdp."2017", stg_demographics_grdp."2018", stg_demographics_grdp."2019", stg_demographics_grdp."2020", stg_demographics_grdp."2021", stg_demographics_grdp."2022"
    FROM stg_demographics_grdp
    LEFT JOIN AttributeDIM
    ON stg_demographics_grdp."Attribute" = AttributeDIM.AttributeDesc
