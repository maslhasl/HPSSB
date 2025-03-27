#2. Двунаправленный связный (связанный) список

class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

#2.1. Добавьте в класс LinkedList2 метод поиска первого узла по его значению.
    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

# 2.2. Добавьте в класс LinkedList2 метод поиска всех узлов по конкретному значению (возвращается список найденных узлов).
    def find_all(self, val):
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

#2.3. и 2.4 Добавьте в класс LinkedList2 метод удаления одного узла по его значению - delete(val, all=False)
#где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент. 

#2.5. Добавьте в класс LinkedList2 метод вставки узла после заданного узла - insert(afterNode, newNode)
#Если afterNode = None и список пустой, добавьте новый элемент первым в списке.
#Если afterNode = None и список непустой, добавьте новый элемент последним в списке.
    def insert(self, afterNode, newNode):
    #Вставляет узел после указанного (безопасная версия)
        if newNode is None:
            return  # Игнорируем None
    
    # Вставка в конец списка
        if afterNode is None:
            if self.head is None:  # Список пуст
                self.head = newNode
                self.tail = newNode
                newNode.prev = None
                newNode.next = None
            else:  # Вставка в конец непустого списка
                newNode.prev = self.tail
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            return
    
    # Вставка в середину списка
        newNode.prev = afterNode
        newNode.next = afterNode.next
        afterNode.next = newNode
    
    # Обновляем tail если вставили после последнего элемента
        if newNode.next is None:
            self.tail = newNode
        else:
            newNode.next.prev = newNode

#2.6. Добавьте в класс LinkedList2 метод вставки узла самым первым элементом.
#add_in_head(newNode)
    def add_in_head(self, newNode):
        #установим связь с головой
        newNode.next = self.head
        #укажем для newNode prev как для головы
        newNode.prev = None
        #Случай непустого списка
        if self.head is not None:
            self.head.prev = newNode
        #Случай пустого списка
        else:
            self.tail = newNode
        self.head = newNode

#2.7. Добавьте в класс LinkedList2 метод очистки всего содержимого (создание пустого списка) -- clean()
    def clean(self):
        self.head = None
        self.tail = None
        
#2.8. Добавьте в класс LinkedList2 метод вычисления текущей длины списка -- len()
    def len(self):
        node = self.head
        count=0
        while node is not None:
            count+=1
            node = node.next
        return count


#2.9. Напишите проверочные тесты для каждого из предыдущих заданий. 
def test_linked_list2():
    
    # Тест 1: Создание и добавление элементов
    lst = LinkedList2()
    n1, n2, n3 = Node(1), Node(2), Node(3)
    lst.add_in_tail(n1)
    lst.add_in_tail(n2)
    lst.add_in_tail(n3)
    assert lst.head == n1
    assert lst.tail == n3
    assert lst.len() == 3
    print("Тест 1 пройден: добавление в хвост")

    # Тест 2: Поиск элементов
    assert lst.find(2) == n2
    assert lst.find(99) is None
    assert lst.find_all(2) == [n2]
    print("Тест 2 пройден: поиск элементов")

    # Тест 3: Удаление одного элемента
    lst.delete(2)
    assert lst.head == n1
    assert lst.tail == n3
    assert n1.next == n3
    assert n3.prev == n1
    assert lst.len() == 2
    print("Тест 3 пройден: удаление одного элемента")

    # Тест 4: Удаление всех элементов
    lst.add_in_tail(Node(2))
    lst.add_in_tail(Node(2))
    lst.delete(2, all=True)
    assert lst.head == n1
    assert lst.tail == n3
    assert lst.len() == 2
    print("Тест 4 пройден: удаление всех вхождений")

    # Тест 5: Удаление единственного элемента
    lst2 = LinkedList2()
    n = Node(1)
    lst2.add_in_tail(n)
    lst2.delete(1)
    assert lst2.head is None
    assert lst2.tail is None
    print("Тест 5 пройден: удаление единственного элемента")

    # Тест 6: Вставка элементов
    lst.insert(n1, Node(1.5))
    assert lst.head.next.value == 1.5
    lst.insert(None, Node(4))  # Вставка в конец
    assert lst.tail.value == 4
    print("Тест 6 пройден: вставка элементов")

    # Тест 7: Вставка в голову
    lst.add_in_head(Node(0))
    assert lst.head.value == 0
    assert lst.head.next == n1
    print("Тест 7 пройден: вставка в голову")

    # Тест 8: Очистка списка
    lst.clean()
    assert lst.head is None
    assert lst.tail is None
    assert lst.len() == 0
    print("Тест 8 пройден: очистка списка")

    # Тест 9: Вставка в пустой список
    lst.insert(None, Node(10))
    assert lst.head.value == 10
    assert lst.tail.value == 10
    print("Тест 9 пройден: вставка в пустой список")

    # Тест 10: Комплексная проверка связей
    lst.clean()
    nodes = [Node(i) for i in range(5)]
    for node in nodes:
        lst.add_in_tail(node)
    
    # Проверка связей
    assert lst.head == nodes[0]
    assert lst.tail == nodes[-1]
    for i in range(1, len(nodes)-1):
        assert nodes[i].prev == nodes[i-1]
        assert nodes[i].next == nodes[i+1]
    print("Тест 10 пройден: комплексная проверка связей")

    # Тест 11: Крайние случаи insert
    lst.clean()
    special_node = Node(999)
    lst.insert(None, special_node)  # Вставка в пустой
    assert lst.head == special_node
    assert lst.tail == special_node
    
    new_head = Node(-1)
    lst.insert(None, new_head)  # Вставка в конец непустого
    assert lst.tail == new_head
    print("Тест 11 пройден: крайние случаи insert")







    


  




    
