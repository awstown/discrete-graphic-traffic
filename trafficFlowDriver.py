# Traffic Model Driver




import traffic_objects as to
import rules as r
import analysis as a


# create the lane with 20 cells
lane = to.Lane(20)
lane.populate(5)
print a.getDensity(lane)

# Loop with the stca model and print out the lane
r.stca(lane,3) # default is 10 iterations