import json 
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# TODO: Add authentication
@app.route('/autosuggest', methods=['POST'])
def autosuggest():
  if request.method == "POST":
    # Receives the data in JSON format in a HTTP POST request
    if not request.is_json:
        return "<p>The content isn't of type JSON<\p>"
    else: 
      data = json.loads(request.data)
      if 'query' in data:
        query = data['query']
        conn = sqlite3.connect("dashworks.db")
        db_query = f"SELECT id, query, date FROM collection WHERE query LIKE '{query}%' LIMIT 10"
        cur = conn.cursor()
        results = cur.execute(db_query).fetchall()
        return jsonify(results)
      abort(400)

if __name__=='__main__':
    app.run()