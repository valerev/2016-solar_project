from matplotlib import pyplot as plt
import numpy as np

def show_speed_of_time(filename, object_number : int):
    fig = plt.figure()
    ax = plt.axes()
    ax.set_title('graph of speed versus time')
    plt.xlabel('T, s')
    plt.ylabel('V, km/s')
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
                        print('Bad choice. No object with such serial number' + '\n')
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


def show_speed_of_distance(filename, object_number_1 : int, object_number_2 : int):
    fig = plt.figure()
    ax = plt.axes()
    ax.set_title('graph of speed versus distance')
    plt.xlabel('D, km')
    plt.ylabel('V, km/s')
    with open(filename, 'r') as source:
        number_of_objects = 0
        counting_objects = True
        counter = 0
        if object_number_1==object_number_2:
            print('Bad choice. You have selected same objects' + '\n')
            return
        X = np.array([])
        Y = np.array([])
        for line in source:
            if counting_objects:
                if line[0] == "#":
                    counting_objects = False
                    if object_number_1<1 or object_number_1>=number_of_objects:
                        print('Bad choice. No object with such serial number' + '\n')
                        return
                    elif object_number_2<1 or object_number_2>=number_of_objects:
                        print('Bad choice. No object with such serial number' + '\n')
                        return
                else:
                    number_of_objects += 1
                continue
            if counter == object_number_1:
                pos_1 = line.split()[:2]
            elif counter == object_number_2:
                Y = np.append(Y, np.sqrt(float(line.split()[3])**2 + float(line.split()[2])**2))
                pos_2 = line.split()[:2]
                delta_x = float(pos_1[0]) - float(pos_2[0])
                delta_y = float(pos_1[1]) - float(pos_2[1])
                X = np.append(X, np.sqrt(delta_x**2 + delta_y**2)) 
            counter += 1; counter %= (number_of_objects + 1)

        ax.plot(X, Y)
        plt.show()



def show_distance_of_time(filename, object_number_1 : int, object_number_2 : int):
    fig = plt.figure()
    ax = plt.axes()
    ax.set_title('graph of distance versus time')
    plt.xlabel('T, s')
    plt.ylabel('D, km')
    with open(filename, 'r') as source:
        number_of_objects = 0
        counting_objects = True
        counter = 0
        if object_number_1==object_number_2:
            print('Bad choice. You have selected same objects' + '\n')
            return
        X = np.array([])
        Y = np.array([])
        for line in source:
            if counting_objects:
                if line[0] == "#":
                    counting_objects = False
                    if object_number_1<1 or object_number_1>=number_of_objects:
                        print('Bad choice. No object with such serial number' + '\n')
                        return
                    elif object_number_2<1 or object_number_2>=number_of_objects:
                        print('Bad choice. No object with such serial number' + '\n')
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

def show_all_graphs(filename, object_number_1, object_number_2):
    fig = plt.figure()
    ax1 = fig.add_subplot(131)
    ax1.set_title('graph of speed versus time')
    ax1.set_xlabel('T, s')
    ax1.set_ylabel('V, km/s')
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
                    if object_number_1 < 1 or object_number_1 >= number_of_objects:
                        print('Bad choice. No object with such serial number' + '\n')
                        return
                else:
                    number_of_objects += 1
                continue
            if counter == 0:
                X = np.append(X, float(line.split()[0]))
            elif counter == object_number_1:
                parameters = line.split()
                Y = np.append(Y, np.sqrt(float(parameters[3])**2 + float(parameters[2])**2)) 
            counter += 1; counter %= (number_of_objects + 1)

        ax1.plot(X, Y)
    
    ax2 = fig.add_subplot(132)
    ax2.set_title('graph of speed versus distance')
    ax2.set_xlabel('D, km')
    ax2.set_ylabel('V, km/s')
    with open(filename, 'r') as source:
        number_of_objects = 0
        counting_objects = True
        counter = 0
        if object_number_1==object_number_2:
            print('Bad choice. You have selected same objects' + '\n')
            return
        X = np.array([])
        Y = np.array([])
        for line in source:
            if counting_objects:
                if line[0] == "#":
                    counting_objects = False
                    if object_number_1<1 or object_number_1>=number_of_objects:
                        print('Bad choice. No object with such serial number' + '\n')
                        return
                    elif object_number_2<1 or object_number_2>=number_of_objects:
                        print('Bad choice. No object with such serial number' + '\n')
                        return
                else:
                    number_of_objects += 1
                continue
            if counter == object_number_1:
                pos_1 = line.split()[:2]
            elif counter == object_number_2:
                pos_2 = line.split()[:2]
                try:
                    delta_x = float(pos_1[0]) - float(pos_2[0])
                    delta_y = float(pos_1[1]) - float(pos_2[1])
                    X = np.append(X, np.sqrt(delta_x**2 + delta_y**2)) 
                    Y = np.append(Y, np.sqrt(float(line.split()[3])**2 + float(line.split()[2])**2))
                except:
                    pass
            counter += 1; counter %= (number_of_objects + 1)

        ax2.plot(X, Y)


    ax3 = fig.add_subplot(133)
    ax3.set_title('graph of distance versus time')
    ax3.set_xlabel('T, s')
    ax3.set_ylabel('D, km')
    with open(filename, 'r') as source:
        number_of_objects = 0
        counting_objects = True
        counter = 0
        if object_number_1==object_number_2:
            print('Bad choice. You have selected same objects' + '\n')
            return
        X = np.array([])
        Y = np.array([])
        for line in source:
            if counting_objects:
                if line[0] == "#":
                    counting_objects = False
                    if object_number_1<1 or object_number_1>=number_of_objects:
                        print('Bad choice. No object with such serial number' + '\n')
                        return
                    elif object_number_2<1 or object_number_2>=number_of_objects:
                        print('Bad choice. No object with such serial number' + '\n')
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

        ax3.plot(X, Y)
        

    plt.show()



if __name__ == "__main__":
    choice = input('Please, choose which graph you want to see:' + '\n' + \
                    '1: graph of speed versus time' + '\n' + \
                    '2: graph of distance between two bodies versus time' + '\n' + \
                    '3: graph of spedd of body versus distance between this and another one' + '\n' + \
                    '4: show all graphs' + '\n')

    file_name = input('Write down name of file with statistics' + '\n')
    
    if choice == '1':
        try:
            object_number = int(input('Choose serial number of observing object' + '\n'))
        except:
            print ('Write only integers as serial number' + '\n')
        show_speed_of_time(file_name, object_number)
    
    elif choice == '2':
        try:
            object_number_1 = int(input('Choose serial number of first observing object' + '\n'))
            object_number_2 = int(input('Choose serial number of second observing object' + '\n'))
        except:
            print ('Write only integers as serial numbers' + '\n')
        show_distance_of_time(file_name, object_number_1, object_number_2)

    elif choice == '3':
        try:
            object_number_1 = int(input('Choose serial number of first observing object' + '\n')) 
            object_number_2 = int(input('Choose serial number of second observing object' + '\n'))
        except:
            print ('Write only integers as serial numbers' + '\n')
        show_speed_of_distance(file_name, object_number_1, object_number_2)
        
    elif choice == '4':
        try:
            object_number_1 = int(input('Choose serial number of first observing object' + '\n')) 
            object_number_2 = int(input('Choose serial number of second observing object' + '\n'))
        except:
            print ('Write only integers as serial numbers' + '\n')
        show_all_graphs(file_name, object_number_1, object_number_2)


    
