import traffic_objects as to

def update_and_move(car, lane, vmax, p, cc):
    """To be used only within other rules definitions. Sets the car's speed appropriately, then moves it."""
    if car.speed > car.g:
        car.speed = car.g
    if car.speed < car.g and car.speed < vmax:
        car.speed += 1
    if car.speed == vmax and cc:
        prob = 0
    else:
        prob = p
    if car.speed > 0 and to.random.randint(1, 100) <= 100*prob:
        car.speed -= 1
    lane.move_car(car)

def stca(data, lane, vmax, n=10, p=0.50, cc=False):
    """Use the STCA model to simulate the specified lane for 'n' discrete steps with probability 'p' for a car slowing down and with a speed limit of 'vmax' (measured in discrete steps). Setting argument 'cc' to 'True' activates Cruise Control mode. 'data' refers to the data-holding object that will store the simulation's data."""
    data.build_position_history(lane)
    data.build_speed_history(lane)
    data.update_length(lane)
    data.update_number(lane)
    for i in range(n):
        lane.g_update_all()
        for car in lane.carlist:
            update_and_move(car, lane, vmax, p, cc)
        #this is where you want to grab data for graphs, animation, etc.
        #print lane
        data.append_position_history(lane)
        data.append_speed_history(lane)
    lane.g_update_all()
    
def ca184(data, lane, vmax, n=10, cc=False):
    """Use the CA184 model to simulate the specified lane for 'n' discrete steps with a speed limit of 'vmax' (measured in discrete steps). Setting argument 'cc' to 'True' activates Cruise Control mode. 'data' refers to the data-holding object that will store the simulation's data."""
    stca(lane, vmax, n, 0, cc)
    
def asep(data, lane, vmax, n=20, p=0, cc=False):
    """Use the ASEP model to simulate the specified lane for 'n' discrete steps with probability 'p' for a car slowing down and with a speed limit of 'vmax' (measured in discrete steps). Setting argument 'cc' to 'True' activates Cruise Control mode. 'data' refers to the data-holding object that will store the simulation's data."""
    data.build_position_history(lane)
    data.build_speed_history(lane)
    data.update_length(lane)
    data.update_number(lane)
    for i in range(n):
        car = to.random.choice(lane.carlist)
        update_and_move(car, lane, vmax, p, cc)
        #this is where you want to grab data for graphs, animation, etc.
        #print lane
        data.append_position_history(lane)
        data.append_speed_history(lane)
        lane.g_update_all()
    