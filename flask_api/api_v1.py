from flask import Flask
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


@app.route('/stores/', methods=['GET', 'POST'])
@app.route('/stores/<name>/', methods=['GET'])
def get_or_create_stores(name=None):
    
    return f'{stores} {name}'


@app.route('/stores/<name>/items/', methods=['GET', 'POST'])
@app.route('/stores/<name>/items/<item>/', methods=['GET'])
def get_or_create_items(name, item=None):
    
    return 'get_or_create_items'