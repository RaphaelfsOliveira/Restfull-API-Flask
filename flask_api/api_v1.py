from flask import Flask, jsonify, request
from flask.views import MethodView

app = Flask(__name__)

if __name__ == "__main__": app.run(debug=True)


@app.route('/')
def home():
    return 'development, active, test'

stores = [
    {
        'name': 'The Store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            },
        ]
    },
]


class StoresAPI(MethodView):

    def get(self, name=None):
        if name is None:
            return jsonify({'stores': stores})
        
        for store in stores:
            if name == store['name']:
                return jsonify(store)
            
        return jsonify({'error': 'store not found'}), 404

    def post(self):
        request_data = request.get_json()
        if request_data:
            new_store = {
                "name": request_data['name'],
                "items": []
            }
            stores.append(new_store)

            return jsonify(new_store)
        
        return jsonify({'error': 'need store data'}), 500

stores_view = StoresAPI.as_view('stores')
app.add_url_rule('/stores/', view_func=stores_view, methods=['GET', 'POST'])
app.add_url_rule('/stores/<name>/', view_func=stores_view, methods=['GET'])


class StoresItemsAPI(MethodView):

    def get(self, name, item=None):
        for store in stores:
            if name == store['name']:
                if item is None:
                    return jsonify({'items': store['items']})
                
                for store_item in store['items']:
                    if item == store_item['name']:
                        return jsonify(store_item)

                return jsonify({'error': 'item not found'}), 404
        
        return jsonify({'error': 'store not found'}), 404
    
    def post(self, name):
        for store in stores:
            if name == store['name']:
                request_data = request.get_json()
                if request_data:

                    new_item = {
                        "name": request_data['name'],
                        "price": request_data['price']
                    }
                    store['items'].append(new_item)

                    return jsonify(new_item)
                
                return jsonify({'error': 'need item data'}), 500

        return jsonify({'error': 'store not found'}), 404

stores_items_view = StoresItemsAPI.as_view('items')
app.add_url_rule('/stores/<name>/items/', view_func=stores_items_view, methods=['GET', 'POST'])
app.add_url_rule('/stores/<name>/items/<item>/', view_func=stores_items_view, methods=['GET'])