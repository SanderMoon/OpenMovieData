---
title: "Node documentation"
permalink: /nodes/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

### Movie
A movie in the database.

**Properties:**
- `title`:(string) - The title of the movie 
- `year`:(integer) - The year the movie was released
- `budget`:(float) - The total budget of the movie
- `rating`:(float) - The IMDB rating of the movie

### Person
A person who has a role in a movie. This currently encompasses Actors, Directors, and Writers. For more information, see the [Relationships](/relationships/) page.

**Properties:**
- `name`:(string) - The name of the person 
- `birth_year`:(integer) - The year the person was born
- `death_year`:(integer) - The year the person died
- `start_year`:(integer) - The start year of the person's active career
- `end_year`:(integer) - The end year of the person's active career

### Oscar
An Oscar award.

**Properties:**
- `category`:(string) - The category of the award
- `year`:(integer) - The year the award was given

### Genre
A genre of a movie.

**Properties:**
- `genre`:(string) - The name of the genre