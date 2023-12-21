from abc import ABC,abstractclassmethod
class Games(ABC):
    @abstractclassmethod
    def calculateIncome(self, numGames):
        pass
    @abstractclassmethod
    def calculateBonus(self, performance , grade):
        pass
