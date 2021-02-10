# example code to make a contour plot of  a function

import numpy as np
import matplotlib.pyplot as plt

lambda1 = 5
lambda2 = 3
omega = 3
a1 = 1
a2 = 1

# example anonymous function
g = lambda x, y: (lambda1 / 2) * np.power((x-a1), 2) + (lambda2 / 2) * np.sin(omega * (y - a2))
  
# calculate function value(s) on a grid
X, Y = np.meshgrid(np.linspace(-1.0, 3.0, endpoint = True), np.linspace(0.0, 4.0, endpoint = True))
Z = g(X, Y)

plot = plt.contour(X, Y, Z)

plt.clabel(plot, inline = 1, fontsize = 10)
plt.title('Example contour plot')

# some addition data points
xs = [0.6, 1.3, 1.78, 1.2, 1]
ys = [1, 3, 1, 2, 1.5]

plt.scatter(xs, ys) # draw points
plt.plot(xs, ys) # add lines between points

plt.show()

