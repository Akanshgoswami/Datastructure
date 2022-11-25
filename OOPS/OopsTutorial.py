class P :
    def __init__(self, x):
        self.set_x(x)
    def get_x(self):
        return self.__value
    def set_x(self, x):
        if x < 0:
            self.__value = 0
        elif x > 1000:
            self.__value = 1000
        else:
            self.__value = x