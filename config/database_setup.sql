-- User: cuenca_challenge
-- DROP USER cuenca_challenge;

CREATE USER cuenca_challenge WITH
  LOGIN
  SUPERUSER
  INHERIT
  CREATEDB
  CREATEROLE
  NOREPLICATION
  PASSWORD 'c0d1ng';
	
CREATE DATABASE n_queens_puzzle
    WITH 
    OWNER = cuenca_challenge
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

GRANT ALL ON DATABASE n_queens_puzzle TO cuenca_challenge;