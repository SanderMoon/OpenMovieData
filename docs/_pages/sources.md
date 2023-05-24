

## Datasets

### The Oscar Award, 1927 - 2023

- **Author(s)**: Raphael Fontes and David Lu
- **Description**: the_oscar_award.csv is a dataset that contains information about the Oscar Awards from 1927 to 2023. The dataset contains information about the year, ceremony, category and winner of the award.
- **Source**: [Kaggle](https://www.kaggle.com/datasets/unanimad/the-oscar-award)
- **Format**: Comma Separated Values (CSV)
- **License**: [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)
- **Content**: The dataset contains information about the year, ceremony, category and winner of the award.

#### Data Dictionary

| Column Name  | Data Type | Description             |
| ------------ | --------- | ----------------------- |
| year_film    | Integer   | Year film was screened  |
| year_ceremony| Integer   | Year ceremony happened  |
| ceremony     | Integer   | Number of the ceremony  |
| category     | String    | Type of nomination      |
| name         | String    | Name of nominee         |
| film         | String    | Title of the film       |
| winner       | Boolean   | True if winner, False otherwise |


### 9000+ Movies Dataset

- **Author(s)**: Doula Isham Rahik Hasan
- **Description**: mymoviedb.csv is a dataset that contains information about 9000+ movies. 
- **Source**: [Kaggle](https://www.kaggle.com/datasets/disham993/9000-movies-dataset)
- **Format**: Comma Separated Values (CSV)
- **License**: [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)
- **Content**: The dataset contains information about the title, overview, popularity, vote count, vote average, original language, genre and poster path of the movie.

#### Data Dictionary

| Column Name       | Data Type | Description             |
| ----------------- | --------- | ----------------------- |
| Release_Date      | Date      | Date when the movie was released |
| Title             | String    | Name of the movie |
| Overview          | String    | Brief summary of the movie |
| Popularity        | Float     | Metric computed by TMDB developers based on various factors |
| Vote_Count        | Integer   | Total votes received from the viewers |
| Vote_Average      | Float     | Average rating based on vote count and the number of viewers out of 10 |
| Original_Language | String    | Original language of the movies |
| Genre             | String    | Categories the movie can be classified as |
| Poster_Url        | String    | Url of the movie's poster |

### Movie Industry
- **Author(s)**: Daniel Grijalva
- **Description**: movies.csv is a dataset that contains data about 220 movies per year, from 1986 to 2016. 
- **Source**: [Kaggle](https://www.kaggle.com/datasets/danielgrijalvas/movies)
- **Format**: Comma Separated Values (CSV)
- **License**: [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)
- **Content**: The dataset contains information about the budget, company, country of origin, director, genre, gross revenue, name, rating, release date, runtime, score, star, votes, writer, and year of the movie.

#### Data Dictionary

| Column Name | Data Type | Description               |
| ----------- | --------- | ------------------------- |
| name        | String    | Name of the movie         |
| rating      | String    | Rating of the movie (R, PG-13, etc.) |
| genre       | String    | Main genre of the film    |
| year        | Integer   | Release year              |
| released    | Date      | Release date              |
| score       | Float     | IMDb score                |
| votes       | Integer   | Count of IMDb user votes  |
| director    | String    | Director of the film      |
| writer      | String    | Writer of the film        |
| star        | String    | Main actor/actress of the film |


### IMDb 5000+ Movies & Multiple Genres Dataset
- **Author(s)**: Rakkesh Aravind
- **Description**: IMDb_All_Genres_etf_clean1.csv is a dataset that contains information about 5453 movies, based on different genres and different languages. These movies are from the early 1920 to 2022.
- **Source**: [Kaggle](https://www.kaggle.com/datasets/rakkesharv/imdb-5000-movies-multiple-genres-dataset)
- **Format**: Comma Separated Values (CSV)
- **License**: [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)
- **Content**: The dataset contains information about the movie title, year of release, director, actors, IMDb rating, main genre, subgenre(s), runtime, rating and total gross.

#### Data Dictionary

| Column Name    | Data Type | Description                    |
| -------------- | --------- | ------------------------------ |
| Movie_Title    | String    | Name of the Movie              |
| Year           | Integer   | Release Year                   |
| Director       | String    | Director of the Movie          |
| Actors         | String    | Names of Actors                |
| Rating         | Float     | IMDb Rating                    |
| Runtime(Mins)  | Integer   | Total Runtime in Minutes       |
| Censor         | String    | Censor Certificate             |
| Total_Gross    | String    | Total Gross Gained             |
| main_genre     | String    | Primary Genre                  |
| side_genre     | String    | Secondary Genre                |


### Demographics of Academy Awards (Oscars) Winners
- **Author(s)**: Felix Mejia
- **Description**: Oscar-demographics-DFE.csv is a dataset that contains information about the demographics of Oscar winners from 1928 to 2015. The dataset contains information about the year, category, name, movie, and demographics of the winner of the category Best Actor, Best Actress, Best Supporting Actor, and Best Supporting Actress and best Director.
- **Source**: [kaggle](https://www.kaggle.com/datasets/fmejia21/demographics-of-academy-awards-oscars-winners)
- **Format**: Comma Separated Values (CSV)
- **License**: [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)
- **Content**: The dataset contains information about the background of the winners of various categories of the Oscars.

#### Data Dictionary

| Column Name            | Data Type | Description                    |
| ---------------------- | --------- | ------------------------------ |
| _unit_id               | Integer   | Unique identifier for the data unit |
| _golden                | Boolean   | (uncertain) Likely a flag for golden standard, TRUE if the data is marked as high quality |
| _unit_state            | String    | (uncertain) Status of the data unit, "finalized" likely means the data is ready for use |
| _trusted_judgments     | Integer   | (uncertain) Number of trusted judgments on this data unit, probably a measure of data quality or reliability |
| _last_judgment_at      | Date      | Date and time of the last judgment, likely indicating when the data was last assessed or updated |
| birthplace             | String    | Birthplace of the person |
| birthplace:confidence  | Float     | Confidence level of the birthplace data, with 1 being 100% confident |
| date_of_birth          | Date      | Date of birth of the person |
| date_of_birth:confidence | Float    | Confidence level of the date of birth data, with 1 being 100% confident |
| race_ethnicity         | String    | Ethnicity of the person |

### IMDB Top 250 Movies Dataset
- **Author(s)**: Chidambara Raju G
- **Description**: This dataset contains the top 250 rated movies on IMDB as of 2021, providing a snapshot of the most popular and highly rated movies of recent times
- **Source**: [kaggle](https://www.kaggle.com/datasets/rajugc/imdb-top-250-movies-dataset)
- **Format**: Comma Separated Values (CSV)
- **License**: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- **Content**: This dataset contains information about the IMDb rank, title, year of release, rating, genre, rating, run time, tagline, budget, and box office collection of the top 250 movies on IMDb.

#### Data Dictionary

| Column Name  | Data Type | Description                                 |
| ------------ | --------- | ------------------------------------------- |
| rank         | Integer   | Rank of the movie                           |
| name         | String    | Name of the movie                           |
| year         | Integer   | Release year                                |
| rating       | Float     | Rating of the movie                         |
| genre        | String    | Genre of the movie                          |
| certificate  | String    | Certificate of the movie                    |
| run_time     | Integer   | Total movie run time in minutes             |
| tagline      | String    | Tagline of the movie                        |
| budget       | Float     | Budget of the movie                         |
| box_office   | Float     | Total box office collection across the world |
