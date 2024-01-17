REASSIGN OWNED BY asyncdb TO matimu;  -- or some other trusted role
DROP OWNED BY asyncdb;
DROP DATABASE IF EXISTS asyncdb;
CREATE DATABASE asyncdb;
DROP ROLE IF EXISTS asyncdb;
CREATE USER asyncdb WITH ENCRYPTED PASSWORD 'asyncdb';
GRANT ALL PRIVILEGES ON DATABASE asyncdb to asyncdb;
\c asyncdb;
GRANT ALL ON SCHEMA public TO  asyncdb;
