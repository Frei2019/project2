// change everything to unreadable, display Username input field, else, display everything normaly

document.addEventListener('DOMContentLoaded', () => {
  // if a username is already set, the form for the input of the username is hidden
  if (localStorage.getItem('username')) {
    document.querySelector('#userform').style.visibility = "hidden";
    document.querySelector('#userform').style.height = "0%";
    document.querySelector('#content').style.visibility = "visible";
    reload();
  };

  // TODO: make sure the Username is displayed somewhere!

  // if the username form is submitted, the username is set to the input value
  var userform = document.querySelector('#userform')

  userform.onsubmit = () => {
    if (document.querySelector('#username').value.length > 5) {
      localStorage.setItem('username', document.querySelector('#username').value);
      userform.style.visibility = "hidden";
      userform.style.height = "0%";
    } else {
      // this sets the backgroundColor to red if a username that is to short was input
      document.querySelector("#username_row").style.backgroundColor = 'red';
      event.preventDefault();
    };
  };
});
