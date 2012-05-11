import traffic_objects as to
def stca(lane, vmax, n=10, p=0.50):
    """Use the STCA model to simulate the specified lane for 'n' discrete steps with probability 'p' for a car slowing down and with a speed limit of 'vmax' (measured in discrete steps)."""
    for i in range(n):
        lane.g_update_all()
        for car in lane.carlist:
            if car.speed > car.g:
                car.speed = car.g
            if car.speed < car.g and car.speed < vmax:
                car.speed += 1
            if car.speed > 0 and to.random.randint(1, 100) <= 100*p:
                car.speed -= 1
            lane.move_car(car)
        print lane #this is where you want to grab data for graphs, animation, etc.
    lane.g_update_all()
