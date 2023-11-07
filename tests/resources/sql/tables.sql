CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL,
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> b8b9c74b13e1

CREATE TABLE customers (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    latitude INTEGER NOT NULL,
    longitude INTEGER NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE warehouses (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    latitude INTEGER NOT NULL,
    longitude INTEGER NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO alembic_version (version_num) VALUES ('b8b9c74b13e1');
