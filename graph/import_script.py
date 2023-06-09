from domainmodel.movie_node import Movie
from domainmodel.person_node import Person
from domainmodel.oscar_node import Oscar
from domainmodel.genre_node import Genre
from domainmodel.actedin_relation import ActedInRelation
from domainmodel.directed_relation import DirectedRelation
from domainmodel.wrote_relation import WroteRelation
from domainmodel.movieNominated_relation import MovieNominatedForRelation
from domainmodel.movieWon_relation import MovieHasWonRelation
from domainmodel.hasGenre_relation import HasGenreRelation
import os
import pandas as pd  # assuming you're loading a .csv or similar data file

# get current working directory
cwd = os.getcwd()

# create relative path to cleaned_data directory
data_dir = os.path.join(cwd, 'cleaned_data')

if __name__ == "__main__":

    # Create the movie nodes 
    movies_df = pd.read_csv(os.path.join(data_dir, 'Movie.csv'))
    for index, row in movies_df.iterrows():
        title = row['movie_name']
        year = row['movie_date']
        rating = row['movie_rating']
        budget = row['budget']
        if not (budget > 0):
            print(budget)
        movie = Movie(title, year, rating, budget)
        movie.create()

    # Create the Oscar nodes 
    oscar_df = pd.read_csv(os.path.join(data_dir, 'Award.csv'))
    for index, row in oscar_df.iterrows():
        category = row['award_category']
        year = row['award_year']
        oscar = Oscar(category, year)
        oscar.create()

    # Create the genre nodes
    genre_df = pd.read_csv(os.path.join(data_dir, 'Genre.csv'))
    for index, row in genre_df.iterrows():
        genre = row['movie_genre']
        genre = Genre(genre)
        genre.create()

    # Create the person nodes 
    person_df = pd.read_csv(os.path.join(data_dir, 'Person_extended.csv'))
    for index, row in person_df.iterrows():
        name = row['person_name']
        dob = row['birth_date']
        dod = row['death_date']
        start_year = row["start_activity"]
        end_year = row['end_activity']
        person = Person(name, dob, dod, start_year, end_year)
        person.create()

    movieNominated_df = pd.read_csv(os.path.join(data_dir, 'Nominated for (Movie).csv'))
    for index, row in movieNominated_df.iterrows():
        # Create the movie 
        movie_name = row['movie_name']
        movie_date = row['movie_date']
        movie = Movie(movie_name, movie_date, None, None)

        # Create the oscar 
        award_cat = row['award_category']
        award_year = row['award_year']
        oscar = Oscar(award_cat, award_year)

        # Create the relationship
        nominatedFor = MovieNominatedForRelation(movie, oscar)
        nominatedFor.create()
    
    movieWon_df = pd.read_csv(os.path.join(data_dir, 'Won (Movie).csv'))
    for index, row in movieWon_df.iterrows():
        # Create the movie 
        movie_name = row['movie_name']
        movie_date = row['movie_date']
        movie = Movie(movie_name, movie_date, None, None)

        # Create the oscar 
        award_cat = row['award_category']
        award_year = row['award_year']
        oscar = Oscar(award_cat, award_year)

        # Create the relationship
        movieWon = MovieHasWonRelation(movie, oscar)
        movieWon.create()
        
    hasGenre_df = pd.read_csv(os.path.join(data_dir, 'Has genre.csv'))
    for index, row in hasGenre_df.iterrows():
        # Create the movie 
        movie_name = row['movie_name']
        movie_date = row['movie_date']
        movie = Movie(movie_name, movie_date, None, None)

        # Create the genre 
        genre = row['movie_genre']
        genre = Genre(genre)

        # Create the relationship
        hasGenre = HasGenreRelation(movie, genre)
        hasGenre.create()

    actedIn_df = pd.read_csv(os.path.join(data_dir, 'Acted in.csv'))
    for index, row in actedIn_df.iterrows():
        # Create the movie 
        movie_name = row['movie_name']
        movie_date = row['movie_date']
        movie = Movie(movie_name, movie_date, None, None)

        # Create the actor 
        actor = row['actor']
        actor = Person(actor)

        # Create the relationship
        actedIn = ActedInRelation(actor, movie)
        actedIn.create()
    
    directed_df = pd.read_csv(os.path.join(data_dir, 'Directed.csv'))
    for index, row in directed_df.iterrows():
        # Create the movie 
        movie_name = row['movie_name']
        movie_date = row['movie_date']
        movie = Movie(movie_name, movie_date, None, None)

        # Create the director 
        director = row['director']
        director = Person(director)

        # Create the relationship
        directed = DirectedRelation(director, movie)
        directed.create()

    wrote_df = pd.read_csv(os.path.join(data_dir, 'Wrote.csv'))
    for index, row in wrote_df.iterrows():
        # Create the movie 
        movie_name = row['movie_name']
        movie_date = row['movie_date']
        movie = Movie(movie_name, movie_date, None, None)

        # Create the writer 
        writer = row['writer']
        writer = Person(writer)

        # Create the relationship
        writed = WroteRelation(director, movie)
        writed.create()

