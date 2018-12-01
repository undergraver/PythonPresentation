"""
============
3D animation
============

A simple example of an animated plot... In 3D!
"""
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


def Gen_RandLine(length, dims=2):
    """
    Create a line using a random walk algorithm

    length is the number of points for the line.
    dims is the number of dimensions the line has.
    """
    lineData = np.empty((dims, length))
    lineData[:, 0] = np.random.rand(dims)
    for index in range(1, length):
        # scaling the random numbers by 0.1 so
        # movement is small compared to position.
        # subtraction by 0.5 is to change the range to [-0.5, 0.5]
        # to allow a line to move backwards.
        step = ((np.random.rand(dims) - 0.5) * 0.1)
        lineData[:, index] = lineData[:, index - 1] + step

    return lineData


def update_lines(num, dataLines, lines):
    for line, data in zip(lines, dataLines):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines

def plot3d(ax,coords3d):
    xcoords = [cp[0] for cp in coords3d]
    ycoords = [cp[1] for cp in coords3d]
    zcoords = [cp[2] for cp in coords3d]

    ax.plot(xs=xcoords,ys=ycoords,zs=zcoords,color='red')    

# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

# Fifty lines of random 3-D lines
data = [Gen_RandLine(25, 3) for index in range(50)]

# Creating fifty line objects.
# NOTE: Can't pass empty arrays into 3d version of plot()
lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]

# Setting the axes properties
ax.set_xlim3d([-10.0, 10.0])
ax.set_xlabel('X')

ax.set_ylim3d([-10.0, 10.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-10.0, 10.0])
ax.set_zlabel('Z')

ax.set_title('3D Test')

# we draw a sphere with R radius around origin (0,0,0)
# we do it with the following points:
# 1. the upper (north) point which is at (0,0,R)
# 2. the lower (south) point which is at (0,0,-R)
# 3. the number of 'intermediate' circles the sphere must have
# 4. the number of points per each previously described circle

R=10 # the radius
NCircles = 10
NPointsPerCircle = 10
North = [0,0,R]

circlePointsArray = [] # multiple circles

South = [0,0,-R]

IncrementAngle=np.pi / (NCircles+1)
angle = 0
for circleIndex in range(NCircles):
    angle = angle + IncrementAngle

    zpos = R*np.cos(angle)
    radius = R*np.sin(angle)
    circlePoints=[]
    circleAngleIncrement = 2.0*np.pi / NPointsPerCircle
    circleAngle = 0
    for circlePointIndex in range(NPointsPerCircle):
        x = radius*np.sin(circleAngle)
        y = radius*np.cos(circleAngle)
        circleAngle = circleAngle+circleAngleIncrement
        circlePoints.append([x,y,zpos])

    plot3d(ax,circlePoints+[circlePoints[0]])

    circlePointsArray.append(circlePoints)


for index in range(NPointsPerCircle):
    arr = [North]
    for circleIndex in range(NCircles):
        arr.append(circlePointsArray[circleIndex][index])
    arr.append(South)
    plot3d(ax,arr)

# Creating the Animation object
#line_ani = animation.FuncAnimation(fig, update_lines, 25, fargs=(data, lines),
#                                   interval=50, blit=False)

#line_ani.save('3danimation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
#plt.axis('off')
plt.show()


