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

    def __str__(self):
        """ Displays the data of each node in the Linked list. """
        current = self.head
        printed = ""
        while current is not None:
            printed += str(current.data) + "\n"
            current = current.next
        return printed
    
    def __len__(self):
        """ Diplays the size of the Linked list. """
        n = 0
        current = self.head
        while current is not None:
            n += 1
            current = current.next
        return n
    
    def __iter__(self):
        """ Define iteration behavior"""
        current = self.head
        while current:
            yield current
            current = current.next

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
    
    def __iter__(self):
        for current in self.linked_list:
            yield current

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
    
    
# Heap sort for books database (max heap to get ascending order)

def max_heapify(books, heap_size, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size and books[left].rate > books[largest].rate:
        largest = left
    if right < heap_size and books[right].rate > books[largest].rate:
        largest = right
    if largest != i:
        books[i], books[largest] = books[largest], books[i]
        max_heapify(books, heap_size, largest)

def build_heap(books):
    heap_size = len(books)
    for i in range ((heap_size//2),-1,-1):
        max_heapify(books,heap_size, i)

def heapsort(books):
    heap_size = len(books)
    build_heap(books)
    for i in range(heap_size-1,0,-1):
        books[0], books[i] = books[i], books[0]
        heap_size -= 1
        max_heapify(books, heap_size, 0)