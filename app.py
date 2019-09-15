
from flask import Flask, jsonify, request, render_template 
from shapely.geometry import Polygon

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')    


@app.route('/polygons', methods=['POST'])
def intersect():
    request_data = request.get_json()

    poly1 = []
    poly2 = []

    for coord_pair in request_data[0]["geometry"]["coordinates"][0]:
        poly1.append(tuple(coord_pair))

    for coord_pair in request_data[1]["geometry"]["coordinates"][0]:
        poly2.append(tuple(coord_pair))

    p1 = Polygon(poly1)
    p2 = Polygon(poly2)
    return(jsonify(p1.intersects(p2)))


app.run(port=3000)
