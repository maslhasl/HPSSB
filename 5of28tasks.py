# Очередь.
#1. В классе Queue нам понадобятся три метода: size() (количество элементов в очереди), enqueue(item) -- добавить элемент в хвост очереди, и dequeue(), 
#которая возвращает элемент из головы очереди, удаляя его. 

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


    def dequeue(self):
        # выдача из головы
        result = None
        if self._size != 0: #не пустой список
            result = self.head.value
            self.head = self.head.next

            if self.head is None: #очередь стала пустой
                self.tail = None
            else:
                self.head.prev = None
            self._size -= 1
            return result

        return result # если очередь пустая

    def size(self):
        return self._size # размер очереди

#2. Оцените меру сложности для операций enqueue() и dequeue().
# enqueue() - O(1)
#
#dequeue() - O(1)
#
# для обоих методов констатная сложность, тк при добавлении/удалении элемента не нужно пересохранять данные, как в случае с динамическим массивом

def tests_equeue():

    #Инициализация очереди
    Q = Queue()
    assert Q.size() == 0, "Размер пустой очереди должен быть = 0"
    assert Q.dequeue() is None, "Извлечение из пустой очереди должно быть равно 0"
    # Добавление элементов
    # Проверка для одного элемента
    Q.enqueue(10)
    assert Q.size() == 1, "Размер очереди с одним элементом должен быть равен 1"
    assert Q.head.value == 10, "Значение начала очереди должно быть равно 10"
    assert Q.tail.value == 10, "Значение конца очереди должно быть равно 10"
    Q.enqueue(20)
    Q.enqueue(30)
    assert Q.head.value == 10, "Неверное значение начала очереди"
    assert Q.head.next.value == 20, "Неверное значение элемента очереди"
    assert Q.tail.value == 30, "Неверное значение конца очереди"
    assert Q.size() == 3, "Размер очереди рассчитан неверно после добавления 3 элементов"

    # Удаление элементов
    assert Q.dequeue() == 10, "Первое извлечение должно соответствовать первому добавлению, т.е. 10"
    assert Q.head.value == 20, "Начало очереди рассчитано неверно после 1-го удаления"
    assert Q.tail.value == 30, "Конец очереди рассчитан неверно полсе 1-го удаления"
    assert Q.size() == 2, "Размер очереди рассчитан неверно после 1-го удаления"
    assert Q.dequeue() == 20, "Второе извлечение должно соответствовать второму добавлению, т.е. 20"
    assert Q.head.value == 30, "Начало очереди рассчитано неверно после 2-го удаления"
    assert Q.tail.value == 30, "Начало очереди рассчитано неверно после 2-го удаления"
    assert Q.size() == 1, "Размер очереди рассчитан неверно после 2-го удаления"
    assert Q.dequeue() == 30, "Третье извлечение должно соответствовать третьему добавлению, т.е. 30"
    assert Q.head is None and Q.tail is None, "После удаления всех элементов очереди, начало и конец очереди должны быть None"
    assert Q.size() == 0, "Размер очереди рассчитан неверно после 3-го удаления"

    # Чередование добавления и удаления
    Q.enqueue(10)
    Q.enqueue(20)
    assert Q.dequeue() == 10
    Q.enqueue(30)
    assert Q.dequeue() == 20
    assert Q.dequeue() == 30
    assert Q.size() == 0, "Очередь должна быть пустой"



