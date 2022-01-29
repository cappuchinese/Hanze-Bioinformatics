import style 
import fighter 

player1 = fighter.Asian(name='Rocky', lives=100, fighting_style = style.Kongfu())
player2 = fighter.European(name='Apollo', lives=100, fighting_style = style.Karate())

player1.attack(player1, player2)
player2.defend(player1, player2)

#change at runtime
player1.fighting_style = style.Karate()
player1.attack(player1, player2)