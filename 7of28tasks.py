# 7. Упорядоченный список


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

# Реализуйте:

#1. Дополнительную опцию asc в конструкторе OrderedList, которая указывает,
# по возрастанию (True) или по убыванию (False)
# должны храниться элементы в массиве.
#Эту опцию сделайте приватной -- изменять её можно только в конструкторе и методе очистки clean().

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc #  приватное поле с порядком сортировки в зависимости от значения asc

# 2. Метод сравнения двух значений compare().
# В общем случае, мы можем хранить в нашем списке произвольные объекты (например, экземпляры класса Cat),
# и способ, которым мы желаем их сравнивать, потенциально может быть самым произвольным.
# Пока сделайте базовый вариант этого метода, который сравнивает числовые значения.

    def compare(self, v1, v2):
        # если элементы идентичны
        if v1 == v2:
            return 0
        # если порядок и элементы соответствуют условиям сортировки
        if (v1 < v2 and self.__ascending) or (v1 > v2 and not self.__ascending):
            return -1
        # в случае когда порядок и элементы не соответствуют условиям сортировки
        else:
            return 1

# 3. Добавление нового элемента по значению add() с единственным параметром -- новым добавляемым значением
# (новый узел для него создавайте внутри метода add).
# Элемент должен вставиться автоматически между элементами с двумя подходящими значениями
# (либо в начало или конец списка) с учётом его значения и признака упорядоченности.
# Используйте для этого метод сравнения значений из предыдущего пункта.

    def add(self, value):
        # Создаем новый узел
        new_node = Node(value)
        # Случай когда список пустой
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        # Случай когда список не пустой
        current = self.head # текущий элемент списка, с ним будем сравнивать
        while current: # Пока current не None цикл будет выполняться
            cmp_result = self.compare(value, current.value)
            if cmp_result <= 0:
                # Добавление элемента перед current в asc/desc случаях
                # Связываем новый элемент с текущими
                new_node.prev = current.prev
                new_node.next = current
                # Если не голова списка
                if current.prev:
                    current.prev.next = new_node
                else: # Если голова списка
                    self.head = new_node
                # новая связь текущего с новым предыдущим
                current.prev = new_node
                return # выход, если выполнилось условие -1/0
            # Переход к новому элементу при невыполнении условия
            current = current.next
        # Если цикл завершился, то есть дошли до конца
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

# 6. Переделайте функцию поиска элемента по значению с учётом признака упорядоченности и возможности раннего прерывания поиска,
# если найден заведомо больший или меньший элемент, нежели искомый. Оцените сложность операции поиска, изменилась ли она?

    def find(self, val):
        current = self.head
        while current:
            cmp_result = self.compare(val, current.value)
            if cmp_result == 0:
                return current
            if cmp_result < 0:
                return None
            current = current.next
        return  None

# 4. Удаление самого первого (одного) элемента по значению: delete(),
# независимо от того, сколько одинаковых элементов по значению.

    def delete(self, val):
        # Если список пустой выходим из метода
        if self.head is None:
            return
        current = self.head
        while current:
            cmp_result = self.compare(val, current.value)
        # Условие в случае нахождения элемента для удаления
            if cmp_result == 0:
                if current.prev:
                    current.prev.next = current.next
                else: # если удаляем голову
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else: # если удаляем хвост
                    self.tail = current.prev
                return # выходим из метода после удаления первого подходящего элемента
            if cmp_result < 0:
                return
            current = current.next


    def clean(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc


    def len(self):
        count = 0
        current = self.head
        while current:
            count+=1
            current = current.next
        return count # здесь будет ваш код

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

#5. Создайте OrderedStringList -- наследник текущего класса, который будет упорядоченно хранить строки.
# Для этого переопределите в нём метод сравнения значений -- он должен сравнивать строки,
# очищенные от начальных и конечных пробелов.

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def custom_strip(self, v):
        whitespace_chars = {' ', '\t', '\n', '\r', '\v', '\f'}
        start = 0
        while start < len(v):
            if v[start] not in whitespace_chars:
                break
            start += 1
        end = len(v) - 1
        while end >= 0:
            if v[end] not in whitespace_chars:
                break
            end -= 1
        if start > end:
            return ""
        return v[start:end + 1]

    def compare(self, v1, v2):
        if type(v1) is str:
            str1 = v1
        else:
            str1 = str(v1)
        if type(v2) is str:
            str2 = v2
        else:
            str2 = str(v2)
        cleaned1 = self.custom_strip(str1)
        cleaned2 = self.custom_strip(str2)

        return super().compare(cleaned1, cleaned2)

#7. Добавьте тесты для добавления, удаления и поиска элемента по его значению
# -- каждый случай с учётом признака упорядоченности.

# Тесты для OrderedList (числа)
def test_ordered_list():

    # Тест 1: Добавление по возрастанию
    asc_list = OrderedList(True)
    asc_list.add(3)
    asc_list.add(1)
    asc_list.add(2)
    values = [node.value for node in asc_list.get_all()]
    assert values == [1, 2, 3], f"Ожидается [1, 2, 3], получено {values}"

    # Тест 2: Добавление по убыванию
    desc_list = OrderedList(False)
    desc_list.add(3)
    desc_list.add(1)
    desc_list.add(2)
    values = [node.value for node in desc_list.get_all()]
    assert values == [3, 2, 1], f"Ожидается [3, 2, 1], получено {values}"

    # Тест 3: Поиск элемента
    assert asc_list.find(2).value == 2, "Должен найти 2"
    assert asc_list.find(5) is None, "Не должен найти 5"

    # Тест 4: Удаление элемента
    asc_list.delete(2)
    values = [node.value for node in asc_list.get_all()]
    assert values == [1, 3], f"После удаления ожидается [1, 3], получено {values}"

    # Тест 5: Длина списка
    assert asc_list.len() == 2, f"Ожидается длина 2, получено {asc_list.len()}"


# Тесты для OrderedStringList (строки)
def test_ordered_string_list():

    # Тест 1: Добавление строк по возрастанию (без учета пробелов)
    asc_str = OrderedStringList(True)
    asc_str.add("  banana")
    asc_str.add("apple  ")
    asc_str.add("  orange ")
    values = [node.value for node in asc_str.get_all()]
    assert values == ["apple  ", "  banana", "  orange "], f"Ожидается ['apple', 'banana', 'orange'], получено {values}"

    # Тест 2: Добавление строк по убыванию
    desc_str = OrderedStringList(False)
    desc_str.add("  banana")
    desc_str.add("apple  ")
    desc_str.add("  orange ")
    values = [node.value for node in desc_str.get_all()]
    assert values == ["  orange ", "  banana", "apple  "], f"Ожидается ['orange', 'banana', 'apple'], получено {values}"

    # Тест 3: Поиск строк (без учета пробелов)
    assert desc_str.find("banana").value == "  banana", "Должен найти banana"
    assert desc_str.find("  banana").value == "  banana", "Должен найти banana с пробелами"
    assert desc_str.find("mango") is None, "Не должен найти mango"

    # Тест 4: Удаление строк
    desc_str.delete("banana")
    values = [node.value for node in desc_str.get_all()]
    assert values == ["  orange ", "apple  "], f"После удаления ожидается ['orange', 'apple'], получено {values}"

    # Тест 5: Очистка списка
    desc_str.clean(True)  # Меняем на сортировку по возрастанию
    assert desc_str.len() == 0, "После clean() список должен быть пустым"

