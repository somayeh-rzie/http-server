# from flask import Flask, request, jsonify
# from pymongo import MongoClient

# app = Flask(__name__)
# client = MongoClient('mongodb://localhost:27017/')
# db = client['mydatabase']

# @app.route('/', methods=['POST'])
# def post_data():
#     # data = request.get_json()

#     # main_dict = data['main']
#     # input_dict = data['input']

#     # for r in input_dict:
#     #     inner_join = {key: r[key] for key in main_dict.keys() if key in r}
#     #     db['collection'].insert_one(inner_join)

#     return '', 200

# @app.route('/', methods=['GET'])
# def get_data():
#     data = []
#     results = db['collection'].find()
#     for result in results:
#         data.append(result)

#     return jsonify(data), 200

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


# from flask import Flask, request, jsonify
# import json
# import uuid

# app = Flask(__name__)

# data_storage = {}

# @app.route('/', methods=['POST'])
# def post_data():
#     data = request.get_json()
#     main_dict = data['main']
#     input_dict = data['input']

#     for r in input_dict:
#         inner_join = {key: r[key] for key in main_dict.keys() if key in r}

#         key = str(uuid.uuid4())

#         data_storage[key] = inner_join

#     return '', 200

# @app.route('/', methods=['GET'])
# def get_data():
#     return jsonify(data_storage), 200

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)



from flask import Flask, request, jsonify
import json
import uuid

app = Flask(__name__)

data_storage_file = 'data.json'

import datetime


@app.route('/', methods=['POST'])
def post_data():
    data = request.get_json()
    main_dict = data['main']
    input_dict = data['input']

    for r in input_dict:
        inner_join = {key: r[key] for key in main_dict.keys() if key in r}
        inner_join["time"] = datetime.datetime.now().strftime('%Y-%m-%d') + ' ' + datetime.datetime.now().strftime('%H:%M:%S')
        
        key = str(uuid.uuid4())

        with open(data_storage_file, 'a') as file:
            json.dump({key: inner_join}, file)
            file.write('\n')

    return '', 200

@app.route('/', methods=['GET'])
def get_data():
    values = []
    with open(data_storage_file, 'r') as file:
        for line in file:
            data = json.loads(line)
            values.extend(data.values())

    return jsonify(values), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)