from flask import Flask, jsonify
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


if __name__ == '__main__':
    app.run(debug=True)

