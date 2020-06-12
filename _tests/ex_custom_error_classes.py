class TooManyPagesReadError(ValueError):
    pass


class Book:

    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0
    
    def __repr__(self):
        return (
            F"<{self.__class__.__name__} {self.name}, read {self.pages_read} pages out of {self.page_count}>"
        )
    
    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages."
            )
        self.pages_read += pages
        print(f"You have now read {pages}, {self.page_count - pages} pages left.")


python_book = Book('python 101', 150)

print(python_book)

try:
    python_book.read(50)
    python_book.read(135)
except TooManyPagesReadError as error:
    print(error)