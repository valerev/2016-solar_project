from matplotlib import pyplot as plt
import numpy as np

def show_speed_of_time(filename, object_number : int):
    fig = plt.figure()
    ax = plt.axes()
    with open(filename, 'r') as source:
        number_of_objects = 0
        counting_objects = True
        counter = 0
        X = np.array([])
        Y = np.array([])
        for line in source:
            if counting_objects:
                if line[0] == "#":
                    counting_objects = False
                    if object_number<1 or object_number>=number_of_objects:
                        print('Bad choice. No object with such serial number')
                        return
                else:
                    number_of_objects += 1
                continue
            if counter == 0:
                X = np.append(X, float(line.split()[0]))
            elif counter == object_number:
                parameters = line.split()
                Y = np.append(Y, np.sqrt(float(parameters[3])**2 + float(parameters[2])**2)) 
            counter += 1; counter %= (number_of_objects + 1)

        print (len(X))
        print (len(Y))
        ax.plot(X, Y)
        plt.show()

if __name__ == "__main__":
    show_speed_of_time('statistics', 1)
