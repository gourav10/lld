"""
The facade pattern provides a simplified interface to a larger body of code, making it easier for clients
to interact with the system.

Problem Statement:
Imagine a home automation system that controls lights, air conditioning, and a music system. Without the facade,
a client needs to understand how each subsystem works. With the facade, we provide a unified interface.
"""
from abc import ABC, abstractmethod

class IGadgets(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod       
    def off(self):
        pass

class Light(IGadgets):
    def on(self):
        return "Lights are ON."

    def off(self):
        return "Lights are OFF."


class AirConditioner(IGadgets):
    def set_temperature(self,temperature):
        return f"Air Conditioner temperature: {temperature}"

    def on(self):
        return "Air Conditioner is ON."
    
    def off(self):
        return "Air Conditioner is OFF."
    
class MusicSystem(IGadgets):
    def play_music(self,song):
        return f"Playing {song} on Music System"
    
    def stop_music(self):
        return f"Stopped playing music on Music System."
    
    def on(self):
        return "Music System is ON."
    
    def off(self):
        return "Music System is OFF"

class HomeAutomationFacade:

    def __init__(self):
        self.light = Light()
        self.air_conditioner = AirConditioner()
        self.music_system = MusicSystem()
    
    def movie_mode(self, song):
        print("Setting up Movei Mode")
        print(self.light.off())
        print(self.air_conditioner.on())
        print(self.music_system.on())
        print(self.music_system.play_music(song))

    def party_mode(self):
        print("Setting up Party Mode")
        print(self.light.on())
        print(self.air_conditioner.on())
        print(self.music_system.on())
        print(self.music_system.play_music())

    def shut_down(self):
        print("Shutting down the House")
        print(self.light.off())
        print(self.air_conditioner.off())
        print(self.music_system.off())

if __name__ == "__main__":
    home = HomeAutomationFacade()
    home.movie_mode("Sweat ft. Zayan Malik")

    