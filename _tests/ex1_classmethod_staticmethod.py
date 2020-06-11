class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        return sum([item['price'] for item in self.items])

    @classmethod
    def franchise(cls, store):
        return cls(f"{store.name} - franchise")

    @staticmethod
    def store_details(store):
        return "{}, total stock price: {}".format(store.name, store.stock_price())

store = Store('Test')
store2 = Store('Amazon')
store2.add_item('Keyboard', 160)

print(
    Store.franchise(store),
    Store.franchise(store2),

    Store.store_details(store),
    Store.store_details(store2),

)
