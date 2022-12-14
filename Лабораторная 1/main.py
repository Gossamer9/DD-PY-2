class Rational:
    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int):
            raise TypeError('Тип числителя должен быть int!')
        self.numerator = numerator
        if not isinstance(denominator, int):
            raise TypeError('Тип знаменателя должен быть int!')
        self.denominator = denominator
    def squaring(self):
        #Возведение во 2 степень
        ...

class Matrix:
    def __init__(self, columlen: int, strlen: int, lst: list):
        self.columlen = columlen
        self.strlen = strlen
        if len(lst) != columlen*strlen:
            raise ValueError('Список неверной длины')
        self.lst = lst

    def transposition(self):
        #Транспонированная матрицы
        ...
    def inverse(self):
        #Обратная матрица
        ...

class Laptop:
    def __init__(self, model: str, manufacturer: str, prise: int):
        self.model = model
        self.manufacturer = manufacturer
        if prise > 50000:
            raise ValueError('Ноутбук слишком дорогой')
        self.prise = prise

if __name__ == "__main__":
    half = Rational (1,2)
    quarter = Rational (1,4)
    ones = Matrix(1,1,[1])
    first_choice = Laptop("Slim7Pro","Lenovo", 40000)
    second_choice = Laptop("MacBook10,1", "Apple", 120000)
    import doctest
    doctest.testmod()
    pass

