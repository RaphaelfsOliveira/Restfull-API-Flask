from flask import Flask, jsonify, request
from flask.views import MethodView

app = Flask(__name__)

if __name__ == "__main__": app.run(debug=True)


@app.route('/')
def home():
    return 'development, active, test'

stores = [
    {
        'name': 'Max Store',
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
        else:
            for store in stores:
                if name == store['name']:
                    return jsonify(store)
                else:
                    return jsonify({'error': 'store not found'})

    def post(self):
        request_data = request.get_json()
        
        new_store = {
            "name": request_data['name'],
            "items": []
        }
        stores.append(new_store)

        return jsonify(new_store)

stores_view = StoresAPI.as_view('stores')
app.add_url_rule('/stores/', view_func=stores_view, methods=['GET', 'POST'])
app.add_url_rule('/stores/<name>/', view_func=stores_view, methods=['GET'])


class StoresItemsAPI(MethodView):

    def get(self, name, item=None):
        if item is None:
            return 'list of items'
        else:
            return 'one items'
    
    def post(self, name):
        return 'create one item'

stores_items_view = StoresItemsAPI.as_view('items')
app.add_url_rule('/stores/<name>/items/', view_func=stores_items_view, methods=['GET', 'POST'])
app.add_url_rule('/stores/<name>/items/<item>/', view_func=stores_items_view, methods=['GET'])