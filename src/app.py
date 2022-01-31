from flask import Flask, Response
app = Flask(__name__)


@app.route('/')
def rude():
    return "Rude!  You could say /hello first, you know."


@app.route('/hello')
def hello_world():
    # https://stackoverflow.com/questions/25860304/how-do-i-set-response-headers-in-flask
    # solution to issue I had with this thing:
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS/Errors/CORSMissingAllowOrigin
    response = Response('{"message": "Hello World" }')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    # docker only publishes this ip, not sure yet how it is with expose
    app.run(host='0.0.0.0', port=5000)
