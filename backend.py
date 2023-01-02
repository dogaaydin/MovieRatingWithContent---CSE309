#importing required Libraries
import pandas as pd   #to create dataframe
import requests       #to send the request to the URL
from bs4 import BeautifulSoup #to get the content in the form of HTML
import numpy as np  # to count the values (in our case)
from openpyxl import Workbook,load_workbook


#assigning the URL with variable name url
url = 'https://www.imdb.com/search/title/?count=250&groups=top_1000&sort=user_rating'
#request allow you to send HTTP request
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

movie_name = []
time = []
rating = []
metascore = []
description = []
Director = []
Stars = []
genre = []


movie_data = soup.findAll('div', attrs= {'class': 'lister-item mode-advanced'})

for store in movie_data:
    name = store.h3.a.text
    movie_name.append(name)
    
    runtime = store.p.find('span', class_ = 'runtime').text.replace(' min', '')
    time.append(runtime)
   
  
    rate = store.find('div', class_ = 'inline-block ratings-imdb-rating').text.replace('\n', '')
    rating.append(rate)
    
    genreName = store.p.find('span', class_ = 'genre').text.replace('\n', '')
    genre.append(genreName)
    
    meta  = store.find('span', class_ = 'metascore').text.replace(' ', '') if store.find('span', class_ = 'metascore') else '^^^^^^'
    metascore.append(meta)
    #since, gross and votes have same attributes, that's why we had created a common variable and then used indexing
    value = store.find_all('span', attrs = {'name': 'nv'})
    

    
    
    describe = store.find_all('p', class_ = 'text-muted')
    description_ = describe[1].text.replace('\n', '') if len(describe) >1 else '*****'
    description.append(description_)
    
    cast = store.find("p", class_ = '')
    cast = cast.text.replace('\n', '').split('|')
    cast = [x.strip() for x in cast]
    cast = [cast[i].replace(j, "") for i,j in enumerate(["Director:", "Stars:"])]
    Director.append(cast[0])
    Stars.append([x.strip() for x in cast[1].split(",")])
    
def showStarData():
    star_DF = pd.DataFrame({'Name of movie' : movie_name , 'Star' :  Stars})
    print(star_DF)
    
def showWatchtimeData():
    watchtime_DF = pd.DataFrame({'Name of movie' : movie_name , 'Watchtime' :  time})
    print(watchtime_DF)

def showRatingData():
    rating_DF = pd.DataFrame({'Name of movie' : movie_name , 'Movie Rating' :  rating})
    print(rating_DF)
    
def showMetaScoreData():
    metascore_DF = pd.DataFrame({'Name of movie' : movie_name , 'Metascore' :  metascore})
    print(metascore_DF)
    
def showGenreData():
    genre_DF = pd.DataFrame({'Name of movie' : movie_name , 'Genre' :  genre})
    print(genre_DF)
    
def showDirectorData():
    director_DF = pd.DataFrame({'Name of movie' : movie_name , 'Director' : Director})
    print(director_DF)
    
def showAllData():
    print(movie_DF)




    
#creating a dataframe using pandas library
movie_DF = pd.DataFrame({'Name of movie': movie_name, 'Watchtime': time, 'Movie Rating': rating, 'Metascore': metascore,'Genre': genre, "Director": Director, 'Star': Stars  })
#print(movie_DF)
'''showStarData()
showYearData()
showWatchtimeData()
showRatingData()
showMetaScoreData()
showGenreData()
showDirectorData()
showAllData()'''
