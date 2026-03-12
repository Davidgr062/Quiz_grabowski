DROP TABLE IF EXISTS text_quiz;


CREATE TABLE text_quiz (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    quiz_titel TEXT,
    frage1 TEXT,
    antwort1 TEXT,
    frage2 TEXT,
    antwort2 TEXT
);

CREATE TABLE schueler_anmelden (
    schueler_name TEXT PRIMARY KEY,
    punktzahl INTEGER
   
);
 