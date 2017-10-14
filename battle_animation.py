from matplotlib import pyplot as plt
from pprint import pprint
from matplotlib.animation import FuncAnimation
import math
import sys
import seaborn

def readfile(*args):

    #Get filename.
    if len(args) > 1:
        filename = args[0]
        reps = int(args[1])
    else:
        filename = "records.log"
        reps = 120

    robotpos = []
    detected = []
    undetected = []

    fr = open(filename, 'r')

    for time in range(reps):
        while(True):
            line = fr.readline()
            if 'TIME' in line:
                index = int(line.split()[1])
                break
        line = fr.readline()

        # Create a local list to append position of different robots.
        locallist = []
        while(True):
            line = fr.readline()
            # Break if encountered end.
            if 'DISCOVERED' in line:
                break

            # Format strings
            info = line.split(',')
            for char in "()":
                info[0] = info[0].replace(char, '')
                info[1] = info[1].replace(char, '')
            xpos = float(info[0].strip())
            ypos = float(info[1].strip())

            # Store position information in tuples
            position = (xpos, ypos)
            locallist.append(position)

        robotpos.append(locallist)
        del locallist

        locallist = []
        while(True):
            line = fr.readline()
            if 'TARGETS' in line:
                break
            info = line.split(',')
            for char in "()":
                info[0] = info[0].replace(char, '')
                info[1] = info[1].replace(char, '')
            xpos = float(info[0].strip())
            ypos = float(info[1].strip())
            position = (xpos, ypos)
            locallist.append(position)

        detected.append(locallist)
        del locallist

        locallist = []
        while(True):
            line = fr.readline()
            if 'TARGETS' in line:
                break
            info = line.split(',')
            for char in "()":
                info[0] = info[0].replace(char, '')
                info[1] = info[1].replace(char, '')
            xpos = float(info[0].strip())
            ypos = float(info[1].strip())
            position = (xpos, ypos)
            locallist.append(position)

        undetected.append(locallist)

    return robotpos, detected, undetected

def plot(robotpos, detected, undetected, radius, time):

    fig, ax = plt.subplots()

    # Highlight the arena
    x1 = range(-radius,radius)
    y1 = list(map(lambda x: math.sqrt(radius*radius - x*x), x1))
    y2 = list(map(lambda x: -math.sqrt(radius*radius - x*x), x1))
    ax.fill_between(x1, radius, y1, facecolor='blue', alpha=0.5)
    ax.fill_between(x1, -radius, y2, facecolor='blue', alpha=0.5)
    ax.axis([-radius,radius,-radius,radius])
    ax.scatter(*zip(*robotpos[0]), s=10, c='r')
    ax.scatter(*zip(*detected[0]), s=10, c='b')
    ax.scatter(*zip(*undetected[0]), s=10, c='g')

    def update(i):
    # Plot the robots and targets
        print(i)
        ax.scatter(*zip(*robotpos[i]), s=2, c='r')
        if len(detected[i])>0:
            ax.scatter(*zip(*detected[i]), s=2, c='b')
        ax.scatter(*zip(*undetected[i]), s=2, c='g')
        return ax

    anim = FuncAnimation(fig, update, frames=range(1, time), interval=50)
    anim.save('arena.mp4', writer='ffmpeg')
    plt.show()

if __name__ == "__main__":
    radius = 100
    time = 120
    if len(sys.argv) > 1:
        radius = int(sys.argv[1])
    if len(sys.argv) > 2:
        time = int(sys.argv[2])
    r, g, b = readfile(time)
    plot(r,g,b, radius, time)
