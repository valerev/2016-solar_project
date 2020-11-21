# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet": 
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    print (len(objects))
    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    
    parametrs = line.split()
    star.R = int(parametrs[1])
    star.color = parametrs[2]
    star.m = float(parametrs[3])
    star.x = float(parametrs[4])
    star.y = float(parametrs[5])
    star.Vx = float(parametrs[6])
    star.Vy = float(parametrs[7])
    

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    
    parametrs = line.split()
    planet.R = int(parametrs[1])
    planet.color = parametrs[2]
    planet.m = float(parametrs[3])
    planet.x = float(parametrs[4])
    planet.y = float(parametrs[5])
    planet.Vx = float(parametrs[6])
    planet.Vy = float(parametrs[7])


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            if isinstance(obj, Star):
                out_file.write('Star %d %s %d %d %d %d %d \n' % (obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy))
            elif isinstance(obj, Planet):
                out_file.write('Planet %d %s %d %d %d %d %d \n' % (obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy))
            else:
                print('There is one impostor among us')


def write_statistics_about_object_to_file(statistics_filename, space_objects):
    """
    Сохраняет статичтические данные о положении и скорости объектов в файл.
    
    Формат вывода:
    
    <x> <y> <Vx> <Vy> 
    <x> <y> <Vx> <Vy>
    ...
    <x> <y> <Vx> <Vy>
    ### 
    
    "###" - означает что данные о всех объектах на данный момент записаны и начинается следующее мгновенье

    Параметры:

    **statistics_filename** - имя файла, в который ведются запись
    **space_objects** - список объектов планет и звёзд
    """

    with open(statistics_filename, 'a') as stat_file:
        for obj in space_objects:
            stat_file.write("%d %d %d %d \n" % (obj.x, obj.y, obj.Vx, obj.Vy))
        stat_file.write("### \n")


if __name__ == "__main__":
    print("This module is not for direct call!")
