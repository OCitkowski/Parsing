
from cryptography.fernet import Fernet



class ChromeX():
    """Chrome browser"""
    __type = "ChromeX"

    def __init__(self, time_sleep:int = 5):
        self.time_sleep = time_sleep
        self.min_time_sleep = 5
        self.hand_time_sleep = 0
        self.print_time_sleep()
        self.bool_time_sleep = self.not_time_sleep()

    def print_time_sleep(self):
        print(self.time_sleep)

    def not_time_sleep(self):
        print('544645645456')
        return False

class FileX(ChromeX):

    def __init__(self, x):
        super(FileX, self).__init__()
        self.x = x

    def print_hand_time_sleep(self):
        print(f' {self.__dict__}  {self.hand_time_sleep}')


def encrypt_in_file(filename):

    with open(filename, "rt") as file:
        data =''
        lines = file.readlines()
        for line in lines:
            copy_l = line
            l_line = line.split('=')
            line = f'{l_line[0]}= {copy_l}'

            data = data + line + '\n'

    with open(filename, "w") as file:
        file.write(data)

if __name__ == '__main__':
    # ff = ChromeX(5)
    encrypt_in_file('xxx.py', )