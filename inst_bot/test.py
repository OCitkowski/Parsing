class Point():

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @classmethod
    def __check_value(cls, val):
        if (isinstance(val, int) or isinstance(val, float)):
            return True
        else:
            return False

    def set_coords(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            print(f' error ')

    def get_coords(self):
        print(self.__x, self.__y)

    @staticmethod
    def sq(x, y):
        return x*x + y*y


if __name__ == '__main__':
    p = Point(2, 3)
    p.get_coords()
    p.set_coords(45, 67)
    p.get_coords()
    p.set_coords('45', 67)
    print(p.sq(7654, 65))
