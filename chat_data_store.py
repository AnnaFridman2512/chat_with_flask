# chat_data_store.py

chat_data = {}


def save_message(room, username, message, current_time):
    """Save a message for a specific room."""

    # If room doesn't exist, create it.
    if room not in chat_data:
        chat_data[room] = []

    # Append the new message.
    chat_data[room].append({
        "date": current_time,
        "username": username,
        "message": message
    })


def get_messages(room):
    """Retrieve messages for a specific room."""
    return chat_data.get(room, [])
