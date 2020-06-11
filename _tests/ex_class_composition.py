class BookShelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f"{self.__class__.__name__} with {len(self.books)} books"


class Book:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"{self.__class__.__name__} {self.name}"


book = Book('Memórias do Subsolo')
book2 = Book('Crime e Castigo')
print(book, book2)

book_shelf = BookShelf(book, book2)

print(book_shelf)