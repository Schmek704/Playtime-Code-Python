#  Street Dice Game
#  Roll a 7 or 11 to win coming out
#  Roll 2,3, or 12 coming out and lose craps
#  Any other number and you have to roll that same number again before you roll a 7
#  Simplified Craps Game
#  No wagering yet!! But its coming!!
# Giggity!

import random

class Dice:
    def roll(self):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        return [die1, die2]


coming_out = True
rolling = True
throw1 = Dice()
point = 0
result = []
total = 0
game = ""

while game != "x":
    while rolling:
        print(input("\n\nHit Enter to Roll>>>"))
        result = throw1.roll()
        total = (result[0] + result[1])
        print(result)
        if coming_out:
            if total == 7 or total == 11:
                print("Front Line Winner, pay the Line!")
            elif total == 2 or total == 3 or total == 12:
                print("CRAPS!! Take the line. No fun on the Craps Train... heeeee's coming out again!!")
            else:
                point = total
                print(f"{point} is the point!  Come on shooter, let's roll another {point}!!!")
                coming_out = False
        else:
            if total == 7:
                print("7 OUT!  Pay the dont's, take the line, pass the dice!!")
                rolling = False
            else:
                if total == point:
                    print(f"{point} winner winner chicken dinner, pay the line, take the don't, the man is on fire!!! Let's do it again!!!")
                    coming_out = True
                else:
                    print(f"Keep Shooting my man, let's find that {point}, these people wanna get paid")
    print("\n\nGood Roll buddy, better luck next time... let's see the next shooter!!!")
    rolling = True
    coming_out = True
    game = input('\n\nNext Shooter>> "Enter" for yes, "x" for Exit:  ')

        
        






