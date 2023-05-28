# book class

def verify_author(author: str):
    if type(author) != str:
        raise TypeError("Author must be string")

def verify_desc(desc: str):
    if type(desc) != str:
        raise TypeError("Description must be string")

def verify_genre(genres: list):
    is_string = lambda genre: type(genre) == str
    if type(genres) != list:
        raise TypeError("Genres must be list of strings")
    for genre in genres:
        if not is_string(genre):
            raise TypeError("Genres must be list of strings")

def verify_isbn(isbn: str):

def verify_rating(rating: float):

def verify_title(title: str):

def verify_total_ratings(total: int):


# user class

def verify_id(user_id: int):
    pass

def verify_name(name: str):
    pass

def verify_fav_genres(genres: "LinkedList"):
    pass

