DROP TABLE IF EXISTS economic_external_debt;

CREATE TABLE IF NOT EXISTS economic_external_debt (
        pcode TEXT,
        AttributeID INTEGER NOT NULL,
        "1960" REAL, "1961" REAL, "1962" REAL, "1963" REAL, "1964" REAL, "1965" REAL, "1966" REAL, "1967" REAL, "1968" REAL, "1969" REAL, "1970" REAL, "1971" REAL, "1972" REAL, "1973" REAL, "1974" REAL, "1975" REAL, "1976" REAL, "1977" REAL, "1978" REAL, "1979" REAL, "1980" REAL, "1981" REAL, "1982" REAL, "1983" REAL, "1984" REAL, "1985" REAL, "1986" REAL, "1987" REAL, "1988" REAL, "1989" REAL, "1990" REAL, "1991" REAL, "1992" REAL, "1993" REAL, "1994" REAL, "1995" REAL, "1996" REAL, "1997" REAL, "1998" REAL, "1999" REAL, "2000" REAL, "2001" REAL, "2002" REAL, "2003" REAL, "2004" REAL, "2005" REAL, "2006" REAL, "2007" REAL, "2008" REAL, "2009" REAL, "2010" REAL, "2011" REAL, "2012" REAL, "2013" REAL, "2014" REAL, "2015" REAL, "2016" REAL, "2017" REAL, "2018" REAL, "2019" REAL, "2020" REAL, "2021" REAL, "2022" REAL,
        FOREIGN KEY(pcode) REFERENCES location(pcode),
        FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
    );

INSERT INTO economic_external_debt(pcode, AttributeID, "1960", "1961", "1962", "1963", "1964", "1965", "1966", "1967", "1968", "1969", "1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022")
    SELECT
        ADM0_PCODE as pcode,
        AttributeDIM."AttributeID",
        "1960", "1961", "1962", "1963", "1964", "1965", "1966", "1967", "1968", "1969", "1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"
    FROM stg_economic_external_debt
    LEFT JOIN AttributeDIM
    ON stg_economic_external_debt."Indicator Name" = AttributeDIM.AttributeDesc
