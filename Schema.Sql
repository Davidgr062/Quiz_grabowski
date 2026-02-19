DROP TABLE IF EXISTS beitraege;

CREATE TABLE beitraege (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    autor TEXT,
    titel TEXT,
    inhalt TEXT
);
