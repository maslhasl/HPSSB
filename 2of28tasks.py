#2. Двунаправленный связный (связанный) список

class Node:
    def __init_(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None: #То есть список пустой
            self.tail = item
            item.prev = None
            item.next = None
        else:                  #Список не пустой
            self.tail.next = item
            item.prev = self.tail
        self.tail = item       #После удаления связей, присваиваем хвосту новое значение

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
        node = node.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next

#2.3. и 2.4 Добавьте в класс LinkedList2 метод удаления одного узла по его значению - delete(val, all=False)
#где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент. 
    def delete(self, val, all=False):
        #Введем переменную текущего узла
        node = self.head
        #Для прохождения по всем узлам списка воспользуемся циклом while
        while node is not None:
            #Условие выполнения удаления
            if node.value == val:
                node_next = node.next #Введем переменную для сохранения следующего узла
                #Связи с предыдущим узлом
                if node.prev is not None: #Случай не начала списка
                    node.prev.next = node.next
                else:                     #Случай начала списка
                    self.head = node.next
                #Связи со следующим узлом
                if node.next is not None: #Случай не конца списка
                    node.next.prev = node.prev
                else: #Случай конца списка
                    self.tail = node.prev
                if not all: #Проверка: удалять первый найденный по значению узел или все 
                    return
                node = node_next #Присвоение переменной следующего по списку значения 

            else: #Случай когда условие удаления не выполнено
                node = node.next
#2.5. Добавьте в класс LinkedList2 метод вставки узла после заданного узла - insert(afterNode, newNode)
#Если afterNode = None и список пустой, добавьте новый элемент первым в списке.
#Если afterNode = None и список непустой, добавьте новый элемент последним в списке.
    def insert(self, afterNode, newNode):
        #Используя метод add_in_tail упростим случай когда: (afterNode = None и список пустой) и (afterNode = None и список не пустой)
        if afterNode is None:
            self.add_in_tail(newNode)
            return
        #Случай когда список не пустой и добавляем узел между элементами
        newNode.next = afterNode.next # связываем новый со следующим за afterNode
        newNode.prev = afterNode # связываем новый с afterNode
        afterNode.next = newNode # обрубаем связь между afterNode и прежним следующим
        if newNode.next is not None: # newNode не хвост
            newNode.next.prev = newNode #связываем ранее следующий за afterNode c newNode
        else: # newNode хвост
            self.tail = newNode # устанавливаем соответствие хвоста newNode-е

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
        self.head = NewNode

#2.7. Добавьте в класс LinkedList2 метод очистки всего содержимого (создание пустого списка) -- clean()
    def clean(self):
        self.head = None
        self.tail = None
        
#2.8. Добавьте в класс LinkedList2 метод вычисления текущей длины списка -- len()
    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count+=1
            node = node.next
        return count


  




    
