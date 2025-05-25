# Movie Tracker API

A simple RESTful backend service built with **Flask** and **SQLite** that allows users to add, view, and delete movies from a local database. This project demonstrates CRUD operations, API design, and working with lightweight databases in Python. 

---

## Features
- Add new movies (title, director, year)
- Retrieve all movies
- Delete movies by ID
- Tested with Postman

---

## Technologies Used
- Python
- Flask
- SQLite
- Postman (for testing)
- VS Code

---

## Project Structure

```
movie_tracker/
├── app.py   
├── movies.db 
├── requirements.txt 
├── README.md  
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/gwendolyngordon/movie_tracker.git
cd movie_tracker
```
### 2. Create and activate a virtual environment

```bash 
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux
```

### 3. Install dependencies 

```bash 
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

## API Endpoints

### POST '/movies'
Add a new movie. 

**Request Body (JSON):**
```json
{
    "title": "Inception",
    "director": "Christopher Nolan",
    "year": 2010
}
```

### GET '/movies'
Retrieve all movies in the database.

### DELETE '/movies/<id>'
Delete a movie by its ID. 

## Tags
'Python' 'Flask' 'SQLite' 'REST API' 'CRUD' 'Backend Development' 'Postman' 

## License

This project is licensed under the MIT License. 