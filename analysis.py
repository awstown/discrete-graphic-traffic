# Traffic Flow analysis module.
import traffic_objects
import matplotlib
matplotlib.use('Agg')
from pylab import figure, show
import numpy as np

def current(lane):
    """Returns the average speed of all cars on the lane"""
    s = 0
    for car in lane.carlist:
        s = s + car.speed
    return float(s)/len(lane.carlist)

def getDensity(lane):
    """Returns the density of traffic (i.e. #ofCars / LengthOfRoad)"""
    return (float(len(lane.carlist)) / lane.length)

def analyze(lane):
    """Spits out Density and current varibles to a file or object outside of the the lane"""
    return 0;

def plotHello():
    # make an agg figure
    fig = figure()
    ax = fig.add_subplot(111)
    ax.plot([1,2,3,4])
    ax.set_title('a simple figure')
    fig.canvas.draw()
    
    # grab rhe pixel buffer and dumpy it into a numpy array
    #buf = fig.canvas.buffer_rgba(0,0)
    #l, b, w, h = fig.bbox.bounds
    #X = np.fromstring(buf, np.uint8)
    #X.shape = h,w,4
    
    # now display the array X as an Axes in a new figure
    fig2 = figure()
    ax2 = fig2.add_subplot(111, frameon=False)
    ax2.imshow(X)
    show()
    
## Generate Data
lor = 100
for i in range(100):
    stca()
    asep()
    ca184()

# Outputs: dataSTCA, dataASEP, dataCA184

## Process Data

# get data for 3 graphs one for each model.

## Plot the graphs
#using matplotlib

    



    

