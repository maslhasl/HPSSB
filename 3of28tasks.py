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
        self.array[self.count] = None #Очистка последнего элемента, после сдвига на всякий случай

        #логика сжатия
        if self.capacity <= 16:  # Ниже минимума не сжимаем
            return

        if self.count < self.capacity / 2:
            # Всегда уменьшаем ровно в 1.5 раза (но не меньше 16)
            new_capacity = max(16, self.capacity * 2 // 3)
            self.resize(new_capacity)


#3. Оцените меры сложности для этих двух методов.
# Для метода insert:
# Случай O(1) - лучший случай: добавление элемента в пустой массив или в конец массива без увеличения capacity

# Случай O(n) - худший случай: добавление элемента в начало массива с большим количеством элементов (например 100 тыс.), тк необходимо будет сдвинуть все элементы

# Средний O(n) - средний случай: добавление элемента в середину массива

# Для метода delete:
# Случай O(1) - лучший случай: удаление элемента с конца массива, сдвиг остальных элементов массива не требуется
# Случай O(n) - худший случай: удаление элемента из начала массива, требуется сдвиг остальных элементов массива
# Случай O(n) - средний случай: удаление элемента из середины массива, требуется сдвиг половины элементов массива

#4. Напишите тесты, проверяющие работу методов insert() и delete():

def test_dynarray():
    print("=== Тестирование DynArray ===")

    # Тест 1: Вставка без превышения буфера
    print("\n1. Вставка элемента без превышения буфера:")
    da = DynArray()
    for i in range(15):
        da.insert(i, i * 10)
    print(f"После 15 вставок: count={len(da)}, capacity={da.capacity} (ожидается capacity=16)")
    for i in range(len(da)):
        assert da[i] == i * 10, f"Ошибка: da[{i}]={da[i]} (ожидается {i * 10})"
    print("Тест 1 пройден: буфер не превышен, элементы корректны")
    del da

    # Тест 2: Вставка с превышением буфера
    print("\n2. Вставка элемента с превышением буфера:")
    da = DynArray()
    for i in range(16):
        da.append(i)  # Заполняем полностью (16 элементов)
    print(f"До вставки: count={len(da)}, capacity={da.capacity}")

    da.insert(16, 160)  # Эта вставка должна вызвать resize
    print(f"После вставки: count={len(da)}, capacity={da.capacity} (ожидается capacity=32)")

    assert da.capacity == 32, "ОШИБКА: буфер не расширился до 32"
    assert len(da) == 17, "ОШИБКА: неверный count после вставки"
    assert da[16] == 160, "ОШИБКА: последний элемент не сохранён"
    print("Тест 2 пройден: буфер корректно расширен")
    del da

    # Тест 3: Попытка вставки в недопустимую позицию
    print("\n3. Попытка вставки в недопустимую позицию:")
    da = DynArray()
    try:
        da.insert(-1, 10)
        print("ОШИБКА: Не вызвано исключение для отрицательного индекса")
    except IndexError:
        print("Успех: Отрицательный индекс вызывает исключение")

    try:
        da.insert(1, 20)
        print("ОШИБКА: Не вызвано исключение для индекса > count")
    except IndexError:
        print("Успех: Индекс > count вызывает исключение")
    print("Тест 3 пройден: недопустимые позиции обрабатываются")
    del da

    # Тест 4: Удаление без изменения буфера
    print("\n4. Удаление элемента без изменения буфера:")
    da = DynArray()
    for i in range(16):
        da.append(i)
    old_capacity = da.capacity

    da.delete(0)
    print(f"После удаления: count={len(da)}, capacity={da.capacity} (должен остаться {old_capacity})")

    assert da.capacity == old_capacity, "ОШИБКА: буфер изменился без необходимости"
    assert len(da) == 15, "ОШИБКА: неверный count после удаления"
    print("Тест 4 пройден: буфер остался прежним")
    del da

    # Тест 5: Удаление с уменьшением буфера
    print("\n5. Удаление с уменьшением буфера (жесткая проверка):")
    da = DynArray()

    # Заполняем до capacity=32
    for i in range(32):
        da.append(i)
    print(f"До удаления: count={len(da)}, capacity={da.capacity}")

    # Удаляем элементы и проверяем каждое изменение
    for step in range(25):
        da.delete(0)
        if len(da) < da.capacity / 2:
            expected = max(16, (da.capacity * 2) // 3)
            assert da.capacity == expected, (
                f"Ошибка на шаге {step + 1}: "
                f"получили {da.capacity}, ожидалось {expected}"
            )
    print(f"После удаления: count={len(da)}, capacity={da.capacity} ")
    print("Тест 5 пройден: буфер сжат корректно")

    # Тест 6: Попытка удаления из недопустимой позиции
    print("\n6. Попытка удаления из недопустимой позиции:")
    da = DynArray()
    try:
        da.delete(-1)
        print("ОШИБКА: Не вызвано исключение для отрицательного индекса")
    except IndexError:
        print("Успех: Отрицательный индекс вызывает исключение")

    da.append(10)
    try:
        da.delete(1)
        print("ОШИБКА: Не вызвано исключение для индекса >= count")
    except IndexError:
        print("Успех: Индекс >= count вызывает исключение")

    try:
        da.delete(0)
        da.delete(0)
        print("ОШИБКА: Не вызвано исключение для пустого массива")
    except IndexError:
        print("Успех: Пустой массив вызывает исключение")
    print("Тест 6 пройден: обработка недопустимых позиций работает")
    del da

# как будто то бы массивы понял лучше списков, по крайней мере в плане логики. Но resize массива до конца не осознал, сделал более предсказуемым (тупым)
