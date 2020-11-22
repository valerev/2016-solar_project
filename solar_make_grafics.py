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

        ax.plot(X, Y)
        plt.show()


def show_distance_of_time(filename, object_number_1 : int, object_number_2 : int):
    fig = plt.figure()
    ax = plt.axes()
    with open(filename, 'r') as source:
        number_of_objects = 0
        counting_objects = True
        counter = 0
        if object_number_1==object_number_2:
            print('Bad choice. You have selected same objects')
            return
        X = np.array([])
        Y = np.array([])
        for line in source:
            if counting_objects:
                if line[0] == "#":
                    counting_objects = False
                    if object_number_1<1 or object_number_1>=number_of_objects:
                        print('Bad choice. No object with such serial number')
                        return
                    elif object_number_2<1 or object_number_2>=number_of_objects:
                        print('Bad choice. No object with such serial number')
                        return
                else:
                    number_of_objects += 1
                continue
            if counter == 0:
                X = np.append(X, float(line.split()[0]))
            elif counter == object_number_1:
                pos_1 = line.split()[:2]
            elif counter == object_number_2:
                pos_2 = line.split()[:2]
                delta_x = float(pos_1[0]) - float(pos_2[0])
                delta_y = float(pos_1[1]) - float(pos_2[1])
                Y = np.append(Y, np.sqrt(delta_x**2 + delta_y**2)) 
            counter += 1; counter %= (number_of_objects + 1)

        ax.plot(X, Y)
        plt.show()


if __name__ == "__main__":
    show_distance_of_time('statistics', 1, 2)
