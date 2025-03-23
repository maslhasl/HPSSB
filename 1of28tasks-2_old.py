#*1.8. Напишите функцию, которая получает на вход два связанных списка, состоящие из целых значений, 
#и если их длины равны, возвращает список, каждый элемент которого равен сумме соответствующих элементов входных списков.
class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val, all=False):
        node = self.head
        prev = None

        while node is not None:
            if node.value == val:
                if prev is None:
                    self.head = node.next
                    if self.head is None:
                        self.tail = None
                else:
                    prev.next = node.next
                    if node.next is None:
                        self.tail = prev
                if not all:
                    return
            else:
                prev = node
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def find_all(self, val):
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            if self.tail is None:
                self.tail = newNode
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
            if afterNode == self.tail:
                self.tail = newNode

    
def sum_linked_lists(list1, list2):
    # Проверяем, равны ли длины списков
    if list1.len() != list2.len():
        return None

    # Создаем новый список для результата
    result_list = LinkedList()

    # Указатели на текущие узлы в списках
    node1 = list1.head
    node2 = list2.head

    # Проходим по спискам и складываем значения
    while node1 is not None and node2 is not None:
        # Сумма значений текущих узлов
        sum_value = node1.value + node2.value

        # Добавляем сумму в новый список
        result_list.add_in_tail(Node(sum_value))

        # Переходим к следующим узлам
        node1 = node1.next
        node2 = node2.next

    return result_list

# Тесты
def test_linked_list():
    # Создаем список
    lst = LinkedList()

    # Тест 1: Добавление элементов
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(2))
    lst.add_in_tail(Node(3))
    assert lst.head.value == 1, "Ошибка: head должен быть 1"
    assert lst.tail.value == 3, "Ошибка: tail должен быть 3"
    assert lst.len() == 3, "Ошибка: длина списка должна быть 3"

    # Тест 2: Удаление первого элемента
    lst.delete(1)
    assert lst.head.value == 2, "Ошибка: head должен быть 2"
    assert lst.len() == 2, "Ошибка: длина списка должна быть 2"

    # Тест 3: Удаление всех элементов с определенным значением
    lst.add_in_tail(Node(2))
    lst.delete(2, all=True)
    assert lst.head.value == 3, "Ошибка: head должен быть 3"
    assert lst.tail.value == 3, "Ошибка: tail должен быть 3"
    assert lst.len() == 1, "Ошибка: длина списка должна быть 1"

    # Тест 4: Очистка списка
    lst.clean()
    assert lst.head is None, "Ошибка: head должен быть None"
    assert lst.tail is None, "Ошибка: tail должен быть None"
    assert lst.len() == 0, "Ошибка: длина списка должна быть 0"

    # Тест 5: Поиск всех узлов с определенным значением
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(2))
    lst.add_in_tail(Node(2))
    found_nodes = lst.find_all(2)
    assert len(found_nodes) == 2, "Ошибка: должно быть найдено 2 узла"
    for node in found_nodes:
        assert node.value == 2, "Ошибка: найденный узел должен иметь значение 2"

    # Тест 6: Вставка узла
    lst.insert(lst.find(1), Node(0))
    assert lst.head.value == 1, "Ошибка: head должен быть 1"
    assert lst.head.next.value == 0, "Ошибка: следующий узел должен быть 0"
    assert lst.len() == 4, "Ошибка: длина списка должна быть 4"

    # Тест 7: Вставка в пустой список
    empty_lst = LinkedList()
    empty_lst.insert(None, Node(10))
    assert empty_lst.head.value == 10, "Ошибка: head должен быть 10"
    assert empty_lst.tail.value == 10, "Ошибка: tail должен быть 10"
    assert empty_lst.len() == 1, "Ошибка: длина списка должна быть 1"



