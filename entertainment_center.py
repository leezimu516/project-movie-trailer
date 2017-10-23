import media
import fresh_tomatoes


# call constructor to initialize the movie info
# (movie_title, movie_storyline, poster_image, trailer_youtube)
toy_story = media.Movie("toy story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

catch_me_if_you_can = media.Movie("Catch Me If You Can",
                                  "American biographical crime film",
                                  "https://upload.wikimedia.org/wikipedia/en/thumb/4/4d/Catch_Me_If_You_Can_2002_movie.jpg/220px-Catch_Me_If_You_Can_2002_movie.jpg",
                                  "https://www.youtube.com/watch?v=71rDQ7z4eFg")

the_godfather = media.Movie("The Godfather",
                            "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BZTRmNjQ1ZDYtNDgzMy00OGE0LWE4N2YtNTkzNWQ5ZDhlNGJmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UY268_CR3,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=sY1S34973zA")
# toy_story.show_trailer()
# print(toy_story.title)
MOVIES = [toy_story, catch_me_if_you_can, the_godfather]
fresh_tomatoes.open_movies_page(MOVIES)
