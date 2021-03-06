class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    
    def __str__(self):
        return f"{self.__class__.__name__} {self.name!r} ({self.connected_by})"
    
    def disconnect(self):
        self.connected = False
        print('Disconnected')


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity
    
    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"
    
    def print(self, pages):
        if self.connected:
            print(f"Printing {pages} pages")
            self.remaining_pages -= pages
            return
        print('Your printer is not connected')


printer = Printer('HP DeskJet', 'USB', 800)
print(printer)
printer.print(150)
print(printer)
printer.disconnect()
printer.print(30)
print(printer.remaining_pages)
        
        