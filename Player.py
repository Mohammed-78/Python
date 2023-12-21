from WorldCup import WorldCup
from TestMatch import TestMatch
class Player:
    def __init__(self, name, age, gender ):
        self.name=name
        self.age=age
        self.gender=gender
    def displaydetails(self, match):
        if match.lower()=='test':
            game=TestMatch()
        elif match.lower()=='world cup':
            game=WorldCup()
        else:
            print('Invalid Match Type')
        income= game.calculateIncome(numGames=int(input("Enter the no of matches played: ")))
        bonus= game.calculateBonus(performance=input("Enter performance best , average or bad:").lower(),grade=input("Enter the Grade: ")).lower()
        print("Name: ",self.name)
        print('Age: ',self.age)
        print('Gender: ',self.gender)
        print('MatchType: ', match)
        print('Income: ', income)
        print('Bonus: ', bonus )
        print('Total Income: ', income+bonus)
        





            