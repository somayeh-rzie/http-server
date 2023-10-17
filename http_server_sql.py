from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# create SQLite database
conn = sqlite3.connect('filtering_service.db',check_same_thread=False)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS filtering_service
             (x INT, y INT, width INT, height INT, time TEXT)''')
conn.commit()

@app.route('/', methods=['POST'])
def post_data():
    data = request.get_json()

    main_dict = data['main']
    input_dict = data['input']

    for r in input_dict:
        
        inner_join = {key: r[key] for key in main_dict.keys() if key in r}

        print(inner_join)

        # c.execute("INSERT INTO database VALUES (?, ?, ?, ?, datetime('now'))",
        #           (rectangle['x'], rectangle['y'], rectangle['width'], rectangle['height']))

        sql = "INSERT INTO filtering_service (" + ", ".join(inner_join.keys()) + " ,time) VALUES (" + ", ".join("?" * len(inner_join.keys())) + ", datetime('now'))"

        print(sql)

        values = tuple(inner_join.values())

        print(values)

        c.execute(sql, values)
    
    conn.commit()

    return '', 200

@app.route('/', methods=['GET'])
def get_data():
    c.execute("SELECT x, y, width, height, time FROM filtering_service")
    rows = c.fetchall()

    data = []
    for row in rows:
        d = {
            'x': row[0],
            'y': row[1],
            'width': row[2],
            'height': row[3],
            'time': row[4]
        }
        data.append(d)

    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)