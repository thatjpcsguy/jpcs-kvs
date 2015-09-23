from flask import Flask, request
import json
import cPickle as pickle
import os

app = Flask(__name__)

@app.route('/project/<project_id>', methods=['GET', 'POST'])
def project(project_id):
    if request.method == 'POST':
        obj = json.loads(request.form['data'])
        pickle.dump(obj, open("data/" + project_id + ".p", "wb"))
	return "success"
    elif request.method == 'GET':
	if os.path.isfile("data/" + project_id + ".p"):
            return json.dumps(pickle.load(open("data/" + project_id + ".p", "rW")))
        else:
            return json.dumps([])


if __name__ == "__main__":
    app.run(port=4000, debug=True, host="0.0.0.0")
