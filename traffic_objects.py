# Defines the Car object and the Lane object. This was built assuming the movement
# of the cars would be handled by a 'rules' script.

import random

class Car(object):
    """Defines a Car object with attributes position, speed, and g, where g is
reserved to store the number of empty spaces ahead of the car.
    """
    def __init__(self, position=0, speed=0):
        self.position = position
        self.speed = speed
        self.g = 0
    def __str__(self):
        return 'Position: %d, Speed: %d\nEmpty spaces ahead: %d' % (self.position, self.speed, self.g)
    def reset(self, position, speed):
        """A slightly more convenient way to set the position and speed simultaneously.
        """
        self.position = position
        self.speed = speed

class Lane(object):
    """Defines a Lane object with attributes length, map, and carlist.
    """
    def __init__(self, spaces=1):
        self.length = spaces
        self.map = []   # uses '_' to represent an empty space, 'n' to represent a space with a car in it.
        self.carlist = []
        for i in range(self.length):
            self.map.append('_')
    def __str__(self):
        return ' '.join(self.map)
    def add_car(self, car):
        """Adds the specified instance 'car' to the lane."""
        if car not in self.carlist:
            self.carlist.append(car)
        self.map_update()
    def remove_car(self, car):
        """Removes the specified instance 'car' from the lane."""
        if car in self.carlist:
            self.carlist.remove(car)
        self.map_update()
    def populate(self, n):
        """Adds n cars to the lane in random positions.
        """
        self.map_update()
        if n > self.map.count('_'):
            if self.map.count('_') == 1: ss = ''
            else: ss = 's'
            if n == 1: ns = ''
            else: ns = 's'
            raise ValueError('Tried to put %d car%s in a lane that has %d empty space%s.' % (n, ns, self.map.count('_'), ss))
        for i in range(n):
            x = random.randint(0, self.length - 1)
            while True:
                if self.map[x] == '_':
                    self.add_car(Car(x))
                    break
                else:
                    x = random.randint(0, self.length - 1)
            self.map_update()
    def map_update(self):
        """Updates the map list to reflect changes in car positions."""
        for spot in range(self.length):
            self.map[spot] = '_'
        for car in self.carlist:
            self.map[car.position] = 'n'
    def g_update_car(self, car):
        """Finds and sets the appropriate g value for a specific car instance.
        """
        self.map_update()
        if car.position != self.length - 1:
            n = car.position + 1
        else:
            n = 0
        count = 0
        while self.map[n] == '_':
            count += 1
            n += 1
            if n > self.length - 1:
                n = n - self.length
        car.g = count
    def g_update_all(self):
        """Finds and sets the appropriate g value for each car instance in the lane.
        """
        for car in self.carlist:
            self.g_update_car(car)
    def print_cars(self):
        """Displays information about each car in 'carlist'. May be useful for debugging, etc.
        """
        for car in self.carlist:
            print '\n', car, '\n' + '-'*27
