CREATE TABLE IF NOT EXISTS review (
    id CHAR(36) PRIMARY KEY,
    text TEXT,
    rating INT(1, 5),
    user_id CHAR(36),
    place_id CHAR(36),
    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (place_id) REFERENCES Place(id)
);