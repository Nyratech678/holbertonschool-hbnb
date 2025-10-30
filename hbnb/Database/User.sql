CREATE TABLE IF NOT EXISTS User (
    id CHAR(36) PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE
);

INSERT INTO User (id, email, first_name, last_name, password, is_admin) 
VALUES ('36c9050e-ddd3-4c3b-9731-9f487208bbc1', 'admin@hbnb.io', 'Admin', 'HBnB','c93ccd78b2076528346216b3b2f701e6', TRUE)