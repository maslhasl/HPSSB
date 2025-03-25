сlass Node:
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
            self.tail = item
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
                result.append(node.value)
            node = node.next
        return result

## 2.3. и 2.4 Добавьте в класс LinkedList2 метод удаления одного узла по его значению - delete(val, all=False)
#где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент. 

#Текстовое описание метода
    def delete_all(self, val, all=False):
      #Введем переменную текущего значения узла, назовем node и присвоим значение головы списка.
      node = self.head
      #С помощью цикла while зациклим прохождение по узлам списка
      while node is not None:
        #Введем условие по которому будет производится удаление элемента,в обратном случае переход к следующему узлу
        if node.value == val: #условие выполения удаления
          #введем переменную которая будет ссылаться на следующий узел относительно текущего в цикле, чтобы в дальнейшем использовать ее
          node_next = node.next 
          #Связи с предыдущим узлом
          if node.prev is not None: #Случай не начала списка (есть предыдущий узел)
            node.prev.next = node.next
          else:                     #(предыдущего узла нет, это голова списка)
            self.head = node.next
          #Связи со следующим узлом
          if node.next is not None: #Случай не конца списка (есть следующий узел)
            node.next.prev = node.prev
          else:                     #(следующего узла нет, это хвост списка)             
            self.tail = node.prev   
          if not all: #Если true то завершаем цикл, то есть удалили один элемент. Если наоборот то продолжаем нещадно удалять элементы
            return
          # Переходим к следующему узлу в случае когда all=True
          node = node_next 
        else: #случай когда удаления не произойдет, а произойдет переход к следующему элементу
          node = node.next  
    def clean(self):
        self.head = None
        self.tail = None
        

    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count+=1
            node = node.next
        return count

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




    
