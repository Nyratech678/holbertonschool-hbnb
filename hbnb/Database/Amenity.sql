CREATE TABLE IF NOT EXISTS Place_Amenity (
    place_id VARCHAR(36),
    amenity_id VARCHAR(36),
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES Place(id),
    FOREIGN KEY (amenity_id) REFERENCES Amenity(id)
);

INSERT INTO Place_Amenity (id, name) VALUES
('d4f8899d-268a-4f75-8a2a-439c3dc5a69c', 'Wifi')
('a04bcda9-cb99-4bad-8e96-a5aaa9bcfa6b ', 'Piscine')
('cdd5aee3-ebdc-4699-9a57-1cfc69627e37', 'Climatisation')