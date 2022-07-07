# themoviedb.org -> dizi ve film arşivi

from typing import Text
import requests
import json

from requests.models import Response

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "37936ef9611e025ebe13f4a5aee2d3e3"

    def getPopulars(self):
        # self.api_url + f"/movie/popular?api_key={self.api_key}&language=en-US&page=1"
        response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=37936ef9611e025ebe13f4a5aee2d3e3&language=en-US&page=1")
        return response.json()
    
    def searchMovie(self, title):
        response = requests.get(f"https://api.themoviedb.org/3/search/keyword?api_key=37936ef9611e025ebe13f4a5aee2d3e3&query={title}&page=1")
        return response.json()
        
    def gettopRated(self):
        response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=37936ef9611e025ebe13f4a5aee2d3e3&language=en-US&page=1")
        return response.json()

movieApi = theMovieDb()

while True:
    secim = input("1-Popular Movies\n2-Search a Movie\n3-Top Rated Movies\n4-Exit\nChoice: ")

    if secim == "4":
        break
    else:
        if secim == "1":
            movies = movieApi.getPopulars()
            for movie in movies['results']:
                print("Title: " + movie['original_title'] + "\n")
        elif secim == "2":
            title = input("Search: ")
            search = movieApi.searchMovie(title)
            for i in search['results']:
                print(i['name'] + "\n")
        elif secim == "3":
            movies = movieApi.gettopRated()
            for movie in movies['results']:
                print(f"Title: {movie['original_title']}\n")

        
