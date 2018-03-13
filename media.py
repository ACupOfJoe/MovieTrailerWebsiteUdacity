# -*- coding: utf-8 -*-
"""
Created on Sat Mar 03 15:00:09 2018

@author: Joe
"""
import webbrowser


class Movie:
    """This class provides a way to store movie related information"""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
            """This is the constructor method that requires a movie title,
            movie storyline poster image link, and trailer link

            Args: 
              movie_title (str): The title of the movie
              movie_storyline (str): The story line of the movie 
              poster_image (str): The URL containing the poster image
                of the movie 
              trailer_youtube (str): The URL from YouTube containg the
                trailer of the movie 

            Returns:
              A new movie object.

            Example:
              toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys 
                        that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=4KPTXpQehio")  # NOQA
            """
            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
            """This method is used to open the trailer link

            Args:
              None

            Returns:
              A web browser with the youtube link opened.

            Example:
            toy_story.show_trailer()

            """
            webbrowser.open(self.trailer_youtube_url)
