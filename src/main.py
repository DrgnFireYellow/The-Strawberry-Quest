from adventurelib import *
# Rooms
town_center = Room("The town center is bustling with people going to and from the market stalls.")

wilderness = Room("A massive temple shaped like a flame is to the south. To the west, there is a strange pond. A short ways to the east there is a giant bolder with a locked door in it.")

town_center.south = wilderness
location = town_center
# Commands
@when("go DIRECTION")
def go(direction):
    global location
    location = location.exit(direction)
    say(location)
say(location)
start()
