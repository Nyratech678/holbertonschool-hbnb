#!/usr/bin/python3
"""
Manual verification script - shows test commands to run
"""

print("""
=================================================================
HBnB API - MANUAL TEST COMMANDS
=================================================================

The Flask server should be running at: http://127.0.0.1:5000

To start the server, run in one terminal:
cd /home/nyratech/holbertonschool-hbnb
PYTHONPATH=/home/nyratech/holbertonschool-hbnb/hbnb:$PYTHONPATH \\
  /home/nyratech/holbertonschool-hbnb/env/bin/python hbnb/app/run.py

Then in another terminal, run these curl commands:

=================================================================
TEST 1: User Login (JWT Authentication)
=================================================================
curl -X POST http://127.0.0.1:5000/api/v1/auth/login \\
  -H "Content-Type: application/json" \\
  -d '{"email":"admin@hbnb.com","password":"admin123"}'

Expected: {"access_token":"<JWT_TOKEN>"}

=================================================================
TEST 2: Get All Users
=================================================================
curl http://127.0.0.1:5000/api/v1/users/

Expected: List of users with admin@hbnb.com and john.doe@example.com

=================================================================
TEST 3: Register New User
=================================================================
curl -X POST http://127.0.0.1:5000/api/v1/users/ \\
  -H "Content-Type: application/json" \\
  -d '{"first_name":"Test","last_name":"User","email":"test@example.com","password":"test123"}'

Expected: {"id":"<UUID>","first_name":"Test","last_name":"User","email":"test@example.com"}

=================================================================
TEST 4: Get All Amenities
=================================================================
curl http://127.0.0.1:5000/api/v1/amenities/

Expected: List of amenities including WiFi, Swimming Pool, Parking

=================================================================
TEST 5: Create New Amenity
=================================================================
curl -X POST http://127.0.0.1:5000/api/v1/amenities/ \\
  -H "Content-Type: application/json" \\
  -d '{"name":"Gym"}'

Expected: {"id":"<UUID>","name":"Gym"}

=================================================================
TEST 6: Get All Places
=================================================================
curl http://127.0.0.1:5000/api/v1/places/

Expected: List of places including "Cozy Apartment"

=================================================================
TEST 7: Get All Reviews
=================================================================
curl http://127.0.0.1:5000/api/v1/reviews/

Expected: List of reviews

=================================================================
TEST 8: Protected Endpoint (requires JWT)
=================================================================
# First get token from TEST 1, then:
curl -X GET http://127.0.0.1:5000/api/v1/auth/protected \\
  -H "Authorization: Bearer <YOUR_JWT_TOKEN>"

Expected: {"message":"Hello user <USER_ID>"}

=================================================================
DATABASE VERIFICATION
=================================================================
The database is stored at: /home/nyratech/holbertonschool-hbnb/hbnb/app/development.db

To inspect the database:
cd /home/nyratech/holbertonschool-hbnb/hbnb/app
sqlite3 development.db
.tables
SELECT * FROM users;
SELECT * FROM amenities;
SELECT * FROM places;
SELECT * FROM reviews;
.quit

=================================================================
PRE-LOADED TEST DATA
=================================================================
Users:
  - admin@hbnb.com / admin123 (admin)
  - john.doe@example.com / password123 (regular user)

Amenities:
  - WiFi
  - Swimming Pool
  - Parking

Places:
  - Cozy Apartment (owner: john.doe@example.com)

Reviews:
  - Review for Cozy Apartment by admin

=================================================================
""")
