from Game import Games
class WorldCup(Games):
    def calculateIncome(self, numGames):
        base_income=int(input("what is the base income: "))
        return numGames*base_income
    def calculateBonus(self , performance, grade):
        if performance=='best':
            if grade=='A':
                bonus=5000
            elif grade=='B':
                bonus=1000
            elif grade=='C':
                bonus=800
        elif performance== 'average':
            bonus=500
        else:
            bonus=250
        return bonus