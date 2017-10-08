import webbrowser


class Movie():
    # This class define a movie with 3 attributes: title, poster, trailer

    def __init__(self, title, poster, trailer):
        # the constructor init all the attributes in Class Movie()
        self.title = title
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
