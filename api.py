from flask import Flask, json, jsonify, request
from data import data
#name of module that is being called = __name__
app = Flask(__name__)
#/ means home
@app.route('/')

def index():
    return jsonify({"data":data, "message": "success!"}), 200
@app.route('/planetinfo', methods=['GET'])
def planetinfo():
    planet = request.args.get('planet')
    planetdata = next(item for item in data if item['name'] == planet)
    try:
       return jsonify({"planetdata": planetdata, "message": "Success!"}), 200
    except:
        return jsonify({"message": "Planet not found!"}), 400

if __name__ == '__main__':
    app.run(debug=True)

