"""
Directory Management:
Design an extensible solution to implement a search filter in OOD for a directory, matching files by size or name.

Requirements:
 - Search by directory
 - filter by file size
 - filter by file name 

Directory
 - name
 - children
 - size

File
 - name
 - size
"""
from abc import ABC, abstractmethod
from collections import deque
from enum import Enum
import threading


class BaseObject(ABC):
    def __init__(self,name,size):
        self.name = name
        self.size = size
    
    @abstractmethod
    def get_name(self):
        return self.name
    
    @abstractmethod
    def get_size(self):
        return self.size

class Directory(BaseObject):
    def __init__(self, name, size):
        super().__init__(name, size)
        self.children = set()

    def get_name(self):
        return super().get_name()
    
    def get_size(self):
        return super().get_size()
    
    def add_content(self,object):
        self.children.add(object)

class File(BaseObject):
    def __init__(self, name, size):
        super().__init__(name, size)

    def get_size(self):
        return super().get_size()
    
    def get_name(self):
        return super().get_name()


class ISearch(ABC):
    @abstractmethod
    def search(self,directory,keyword):
        pass

class FileNameSearch(ISearch):
    def __init__(self):
        super().__init__()
        self.result = {}

    def bfs(self,root,keyword):
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if keyword in node.get_name():
                    if(isinstance(node,Directory)):
                        if "DIR" in self.result:
                            self.result["DIR"].append(node.get_name())
                        else:
                            self.result["DIR"] = [node.get_name()]
                        for child in node.children:
                            q.append(child)
                    else:
                        if "FILE" in self.result:
                            self.result["FILE"].append(node.get_name())
                        else:
                            self.result["FILE"] = [node.get_name()]
        return self.result
    
    def search(self, directory, keyword):
        return self.bfs(directory,keyword)
    
class FileSizeSearch(ISearch):
    
    def __init__(self):
        self.result = {}

    def bfs(self,root,keyword):
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if keyword == node.size():
                    if(isinstance(Directory,node)):
                        if "DIR" in self.result:
                            self.result["DIR"].append(node.get_name())
                        else:
                            self.result["DIR"] = [node.get_name()]
                        for child in node.children:
                            q.append(child)
                    else:
                        if "FILE" in self.result:
                            self.result["FILE"].append(node.get_name())
                        else:
                            self.result["FILE"] = [node.get_name()]
        return self.result
    
    def search(self, directory, keyword):
        return self.bfs(directory,keyword)
    
class FileSeachManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(FileSeachManager,cls).__new__(cls)
            return cls
        
    def __init__(self):
        self.search_strategy = None
        pass

    def set_search_strategy(self,search_strategy:ISearch):
        self.search_strategy = search_strategy

    def print_search_result(self,result):
        for item in result:
            print(item,result[item])

    def search(self,keyword,directory):
        result = self.search_strategy.search(keyword,directory)
        self.print_search_result(result)



if __name__ == "__main__":
    dir1 = Directory("ABC",5)
    dir2 = Directory("QWEBC",2)
    dir3 = Directory("POQWEBC",8)

    file1 = File("UIYABC",3)
    file2 = File("HJLAB",9)
    file3 = File("POIU",6)

    dir1.children.add(file1)
    dir2.children.add(file2)
    dir1.children.add(dir2)
    dir2.children.add(file3)
    dir2.children.add(dir3)

    fileManager = FileSeachManager()
    search_strategy = FileNameSearch()
    
    fileManager.set_search_strategy(search_strategy)
    fileManager.search("BC",dir1)
    




