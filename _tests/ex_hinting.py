from typing import List # Tuple, Set, etc ...

class Book:
    def __init__(self, name: str):
        self.name = name
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.name}"

class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__} with {len(self.books)} books"


book = Book('Memórias do Subsolo')
book2 = Book('Crime e Castigo')
print(book, book2)

book_shelf = BookShelf([book, book2])

print(book_shelf)