from app import create_app

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

app = create_app()

if __name__ == '__main__':
    print(id(app))
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
