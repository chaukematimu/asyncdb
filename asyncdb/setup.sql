-- REASSIGN OWNED BY test TO postgres;  -- or some other trusted role
-- DROP OWNED BY test;
DROP DATABASE IF EXISTS test;
CREATE DATABASE test;
DROP ROLE IF EXISTS test;
CREATE USER test WITH ENCRYPTED PASSWORD 'test';
GRANT ALL PRIVILEGES ON DATABASE test to test;
\c test;
GRANT ALL ON SCHEMA public TO  test;
