from flask import Flask, request, jsonify
from flask_cors import CORS

server1 = Flask(__name__)
@server1.route("/hello/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    server1.run(debug=True)