"""
File Storage System (e.g., Google Drive)
Key Classes: What will be the key classes, and what will be their relationships in a file storage system?
File Operations: How would you handle different file operations, for example, upload, download, and sharing of files?
User Permissions and File Versioning: How do you handle user permissions with respect to file versioning, enforcement of security,
and integrity?

Upload,
Download,
Sharing
User Permission
File Versioning

File
 - content: latest value
 - versions: map(timestamp, content)
 - timestamp
 - id
 - filename
 - users: [(User_id,permission)]

User
 - id
 - files: [file_ids]
 - 

Permission
 - use_id
 - permission_level

FileManager:
 - storage: (files)

User -> upload-> file subscribers get notified
Sharing 
"""
from enum import Enum

class File:
    def __init__(self,name):
        self.version = 0 
        self.name = name
        self.content = ""
        self.versions = []
        self.timestamp = ""
        self.users = []
        pass

    def addContent(self,content):
        self.content = content
    
    def updateVersion(self,content):
        self.version+=1
        self.content = content
        self.versions.append((self.versions,content))

    def addUser(self,user_id,permission):
        self.users.append((user_id, permission))
    
    def addTimeStamp(self,timestamp):
        self.timestamp = timestamp

class User:
    def __init__(self, username,id):
        self.name = username
        self.user_id = id
        self.files = []
        pass
    
    def addFiles(self, file_id):
        self.files.append(file_id)


class PermissionType(Enum):
    READ = 1
    WRITE = 2

class Permission:
    def __init__(self,user_id,permission_type):
        self.permission_level = permission_type
        self.user_id = user_id

class FileManager:

    def __init__(self,user):
        self.timestamp = 0
        self.user = user
        self.file_storage = {}
        self._observers = set()

    def add_user(self,observer):
        self._observers.append(observer)
    
    def remove_user(self,observer):
        self._observers.append(observer)
    
    def notify(self,message):
        for obs in self._observers:
            obs.update(message)

    def create_file(self,name,content):
        file =  File(name)
        file.addContent(content)
        
        self.timestamp+=1
        self.file_storage[file]=self.timestamp
        return file

    def upload(self,file,user):
        if file in self.file_storage:
            # Check for file version
            if self.file_storage[file] not in file.versions:
                file.versions.append(file)
        user.files.append(file)
        print(f"{file.name} uploaded successfully! at {self.timestamp}")
        self.timestamp+=1
        pass

    def share(self,file,user,collabs):
        for user,permission_type in collabs:
            file.addUser(user,permission_type)
            print(f"{file.name} shared with {user.name}")
        self.timestamp+=1
        pass

    def download(self,file_name):
        for file in self.file_storage:
            if file_name == file.name:
                return "Downloaded file {file_name} successfully!"
        return "Unable to download file"


if __name__ == "__main__":
    user1 = User("Gourav","1")
    user2 = User("Neel","2")
    user3 = User("Mayan","3")

    manager = FileManager(user1)
    manager.add_Users(user1)
    manager.add_user(user2)
    manager.add_user(user3)
    file = manager.create_file("LLD","LLD is Great!")

    manager.upload(file,user1)
    manager.share(file,user1,[(user2,PermissionType.READ),(user3,PermissionType.READ)])
    print(manager.download(file))