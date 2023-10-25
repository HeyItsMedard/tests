class Data:
    def __init__(self, data1, data2, data3):
        self._data1 = data1
        self._data2 = data2
        self._data3 = data3

    @classmethod
    def from_array(cls, array):
        return cls(*array)

    @staticmethod
    def welcome_user(user):
        print(f'Hello {user} you are using Data class currently')

    def __str__(self):
        return f'{self._data1}, {self._data2}, {self._data3}'

d = Data(1, 2, 3)
d2 = Data.from_array([3, 4, 5])
d2.welcome_user('Bob')
Data.welcome_user('Alice')
print(d2)
