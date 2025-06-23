Late Show API
The Late Show API is a Flask-based RESTful API for managing a late-night talk show database. It allows users to register, authenticate with JWT, and manage guests, episodes, and their appearances with ratings. The API uses PostgreSQL for data storage, SQLAlchemy for ORM, Flask-Migrate for database migrations, and Flask-JWT-Extended for authentication.
Features

User Authentication: Register and login with JWT-based authentication.
Guest Management: Retrieve a list of guests with their names and occupations.
Episode Management: Create, retrieve, and delete episodes with associated dates and numbers.
Appearance Management: Record guest appearances on episodes with ratings (1-5).
Database Seeding: Populate the database with sample data for testing.

Project Structure
late_show_api/
├── server/
│   ├── __init__.py           # Application factory and Flask extensions
│   ├── app.py                # Entry point for the Flask app
│   ├── config.py             # Configuration settings
│   ├── seed.py               # Script to seed the database
│   ├── models/
│   │   ├── __init__.py       # Model imports
│   │   ├── user.py           # User model
│   │   ├── guest.py          # Guest model
│   │   ├── episode.py        # Episode model
│   │   ├── appearance.py     # Appearance model
│   ├── controllers/
│   │   ├── auth_controller.py      # Authentication endpoints
│   │   ├── guest_controller.py     # Guest endpoints
│   │   ├── episode_controller.py   # Episode endpoints
│   │   ├── appearance_controller.py # Appearance endpoints
├── venv/                     # Virtual environment
├── .env                      # Environment variables
├── migrations/               # Flask-Migrate migration files
├── README.md                 # Project documentation

Prerequisites

Python 3.8+
PostgreSQL (installed and running)
Git
macOS/Linux/Windows

Setup Instructions
1. Clone the Repository
git clone https://github.com/your-username/late_show_api.git
cd late_show_api

2. Create and Activate a Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# For Windows: venv\Scripts\activate

3. Install Dependencies
pip install flask flask-sqlalchemy flask-migrate flask-jwt-extended psycopg2-binary python-dotenv

4. Configure Environment Variables
Create a .env file in the project root with the following content:
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/late_show_db
JWT_SECRET_KEY=your-very-secure-secret-key

Replace your-very-secure-secret-key with a strong secret key.
5. Set Up PostgreSQL Database
Ensure PostgreSQL is running (e.g., via Homebrew on macOS: brew services start postgresql). Create the database:
createdb -h localhost -U postgres late_show_db

6. Initialize and Apply Migrations
Set the FLASK_APP environment variable and initialize Flask-Migrate:
export FLASK_APP=server.app  # On macOS/Linux
# For Windows: set FLASK_APP=server.app
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

7. Seed the Database (Optional)
Populate the database with sample data:
python server/seed.py

8. Run the Application
Start the Flask development server:
flask run

The API will be available at http://127.0.0.1:5000.
API Endpoints
Authentication

POST /register: Register a new user
Request: { "username": "string", "password": "string" }
Response: { "message": "User registered successfully" } (201)


POST /login: Login and get JWT token
Request: { "username": "string", "password": "string" }
Response: { "access_token": "string" } (200)



Guests

GET /guests: Retrieve all guests
Response: [{ "id": int, "name": "string", "occupation": "string" }, ...] (200)



Episodes

GET /episodes: Retrieve all episodes
Response: [{ "id": int, "date": "YYYY-MM-DD", "number": int }, ...] (200)


GET /episodes/: Retrieve episode details with appearances
Response: { "id": int, "date": "YYYY-MM-DD", "number": int, "appearances": [{ "id": int, "rating": int, "guest_id": int, "guest_name": "string" }, ...] } (200)


DELETE /episodes/: Delete an episode (JWT required)
Response: { "message": "Episode deleted successfully" } (200)



Appearances

POST /appearances: Create a guest appearance (JWT required)
Request: { "rating": int, "guest_id": int, "episode_id": int }
Response: { "id": int, "rating": int, "guest_id": int, "episode_id": int } (201)



Testing the API
Use tools like Postman or curl to test endpoints. Example:
curl -X POST http://127.0.0.1:5000/register -H "Content-Type: application/json" -d '{"username":"testuser","password":"testpass"}'

To access protected endpoints (e.g., POST /appearances), include the JWT token in the Authorization header:
curl -X POST http://127.0.0.1:5000/appearances -H "Authorization: Bearer <your-token>" -H "Content-Type: application/json" -d '{"rating":4,"guest_id":1,"episode_id":1}'

Troubleshooting

Database Connection Errors: Ensure PostgreSQL is running and the DATABASE_URL in .env is correct.
Flask-Migrate Issues: If flask db commands fail, verify FLASK_APP=server.app and reinstall dependencies.
Import Errors: Check server/app.py and server/__init__.py for correct imports.

Run Flask in debug mode for detailed errors:
flask --debug run

Contributing

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
=