# The Data Scraping project during the Master of Data Science program, HSE, Moscow.
# IMDB actors movie distances


Working on the [Six degrees of separation](https://en.wikipedia.org/wiki/Six_degrees_of_separation) theory or the game [Six Degrees of Kevin Bacon](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon). 

The idea is simple. We introduce a special measure of distance between actors. How is it measured? If two actors played in the same movie, the distance between them is 1. If two actors never played in the same move, but there is some actor, who played in some movies with each of the actors, then the distance between the actors is 2. And so on. Let's call it *movie distance*.


### 1. We should get movie descriptions for every highest-paid actor of 2019. They are 

1. Dwayne Johnson
2. Chris Hemsworth
3. Robert Downey Jr.
4. Akshay Kumar
5. Jackie Chan
6. Bradley Cooper
7. Adam Sandler
8. Scarlett Johansson
9. Sofia Vergara
10. Chris Evans. 

### 2. Find the distance between actors

![image](https://user-images.githubusercontent.com/41555285/225527595-82afc241-2fd1-4f8d-85c6-4205999c0fc9.png)

### 3. Collect data and save it to files. Every actor should have a separate text file with descriptions of all movies an actor played in.

### 4. For every actor we should provide a picture of a wordcloud, based on movie descriptions for that actor. 
Example: Dwayne Johnson's wordcloud'

![image](https://user-images.githubusercontent.com/41555285/225527692-98d239c3-68f8-4db1-badd-39b3c110189a.png)


