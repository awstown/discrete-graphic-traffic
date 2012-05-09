# Traffic Flow analysis module.
import traffic_objects


def getDensity(l):
    """Returns the density of traffic (i.e. #ofCars / LengthOfRoad)"""
    return (float(len(l.carlist)) / l.length)

def current(lane):
    return 0
    


