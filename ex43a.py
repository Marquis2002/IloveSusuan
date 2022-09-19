import random
# This is the war system.


WORDS = []
txt = open("words.txt")
for word in txt.readlines():
    WORDS.append(word)

player_hit_points = 100
player_defences = 0
player_phsical_damage = random.randint(2, 5)


class Aliens(object):

    def __init__(self):
            self.hit_points = random.randint(1, 99)
            self.defences = random.randint(0, 5)
            self.phsical_damage = random.randint(0, 5)
            self.name = random.choice(WORDS)
            

    def encounter(self):
        print(f"This is an alien named {self.name}, whose hp is {self.hit_points}, \
              defences is {self.defences}, phisical damage is {self.phsical_damage}.")
        global player_hit_points
        global player_defences
        global player_phsical_damage
        while self.hit_points > 0:
            action = input("[Your turn]> ")
            
            if action == "attack":
                self.hit_points += self.defences - player_phsical_damage
            elif action == "storage":
                player_phsical_damage += random.randint(0,5)
            elif action == "dodge":
                
                if random.randint(0, 1):
                    continue
                else:
                    pass
            
            else:
                print("Can't understand. You have only three choices: attack, energy storage, dodge.")
                continue
            
            print(f"{self.name}'s hp is {self.hit_points}, defences is {self.defences}, \
                  phisical damage is {self.phsical_damage}.")
            player_hit_points += player_defences - self.phsical_damage
            print(f"The alien kicked your egg, and your hp is {player_hit_points}.")
            if player_hit_points <= 0:
                return 0

        print(f"You have beaten {self.name}.")
        return 1
        

