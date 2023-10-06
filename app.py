from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import pyrebase
from pymongo import MongoClient
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY','1324456789')
client = MongoClient(os.getenv('mongostr'), serverSelectionTimeoutMS=60000)
db = client[""]