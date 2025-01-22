from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def select(self):
        pass

# Concrete products
class WindowsButton(Button):
    def render(self):
        return "rendering Windows Button"
    
class MacButton(Button):
    def render(self):
        return "rendering Mac Button"
    
class WindowsCheckbox(Checkbox):
    def select(self):
        return "selecting windows checkbox"

class MacCheckbox(Checkbox):
    def select(self):
        return "selecting Mac checkbox"

# Abstract factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

# Concreate Factory 
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()
    
    def create_checkbox(self):
        return WindowsCheckbox()
    
class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()
    
    def create_checkbox(self):
        return MacCheckbox()
    
def get_gui_components(factory:GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.select())

if __name__ == "__main__":
    factory = WindowsFactory()
    get_gui_components(factory)
    

