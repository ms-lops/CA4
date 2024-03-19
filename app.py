import os
import pymongo
from flask import Flask, render_template

app = Flask(__name__)

def get_rows(database_name, collection_name, auth_source):
    
    username = os.environ.get('MONGODB_USERNAME')
    password = os.environ.get('MONGODB_PASSWORD')
    print(f"MONGODB_USERNAME: {username}")
    print(f"MONGODB_PASSWORD: {password}")

    if not username or not password:
        raise ValueError("MongoDB username or password not provided in environment variables")

    # MongoDB connection URI with authentication
    # Construct MongoDB connection URI
    uri = f"mongodb://{os.environ['MONGODB_USERNAME']}:{os.environ['MONGODB_PASSWORD']}@localhost:27017/?authSource=admin"


    # Connect to MongoDB
    client = pymongo.MongoClient(uri)
    print(client);
    # Select database
    db = client[database_name]

    # Select collection
    collection = db[collection_name]

    # List all documents in the collection
    documents = [doc for doc in collection.find()]
    return documents

@app.route('/')
def index():
    try:
        database_name = "Database"  
        collection_name = "Collection"  
        auth_source = "authSource=admin"  # Change this to your MongoDB authentication database
        rows = get_rows(database_name, collection_name, auth_source)
        print(rows)
        return render_template('index.html', rows=rows)
    except Exception as e:
        return str(e), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
