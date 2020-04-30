# Project2
Project 2 for Web Programming with Python and JavaScript

## Python
### application.py
#### General Information:
- Contains variable chats of class ChatCollection, storing all the information of the chats, the class is imported from model.py which implments all the functionalities that are necessary
- Welcome and Large are added as chats, to have some demonstration chats on boot

#### Contains the following routes / socketio:
- app.route "/" returns the index.html
- app.route "/chat/<string:chatname>" takes a chatname and returns the content of that chat as a json. This allows to load the chat history of a specific chat, this is called when the user clicks on a chatname
- @socketio.on("submit message"): takes a message (json with chat, message and author), updates the chats variable serverside and emits "new message". This is used to register and distribute a new message, is called when a user clicks "Send"
- @socketio.on("add chat"): takes a chat (json with chatname and author), updates the chats variable serverside and emits "new chat". This is used to register and distribute that a new chat was added. Is called when a user clicks "Add Chat"
- @socketio.on("typing"): takes istyping (json with chatname and author), emits "user typing". This allows to display that a user is typing. Is called when a keystroke is registered.

## .html Files
* index.html: Contains the style information and the page html, it takes a list of chats to be able to list all chats that currently exist. Naming is a bit of a mess, I have to look into standard naming / style guide. Also, the css could be taken out of the html to make it cleaner.

## Javascript
#### On load 
- it is checked if "username" exists in the localStorage, if no, a form prompting the user for a username is displayed, and everything else is hidden.
- socket connection is established 
- If "chatname" does not exist in the localStorage it is set to "Welcome". This will lead to the Welcome chat being displayed the first time a user arrives on the page
- add_display_link() is called

#### Functions
- get_display_chathistory: This function gets and displays the chathistory of the chat with name "chatname"
- add_message: This function allows to add messages to the chat history (Only visually!)
- add_display_link: all links in the overview trigger the loading of the history of the selected chat

#### Event Listener
- Keyup: if the enter key is pressed, the sendbutton is clicked. For every other keystroke, the typing message is emitted
- onclick Add Chat: If a chatname was input, and the chatname does not exist yet, a "add chat" is emitted
- onclick Send: if the send button is clicked the new message is emitted to the websocket.

#### Socket Listener
- socket.on 'new message' : if a new message is received the function add_message is called with the appropriate arguments
- socket.on 'new chat': If a new chat message is received, the html element "#lichatlist" is added a new child (the new chat)
- socket.on 'user typing': If a user typing message is received the data field #istypingfield is filled with the appropriate text. (Note the animation reset!)
