---
title: "Node documentation"
permalink: /nodes/
---


### Movie
A movie in the database.

**Properties:**
- `title`:(string) - The title of the movie 
- `release_year`(integer): - The year the movie was released 
- `duration`(integer): The duration of the movie in minutes
- `rating`:(string) - The rating of the movie
- `budget`(float): The budget of the movie
- `gross`(float): The gross revenue of the movie

### Person
A person who has a role in a movie.

**Properties:**
- `name`(string): The name of the person 
- `birth_date`(date): The year the person was born
- `alive`(boolean): Whether the person is alive or not
- `age`(integer): The age of the person

### Oscar
An Oscar award.

**Properties:**
- `category`:(string) - The category of the award
- `year`:(integer) - The year the award was given

### Genre
A genre of a movie.

**Properties:**
- `category`:(string) - The category of the genre

### Certification
A certification of a movie, like PG-13 or R-rated.

**Properties:**
- `type`: (string) - The type of the certification
