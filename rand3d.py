import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import random


def random_color():
    color_arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    color = ""
    for i in range(6):
        color += color_arr[random.randint(0, 14)]
    return "#" + color


if __name__ == "__main__":
    ndarray = np.random.random_sample((100, 3))
    print(ndarray)

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    for i in ndarray:
        ax.scatter(abs(i[0]), abs(i[1]), abs(i[2]), c=random_color())

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()
