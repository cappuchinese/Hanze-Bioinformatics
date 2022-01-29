class Style:

    def attack(self, opponent):
        ...

    def defend(self, attacker):
        ...

class Kongfu(Style):
    def attack(self, atacker, opponent):
        msg = '{0.name} attacking {1.name} in Kongfu style'.format(atacker, opponent)
        print(msg)

    def defend(self, atacker, defender):
        msg = '{0.name} defending {1.name} in Kongfu style'.format(defender, atacker)
        print(msg)


class Karate(Style):
    def attack(self, atacker, opponent):
        msg = '{0.name} attacking {1.name} in Karate style'.format(atacker, opponent)
        print(msg)

    def defend(self, atacker, defender):
        msg = '{0.name} defending {1.name} in Karate style'.format(defender, atacker)
        print(msg)
        