from abc import ABC, abstractmethod
from enum import Enum

class IProgramLanguage(ABC):
    @abstractmethod
    def compile(self,input)->bool:
        pass

    @abstractmethod
    def syntax_check(self,input)->bool:
        pass
    
    @abstractmethod
    def run(self,input)->bool:
        pass

class LanguageType(Enum):
    JAVA = 1
    PYTHON = 2
    C_SHARP = 3

class JAVA(IProgramLanguage):
    def __init__(self):
        super().__init__()
        self.keywords = ["class","int", ""]
        self.syntax = [";"]
        print("Selected JAVA Language")

    def compile(self, input):
        return True
    
    def syntax_check(self, input):
        error_list = []
        try:
            for i,line in enumerate(input):
                for keyword in self.syntax:
                    if  keyword not in line:
                        error_list.append(f"Keyword not found in line: {i+1}")
        except:
            return "Compiler Failed!"
        if len(error_list)>0:
            return False
        else:
            return True
    
    def run(self, input):
        return "Executed Java code!"
    
class Python(IProgramLanguage):
    def __init__(self):
        self.syntax = ["[","]"]
        self.keywords = ["for","each"]
        print("Selected Python Language")

    def compile(self, input):
        error_list = []
        if input:
            for i,line in input:
                for keyword in self.keywords:
                    if keyword not in line:
                        error_list.append(f"error in line: {keyword}")

        if len(keyword)>0:
            return True
        else:
            return False
        
    def syntax_check(self, input):
        counter=0
        for syn in self.syntax:
            if syn not in input:
                counter+=1
        
        return counter==0
    
    def run(self, input):
        return "Python code executed!"
    
class LanguageFactory:
    @staticmethod
    def getLanguage(languageType:LanguageType):
        if languageType == LanguageType.JAVA:
            return JAVA()
        elif languageType == LanguageType.PYTHON:
            return Python()
        return None
    
class CodeEditor:
    def __init__(self):
        self.language = None
        self.compile_success = False
    
    def select_language(self,langType:LanguageType):
        self.language = LanguageFactory.getLanguage(langType)
    
    def codeExecute(self,input):
        if self.codeCompile(input):
            return self.language.run(input)
        
    def codeCompile(self,input):
        return self.language.compile(input)
    
    def codeSyntaxHighlight(self,input):
        return self.language.syntax_check(input)
        

def main():
    codeEditor = CodeEditor()
    codeEditor.select_language(LanguageType.JAVA)
    input = "class Jaba{{}}"
    print(input)
    codeEditor.codeSyntaxHighlight(input)
    # codeEditor.codeCompile(input)
    print(codeEditor.codeExecute(input))

    

if __name__ == "__main__":
    main()