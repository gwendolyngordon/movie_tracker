from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'movies.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            director TEXT NOT NULL,
            year INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/movies', methods=['GET'])
def get_movies():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()
    conn.close()
    movies = [{"id": row[0], "title": row[1], "director": row[2], "year": row[3]} for row in rows]
    return jsonify(movies)

@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    title = data.get('title')
    director = data.get('director')
    year = data.get('year')
    if not all([title, director, year]):
        return jsonify({"error": "Missing movie details"}), 400
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO movies (title, director, year) VALUES (?, ?, ?)", (title, director, year))
    conn.commit()
    conn.close()
    return jsonify({"message": "Movie added successfully"}), 201

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id))
    conn.commit()
    conn.close()
    return jsonify({"message": f"Movie with ID {movie_id} deleted."})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)