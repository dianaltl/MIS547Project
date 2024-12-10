from flask import Flask, request, render_template
from pymongo import MongoClient
import os

database = "csaf_data"  # Replace with your actual database name
MONGO_URI = f"mongodb+srv://doadmin:g82e75ZHyKn3406G@group3-db-bab860b8.mongo.ondigitalocean.com/{database}?tls=true"

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client['csaf_data']
collection = db['gold_standard']

@app.route('/', methods=['GET', 'POST'])
def search():
    query = ""
    results = []

    if request.method == 'POST':
        query = request.form.get('query')
        # Simple MongoDB search by field 'name'
        results = collection.find({"name": {"$regex": query, "$options": "i"}})

    return render_template('search.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)
