"""
Matplotlib Animation Example

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

R2=8
R1=3
StarCorners=5
transformSteps=40

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-R2, R2), ylim=(-R2, R2))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    i = i % transformSteps
    half = transformSteps / 2

    if i <= half:
        innerRadius = R2 - (R2-R1)*i/(half)
    else:
        i = i - half - 1
        # i can be now from 0 to half
        innerRadius = R1 + (R2-R1)*(i)/(half)
    # the even point values are on innerRadius
    # the odd points are on on R2
    x = []
    y = []
    totalPoints = 2*StarCorners
    start = np.pi/2 - 2.0*np.pi / totalPoints if StarCorners % 2 == 1 else 0.0
    for index in range(totalPoints):
        angle = start + 2.0*np.pi / totalPoints * index
        radiusUsed = innerRadius if (index % 2 == 0) else R2
        xp = radiusUsed * np.cos(angle)
        yp = radiusUsed * np.sin(angle)
        x.append(xp)
        y.append(yp)

    line.set_data(x + [x[0]], y+[y[0]])
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=2000, interval=1000.0/transformSteps, blit=False)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
