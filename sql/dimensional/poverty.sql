DROP TABLE IF EXISTS poverty;

CREATE TABLE IF NOT EXISTS poverty (
        id INTEGER PRIMARY KEY,
        pcode TEXT,
        AttributeID INTEGER NOT NULL,
        DomainID INTEGER NOT NULL,
        "2015" REAL,
        "2018" REAL,
        "2021p" REAL,
        FOREIGN KEY(pcode) REFERENCES location(pcode),
        FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
        FOREIGN KEY(DomainID) REFERENCES DomainDim(DomainID)
);

INSERT INTO poverty(pcode, AttributeID, "2015", "2018", "2021p", DomainID)
    SELECT pcode,
        AttributeID, "2015", "2018", "2021p",
        (SELECT DomainID FROM DomainDim WHERE DomainDesc = 'Family')
    FROM poverty_food_threshold_subsistence_family;

INSERT INTO poverty(pcode, AttributeID, "2015", "2018", "2021p", DomainID)
    SELECT pcode,
        AttributeID, "2015", "2018", "2021p",
        (SELECT DomainID FROM DomainDim WHERE DomainDesc = 'Population')
    FROM poverty_food_threshold_subsistence_pop;

INSERT INTO poverty(pcode, AttributeID, "2015", "2018", "2021p", DomainID)
    SELECT pcode,
        AttributeID, "2015", "2018", "2021p",
        (SELECT DomainID FROM DomainDim WHERE DomainDesc = 'All')
    FROM poverty_income_gap;

INSERT INTO poverty(pcode, AttributeID, "2015", "2018", "2021p", DomainID)
    SELECT pcode,
        AttributeID, "2015", "2018", "2021p",
        (SELECT DomainID FROM DomainDim WHERE DomainDesc = 'Family')
    FROM poverty_magnitude_poor_family;

INSERT INTO poverty(pcode, AttributeID, "2015", "2018", "2021p", DomainID)
    SELECT pcode,
        AttributeID, "2015", "2018", "2021p",
        (SELECT DomainID FROM DomainDim WHERE DomainDesc = 'Population')
    FROM poverty_magnitude_poor_pop;

INSERT INTO poverty(pcode, AttributeID, "2015", "2018", "2021p", DomainID)
    SELECT pcode,
        AttributeID, "2015", "2018", "2021p",
        (SELECT DomainID FROM DomainDim WHERE DomainDesc = 'Family')
    FROM poverty_magnitude_subsistence_poor_family;

INSERT INTO poverty(pcode, AttributeID, "2015", "2018", "2021p", DomainID)
    SELECT pcode,
        AttributeID, "2015", "2018", "2021p",
        (SELECT DomainID FROM DomainDim WHERE DomainDesc = 'Population')
    FROM poverty_magnitude_subsistence_poor_pop;

INSERT INTO poverty(pcode, AttributeID, "2015", "2018", "2021p", DomainID)
    SELECT pcode,
        AttributeID, "2015", "2018", "2021p",
        (SELECT DomainID FROM DomainDim WHERE DomainDesc = 'Family')
    FROM poverty_poverty_incidence_threshold_family;

INSERT INTO poverty(pcode, AttributeID, "2015", "2018", "2021p", DomainID)
    SELECT pcode,
        AttributeID, "2015", "2018", "2021p",
        (SELECT DomainID FROM DomainDim WHERE DomainDesc = 'Population')
    FROM poverty_poverty_incidence_threshold_pop;

INSERT INTO poverty(pcode, AttributeID, "2015", "2018", "2021p", DomainID)
    SELECT pcode,
            AttributeID, "2015", "2018", "2021p",
            (SELECT DomainID FROM DomainDim WHERE DomainDesc = 'All')
    FROM poverty_poverty_severity;