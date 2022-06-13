from flask import Flask, request, jsonify
import os
os.chdir(r"C:\Users\minem\OneDrive\Desktop\Machine learning Toxic classification\Toxic_classification_app\toxicapp\lib\DebugPurposes")
print(os.getcwd())
app = Flask(__name__)


@app.route('/api', methods=['GET'])
def hello_world():

    d = {}

    d['Query'] = str(request.args['Query'])

    return jsonify(d)


if __name__ == '__main__':
    app.run(port=5001, debug=True)
# app = Flask(__name__)


# @app.route('/')
# @app.route('/hello')
# def hello():
#     return "Hello World!"


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5001, debug=True)
