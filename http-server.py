from flask import Flask, request, jsonify
import sqlite3
import json

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

    # main rectangle
    main = data['main']

    # input rectangles
    rectangles = data['input']
    
    # check intersection with main for each rectangle in input
    for r in rectangles:

        if(check_intersection(main, r)):

            # if has intersection then store in database
            sql = "INSERT INTO filtering_service (" + ", ".join(r.keys()) + " ,time) VALUES (" + ", ".join("?" * len(r.keys())) + ", datetime('now'))"

            values = tuple(r.values())

            c.execute(sql, values)
    
    conn.commit()

    return '', 200


@app.route('/', methods=['GET'])
def get_data():

    c.execute("SELECT x, y, width, height, time FROM filtering_service")
    rows = c.fetchall()

    data=[]

    for row in rows:
        d = {
            'x': row[0],
            'y': row[1],
            'width': row[2],
            'height': row[3],
            'time': row[4]
        }
        data.append(d)

    # prevent alphanumerically sorting keys
    response_body = json.dumps(data, sort_keys=False)

    return response_body, 200


def check_intersection(main_rect, input_rect):
    
    # create the main rectangle
    main_rect = create_rectangle(main_rect)

    # create each input rectangle
    input_rect = create_rectangle(input_rect)

    # check for intersection

    if main_rect.intersects(input_rect):
        return True
    else:
        return False

def create_rectangle(rect_data):

    x = rect_data['x']
    y = rect_data['y']
    width = rect_data['width']
    height = rect_data['height']

    # create a rectangle object using given dimensions
    return Rectangle(x, y, width, height)


class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def intersects(self, other_rect):
        # check 4 situations which two rectangles can't have intersection
        return not (self.x + self.width <= other_rect.x or
                    other_rect.x + other_rect.width <= self.x or
                    self.y + self.height <= other_rect.y or
                    other_rect.y + other_rect.height <= self.y)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
