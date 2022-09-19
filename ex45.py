from random import randint
from sys import argv

# A game of teasing girls


class Scene(object):

    def enter(self):
        """return a string"""
        print("This function has not been configured.")


class FirstPlace(Scene):
    
    def enter(self):
        print(">>>>First place")
        return("second_place")


class SecondPlace(Scene):
    
    def enter(self):
        print(">>>>Second place")
        return("third_place")


class ThirdPlace(Scene):
    
    def enter(self):
        print(">>>>Third place")
        return("third_place")

class Engine(object):

    def __init__(self, first_map):
        self.first_map = first_map
        self.last_map = 'third_place'

    def play(self):
        self.current_map = self.first_map.opening_map()
        self.next_map = self.current_map.enter()

        while self.next_map != self.last_map:
            self.current_map = self.first_map.next_map(self.next_map)
            self.next_map = self.current_map.enter()    

        self.first_map.next_map(self.next_map).enter()

class Map(object):

    map_dict = {
        'first_place': FirstPlace(),
        'second_place': SecondPlace(),
        'third_place': ThirdPlace(),
    }

    def __init__(self, map_name):
        self.map_name = map_name
        
    def opening_map(self):
        """return an instance of Scene class"""
        return (Map.map_dict.get(self.map_name))
    
    def next_map(self, next_map_name):
        """return an instance of Scene class"""
        return (Map.map_dict.get(next_map_name))


a_map = Map('first_place')
a_game = Engine(a_map)
a_game.play()

