class Book:

    def __init__(self,title,author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Book title: {self.title}")
        print(f"Name of author: {self.author}")

book1 = Book("Eattavum priyapetta ninnod","Nimna vijay")
book1.display()