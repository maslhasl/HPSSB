#Очередь.
from logging import exception


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
# 5.* Добавьте функцию, которая обращает все элементы в очереди в обратном порядке.

    def reverse(self):
        stack = Stack() # воспользуемся классом стек и используем архитектуру стека
        while self.size() > 0: # заполним стек элементами из очереди
            stack.push(self.dequeue())
        while stack.size() > 0: # вернем элементы в очередь из стека, но уже в обратном порядке
            self.enqueue(stack.pop())



#4.* Реализуйте очередь с помощью двух стеков.

#Введем класс стека и методы к нему
class Stack:
    def __init__(self):  # Оставляю метод без изменений, как указано в заготовке. Надеюсь это не ошибка.
        self.stack = []

    # 1. Подберите подходящую динамическую структуру данных для хранения стека. Реализуйте методы size(), pop(), push() и peek().
    # Добавьте тесты для каждого из этих четырёх методов.
    # Оцените меру сложности для операций pop и push.

    def size(self):  # Оставляю метод без изменений, как указано в заготовке. Надеюсь это не ошибка.
        return len(self.stack)

    def pop(self):
        if self.size() != 0:  # если стек не пустой
            result = self.stack[-1]  # используя возможности списка обращаемся сразу к последнему элементу стека
            self.stack = self.stack[:-1]  # пересохраняем стек без последнего элемента с помощью среза
            return result
        return None  # если стек пустой

    def push(self, value):
        self.stack.append(value)  # используем имеющийся метод добавления в конец списка, тк для стека использую тип данных python list

    def peek(self):
        if self.size() != 0:  # если стек не пустой
            result = self.stack[-1]
            return result
        return None  # если стек пустой
# Введем класс очереди на двух стеках и методы к нему с использованием методов класса стека
class _2stacks_queue:
    def __init__(self): #Создаем очередь на двух стеках
        self.stack_in = Stack()
        self.stack_out = Stack()

    def size_2s(self):
        return self.stack_in.size() + self.stack_out.size()

    def enqueue_2s(self, item): # Метод добавления элементов
        # Используем метод добавления из класса стека
        self.stack_in.push(item)

    def dequeue_2s(self):
        # Введем проверку на наличие элементов в стеках
        if self.stack_in.size() == 0 and self.stack_out.size() == 0:
            return None # случай когда возвращать нечего
        # Перенос элементов только в случае если стек out пуст
        if self.stack_out.size() == 0:
            while self.stack_in.size() > 0:
                self.stack_out.push(self.stack_in.pop())
        # отдаем верхний элемент out стека
        return self.stack_out.pop()

#6.* Реализуйте круговую (циклическую буферную) очередь статическим массивом фиксированного размера. Добавьте ей метод проверки, полна ли она (при этом добавление новых элементов невозможно).
#Обеспечьте эффективное управление указателями начала и конца очереди в рамках массива, чтобы избежать неоправданных сдвигов данных. 
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity # ёмкость очереди: задается внешне, фиксирована
        self.size = 0 # текущий размер очереди
        self.head = 0 # начало очереди
        self.tail = 0 # конец очереди
        self.queue = [None]*capacity # массив, определяемый ёмкостью

    def is_full(self): # проверка на заполненность очереди
        return self.size == self.capacity
    def is_empty(self): # проверка на пустую очередь
        return self.size == 0

    def enqueue_circle(self, item): # добавляем новый элемент в очередь
        if self.is_full():
            raise exception("Очередь заполнена, добавление элементов невозможно.")
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue_circle(self): # отдаем первый добавленный элемент и удаляем его
        if self.is_empty():
            raise exception("Очередь пуста, удаление элемента невозможно.")
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def peek_circle(self): # отдаем элемент без удаления
        if self.is_empty():
            return None
        result = self.queue[self.head]
        return result






