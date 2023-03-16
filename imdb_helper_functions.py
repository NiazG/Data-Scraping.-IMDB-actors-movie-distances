import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
import itertools
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import STOPWORDS


actors_all = {}
movies_all = {}
actors_info = {}
movies_info = {}
movie_desc = {}
actors_movie_info = {}

def get_actors_by_movie_soup(cast_page_soup, num_of_actors_limit=None):
    # taking the table with onlt the casts
    casts = cast_page_soup.find_all('table', class_='cast_list')
    global actors_all
    actors_list = []
    # including the limit in case we need only some actors
    if num_of_actors_limit == None:
        limit = len(casts[0])
    else:
        limit = num_of_actors_limit
    # looking through the casts table
    for soup in casts:
        #taking only the tr tag with odd and even classes
        for soupp in soup.find_all('tr', class_ = re.compile(r'(odd|even)')):
            #there are 4 td tags in he tr tag. The desired one is the second td tag
            #each actors name and the link are in the tag 'a'
            
            actor = soupp.find_all('td')[1].find_all('a')[0].text[1:-1].strip('r')
            link = 'https://www.imdb.com' + soupp.find_all('td')[1].find_all('a')[0]['href']
            
            #finding them and adding to the list of actors
            actors_list.append((actor,link))
            actors_all[actor] = link
            # reducing the limit
            limit -= 1
            if limit == 0:
                return actors_list
                break
    return actors_list


def get_movies_by_actor_soup(actor_page_soup, num_of_movies_limit=None):
    #movies are in the div tag with the class 'actor-ttnumber' or 'actress-ttnumber'
    #used the re.compile to catch the actor and actress classes in div tags
    performance = actor_page_soup('div', attrs={'id' : re.compile(r'\Aact[a-z-]{2,5}tt[\d]*')})
    global movies_all
    movies_list = []
    # including the limit in case we need only some movies
    if num_of_movies_limit == None:
        limit = len(performance)
    else:
        limit = num_of_movies_limit
    for perf in performance:
        # used the re.compile to catch the not the full feature movies
        if len(re.findall(re.compile(r'(Music Video|\(Short\b\)|TV Series'+\
                                        '|\(Video Game\)|Video short'+\
                                        '|\(Video\)|TV Movie|TV Mini Series'+\
                                        '|TV Series short|TV Special|Mini-Series|Documentary short|'+\
                                        'Podcast Series|Podcast Episode)'),perf.text)) == 0:
            for movie in perf.find_all('a'):
                # add try except to omit the non-released movies
                try:
                    if 'in_production' in movie['class']:
                        movies_list.pop()
                        limit += 1
                        break
                except:
                    #add if statement to omit empty links or links with some symbols
                    if 'title' in movie['href']:
                        movies_list.append((movie.text, 'https://www.imdb.com' + movie['href']))
                        movies_all[movie.text] = 'https://www.imdb.com' + movie['href']
                        #reducing the limit
                        limit -= 1
                        if limit == 0:
                            return movies_list
                
    return movies_list

def check_www(url):    
    if re.search('www', url):
        return url
    else:
        url = url.replace('https://', 'https://www.')
        return url


def updating_by_actors(act_url, num_of_movies_limit=None):
    act_url = check_www(act_url)
    movies_of_actor = {}
    list_mov = get_movies_by_actor_soup(get_soup(act_url), num_of_movies_limit)
    movies_of_actor[act_url] = []
    for movie in list_mov:
        movies_of_actor[act_url].append(movie[1])
    return movies_of_actor

def updating_by_movies(mov_url, num_of_actors_limit=None):
    mov_url = check_www(mov_url)
    actors_of_movie = {}
    list_act = get_actors_by_movie_soup(get_soup(mov_url+'fullcredits?ref_=tt_cl_sm'), num_of_actors_limit)
    actors_of_movie[mov_url] = []
    for actor in list_act:
        actors_of_movie[mov_url].append(actor[1])
    return actors_of_movie

def get_soup(url):
    url = check_www(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    return soup

def get_movie_descriptions_by_actor_soup(actor_page_soup):
    global movie_desc
    text = ''
    actor_movies = get_movies_by_actor_soup(actor_page_soup)
    for movie in actor_movies:
        
        if movie[0] not in movie_desc:
            movie_soup = get_soup(movie[1])
            movie_text = movie_soup.find_all('span', class_='GenresAndPlot__TextContainerBreakpointL-cum89p-1 gwuUFD')[0].text
            movie_desc[movie[0]] = movie_text
            text  = text + ' ' + movie_text
        else:
            text  = text + ' ' + movie_desc[movie[0]]
            
            
    return text

def get_wordcloud(text):
    wc = WordCloud(stopwords = stopwords,
                   background_color="white",
                   random_state=42,
                   collocations=False)
    wc.generate(text)
    plt.figure(figsize=(8, 6), dpi=80)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis('off')
    plt.show()