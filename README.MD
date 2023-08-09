The goal of this task is to write a back end chat service using Flask.

A simple HTML/JS front end client that uses the service is provided - index.html
The service exposes three APIs:

1. "GET /<room>"
Will return the static HTML (the provided front end), regardless of the room provided.

2. "POST /chat/<room>"
Accepts a chat line from a user:

Will accept 2 form data fields - `username` and `message`. 
Will save date, time, username and message per room.
3. "GET /chat/<room>"
Returns the full chat in a room:

Chat formatted as a list of "\n" delimited lines (1 per message).
Each line formatted according to the example:
"[2018-02-25 14:00:51] omri: hi everybody!"
Work plan
A suggested implementation order:

Implement Flask app that returns the static HTML on "GET /".
Add "GET /<room>" (it should work the same as step 1).
Implement "GET /chat/<room>", and test it with mock data you created manually (for instance, if you save the room data in a file - just manually create a mock file).
Implement "POST /api/chat/<room>". Check it behaves as expected in multiple rooms and across multiple browsers.
