# The Data Scraping project during the Master of Data Science program, HSE, Moscow.
# IMDB actors movie distances


Working on the [Six degrees of separation](https://en.wikipedia.org/wiki/Six_degrees_of_separation) theory or the game [Six Degrees of Kevin Bacon](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon). 

The idea is simple. We introduce a special measure of distance between actors. How is it measured? If two actors played in the same movie, the distance between them is 1. If two actors never played in the same move, but there is some actor, who played in some movies with each of the actors, then the distance between the actors is 2. And so on. Let's call it *movie distance*.
