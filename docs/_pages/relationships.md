---
title: "Relationship documentation"
permalink: /relationships/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

### ACTED_IN
Represents a person acting in a movie.

```
(Person)-[:ACTED_IN]->(Movie)
```

### DIRECTED
Represents a person directing a movie.

```
(Person)-[:DIRECTED]->(Movie)
```

### WROTE
Represents a person writing a movie.

```
(Person)-[:WROTE]->(Movie)
```

### HAS_WON
Represents an entity winning an Oscar (Person or Movie).

```
(Person or Movie)-[:HAS_WON]->(Oscar)
(Movie)-[:HAS_WON]->(Oscar)
```

### NOMINATED_FOR
Represents an entity being nominated for an Oscar (Person or Movie).

```
(Person)-[:NOMINATED_FOR]->(Oscar)
(Movie)-[:NOMINATED_FOR]->(Oscar)
```

### MOVIE_HAS_GENRE
Represents a movie having a genre.

```
(Movie)-[:MOVIE_HAS_GENRE]->(Genre)
```