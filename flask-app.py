from flask import Flask, request, send_from_directory, jsonify
from datetime import datetime
import os

# Check if messages.py exists, if not, create it with an empty dictionary
if not os.path.exists('messages.py'):
    with open('messages.py', 'w') as f:
        f.write('chat_data = {}\n')

# Import chat_data from messages.py
from messages import chat_data

app = Flask(__name__, static_url_path='')


@app.route('/<room>')
def room_redirect(room):
    # This will redirect to the main chatroom view with the given room name
    return send_from_directory('.', 'index.html')


@app.route('/chat/<room>', methods=['GET'])
def get_chat(room):
    # Retrieve chat messages for the specified room
    chat = chat_data.get(room, [])

    # Format the chat for display
    formatted_chat = "\n".join(
        ["[{date}] {username}: {message}".format(**entry) for entry in chat])

    return formatted_chat


@app.route('/api/chat/<room>', methods=['POST'])
def post_chat(room):
    # Retrieve the username and message from the form data
    username = request.form.get('username')
    message = request.form.get('msg')

    # Format the current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Append the new message to chat_data
    chat_data.setdefault(room, []).append({
        "date": current_time,
        "username": username,
        "message": message
    })

    # Save the updated chat_data back to messages.py
    with open('messages.py', 'w') as f:
        f.write('chat_data = {}\n'.format(repr(chat_data)))

    return jsonify(success=True)


if __name__ == "__main__":
    app.run(debug=True)
