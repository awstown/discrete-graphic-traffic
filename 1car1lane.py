#This code defines two objects, a Car and a Lane, then creates
#an instance of each of those objects, then adds the car to the
#lane, then moves the car along the lane at a constant, user-
#defined velocity. To represent the lane visually, I have the
#terminal print an 'n' to represent where the car is on a lane
#of underscores. Each line printed represents a single moment
#in time.

class Car(object):
    def __init__(self, pos=0, vel=0):
        self.position = pos
        self.speed = vel
    def __str__(self):
        return 'Position: %d, Speed: %d' % (self.position, self.speed)

class Lane(object):
    def __init__(self, spaces=1):
        self.length = spaces
        self.map = []
        self.carlist = []
        for i in range(self.length):
            self.map.append('_')
    def __str__(self):
        return ' '.join(self.map)
    def add_car(self, car):
        if car not in self.carlist:
            self.carlist.append(car)
        self.map[car.position] = 'n'
    def update_all(self):
        for car in self.carlist:
            self.map[car.position] = '_'
            car.position += car.speed
            if car.position > self.length - 1:
                car.position = car.position - self.length
            self.map[car.position] = 'n'

length = int(raw_input('Length of the lane: '))
vel = int(raw_input('Speed of the car: '))
lane = Lane(length)
toyota = Car(0, vel)
lane.add_car(toyota)
for i in range(19):
    print lane
    lane.update_all()
print lane
        
