import style

class Fighter:
    def __init__(self, name=None, lives=100):
        self.name = name 
        self.lives = lives
        self.fighting_style = style.Style()

    def attack(self, attacker, opponent):
        self.fighting_style.attack(attacker, opponent)

    def defend(self, attacker, defender):
        self.fighting_style.defend(attacker, defender)


class Asian(Fighter):
    def __init__(self, name=None, lives = None, fighting_style = None):
        super(Asian, self).__init__(name, lives)
        self.fighting_style = fighting_style

    def looks(self):
        print(f'{self.name} has Asian looks')


class European(Fighter):
    def __init__(self, name=None, lives = None, fighting_style = None):
        super(European, self).__init__(name, lives)
        self.fighting_style = fighting_style

    def looks(self):
        print(f'{self.name} has European looks')
