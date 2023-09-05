from flask import Flask, render_template, request, send_file, send_from_directory
from flask_cors import CORS
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)
cors = CORS(app)

cred = credentials.Certificate('book-my-tickets.json')
firebase_admin.initialize_app(cred)
firestore_client = firestore.client()

@app.route('/movies', methods=['GET'])
def fetchMovies():
    foundMovies = firestore_client.collection('movies').get()
    if len(foundMovies) != 0:
        return {'data' : [i.to_dict() for i in foundMovies]} 
    return {}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)    