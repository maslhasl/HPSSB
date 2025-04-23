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

    def compare(self, v1, v2):
        # переопределённая версия для строк
        return 0

#7. Добавьте тесты для добавления, удаления и поиска элемента по его значению
# -- каждый случай с учётом признака упорядоченности.