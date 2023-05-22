1 Movie Database Web App

This Flask web application allows you to manage and display movie data using a SQLite database. You can add new movies to the database, retrieve and display movie information

    main.py # Flask app file
    moviesdata.db # SQLite database file
    newmovies #database table name

2 Prerequisites

- Python 3.x
- Flask (`pip install flask`)
Install the required Python dependencies 


3. Access the web application by opening a web browser and visiting `http://localhost:5000`.

4.Functionality

The web application provides the following functionality:

- Adding a Movie:
- Navigate to the homepage.
- Fill in the input fields for movie title, genre, and rating.
- Click on the "Add Movie" button.
- The movie details will be added to the database, and the result page will display the entered movie information.

- Displaying Top Rated Movies:
- Navigate to the homepage.
- Fill in the input field for the number of movies (1-10).
- Click on the "Get Movies" button.
- The top rated movies will be retrieved from the database and displayed on the result page.


 5.Directory Structure

The directory structure of the project is as follows:
    main.py # Flask app file
    moviesdata.db # SQLite database file
    newmovies #table name
    
    static/
        css/
            style.css # CSS file for styling
    templates/
        index.html # HTML template for input forms
        all_movies.html # HTML template for displaying results
        add_movies.html # HTML template for Movie name,genre, rating

