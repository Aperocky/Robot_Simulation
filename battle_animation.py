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
    if len(undetected[0])>0:
        ax.scatter(*zip(*detected[0]), s=10, c='b')
    if len(undetected[0])>0:
        ax.scatter(*zip(*undetected[0]), s=10, c='g')

    def update(i):
    # Plot the robots and targets
        ax.scatter(*zip(*robotpos[i]), s=2, c='r')
        if len(detected[i])>0:
            ax.scatter(*zip(*detected[i]), s=2, c='b')
        if len(undetected[i])>0:
            ax.scatter(*zip(*undetected[i]), s=2, c='g')
        return ax

    anim = FuncAnimation(fig, update, frames=range(1, time), interval=50)
    plt.show()
    return anim
    # anim.save('arena.mp4', writer='ffmpeg')

if __name__ == "__main__":
    save = False
    radius = 100
    time = 120
    fname = "arena"
    if len(sys.argv) > 1 and not sys.argv[1] == 'DEFAULT':
        radius = int(sys.argv[1])
    if len(sys.argv) > 2 and not sys.argv[2] == 'DEFAULT':
        time = int(sys.argv[2])
    if len(sys.argv) > 3 and sys.argv[3] == 'save':
        save = True;
    if len(sys.argv) > 4:
        fname = sys.argv[4]
    r, g, b = readfile(time)
    anim = plot(r,g,b, radius, time)
    if save:
        anim.save(fname+'.mp4', writer='ffmpeg')
