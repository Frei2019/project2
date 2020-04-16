from time import time

class ChatCollection:
    def __init__(self):
        self.chats = []

    def add_chat(self, chat):
        """
        Takes chat of type Chat and appends it to list of chats
        """
        self.chats.append(chat)

    def chat_exists(self, name):
        """
        Takes string and returns True if the chatname already exists, False
        otherwise
        """
        for chat in self.chats:
            if name == chat.chat_name:
                return True
        return False

    def get_chat_by_name(self, name):
        """
        Takes string and returns the chat with the matching name
        """
        if chat_exists(name):
            return [chat for chat in chats if chat.chat_name == name][0]
        else:
            raise ValueError('A chat could not be found when it should have!')

    def add_message(self, message_content, user, chat_name):
        """
        Takes the message content, the user and the chatname (all strings), Adds
        a new message to the appropriate chat
        """
        if chat_exists(chat_name):
            chat = get_chat_by_name(chat_name)
            chat.add_message(Message(message_content, user))
        else:
            raise ValueError('A chat could not be found when it should have!')

class Chat:
    def __init__(self, chat_name, user):
        self.chat_name = chat_name
        self.messages = [Message("A new chat was established", user)]

    def add_message(self, message):
        """
        Adds a new message to the chat and calls sort_messages
        """
        self.messages.append(message)
        self.sort_messages()

    def sort_messages(self):
        """
        sorts the messages in place and reduces list to the newest 50 messages
        """
        # sorts self.messages by timestamp descending (in place)
        self.messages.sort(key=lambda x: x.timestamp, reverse=True)
        self.messages = self.messages[:50]

    def last_change(self):
        """
        returns the timestamp of the newest message
        """
        return messages[0].get_time()

class Message:
    def __init__(self, content, user):
        self.content = content
        self.user = user
        self.timestamp = int(time()*1000)

    def get_time(self):
        """
        returns the timestamp
        """
        return self.timestamp
