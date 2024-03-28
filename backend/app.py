# backend/app.py
from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(mongo_uri)
db = client.user_db

@app.route('/submit', methods=['POST'])
def submit():
    name = request.json['name']
    email = request.json['email']
    db.users.insert_one({"name": name, "email": email})
    return jsonify({"message": "User information saved"}), 201
