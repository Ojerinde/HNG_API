from flask import Flask, jsonify, request
from flask_cors import CORS

import string

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


@app.route('/', methods=['POST'])
def post():
    operator = request.json['operation_type']
    x = request.json['x']
    y = request.json['y']

    operation_type = operator.lower()

    result = 0
    if operation_type in ['addition', 'subtraction', 'multiplication', 'division']:
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
    else:
        words = operation_type.translate(str.maketrans('', '', string.punctuation)).split()
        new_operator = ''
        for word in words:
            if word in ['add', 'addition', 'sub','subtract', 'minus','subtraction', 'plus', 'sum', 'multiply', 'times', "mul", "multiplication" ]:
                new_operator = word
                break
            
        operation_type = new_operator
        numbers = []   
        for word in words:
            if word.isnumeric():
                numbers.append(int(word))

        result = 0
        for num in numbers:
            if new_operator == 'add' or new_operator == 'addition' or new_operator == 'plus' or new_operator == 'sum':
                result += num
            elif new_operator == 'mul' or new_operator == 'multiply' or new_operator == 'times' or new_operator == 'multiplication':
                result *= num
            elif new_operator == 'sub' or new_operator == 'subtract' or new_operator == 'minus' or new_operator == 'subtraction':
                result -= num
            
    return jsonify({
        "slackUsername": "JoelOjerinde",
        "operation_type": operation_type,
        "result": result
    }), 200


if __name__ == '__main__':
    app.run(debug=True)

