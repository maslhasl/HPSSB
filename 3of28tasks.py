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
        #Случай когда i < 0 или i > count
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        #Случай когда count == capacity
        if self.count == self.capacity:
            self.resize(2 * self.capacity) #Увеличиваем capacity
        #Случай когда i < count
        if i < self.count:
            for j in range(self.count,i,-1): #Сдвигаем элементы с индексом >= i+1 вправо
                self.array[j] = self.array[j-1]
        #Вставляем itm на место с индексом i
        self.array[i] = itm
        self.count += 1 #Увеличиваем count на 1


#2. Добавьте метод delete(i), который удаляет объект из i-й позиции, при необходимости сжимая буфер.
    def delete(self, i):
        if self.count == 0:
            raise IndexError('DynArr is empty')
        #Случай когда i < 0 или i > count
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        for j in range(i,self.count-1):
            self.array[j] = self.array[j+1]

        self.count -= 1 #Уменьшаем количество элементов на один
        self.array[self.count] = None #Очистка последнего элемента, после сдвига

        #Уменьшение capacity массива
        if self.count < self.capacity/2:
            new_capacity = max(16, int(self.capacity / 1.5))
            if new_capacity != self.capacity:
                self.resize(new_capacity)
        # удаляем объект в позиции i

#В обоих случаях, если индекс i лежит вне допустимых границ, генерируйте исключение.
#Важно, единственное исключение: для метода insert() параметр i может принимать значение,
#равное длине рабочего массива count, в таком случае добавление происходит в его хвост.

