from flask import Flask, jsonify
from cfhelloworld.helloworld import hw
app = Flask(__name__)

app.register_blueprint(hw, url_prefix = '/helloworld')

@app.route('/')
def hello_function():
    return jsonify({"hello":"world"})




if __name__ == '__main__':
    app.run()