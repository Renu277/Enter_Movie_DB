from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)

moviesList = []

@app.route('/', methods=['GET', 'POST'])
def movies_manager():
    if request.method == 'POST':
        choice = request.form['choice']
        if choice == '1':
            return redirect(url_for('add_movie'))
        elif choice == '2':           
           return redirect(url_for('all_movies'))
        elif choice == '3':           
           return print('-----')
    return render_template('index.html', moviesList=moviesList)


@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        nName = request.form['name']
        nGenre = request.form['genre']
        nRating = request.form['ratings']
        moviesList.append([nName, nGenre, nRating])
        ###############
        db = sqlite3.connect('moviesdata.db')#mdata = moviedata
        cur = db.cursor()
        cur.execute("INSERT INTO newmovies (Title, Genre, Rating) VALUES (?, ?, ?)",
                    (nName, nGenre, nRating))
        db.commit()
        db.close()
        #moviesList.append([nName, nGenre, nRating])
        return redirect(url_for('movies_manager'))
    return render_template('add_movie.html')
@app.route('/all_movies')
def all_movies():
    return render_template('all_movies.html', moviesList=moviesList)

if __name__ == '__main__':
    app.run(debug=True)