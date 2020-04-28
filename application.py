import os
import json
import time
from time import sleep

from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
from models import *

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

chats = ChatCollection()

chats.add_chat("Welcome", "Admin")
sleep(1)
chats.add_message("Welcome", "Admin", "Welcome to our chat application, friend!")

if True:
    chats.add_chat("TestChat1", "Bob")
    sleep(1)
    chats.add_message("TestChat1", "Bob", "Hello World!")
    sleep(1)
    chats.add_message("TestChat1", "Alice", "Hello World yourself!")
    sleep(1)
    chats.add_message("TestChat1", "cfrei", "Hello World yourself 2!")



# It seems stupid to always send all chats with all messages, not necessary..
# this could be just sending a "new message notification", the complete thing
# is only loaded when the page is freshly loaded (F5)

@app.route("/")
def index():
    """
    display the chat-page given in index.html
    """
    print("index was opened")
    return render_template("index.html", chats=chats.get_chats())

@app.route("/chat/<string:chatname>", methods=['POST'])
def get_chat(chatname):
    """
    Takes the name of a chat and sends back the chat object
    """
    # print(chats.get_chat_by_name(chatname))
    # continue here, chats object is not inputable in jsonify
    return jsonify(chats.get_chat_by_name(chatname))

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
    print("message was submitted")
    message = message['message']
    message['timestamp'] = int(time()*1000)
    chats.add_message(message['chat'], message['author'], message['content'], message['timestamp'])
    # emit new_message to clients, handle this on client side
    emit('new message', message, broadcast=True)

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

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
