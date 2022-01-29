class Fighter:
    def __init__(self, name=None, lives=100):
        self.name = name 
        self.lives = lives
    
    def attack(self, opponent):
        print('{0.name} attacks {1.name}'.format(self, opponent) )


    def defend(self, attacker):
        print('{0.name} defended an attack from {1.name}'.format(self, attacker) )


player1 = (Fighter('Rocky'))
player2 = (Fighter('Apollo'))

player1.attack(player2)
player2.defend(player1)
player2.attack(player1)
player1.defend(player2)