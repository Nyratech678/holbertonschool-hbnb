CREATE TABLE IF NOT EXISTS Place (
    id CHAR(36) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    price_by_night DECIMAL(10, 2) NOT NULL,
    latitude FLOAT,
    longitude FLOAT,
    owner_id CHAR(36) NOT NULL
);