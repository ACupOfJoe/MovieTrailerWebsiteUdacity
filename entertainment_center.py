# -*- coding: utf-8 -*-
"""
Created on Sat Mar 03 15:00:37 2018

@author: Joe
"""

import media
import fresh_tomatoes

"""All of the following objects will follow this format:
object_name = media.Movie(movie_title, movie_storyline, poster_image,
trailer_youtube). These objects hold the content for teach of the movies
that will be accessed on the fresh_tomatoes.html code"""

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


hitch = media.Movie("Hitch",
                    "Dating coach Alex Hitchens mentors a bumbling client," +
                    " Albert who hopes to win the heart of the glamorous" +
                    " Allegra Cole",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/Hitch_poster.JPG/220px-Hitch_poster.JPG",  # NOQA
                    "https://www.youtube.com/watch?v=dMaq_pfxs-0")

school_of_rock = media.Movie("School of Rock", "Teacher uses " +
                             "music to teach kids",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "A rat helps a boy cook",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "A man travels to the" +
                                " past to meet his heroes",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games", "People watch kids fight" +
                           " to the death",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [avatar, toy_story, hitch, school_of_rock, ratatouille,
          midnight_in_paris, hunger_games]

# Open movies into a new web brwoser using the fresh_tomatoes'
# open_movies_page method.
fresh_tomatoes.open_movies_page(movies)
