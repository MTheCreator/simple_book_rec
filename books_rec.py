class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        """ Returns True if the Linked list is empty, else None. """
        return self.head is None

    def append(self, data):
        """ Adds a node to the end of the Linked list. """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        """ Adds a node to the beggining of the Linked list. """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """ Deletes the first occurence of a node with the inputed data if found. """
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        """ Displays the data of each node in the Linked list. """
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def is_empty(self):
        """ Returns True if the stack is empty, else False """
        return self.linked_list.is_empty()

    def push(self, data):
        """ Pushes a node in the beggining of a stack. """
        self.linked_list.prepend(data)

    def pop(self):
        """ Pops a node from the beggining of a stack whilst returning the data in the popped node. """
        if self.is_empty():
            raise IndexError("Stack is empty")
        top_data = self.linked_list.head.data
        self.linked_list.delete(top_data)
        return top_data

class Queue:
    def __init__(self):
        self.linked_list = LinkedList()

    def is_empty(self):
        """ Returns True if the queue is empty, else False """
        return self.linked_list.is_empty()

    def enqueue(self, data):
        """ Adds a node to the tail of the queue. """
        self.linked_list.append(data)

    def dequeue(self):
        """ Removes a node from the head of the queue, returns the data in the removed node. """
        if self.is_empty():
            raise IndexError("Queue is empty")
        front_data = self.linked_list.head.data
        self.linked_list.delete(front_data)
        return front_data


class user:
    def __init__(self, id: int, name: str, fav_genres: LinkedList, library: LinkedList, whishlist: LinkedList):
        self.id =id
        self.name = name
        self.fav_genres = fav_genres
        self.library = library
        self.whishlist = whishlist


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



