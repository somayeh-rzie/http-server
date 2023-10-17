from flask import Flask, request, jsonify
import json
import uuid
import datetime

app = Flask(__name__)

# file which we store data in
data_storage_file = 'data.json'


@app.route('/', methods=['POST'])
# method for post
def post_data():
    # get json from the request
    data = request.get_json()
    # split into main and input part
    main_dict = data['main']
    input_dict = data['input']

    # for each member of input_dict we calculate the inner join of input and main
    # and then add time to it
    for r in input_dict:
        inner_join = {key: r[key] for key in main_dict.keys() if key in r}
        inner_join["time"] = datetime.datetime.now().strftime('%Y-%m-%d') + ' ' + datetime.datetime.now().strftime('%H:%M:%S')
        
        # since the data is unstructured we use a pair of key and value to store data in the file
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
            # we just need values the key is not important
            values.extend(data.values())

    return jsonify(values), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)