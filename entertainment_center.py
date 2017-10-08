import media
import fresh_tomatoes


# create 6 movie instances
movie1 = media.Movie(
    "Toy Story 3",
    "https://i.ytimg.com/vi_webp/XSvTH668d50/movieposter.webp",
    "https://www.youtube.com/watch?v=ZZv1vki4ou4"
    )
movie2 = media.Movie(
    "Monsters University",
    "https://i.ytimg.com/vi_webp/-2n6esRBs2k/movieposter.webp",
    "https://www.youtube.com/watch?v=QxrQ6BaijAY"
    )
movie3 = media.Movie(
    "Finding Nemo",
    "https://i.ytimg.com/vi_webp/EDTaekvVbSI/movieposter.webp",
    "https://www.youtube.com/watch?v=2zLkasScy7A"
    )
movie4 = media.Movie(
    "Cars",
    "https://i.ytimg.com/vi_webp/_Xbh2ivT0gg/movieposter.webp",
    "https://www.youtube.com/watch?v=SbXIj2T-_uk"
    )
movie5 = media.Movie(
    "Ratatouille",
    "https://i.ytimg.com/vi_webp/eh62Ri60lXI/movieposter.webp",
    "https://www.youtube.com/watch?v=niD-jahFURU"
    )
movie6 = media.Movie(
    "Wall-E",
    "https://i.ytimg.com/vi_webp/5RcNwlq7JSw/movieposter.webp",
    "https://www.youtube.com/watch?v=8-_9n5DtKOc"
    )

# create movies list
movies = [movie1, movie2, movie3, movie4, movie5, movie6]

# call function open_movies_page() to create a web page
fresh_tomatoes.open_movies_page(movies)
