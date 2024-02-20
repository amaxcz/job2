SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'demo1_db';

REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM demo1_user;
REVOKE ALL PRIVILEGES ON SCHEMA public FROM demo1_user;

DROP DATABASE IF EXISTS demo1_db;

DROP OWNED BY demo1_user;
DROP USER IF EXISTS demo1_user;
