// change everything to unreadable, display Username input field, else, display everything normaly

document.addEventListener('DOMContentLoaded', () => {
  // if a username is already set, the form for the input of the username is hidden
  if (localStorage.getItem('username')) {
    document.querySelector('#userform').style.visibility = "hidden";
    document.querySelector('#userform').style.height = "0%";
    document.querySelector('#content').style.visibility = "visible";
    document.querySelector('#pagetitle').innerHTML = "CFrei89's Chat - " + localStorage.getItem('username')
  }

  // connect to websocket
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  // if the username form is submitted, the username is set to the input value
  var userform = document.querySelector('#userform');
  userform.onsubmit = () => {
    if (document.querySelector('#username').value.length > 4) {
      localStorage.setItem('username', document.querySelector('#username').value);
      userform.style.visibility = "hidden";
      document.querySelector('#content').style.visibility = 'visible';
      userform.style.height = "0%";
      document.querySelector('#pagetitle').innerHTML = "CFrei89's Chat - " + localStorage.getItem('username')
    } else {
      // this sets the backgroundColor to red if a username that is to short was input
      document.querySelector("#username_row").style.backgroundColor = 'red';
      event.preventDefault();
    };
  };

  // This is the Welcome chat, displayed when first opening the page
  if (!localStorage.getItem('chatname')) {
    localStorage.setItem('chatname', 'Welcome');
  }
  get_display_chathistory(localStorage.getItem('chatname'));

  // This function gets and displays the chathistory of the chat with name "chatname"
  function get_display_chathistory(chat) {
    localStorage.setItem('chatname', chat)
    // set title to include the chatname
    document.querySelector('#chathistorytitle').innerHTML = 'Chat History - ' + chat
    // remove everything in the chat history display
    document.querySelector('#chathistory').innerHTML = '';
    // create HTTP Request that will then get the chat history of the selected chat
    const request = new XMLHttpRequest();
    request.open('POST', '/chat/' + chat);
    request.send()
    request.onload = () => {
      const data = JSON.parse(request.responseText);
      Object.keys(data).forEach(function(element) { // TODO continue here
        var arr = data[element]
        add_message(element, arr.content, arr.user)
      })
    }
  }

  // This function allows to add messages to the chat history (Only visually!)
  function add_message(timestamp, content, user) {
    // Create new message in the chat history
    const post = document.createElement('div');
    const post_wrapper = document.createElement('div');

    if (localStorage.getItem('username') == user){
      post.className = 'ownmessage m-2 p-2';
      post_wrapper.className = "d-flex flex-row-reverse"
    } else {
      post.className = 'foreignmessage m-2 p-2';
      post_wrapper.className = "d-flex flex-row"
    }

    const d = new Date(parseInt(timestamp))
    if (d.getMinutes() < 10) {
      var minutes = '0' + d.getMinutes().toString()
    } else {
      var minutes = d.getMinutes().toString()
    }
    if (d.getHours() < 10) {
      var hours = '0' + d.getHours().toString()
    } else {
      var hours = d.getHours().toString()
    }
    post.innerHTML = '<b>' + user + '</b>' + '<i>(' + hours + ':' + minutes + ')</i>' + ': ' + content;

    post_wrapper.appendChild(post)

    document.querySelector('#chathistory').append(post_wrapper)
  }

  // all links in the overview trigger the loading of the history of the selected chat
  document.querySelectorAll('.chat').forEach(function(button) {
    button.onclick = function() {
      get_display_chathistory(button.id);
    };
  });

  // make the enter key work
  var input = document.getElementById("chatinput");
  // Execute a function when the user releases a key on the keyboard
  input.addEventListener("keyup", function(event) {
    // Number 13 is the "Enter" key on the keyboard
    if (event.keyCode === 13) {
      // Cancel the default action, if needed
      event.preventDefault();
      // Trigger the button element with a click
      document.getElementById("sendbutton").click();
    }
  });

  // TODO: add possibilty to add chats
  // TODO: add that the user is scrolled down

  // if the send button is clicked the new message is emitted to the websocket
  document.querySelector('#sendbutton').onclick = function () {
    console.log("click")
    const chat_content = document.querySelector('#chatinput').value
    if (chat_content) {
      console.log(chat_content)
      // Reset input field
      document.querySelector('#chatinput').value = ''
      message={
       'chat': localStorage.getItem('chatname'),
       'content': chat_content,
       'author': localStorage.getItem('username')
      };
      socket.emit("submit message", {'message': message});
    }
  }

  socket.on('new message', data => {
      console.log(data['timestamp'])
      add_message(data['timestamp'], data['content'], data['author'])
  });
});
