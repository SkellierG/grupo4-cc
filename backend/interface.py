from abc import ABC, abstractmethod

class Iadivinar(ABC):
    
    def __init__(self):
        self.number = 0

    @abstractmethod
    def getNumber:
        pass
    
    @abstractmethod
    def setNumber:
        pass

    @abstractmethod
    def compareNumbers(self, number):
        pass

    @abstractmethod
    def feedback(self, number):
        pass

    @abstractmethod:
    def retry:
        pass

