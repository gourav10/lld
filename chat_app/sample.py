"""
Chat Application
Key Features: What would be the key features of a chat application, for example, user, message, and chat room?
Message Handling: How would you provide the facility to send, receive, and store messages? How are messages delivered in real-time?
User Authentication: How do you handle user authentication while ensuring secure communication?

User
 - userID
 - message
 + send
 + receive
 + store

Message
 - messageID
 - user ID
 - timestamp


ChatRoom
 - list of users
 - 
"""

from enum import Enum
import heapq

class ChatRoom:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = cls.__init__()
        return cls._instance
    
    def __init__(self):
        self.users = set()
        pass
    
    def addUser(self,user):
        print(f"{user.name} is using Chat App!")
    
    def sendMessage(self,sender, receiver,message):
        try:
            if receiver not in self.users:
                raise Exception(f"{receiver.name} not found! Failed to send message")

            sender.receive(ActionType.SEND, receiver.name,message)
            receiver.receive(ActionType.RECEIVE, sender.name,message)
        except Exception as e:
            print(e)

    def encryptMessage(self,message):
        message.content = "***"+message.content+"**"
        message.isEncrypted = True
        return message
    

class ActionType(Enum):
    SEND = 1
    RECEIVE = 2

class Message:
    def __init__(self,message,timestamp):
        self.timestamp = timestamp
        self.content = message
        self.isEncrypted = False


class User:
    def __init__(self, userID, username):
        self.userID = userID
        self.name = username
        self.messages = []
        self.chat_manager = None
        self.chat_manager.addUser(self)
        pass

    def create_group(self,members):
        self.chat_manager = ChatRoom()
        self.chat_manager.addUser(self)
        for member in members:
            self.chat_manager.addUser(member)

    def send(self,timestamp, message,receiver):
        message = Message(receiver,message)
        self.chat_manager.sendMessage(self,receiver,message)

    def receive(self,actionType,userName,message):
        print([userName,actionType,message])
        message = self.chat_manager.encryptMessage(message)
        self.messages([userName,actionType,message])


user1 = User(1,"Gourav")
user2 = User(2,"Neelesh")
user1.createGroup()
user1.send(12,"Hello!",user2.userID)
