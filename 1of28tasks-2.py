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
# Тест 1: Списки равной длины
list1 = LinkedList()
list1.add_in_tail(Node(1))
list1.add_in_tail(Node(2))
list1.add_in_tail(Node(3))

list2 = LinkedList()
list2.add_in_tail(Node(4))
list2.add_in_tail(Node(5))
list2.add_in_tail(Node(6))

result = sum_linked_lists(list1, list2)
assert result is not None, "Ошибка: результат не должен быть None"
result_values = []
node = result.head
while node is not None:
    result_values.append(node.value)
    node = node.next
assert result_values == [5, 7, 9], "Ошибка: результат должен быть [5, 7, 9]"

# Тест 2: Списки разной длины
list1 = LinkedList()
list1.add_in_tail(Node(1))
list1.add_in_tail(Node(2))

list2 = LinkedList()
list2.add_in_tail(Node(4))
list2.add_in_tail(Node(5))
list2.add_in_tail(Node(6))

result = sum_linked_lists(list1, list2)
assert result is None, "Ошибка: результат должен быть None (длины не равны)"

# Тест 3: Пустые списки
list1 = LinkedList()
list2 = LinkedList()

result = sum_linked_lists(list1, list2)
assert result is not None, "Ошибка: результат не должен быть None"
assert result.len() == 0, "Ошибка: результат должен быть пустым списком"

print("Все тесты прошли успешно!")
