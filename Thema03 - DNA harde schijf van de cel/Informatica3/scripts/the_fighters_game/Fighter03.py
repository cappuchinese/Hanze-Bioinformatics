class Fighter:
    def __init__(self, name=None, lives=100):
        self.name = name 
        self.lives = lives
    
    def attack(self, opponent):
        print('{0.name} attacks {1.name}'.format(self, opponent) )


    def defend(self, attacker):
        print('{0.name} defended an attack from {1.name}'.format(self, attacker) )


class EuropeanFighter(Fighter):
    @property
    def looks(self):
        print('{0.name} has European looks'.format(self))
    
    @property
    def style(self):
        print('{0.name} fighting style is kick-boxing'.format(self))


class AsianFighter(Fighter):
    @property
    def looks(self):
        print('{0.name} has Asian looks'.format(self))
    
    @property
    def style(self):
        print('{0.name} fighting style is karate'.format(self))


player1 = (EuropeanFighter('Rocky'))
player2 = (AsianFighter('Apollo'))
player1.looks
player2.looks
player1.style
player2.style

player1.attack(player2)
player2.defend(player1)
player2.attack(player1)
player1.defend(player2)