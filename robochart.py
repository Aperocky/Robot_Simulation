import subprocess
from matplotlib import pyplot as plt

klist = []
for i in range(10):
    m = (i+1);
    n = (i+1);
    radius = 100;
    value = (subprocess.Popen("java -jar Robotarium.jar %d %d 100" %(m, n), shell=True, stdout=subprocess.PIPE).
                 communicate()[0])
    klist.append(float(value.rstrip()))

fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.plot(range(1,11),klist, '.')
ax.set_title("M = N, Radius = 100")
ax.set_xlabel('Robots/Targets Number')
ax.set_ylabel('Average Detection over 20 Cycles')
ax.grid(True)
fig1.savefig('figure1.png')

klist.clear()
for i in range(10):
    m = (i+1);
    n = (i+1)*2;
    radius = 100;
    value = (subprocess.Popen("java -jar Robotarium.jar %d %d 100" %(m, n), shell=True, stdout=subprocess.PIPE).
                 communicate()[0])
    klist.append(float(value.rstrip()))

fig2 = plt.figure()
ax = fig2.add_subplot(111)
ax.plot(range(1,11), klist, '.')
ax.set_title('2M = N, Radius = 100')
ax.set_xlabel('Robots Number')
ax.set_ylabel('Average Detection over 20 Cycles')
ax.grid(True)
fig2.savefig('figure2.png')

klist.clear()
for i in range(5):
    m = (i+1)*2;
    n = (i+1);
    radius = 100;
    value = (subprocess.Popen("java -jar Robotarium.jar %d %d 100" %(m, n), shell=True, stdout=subprocess.PIPE).
                 communicate()[0])
    klist.append(float(value.rstrip()))

fig3 = plt.figure()
ax = fig3.add_subplot(111)
ax.plot(range(1,6), klist, '.')
ax.set_title('M = 2N, Radius = 100')
ax.set_xlabel('Target Number')
ax.set_ylabel('Average Detection over 20 Cycles')
ax.grid(True)
fig3.savefig('figure3.png')

klist.clear()
dlist = []
for i in range(9):
    m = 10;
    n = 10;
    radius = (i+2)*50;
    value = (subprocess.Popen("java -jar Robotarium.jar %d %d %d" %(m, n, radius), shell=True, stdout=subprocess.PIPE).
                 communicate()[0])
    klist.append(float(value.rstrip()))
    dlist.append(radius)

fig4 = plt.figure()
ax = fig4.add_subplot(111)
ax.plot(dlist, klist, '.')
ax.set_title('M=N=10, Radius from 100m to 500m')
ax.set_xlabel('Radius in meters')
ax.set_ylabel('Average Detection over 20 Cycles')
ax.grid(True)
fig4.savefig('figure4.png')
plt.close()

for k in range(5):

    radius = (k+1)*100
    klist.clear()
    ratio = [.2, .5, 1, 4, 10]
    for i in ratio:
        m = 5;
        n = int(i*m)
        value = (subprocess.Popen("java -jar Robotarium.jar %d %d %d" %(m, n, radius), shell=True, stdout=subprocess.PIPE).
                     communicate()[0])
        klist.append(float(value.rstrip()))

    figname = 'figure1' + str(k)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(range(5), klist, '.')
    ax.set_title('Detection as n/m ratio change, Robots = 5, Radius = %d' % radius)
    ax.set_xlabel('Ratio n/m')
    plt.xticks(range(5), ratio)
    ax.set_ylabel('Average Detection over 20 Cycles')
    ax.grid(True)
    fig.savefig(figname+'.png')
    plt.close()
