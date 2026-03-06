DROP TABLE IF EXISTS text_quiz;
DROP TABLE IF EXISTS schueler_anmelden;

CREATE TABLE text_quiz (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    quiz_titel TEXT,
    frage1 TEXT,
    antwort1 TEXT,
    frage2 TEXT,
    antwort2 TEXT
);

CREATE TABLE schueler_anmelden (
    name TEXT PRIMARY KEY,
    nachname  TEXT,
    punktzahl INTEGER
   
);
 