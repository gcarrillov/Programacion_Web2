from flask import Flask, render_template_string, jsonify
import sqlite3

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>IMDB AJAX Viewer</title>
</head>
<body>
    <h1>Películas IMDB</h1>
    <ul id="movieList"></ul>

    <script>
    document.addEventListener("DOMContentLoaded", function () {
        fetch("/movies")
            .then(response => {
                if (!response.ok) throw new Error("Error al obtener datos del servidor");
                return response.json();
            })
            .then(data => {
                const list = document.getElementById("movieList");
                data.forEach(movie => {
                    const item = document.createElement("li");
                    item.textContent = movie.id + " - " + movie.title;
                    list.appendChild(item);
                });
            })
            .catch(error => {
                console.error("Error:", error);
                alert("Hubo un error al cargar las películas.");
            });
    });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/movies')
def get_movies():
    try:
        conn = sqlite3.connect('imdb.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, title FROM Movie LIMIT 10")
        data = cursor.fetchall()
        movies = [{'id': row[0], 'title': row[1]} for row in data]
        return jsonify(movies)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
