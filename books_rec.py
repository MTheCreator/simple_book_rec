from usefulclasses import Node, LinkedList, Stack, Queue

class user:
    def __init__(self, id: int, name: str, fav_genres: LinkedList, library: Queue, wishlist: Queue):
        self.id =id
        self.name = name
        self.fav_genres = fav_genres
        self.library = library
        self.wishlist = wishlist
        
    def read_book(self):
        pass
    def rate_book(self):
        pass
    def add_to_wishlist(self):
        pass

    def search_author(self):

    def search_book(self):

    def search_genre(self):

    def search_keywords(self):

    def most_checked_genre(self):

    def most_checked_author(self):



class book:
    def __init__(self, author: str, desc: str, genre: list, isbn: str, pages: int, rating: int, title: str, totalratings: int):
        self.author = author                    # Initialisation of the author of the book
        self.desc = desc                        # Short description of the content of the book
        self.genre = genre                      # List that provides the many genres that the book lies within 
        self.isbn = int(isbn)                   # ID of the book, used to ease the access to the book objects
        self.pages = pages                      # Number of pages in each book, other mean of recommendation
        self.rating = rating                    # A ratiing on 5, with 5 being the most recommendable and 0 the least
        self.title = title                      # Initialisation of the title of the book
        self.totalratings = totalratings        # The total number of given ratings to the book, popularity credential



