from flask import Flask, request, send_from_directory
from datetime import datetime

app = Flask(__name__)

# Define the route for the root endpoint
@app.route('/')
def index():
    # Serve the index.html file
    return send_from_directory('.', 'index.html')













if __name__ == "__main__":
    app.run(debug=True)
