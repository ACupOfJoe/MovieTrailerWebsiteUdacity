# -*- coding: utf-8 -*-
"""
Created on Sat Mar 03 15:00:09 2018

@author: Joe
"""
import webbrowser


class Movie():
       """This class provides a way to store movie related information"""
       
       VALID_RATINGS = ["G", "PG", "PG-13", "R"]
       
       """This is the constructor method that requires a movie title, movie storyline
        poster image link, and trailer link"""
       def __init__(self, movie_title, movie_storyline, poster_image, 
                    trailer_youtube):
              self.title = movie_title
              self.storyline = movie_storyline 
              self.poster_image_url = poster_image 
              self.trailer_youtube_url = trailer_youtube
        """This method is used to open the trailer link"""
       def show_trailer(self):
              webbrowser.open(self.trailer_youtube_url)
              