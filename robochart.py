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

plt.plot(range(1,11),klist, '.')
plt.title('M = N, Radius = 100')
plt.xlabel('Robots/Targets Number')
plt.ylabel('Average Detection over 20 Cycles')
plt.grid(True)
plt.show()
plt.close()

klist.clear()
for i in range(10):
    m = (i+1);
    n = (i+1)*2;
    radius = 100;
    value = (subprocess.Popen("java -jar Robotarium.jar %d %d 100" %(m, n), shell=True, stdout=subprocess.PIPE).
                 communicate()[0])
    klist.append(float(value.rstrip()))

plt.plot(range(1,11), klist, '.')
plt.title('2M = N, Radius = 100')
plt.xlabel('Robots Number')
plt.ylabel('Average Detection over 20 Cycles')
plt.grid(True)
plt.show()
plt.close()

klist.clear()
for i in range(5):
    m = (i+1)*2;
    n = (i+1);
    radius = 100;
    value = (subprocess.Popen("java -jar Robotarium.jar %d %d 100" %(m, n), shell=True, stdout=subprocess.PIPE).
                 communicate()[0])
    klist.append(float(value.rstrip()))

plt.plot(range(1,6), klist, '.')
plt.title('M = 2N, Radius = 100')
plt.xlabel('Target Number')
plt.ylabel('Average Detection over 20 Cycles')
plt.grid(True)
plt.show()
plt.close()

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

plt.plot(dlist, klist, '.')
plt.title('M=N=10, Radius from 100m to 500m')
plt.xlabel('Radius in meters')
plt.ylabel('Average Detection over 20 Cycles')
plt.grid(True)
plt.show()
plt.close()