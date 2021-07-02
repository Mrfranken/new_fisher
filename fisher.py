from flask import Flask, make_response, jsonify

__author__ = 'Vince'

app = Flask(__name__)
app.config.from_object('config')

# @app.route('/hello/')
# def hello():
#     # return 'hello, Vince'
#     headers = {
#         'content-type': 'text/plain',
#         'location': 'https://www.google.com'
#     }
#     resp = make_response('<html></html>', 301)
#     resp.headers = headers
#     return resp

from app.web import book

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
