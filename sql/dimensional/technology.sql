DROP TABLE IF EXISTS technology;

CREATE TABLE IF NOT EXISTS technology (
        id INTEGER PRIMARY KEY,
        pcode TEXT,
        AttributeID INTEGER NOT NULL,
        DomainID INTEGER NOT NULL,
        "2010",
        "2013",
        "2015",
        "2017",
        FOREIGN KEY(pcode) REFERENCES location(pcode),
        FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
        FOREIGN KEY(DomainID) REFERENCES DomainDim(DomainID)
    );

INSERT INTO technology(pcode, AttributeID, "2013", "2015", "2017", DomainID)
    SELECT pcode,
        AttributeID, "2013", "2015", "2017",
        (SELECT DomainID FROM DomainDim WHERE DomainDesc = 'Business Process Management')
    FROM technology_core_ict_indicators_under_bpm;

INSERT INTO technology(pcode, AttributeID, "2010", "2013", "2015", "2017", DomainID)
    SELECT pcode,
        AttributeID, "2010", "2013", "2015", "2017",
        (SELECT DomainID FROM DomainDim WHERE DomainDesc = 'Information Economy')
    FROM technology_core_ict_indicators_under_information_economy;

    