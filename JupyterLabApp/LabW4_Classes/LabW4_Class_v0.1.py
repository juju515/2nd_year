# Import the library

import matplotlib.pyplot as plt
#%matplotlib inline

class Circle:

    def __init__(self, color, radius):
        self._color = color
        self._radius = radius

    # Method
    def add_radius(self, r):
        self._r = r
        radius = Circle._radius + r

    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

Circle("red",5)