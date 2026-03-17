"""
1) Abstraction is the method of highlighting essential features and hiding implementation details
2) The class of Abstraction is called abstract base class (ABC). It should be inherit from class ABC from abc.py
3) All methods inside abstract base class should be abstract methods. It can be done with the decorator called
abstractmethod
4) The class which inheriting the features of abstract base class should override all the methods of ABC
5) Decorator starts with '@'
"""

from abc import ABC, abstractmethod

class Bike(ABC):    #   This is abstract base class inheriting features from ABC
    
    @abstractmethod
    def transmission(self): pass

    @abstractmethod
    def start(self): pass

class Pulsar(Bike): # class which inherits from ABC Bike

    def transmission(self): # overriding method of abc Bike
        print("Pulsar transmission")

    def start(self):    # overriding method of abc Bike
        print("Pulsar start method")

pulsar_instance = Pulsar()
pulsar_instance.transmission()
pulsar_instance.start()