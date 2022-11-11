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
            if object_type == "star":  # FIXME: do the same for planet
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            else:
                print("Unknown space object")

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

    line = line.split()
    star.m = float(line[3])
    star.color = line[2]
    star.type = line[0]
    star.x = int(line[4])
    star.y = int(line[5])
    star.vx = int(line[6])
    star.vy = int(line[7])
    star.R = int(line[1])
    pass


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
       Входная строка должна иметь слеюущий формат:
       Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

       Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
       Пример строки:
       Planet 10 red 1000 1 2 3 4

       Параметры:

       **line** — строка с описанием планеты.
       **planet** — объект звезды.
       """
    a = line.split(" ")
    planet.R = float(a[1])
    planet.color = a[2]
    planet.m = int(a[3])
    planet.x = int(a[4])
    planet.y = int(a[5])
    planet.Vx = int(a[6])
    planet.Vy = int(a[7])
    #данные о планете
    pass 


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
            print(out_file, "%s %d %s %f %f %f %f %f" % (obj.type, obj.R, obj.color, obj.m, obj.x, obj.y, obj.vx, obj.vy))
            # FIXME: should store real values


# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")
