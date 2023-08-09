from flask import Flask, request, send_from_directory
from datetime import datetime

app = Flask(__name__)

# Create a chat data dictionary to hold chat messages for different rooms.
chat_data = {

}


# Define the route for the root endpoint
@app.route('/')
@app.route('/<room>')# Serve the index.html file, regardless of whether a room is specified.
def index():
    # Serve the index.html file
    return send_from_directory('.', 'index.html')


# Define the GET endpoint to retrieve chat messages for a specific room.
@app.route('/chat/<room>', methods=['GET'])
def get_chat(room):
    # Fetch chat messages for the specified room from the chat_data.
    # If no messages exist for that room, return an empty list.
    chat = chat_data.get(room, [])

    # Convert each chat entry to the specified string format.
    formatted_chat = "\n".join(["[{date}] {username}: {message}".format(**entry) for entry in chat])

    # Return the formatted chat messages as a response.
    return formatted_chat











if __name__ == "__main__":
    app.run(debug=True)
