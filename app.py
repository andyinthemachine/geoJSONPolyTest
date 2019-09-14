
# import sys;
# print (sys.path)
from flask import Flask, jsonify, request, render_template  # capitalize class, lowercase method 

app = Flask(__name__)

stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

c
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})       


@app.route('/polygons', methods=['POST'])
def intersect():
    request_data = request.get_json()
    # new_poly = {
    #     'name': request_data['name'],
    #     'items': []
    # }
    # stores.append(new_store)
    print(request_data)
    return jsonify(request_data)


@app.route('/store/<string:name>', methods=['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})





app.run(port=3000)
