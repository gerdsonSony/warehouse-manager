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

-- Running upgrade b8b9c74b13e1 -> 34263ba28278

ALTER TABLE customers MODIFY latitude DOUBLE NOT NULL;

ALTER TABLE customers MODIFY longitude DOUBLE NOT NULL;

ALTER TABLE warehouses MODIFY latitude DOUBLE NOT NULL;

ALTER TABLE warehouses MODIFY longitude DOUBLE NOT NULL;

UPDATE alembic_version SET version_num='34263ba28278' WHERE alembic_version.version_num = 'b8b9c74b13e1';
