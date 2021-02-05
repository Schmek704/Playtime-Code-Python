#  Street Dice Game
#  Roll a 7 to win coming out
#  Any other number and you have to roll that same number again before you roll a 7
#  Simplified Craps Game

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


while rolling:
    print(input("\n\nHit Enter to Roll>>>"))
    result = throw1.roll()
    total = (result[0] + result[1])
    print(result)
    if coming_out:
        if total == 7:
            print("Front Line Winner, pay the Line!")
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
                print(f"{point} winner winner chicken dinner, pay the line, take the don't, the man is on fire!!!")
                coming_out = True
            else:
                print(f"Keep Shooting my man, let's find that {point}, these people wanna get paid")
print("Good Roll buddy, better luck next time...")
        






