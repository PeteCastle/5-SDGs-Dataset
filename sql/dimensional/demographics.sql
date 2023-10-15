DROP TABLE IF EXISTS demographics;

CREATE TABLE IF NOT EXISTS demographics (
        id INTEGER PRIMARY KEY,
        pcode TEXT,
        AttributeID INTEGER NOT NULL,
        DomainID INTEGER NOT NULL,
        "2000" REAL, "2001" REAL, "2002" REAL, "2003" REAL, "2004" REAL, "2005" REAL, "2006" REAL, "2007" REAL, "2008" REAL, "2009" REAL, "2010" REAL, "2011" REAL, "2012" REAL, "2013" REAL, "2014" REAL, "2015" REAL, "2016" REAL, "2017" REAL, "2018" REAL, "2019" REAL, "2020" REAL, "2021" REAL, "2022" REAL,
        FOREIGN KEY(pcode) REFERENCES location(pcode),
        FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
        FOREIGN KEY(DomainID) REFERENCES DomainDim(DomainID)
    );

INSERT INTO demographics(pcode, AttributeID,"2018", "2019", "2020", "2021", "2022", DomainID)
    SELECT pcode, 
            AttributeID, 
            "2018", 
            "2019", 
            "2020", 
            "2021", 
            "2022",
            (SELECT DomainID FROM DomainDim WHERE DomainDesc = 'Consumer Price Index') AS DomainID
    FROM demographics_cpi;

INSERT INTO demographics(pcode, AttributeID, "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", DomainID)
    SELECT pcode,
            AttributeID, "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022",
            (SELECT DomainID FROM DomainDim WHERE DomainDesc = 'Gross Regional Domestic Product')
    FROM demographics_grdp;

INSERT INTO demographics(pcode, AttributeID,"2010", DomainID)
    SELECT pcode,
        AttributeID, "2010",
        (SELECT DomainID FROM DomainDim WHERE DomainDesc = 'Languages')
    FROM demographics_languages;

INSERT INTO demographics(pcode, AttributeID,"2020", DomainID)
    SELECT pcode,
        AttributeID, "2020",
        (SELECT DomainID FROM DomainDim WHERE DomainDesc = 'Population')
    FROM demographics_population;

INSERT INTO demographics(pcode, AttributeID,"2019", DomainID)
    SELECT pcode,
        AttributeID, "2019",
        (SELECT DomainID FROM DomainDim WHERE DomainDesc = 'Transportation')
    FROM demographics_transportation;