CREATE TABLE IF NOT EXISTS DomainDim (
        DomainID INTEGER PRIMARY KEY,
        DomainDesc TEXT UNIQUE
    );

INSERT OR IGNORE INTO DomainDim(DomainDesc) 
    VALUES
        ("Consumer Price Index"),
        ("Gross Regional Domestic Product"),
        ("Languages"),
        ("Population"),
        ("Transportation");

INSERT OR IGNORE INTO DomainDim(DomainDesc) 
    VALUES
        ("Disaster Risk and Reduction Implementation"),
        ("Evacuation Center"),
        ("Vulnerable Groups");

INSERT OR IGNORE INTO DomainDim(DomainDesc) 
    VALUES
        ("General"),
        ("External Debt"),
        ("Farmer Wage");

INSERT OR IGNORE INTO DomainDim(DomainDesc) 
    VALUES
        ("Family"),
        ("Population"),
        ("All");

INSERT OR IGNORE INTO DomainDim(DomainDesc) 
    VALUES
        ("Business Process Management"),
        ("Information Economy");