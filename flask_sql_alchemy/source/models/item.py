from db import db


class Item(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    price = db.Column(db.Float(precision=2))
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def to_json(self):
        return {'id': self.id, 'name': self.name, 'price': self.price}

    @classmethod
    def search_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def _all(cls):
        return cls.query.all()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        