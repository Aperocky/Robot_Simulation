from matplotlib import pyplot as plt
from pprint import pprint
import sys
import math

def readfile(*args):

    filename = 'records.log'
    #Get filename.
    if len(args) > 0:
        reps = int(args[0])
    else:
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

        robotpos.extend(locallist)
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

        detected.extend(locallist)
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

        undetected.extend(locallist)

    return robotpos, detected, undetected

def plot(robotpos, detected, undetected, radius):

    # Highlight the arena
    x1 = range(-radius,radius)
    y1 = list(map(lambda x: math.sqrt(radius*radius - x*x), x1))
    y2 = list(map(lambda x: -math.sqrt(radius*radius - x*x), x1))
    plt.fill_between(x1, radius, y1, facecolor='blue', alpha=0.5)
    plt.fill_between(x1, -radius, y2, facecolor='blue', alpha=0.5)

    # Plot the robots and targets
    plt.scatter(*zip(*robotpos), s=4, c='r')
    plt.scatter(*zip(*detected), s=4, c='b')
    plt.scatter(*zip(*undetected), s=4, c='g')
    plt.axis([-radius,radius,-radius,radius])
    plt.show()
    plt.savefig("arenamap.png")

if __name__ == "__main__":
    radius = 100
    time = 120
    if len(sys.argv) > 1:
        radius = int(sys.argv[1])
    if len(sys.argv) > 2:
        time = int(sys.argv[2])
    r, g, b = readfile(time)
    plot(r,g,b, radius)
