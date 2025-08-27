CREATE DATABASE visits WITH OWNER postgres ENCODING 'UTF8';

\c visits

CREATE SCHEMA visits;

GRANT ALL PRIVILEGES ON DATABASE visits TO postgres ;
GRANT ALL PRIVILEGES ON SCHEMA visits TO postgres ;

CREATE TABLE visits.visits (
    counter integer NOT NULL
);

INSERT INTO visits.visits VALUES (0);
