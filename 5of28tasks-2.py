#Очередь.

#Реализуем очередь с помощью связного списка
class Queue_Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0 # счетчик размера
        # инициализация хранилища данных


    def enqueue(self, item):
        # вставка в хвост
        new_node_queue = Queue_Node(item)

        if self.tail is None:  #пустой список
            self.head = new_node_queue
            self.tail = new_node_queue
        else:  #не пустой список
            new_node_queue.prev = self.tail
            self.tail.next = new_node_queue
            self.tail = new_node_queue
        self._size += 1


    def dequeue(self): # Поправил метод чтобы не было вложенных if-ов, как реализовать вообще без условий, пока для меня загадка
        #выдача элемента из головы очереди
        result = None
        # пустой список
        if self._size == 0:
            return result
         #не пустой список
        result = self.head.value # Присваиваем значение результирующей переменной
        self.head = self.head.next # Головой очереди делаем следующий за ней узел
        if self.head is None: # Очередь стала пустой
            self.tail = None
        else:
            self.head.prev = None
        self._size -= 1
        return result # если очередь пустая

    def size(self):
        return self._size # размер очереди


#3.* Напишите функцию, которая "вращает" очередь по кругу на N элементов.

    def enqueue_rotate(self, n):
        #вычисляем на сколько надо подвинуть элементы в зависимости от размера очереди
        length = self.size()
        #Случай когда очередь пустая
        if length == 0:
            return

        n = n % length # шаг вращения без кратной составляющей
        #Случай когда очередь кратна шагу вращения
        if n == 0:
            return
        #
        for i in range(n):
            element = self.dequeue()
            self.enqueue(element)

        #Случай когда очередь равна шагу вращения
        #с помощью цикла осуществляем перемещение элементов очереди.
# q = Queue()
# q.enqueue('first')
# q.enqueue('second')
# q.enqueue('third')
# print('до смещения:')
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print('после смещения:')
# q.enqueue('first')
# q.enqueue('second')
# q.enqueue('third')
# q.enqueue_rotate(-1)
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())

#4.* Реализуйте очередь с помощью двух стеков.

#5.* Добавьте функцию, которая обращает все элементы в очереди в обратном порядке.

#6.* Реализуйте круговую (циклическую буферную) очередь статическим массивом фиксированного размера. Добавьте ей метод проверки, полна ли она (при этом добавление новых элементов невозможно).
#Обеспечьте эффективное управление указателями начала и конца очереди в рамках массива, чтобы избежать неоправданных сдвигов данных. 
