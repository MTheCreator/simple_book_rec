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


"""import json

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = ['Genre1', 'Genre2', 'Genre3', 'Genre4', 'Genre5']

data = []

for i in range(len(list1)):
    item = {
        'id': list1[i],
        'name': list2[i],
        'genres': list3[i]
    }
    data.append(item)

with open('data.json', 'w') as file:
    json.dump(data, file)"""


