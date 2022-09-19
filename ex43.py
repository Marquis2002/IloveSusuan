from sys import argv
from random import randint
import ex43a

class Scene(object):

    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        # print(">>>>> play")
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("finished")
        
        # print("^^before while,  current_scene is: ", current_scene, "last_scene is : ", last_scene)

        while last_scene != current_scene:
            # print("^^top of while,  current_scene is: ", current_scene, "last_scene is : ", last_scene)
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            # print("^^end of while,  current_scene is: ", current_scene, "last_scene is : ", last_scene, 
            # "next_scene_name is: ", next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()
        # print("^^end of play,  current_scene is: ", current_scene, "last_scene is : ", last_scene, 
        # "next_scene_name is: ", next_scene_name)



class Death(Scene):
    quips = [ "You died.  You kinda suck at this.",
         "Your mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this."
         ]
    
    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class CentralCorridor(Scene):



    def enter(self):

        print("You are faced with a Gothons soldier, fight!")

        action = input("> ")

        if action ==  "shoot!":
            print("Missed him, you are killed.")
        elif action == "dodge!":
            print("Your foot slips and died.")
        elif action == "tell a joke":
            print("You enter the weapon armory door.")
            return("laser_weapon_armory")
        else:
            print("Can't understand.")
            return("central_corridor")

class LaserWeaponArmory(Scene):

    def enter(self):
        print("You dive into the armory and find the bomb you need in a box with lockpad, it is 2 digits.\nHowever you only have 10 chances.")
        code = "{}{}".format(randint(1, 9), randint(1, 9))
        print(code)
        guess = input("[keypad]> ")
        guesses = 1

        while guess != code and guesses < 10:
            print("Bzzzzzed!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print("You leave the armory with the bomb, enter the bridge.")
            return("the_bridge")

        else:
            print("you died")
            return("death")


class TheBridge(Scene):

    def enter(self):
        print("You enter the bridge with the bomb and run into 5 Gothons.")

        action = input("> ")
        
        if action == "throw the bomb!":
            print("Stupid decision!")
            return("death")
        elif action == "slowly place the bomb":
            print("You place the bomb, close the door, run to the escape pod!")
            return("the_gate")


class TheGate(Scene):

    def enter(self):
        print("You run into an alien with a gun, you have to beat him before you enter the EscapePod.")
        alien = ex43a.Aliens()
        if alien.encounter():
            print("You beat him, good luck!")
            return("escape_pod")
        else:
            print("The alien took you to the ship and killed you!")
            return("death")


class EscapePod(Scene):

    def enter(self):
        print("You enter the chamber with 5 escape pods, there is only one good one, try to pick it!")
        good_one = randint(1,5)
        print(good_one)
        guess = int(input("[pod #]> "))

        if good_one != guess:
            print("You die!")
            return("death")
        else:
            print("Congratulations!")
            return("finished")


class Finished(Scene):

    def enter(self):
        print("You won!")
        return("finished")


class Map(object):
    
    scenes = {
        "central_corridor": CentralCorridor(),
        "laser_weapon_armory": LaserWeaponArmory(),
        "the_bridge": TheBridge(),
        "the_gate":TheGate(),
        "escape_pod": EscapePod(),
        "finished": Finished(),
        "death": Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
