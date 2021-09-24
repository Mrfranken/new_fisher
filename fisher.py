from app import create_app
from flask import make_response





app = create_app()

@app.route('/hello/')
def hello():
    # return 'hello, Vince'
    headers = {
        'content-type': 'text/plain',
        'location': 'https://www.google.com'
    }
    resp = make_response('<html></html>', 301)
    resp.headers = headers
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
