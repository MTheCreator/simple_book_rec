class user(object):
    def __init__(self, ID: int, Name: str, Genres: list):
        self.id = ID
        self.name = Name
        self.genres = Genres

class Book(object):
    def __init__(self, title: str, author: str, genre: str, rating: float, ISBN: int):
        self.title= title
        self.author= author
        self.genre= genre
        self.rating= rating
        self.ISBN= ISBN

Ratings = dict()

