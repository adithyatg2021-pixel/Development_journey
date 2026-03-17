from abc import ABC, abstractmethod

class Editor(ABC):

    @abstractmethod
    def open(self): pass

    @abstractmethod
    def execute(self): pass

    @abstractmethod
    def debug(self): pass

class Vscode(Editor):

    def open(self):
        print("Vs code open method")

    def execute(self):
        print("Vs code execute method")

    def debug(self):
        print("Vs code debug method")

class Pycharm(Editor):

    def open(self):
        print("Pycharm open method")

    def execute(self):
        print("Pycharm execute method")

    def debug(self):
        print("Pycharm debug method")

vsc_instance = Vscode()
vsc_instance.open()
vsc_instance.execute()
vsc_instance.debug()

pycharm_instance = Pycharm()
pycharm_instance.open()
pycharm_instance.execute()
pycharm_instance.debug()
