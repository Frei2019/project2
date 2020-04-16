from time import time

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
