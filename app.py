from flask import Flask
app = Flask(__name__)


@app.route('/')
def rude():
    return "Rude!  You could say /hello first, you know."


@app.route('/hello')
def hello_world():
    return {"message": "Hello World"}


if __name__ == '__main__':
    # docker only publishes this ip, not sure yet how it is with expose
    app.run(host='0.0.0.0', port=5000)
