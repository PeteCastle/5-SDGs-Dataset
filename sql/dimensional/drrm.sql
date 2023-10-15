CREATE TABLE IF NOT EXISTS drrm (
    id INTEGER PRIMARY KEY,
    pcode TEXT,
    AttributeID INTEGER NOT NULL,
    DomainID INTEGER NOT NULL,
    "2016" REAL, "2017" REAL, "2018" REAL, "2019" REAL, "2020" REAL, "2021" REAL, "2022" REAL,
    FOREIGN KEY(pcode) REFERENCES location(pcode),
    FOREIGN KEY(AttributeID) REFERENCES AttributeDIM(AttributeID)
    FOREIGN KEY(DomainID) REFERENCES DomainDim(DomainID)
);

INSERT INTO drrm(pcode, AttributeID, "2016", "2017", "2018", "2019", "2020", "2021", DomainID)
    SELECT pcode,
        AttributeID, "2016", "2017", "2018", "2019", "2020", "2021",
        (SELECT DomainID FROM DomainDim WHERE DomainDesc = 'Disaster Risk and Reduction Implementation')
    FROM drrm_drr_implementation;

INSERT INTO drrm(pcode, AttributeID, "2019", DomainID)
    SELECT pcode,
        AttributeID, "2019",
        (SELECT DomainID FROM DomainDim WHERE DomainDesc = 'Evacuation Center')
    FROM drrm_evacuation_center;

INSERT INTO drrm(pcode, AttributeID, "2018", DomainID)
    SELECT pcode,
        AttributeID, "2018",
        (SELECT DomainID FROM DomainDim WHERE DomainDesc = 'Vulnerable Groups')
    FROM drrm_vulnerable_groups;