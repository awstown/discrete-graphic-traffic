class Car(object):
    def __init__(self, pos=0, vel=0):
        self.position = pos
        self.speed = vel
        self.g = 0      #number of empty spaces ahead of car
    def __str__(self):
        return '\nPosition: %d, Speed: %d\nEmpty spaces ahead: %d' % (self.position, self.speed, self.g)
    def reset(self, pos, vel):
        self.position = pos
        self.speed = vel
    def add_pos(self, d):
        self.position += d

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
    def update_map(self):
        for spot in range(self.length):
            self.map[spot] = '_'
        for car in self.carlist:
            car.position += car.speed
            if car.position > self.length - 1:
                car.position = car.position - self.length
            self.map[car.position] = 'n'
    def g_update_car(self, car):
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
        for car in self.carlist:
            self.g_update_car(car)
    def print_all_cars(self):
        for car in self.carlist:
            print car

