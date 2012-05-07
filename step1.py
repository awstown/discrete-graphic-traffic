

class Car(object):
    """ Represents a car it has the follow attributes:
        position, velocity, 
    """

    # Constructor
    def __init__(self, position=0, velocity=1):
        self.position = position
        self.velocity = velocity

    # String
    def __str__(self):
        return 'Position: %d Velocity: %d' % (self.position, self.velocity)

class Lane(object):
    """ Represents a single lane that is capable of hold multiple cars.
        It also has methods for manipulating the cars.
    """

    # Constructor
    def __init__(self, cars):
        self.cars = cars;

    # Methods
    def 
        
