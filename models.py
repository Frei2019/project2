from time import time
import json

class ChatCollection:
    def __init__(self):
        self.chats = []

    def get_chats(self):
        return self.chats

    def add_chat(self, chat_name, user):
        """
        Takes chat_name and user and appends a new chat to list of chats
        returns 1 if successful, 0 if not (if the chat name is not unique)
        """
        if self.chat_exists(chat_name):
            return 0
        else:
            self.chats.append(Chat(chat_name, user))
            return 1

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
        if self.chat_exists(name):
            chats = self.get_chats_as_json()
            return chats.get(name)
        else:
            raise ValueError('A chat could not be found when it should have!')

    def get_chats_as_json(self):
        """
        creates dict out of the Chats Object
        """
        chats_dict = {}
        for chat in self.chats:
            chat_dict = {}
            i = 0
            for message in chat.get_messages():
                message_dict = {}
                message_dict['content'] = message.content
                message_dict['user'] = message.user
                chat_dict[str(message.timestamp)] = message_dict
            chats_dict[chat.get_name()] = chat_dict
        return chats_dict

    def add_message(self, chat_name, user, message_content, timestamp=0):
        """
        Takes the message content, the user and the chatname (all strings), Adds
        a new message to the appropriate chat
        """
        if self.chat_exists(chat_name):
            chat = [chat for chat in self.chats if chat.chat_name == chat_name][0]
            chat.add_message(Message(message_content, user, timestamp))
        else:
            raise ValueError('A chat could not be found when it should have!')


class Chat:
    def __init__(self, chat_name, user, timestamp=0):
        self.chat_name = chat_name
        self.messages = [Message("A new chat was established", user, timestamp)]

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
        self.messages = self.messages[:100]

    def last_change(self):
        """
        returns the timestamp of the newest message
        """
        return messages[0].get_time()

    def get_name(self):
        """
        returns the chat name
        """
        return self.chat_name

    def get_messages(self):
        """
        returns all messages as list
        """
        return self.messages

class Message:
    def __init__(self, content, user, timestamp=0):
        self.content = content
        self.user = user
        if not timestamp:
            self.timestamp = int(time()*1000)
        else:
            self.timestamp = timestamp

    def get_time(self):
        """
        returns the timestamp
        """
        return self.timestamp
