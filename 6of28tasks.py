# 6. Двусторонняя очередь (deque)


# 7.1. Почему и как будет различаться мера сложности для addHead/removeHead и addTail/removeTail?
# Через двусвязный список:
# В случае реализации через двусвязный список все методы O(1) тк мы не пересоздаем массив, а просто перенаправляем связи крайних элементов
# Через массив:
# В случае реализации на массиве (питоновский list под капотом тоже массив, если я верно понял Вашу теорию в заданиях)
#при addFront надо двигать все элементы вправо, то есть сложность O(n)
#при removeFront тоже O(n) тк сдвиг оставшихся элементов уже влево
#addTail будет O(1) пока есть запас capacity, иначе мы увеличиваем capacity и пересоздаем массив и будет уже O(n)
#removeTail аналогично O(1), пока не надо менять capacity уже в меньшую сторону, тогда тоже O(n)

# Реализуем deque с помощью двусвязного списка
# Для этого введем класс Узел (Node)

class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self._size = 0
        self.head = None
        self.tail = None

    def addFront(self, item):
        # добавление в голову
        new_node = Node(item)
        if self.head is None: # пустая очередь
            self.head = new_node
            self.tail = new_node
        else: # не пустая очередь
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def addTail(self, item):
        # добавление в хвост
        new_node = Node(item)
        if self.tail is None: # пустая очередь
            self.tail = new_node
            self.head = new_node
        else: # не пустая очередь
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def removeFront(self):
        # удаление из головы
        if self.head is None: # пустая очередь
            return None
        value = self.head.value
        if self.head == self.tail: # один элемент в очереди
            self.head = None
            self.tail = None
            self._size -= 1
            return value
         # общий случай
        self.head = self.head.next
        self.head.prev = None
        self._size -= 1
        return value

    def removeTail(self):
        # удаление из хвоста
        if self.tail is None:
            return None # если очередь пуста
        value = self.tail.value
        if self.head == self.tail: # один элемент в очереди
            self.tail = None
            self.head = None
            self._size -= 1
            return value
         # общий случай
        self.tail = self.tail.prev
        self.tail.next = None
        self._size -= 1
        return value

    def size(self):
        return self._size # размер очереди

# 7.2. Добавьте для каждого из четырёх вышеупомянутых методов тесты: проверяйте изменившуюся длину очереди и наличие или отстутствие в ней добавляемого/удаляемого элемента. 

def deque_tests():
    deque = Deque()

    # Тест 1: Добавление в начало (addFront)
    deque.addFront(10)
    assert deque.size() == 1, f"Ожидался размер 1, получено {deque.size()}"
    assert deque.head.value == 10, "Ожидалось значение 10 в head"
    assert deque.tail.value == 10, "Ожидалось значение 10 в tail"

    # Тест 2: Добавление в конец (addTail)
    deque.addTail(20)
    assert deque.size() == 2, f"Ожидался размер 2, получено {deque.size()}"
    assert deque.head.value == 10, "Ожидалось значение 10 в head"
    assert deque.tail.value == 20, "Ожидалось значение 20 в tail"

    # Тест 3: Удаление из начала (removeFront)
    val = deque.removeFront()
    assert val == 10, f"Ожидалось 10, получено {val}"
    assert deque.size() == 1, f"Ожидался размер 1, получено {deque.size()}"
    assert deque.head.value == 20, "Ожидалось значение 20 в head"
    assert deque.tail.value == 20, "Ожидалось значение 20 в tail"

    # Тест 4: Удаление из конца (removeTail)
    val = deque.removeTail()
    assert val == 20, f"Ожидалось 20, получено {val}"
    assert deque.size() == 0, f"Ожидался размер 0, получено {deque.size()}"
    assert deque.head is None, "Ожидалось None в head"
    assert deque.tail is None, "Ожидалось None в tail"

    # Тест 5: Удаление из пустой очереди
    assert deque.removeFront() is None, "Ожидалось None"
    assert deque.removeTail() is None, "Ожидалось None"
    assert deque.size() == 0, f"Ожидался размер 0, получено {deque.size()}"

    # Тест 6: Множественные операции
    deque.addFront(100)
    deque.addTail(200)
    deque.addFront(300)
    assert deque.size() == 3, f"Ожидался размер 3, получено {deque.size()}"
    assert deque.removeTail() == 200, "Ожидалось 200"
    assert deque.removeFront() == 300, "Ожидалось 300"
    assert deque.removeFront() == 100, "Ожидалось 100"
    assert deque.size() == 0, f"Ожидался размер 0, получено {deque.size()}"




# Вы писали про рефлексию.
# Концепции я понимаю, но когда дело доходит до реализации...
# Почему-то конструкции не складываются, или складываются очень сложно и долго.
# Но так приятно когда в итоге решаешь задачу.
# И если быть честным бывает прибегаю к помощи ИИ, тк времени не хватает (это моя проблема конечно же).
# Плюс Ваши посты с резкой сменой риторики насчет ИИ, с одной стороны неудивительно.
# С другой мысль, а не сарказм ли это над публикой, которая лайкает все. Хотя в Вашем сообществе мне кажется своя публика.
# И вектор который я избрал изначально: разбираться в базе и фундаменте, а там будь что будет, уже не кажется таким стройным и прочным.
# Тк пока я со своей скоростью понимания разберусь в базовых концептах, тот самый школьник вооружившись десятком промтов решит задачу к которой я все еще планирую приступить.
# Пока писал, пришел к мысли: Делать! С ИИ, без ИИ, без разницы, лишь бы делать и забить на желание догрызться до понимания математики и навыка написания кода, как пишу сейчас - сходу.
# А может это все от лукавого:)
# Спасибо за Ваши занятия и посты, выбивают почву из-под ног!
# Была еще мысль, что может проще сделать себе сеппуку, дабы не дожидаться момента, когда будешь унижен кремниевым разумом
# Но вспоминаешь, что ты христианин и надо идти несмотря ни на что
# Извиняюсь за словоблудие, накипело:)