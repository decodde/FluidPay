from flask import Flask, render_template, request, redirect, url_for,jsonify
from pymongo import MongoClient
from available_ports import getPorts;
import json
app = Flask(__name__, static_url_path='/static')

client = MongoClient('localhost', 27017)
db = client['mydatabase']

@app.route('/')
def index():
    # Retrieve all documents from the collection
    data = list(db.my_collection.find())
    _availablePorts = getPorts()
    print(_availablePorts)
    _data =  _availablePorts
    return render_template('index.html', data=_data)

@app.route('/add', methods=['POST'])
def add():
    # Insert a new document into the collection
    new_doc = {'name': request.form['name'], 'email': request.form['email']}
    db.my_collection.insert_one(new_doc)
    return redirect(url_for('index'))

@app.route('/edit/<id>', methods=['POST'])
def edit(id):
    # Update an existing document in the collection
    db.my_collection.update_one({'_id': ObjectId(id)}, {'$set': {'name': request.form['name'], 'email': request.form['email']}})
    return redirect(url_for('index'))

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    # Delete a document from the collection
    db.my_collection.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))


@app.route("/getAvailablePorts", methods=["GET"])
def availablePorts():
    availPorts = getPorts()
    print(availPorts)
    return availPorts

if __name__ == '__main__':
    app.run(debug=True)
