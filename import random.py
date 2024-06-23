import random
import matplotlib.pyplot as plt
x = []
y = [] 
for i in range(50):
    x.append(random.randrange(0, 101))
    y.append(random.randrange(0, 101))

plt.scatter(x,y)
plt.show()