


import uuid


from flask import Flask
app = Flask(__name__)
my_uuid = uuid.uuid4
print(str(my_uuid))

@app.route('/titanic_wipeout')
def hello_world():
    return 'Hello World!'

@app.route('/titanic_predict')
def bye_world2():
    return 'Bye World!'

@app.route('/titanic_train')
def bye_world3():
    return 'Bye World!'


if __name__ == '__main__':
    app.run(debug=True, port=5000,  host='0.0.0.0')