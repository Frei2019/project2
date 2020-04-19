import os

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from models import *

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

chats = ChatCollection()

if True:
    chats.add_chat("TestChat1", "Bob")
    chats.add_message("TestChat1", "Hello World!", "Bob")
    chats.add_message("TestChat1", "Hello World yourself!", "Alice")


# It seems stupid to always send all chats with all messages, not necessary..
# this could be just sending a "new message notification", the complete thing
# is only loaded when the page is freshly loaded (F5)

@app.route("/")
def index():
    """
    display the chat-page given in index.html
    """
    # TODO: prompt for user name, make sure it is stored in the browser!
    return render_template("index.html", chats=chats)

@socketio.on("submit message")
def send_message(message):
    """
    socket to receive new messages to be added
    data should be json of shape:
    {
        "chat": "Chat 1",
        "message": "Bla bla bla",
        "author": "Bob"
    }
    Note that the timestamp is taken on the server side!
    """
    # update chats
    # TODO

    # emit new_message to clients, handle this on client side
    emit("new message", message, broadcast=True)

@socketio.on("add chat")
def add_chat(chat):
    """
    socket to receive new chat to be added
    data should be json of shape:
    {
        "chatname": "NewChat",
        ""
    }
    """
    # TODO
