from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# Set Cors for all resources and all origins
CORS(app, resources={"*": {"origins": "*"}})

# Add Request methods
@app.after_request
def after_request(response):
    response.headers.add("Allow-Control-Allow-Headers",
                         "Content-Type,Authorization,true")
    response.headers.add("Access-Control-Allow-Methods",
                         "GET,PATCH,POST,PUT,DELETE,OPTIONS")
    return response




@app.route('/')
def get():
    return jsonify({
        'slackUsername': 'JoelOjerinde',
        'age': 20,
        'bio': 'I am a Full stack developer and an Electrical and Electronics Engineering student at the University of Ilorin',
        'backend': True,
    })
# “Can you please add the following numbers together - 13 and 25.”

@app.route('/', methods=['POST'])
def post():
    operation_type = request.json['operation_type']
    x = request.json['x']
    y = request.json['y']

    result = 0
    if operation_type == 'addition':
        result = x + y
    elif operation_type == 'subtraction':
        result = x - y
    elif operation_type == 'multiplication':
        result = x * y
    elif operation_type == 'division':
        result = x / y
    else:
        result = 'Invalid Operation'

    return jsonify({
        "slackUsername": "JoelOjerinde",
        "operation_type": operation_type,
        "result": result
    }), 200


if __name__ == '__main__':
    app.run()

