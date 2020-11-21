from matplotlib import pyplot as plt
import numpy as np

def show_speed_of_time(filename, object_number):
    fig = plt.figure()
    ax = plt.axes()
    with open(filename, 'r') as source:
        number_of_objects = 0
        counting_objects = True
        counter = 0
        for line in source:
            if counting_objects:
                if line[0] == "#":
                    counting_objects = False
                else:
                    number_of_objects += 1
                continue
            if counter == object_number:
                parameters = line.split()
                speed = np.sqrt(float(parameters[3])**2 + float(parameters[2])**2)  # FIXME: Graph doesn't look normally
                ax.scatter(speed, counter)
            counter += 1; counter %= (number_of_objects + 1)

    plt.show()

if __name__ == "__main__":
    show_speed_of_time('statistics', 1)
