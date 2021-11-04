DROP TABLE IF EXISTS grants;

CREATE TABLE IF NOT EXISTS grants (
    name    TEXT NOT NULL PRIMARY KEY,
    kind    TEXT NOT NULL,
    shares  INTEGER NOT NULL,
    date    TEXT NOT NULL,
    cliff   INTEGER NOT NULL,
    vesting INTEGER NOT NULL,
    strike  FLOAT
);
