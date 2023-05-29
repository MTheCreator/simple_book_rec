from usefulclasses import LinkedList
# BOOK CLASS

def verify_author(author: str):
    if type(author) != str:
        raise TypeError("Author must be string")

def verify_desc(desc: str):
    if type(desc) != str:
        raise TypeError("Description must be string")
    
def verify_genre(genre: str):
    if type(genre) != str:
        raise TypeError("Genre must be of type string")

def verify_genre_list(genres: list):
    if type(genres) != list:
        raise TypeError("Genres must be list of strings")
    for genre in genres:
        verify_genre(genre)

def verify_isbn(isbn: str):
    if type(isbn) != str:
        raise TypeError("ISBN must be string of numbers")
    
def verify_rating(rating: float):
    if type(rating) != float:
        raise TypeError("Rating must be of type float")
    elif rating < 0 or rating > 5:
        raise ValueError("Rating must be between 0 and 5")

def verify_title(title: str):
    if type(title) != str:
        raise TypeError("Title must be string")

def verify_total_ratings(total: int):
    if type(total) != int:
        raise TypeError("Total ratings must be of type int")
    elif total < 0:
        raise ValueError("Total ratings must be positive")

def verify_book(author: str, desc: str, genre: list, isbn: str, title: str, rating: float, total_ratings: int):
    verify_author(author)
    verify_desc(desc)
    verify_genre_list(genre)
    verify_isbn(isbn)
    verify_title(title)
    verify_rating(rating)
    verify_total_ratings(total_ratings)
    
# USER CLASS

def verify_id(user_id: int):
    if type(user_id) != int:
        raise TypeError("User id must be of type int")
    elif user_id < 0:
        raise ValueError("User id must be a positive value")

def verify_name(name: str):
    if type(name) != str:
       raise ValueError("Name must be of type string")

def verify_fav_genres(genres: 'LinkedList'):
    if type(genres) != LinkedList:
        raise TypeError("List of genres must be of type linked list")
    for node in genres:
        if type(node.data) != str:
            raise TypeError("Genre must be of type string")
        
def verify_user(user_id: int, name: str, genres: 'LinkedList'):
    verify_id(user_id)
    verify_name(name)
    verify_fav_genres(genres)

def verify_rate(rate: int):
    if type(rate) != int:
        raise TypeError("Rate value must be int")
    elif rate < 0 or rate > 5:
        raise ValueError("Rate must be between 0 and 5")

def verify_lower_higher(lower: int, higher: int):
    if type(lower) != int:
        raise TypeError("Lower must be of type int")
    if type(higher) != int:
        raise TypeError("Higher must be of type int")
    elif lower > higher:
        raise ValueError("Lower must be less than Higher")
    elif lower < 0:
        raise ValueError("Lower must be positive")