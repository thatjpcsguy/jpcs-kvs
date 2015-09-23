from flask import Flask, request, jsonify
import json
import cPickle as pickle
import os

app = Flask(__name__)

@app.route('/<endpoint>/<key_id>', methods=['GET', 'POST'])
def project(endpoint, key_id):
    directory = "data/" + endpoint
    filename = directory + "/" + key_id + ".p"

    if request.method == 'POST':
        if not os.path.exists(directory):
            os.makedirs(directory)
        obj = json.loads(request.form['data'])
        pickle.dump(obj, open(filename, "wb"))
	return jsonify({"data": "success"})
    elif request.method == 'GET':
	if os.path.isfile(filename):
            return jsonify({"data": pickle.load(open(filename, "rW"))})
        else:
            return jsonify({"data": None})


if __name__ == "__main__":
    app.run(port=4000, debug=True, host="0.0.0.0")
