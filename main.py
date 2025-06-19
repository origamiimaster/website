"""Main file to run for the server"""

from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='')


# @app.route('/')
# def hello():
#     return "Hello World"
#
@app.route('/<path:path>')
def send_index(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run()
