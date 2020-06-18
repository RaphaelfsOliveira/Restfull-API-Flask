from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

if __name__ == "__main__": app.run(debug=True)

@app.route('/')
def home():
    return 'new api'


items = []

class Items(Resource):
    
    def get(self, name=None):
        if name is None:
            return {'items': 'list of items'}
        
        for item in items:
            if item['name'] == name:
                return item
        
        return {'message': 'item not found'}, 404
    
    def post(self, name, price=0):
        if name:
            new_item = {
                'name': name,
                'price': price
            }
            items.append(new_item)
            
            return new_item, 201
        
        return {'message': 'item need name'}, 500
        


api.add_resource(Items, '/items/<string:name>')