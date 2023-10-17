from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']

@app.route('/', methods=['POST'])
def post_data():
    data = request.get_json()

    main_dict = data['main']
    input_dict = data['input']

    for r in input_dict:
        inner_join = {key: r[key] for key in main_dict.keys() if key in r}
        db['collection'].insert_one(inner_join)

    return '', 200

@app.route('/', methods=['GET'])
def get_data():
    data = []
    results = db['collection'].find()
    for result in results:
        data.append(result)

    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)