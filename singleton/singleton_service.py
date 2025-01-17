from abc import ABC, abstractclassmethod
import json
import os
import threading
"""
Design a singleton class to manage a configuration service for a Library Management System. The service should:

1. Load configuration settings from a file (e.g., database connection strings, max borrowing limit, etc.).
2. Allow retrieval of specific settings via a get_setting(key) method.
3. Ensure only one instance of the configuration service exists throughout the application lifecycle.

Requirements:

1. Implement the Singleton Design Pattern in your preferred language.
2. Ensure thread safety if applicable.
3. Add methods to simulate loading and retrieving configuration values.

"""

class ConfigurationService:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args,**kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
                cls._instance.config_file_path = 'config.json'
                cls._instance.load()
            return cls._instance

    def load(self):
        print(self.config_file_path)
        if(os.path.exists(self.config_file_path)):
            print("Config File Exist")
            print(os.path.getsize(self.config_file_path))
        else:
            print("Config file doesn't exist!")

        if os.path.getsize(self.config_file_path) > 0: 
            with open(self.config_file_path,"r") as file:
                self.data = json.load(file)
                print("Configurations loaded successfully!")
        


    def get_setting(self,key):
        print(self.data["settings"])
        for k in self.data["settings"]:
            if key == k:
                print(key,self.data["settings"][key])
                return self.data["settings"][key]
        return None

if __name__=="__main__":
    configReader = ConfigurationService()
    configReader.get_setting("connection_string")

    configReader2 = ConfigurationService()
    print(configReader2 ==configReader)