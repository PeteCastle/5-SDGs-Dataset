DROP TABLE IF EXISTS SDGDim;

CREATE TABLE IF NOT EXISTS SDGDim (
    code INT PRIMARY KEY,
    title TEXT,
    description TEXT,
    uri TEXT
);

INSERT INTO SDGDim(code, title, description, uri)
SELECT code, title, description, uri
FROM stg_sdggoals

    