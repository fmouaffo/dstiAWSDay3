


import uuid


from flask import Flask
app = Flask(__name__)
my_uuid = uuid.uuid4()
print(str(my_uuid))

@app.route('/Hello')
def hello_world():
    ret = '<p>Hello World! '+my_uuid +' <p>'
    return ret

@app.route('/bye')
def bye_world():
    ret = '<p>Hello World! '+my_uuid +' <p>'
    return ret


if __name__ == '__main__':
    app.run(debug=True, port=5000,  host='0.0.0.0')
