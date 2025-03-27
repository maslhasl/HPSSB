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
    def delete(self, val, all=False):
        node = self.head  # Начинаем с головы списка
    
        while node is not None:  # Пока не дошли до конца
            if node.value == val:  # Если нашли нужное значение
                # Случай 1: Удаляемый узел — это голова (нет предыдущего)
                if node.prev is None:  
                    self.head = node.next  # Головой становится следующий узел
                else:
                    node.prev.next = node.next  # Иначе "перепрыгиваем" удаляемый узел

                # Случай 2: Удаляемый узел — это хвост (нет следующего)
                if node.next is None:  
                    self.tail = node.prev  # Хвостом становится предыдущий узел
                else:
                    node.next.prev = node.prev  # Иначе "перепрыгиваем" удаляемый узел

                if not all:  # Если нужно удалить только первый найденный — выходим
                    return  
        
            node = node.next  # Переходим к следующему узлу
#2.5. Добавьте в класс LinkedList2 метод вставки узла после заданного узла - insert(afterNode, newNode)
#Если afterNode = None и список пустой, добавьте новый элемент первым в списке.
#Если afterNode = None и список непустой, добавьте новый элемент последним в списке.
    def insert(self, afterNode, newNode):
        # Случай 1: Список пустой и afterNode = None
        if self.head is None and afterNode is None:
            self.head = newNode
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
            return

        # Случай 2: Вставка в конец (afterNode = None, но список не пустой)
        if afterNode is None:
            newNode.prev = self.tail  # Новый узел ссылается на старый хвост
            newNode.next = None       # Следующего узла нет (он последний)
            self.tail.next = newNode  # Старый хвост ссылается на новый узел
            self.tail = newNode       # Новый узел теперь хвост
            return

        # Случай 3: Вставка после заданного узла (afterNode не None)
        newNode.prev = afterNode      # Новый узел ссылается на afterNode
        newNode.next = afterNode.next # Новый узел ссылается на следующий после afterNode

        if afterNode.next is not None: # Если afterNode не был хвостом
            afterNode.next.prev = newNode  # Узел после afterNode теперь ссылается на newNode
        else:
            self.tail = newNode       # Если afterNode был хвостом, newNode теперь хвост

        afterNode.next = newNode      # afterNode теперь ссылается на newNode

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
    # Тест 1: Инициализация и add_in_tail
    lst = LinkedList2()
    lst.add_in_tail(Node(10))
    lst.add_in_tail(Node(20))
    lst.add_in_tail(Node(30))
    assert lst.head.value == 10
    assert lst.tail.value == 30
    assert lst.head.next.value == 20
    assert lst.tail.prev.value == 20

    # Тест 2: find (2.1)
    found = lst.find(20)
    assert found.value == 20
    assert found.prev.value == 10
    assert found.next.value == 30
    assert lst.find(99) is None  # Несуществующее значение

    # Тест 3: find_all (2.2)
    lst.add_in_tail(Node(20))  # Добавляем еще один 20
    found_nodes = lst.find_all(20)
    assert len(found_nodes) == 2
    assert all(node.value == 20 for node in found_nodes)
    assert lst.find_all(99) == []  # Несуществующее значение

    # Тест 4: delete (2.3-2.4)
    lst.delete(20)  # Удаляем первый 20
    assert lst.head.next.value == 30  # Теперь 10 -> 30 -> 20
    assert lst.tail.prev.value == 30

    lst.delete(20, all=True)  # Удаляем все 20
    assert lst.tail.value == 30  # Теперь только 10 -> 30

    # Тест 5: insert (2.5)
    lst.insert(None, Node(40))  # Вставка в конец
    assert lst.tail.value == 40
    assert lst.tail.prev.value == 30

    lst.insert(lst.head, Node(15))  # Вставка после головы
    assert lst.head.next.value == 15
    assert lst.head.next.next.value == 30

    # Тест 6: add_in_head (2.6)
    lst.add_in_head(Node(5))
    assert lst.head.value == 5
    assert lst.head.next.value == 10

    # Тест 7: clean (2.7)
    lst.clean()
    assert lst.head is None
    assert lst.tail is None

    # Тест 8: len (2.8)
    lst.add_in_tail(Node(100))
    lst.add_in_tail(Node(200))
    assert lst.len() == 2

    # Тест 9: Особые случаи
    empty_lst = LinkedList2()
    empty_lst.insert(None, Node(1))  # Вставка в пустой список
    assert empty_lst.head.value == 1
    assert empty_lst.tail.value == 1

    empty_lst.delete(1)
    assert empty_lst.head is None







    


  




    
