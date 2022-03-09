import math
def proverka():
    check=True
    while check:
        try:
            x = float(input())
            check=False
        except ValueError:
            print("Введены некорректные данные(буквы или символы)")
    return x

def main():
    print("Введите координаты первой точки по оси х")
    x1=proverka()
    print("Введите координаты второй точки по оси х")
    x2 = proverka()
    print("Введите координаты первой точки по оси у")
    y1= proverka()
    print("Введите координаты второй точки по оси у")
    y2 = proverka()
    c=math.sqrt((x2-x1)**2+(y2-y1)**2)
    print(c)


if __name__ == '__main__':
    print("Введите 1,чтобы посчитать расстояние между точками, или 0, чтобы завершить")
    m=proverka()
    while m != 0:
        if (m == 1):
            main()
            print("Введите 1,чтобы посчитать расстояние между точками, или 0, чтобы завершить")
            m = proverka()
        else:
            while (m != 0) and (m != 1):
                print("Введены некорректные данные, введите 1,чтобы посчитать расстояние между точками, или 0, чтобы завершить")
                m = proverka()


