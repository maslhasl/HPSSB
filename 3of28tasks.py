import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1
#1. Добавьте метод insert(i, itm), который вставляет в i-ю позицию объект itm, сдвигая вперёд все последующие элементы.
# Учтите, что новая длина массива может превысить размер буфера.
    def insert(self, i, itm):
        #Случай когда i < 0 и i > count
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        #Случай когда count == capasity
            #Увеличиваем capacity
            #Случай когда i == count
                #Добавляем itm в хвост массива
            #Случай когда i < count
                #Сдвигаем элементы с индексом >= i+1 вправо
                #Добавляем itm на освободившееся место
            #Увеличиваем count на 1

        #Случай когда count < capacity
            #Случай когда i > count
                #Добавляем itm в хвост массива
            #Случай когда i < count
                #Сдвигаем элементы с индексом >= i+1 вправо
                #Добавляем itm на освободившееся место
            #Увеличиваем count на 1
    #добавляем объект itm в позицию i, начиная с 0

#2. Добавьте метод delete(i), который удаляет объект из i-й позиции, при необходимости сжимая буфер.
    def delete(self, i):
        # удаляем объект в позиции i

#В обоих случаях, если индекс i лежит вне допустимых границ, генерируйте исключение.
#Важно, единственное исключение: для метода insert() параметр i может принимать значение,
#равное длине рабочего массива count, в таком случае добавление происходит в его хвост.

