#4. Стек

class Stack:
    def __init__(self):  #Оставляю метод без изменений, как указано в заготовке. Надеюсь это не ошибка.
        self.stack = []

#1. Подберите подходящую динамическую структуру данных для хранения стека. Реализуйте методы size(), pop(), push() и peek().
#Добавьте тесты для каждого из этих четырёх методов.
#Оцените меру сложности для операций pop и push.
    
    def size(self):  #Оставляю метод без изменений, как указано в заготовке. Надеюсь это не ошибка.
        return len(self.stack)

    def pop(self):
        if self.size() != 0: # если стек не пустой
            result = self.stack[-1] #используя возможности списка обращаемся сразу к последнему элементу стека
            self.stack = self.stack[:-1] # пересохраняем стек без последнего элемента с помощью среза
            return result
        return None # если стек пустой

    def push(self, value):
        self.stack.append(value) # используем имеющийся метод добавления в конец списка, тк для стека использую тип данных python list

    def peek(self):
        if self.size() != 0: # если стек не пустой
            result = self.stack[-1]
            return result
        return None # если стек пустой

#2. Переделайте реализацию стека так, чтобы она работала не с хвостом списка как с верхушкой стека, а с его головой.

# В данном задании если использование возможностей python list не будет ошибкой, то изменение методов pop и peek просто: меняем индексы
# а для метода push воспользуемся также особенностью срезов
    def re_pop(self):
        if self.size() != 0: # если стек не пустой
            result = self.stack[0] # используя возможности списка обращаемся сразу к последнему элементу стека
            self.stack = self.stack[1:] # пересохраняем стек без последнего элемента с помощью среза
            return result
        return None # если стек пустой

    def re_push(self, value):
        self.stack[:0] = [value] # используем возможности срезов для python list

    def re_peek(self):
        if self.size() != 0: # если стек не пустой
            result = self.stack[0]
            return result
        return None # если стек пустой

def test_stack():

    # Тест 1: Проверка пустого стека
    s = Stack()
    assert s.size() == 0, "Тест 1: размер пустого стека должен быть 0"
    assert s.pop() is None, "Тест 1: pop из пустого стека должен возвращать None"
    assert s.peek() is None, "Тест 1: peek пустого стека должен возвращать None"
    print("Тест 1 пройден - поведение пустого стека корректно")

    # Тест 2: Проверка push и size
    s = Stack()
    s.push(10)
    assert s.size() == 1, "Тест 2: размер стека после push должен увеличиться"
    assert s.peek() == 10, "Тест 2: peek должен вернуть последний добавленный элемент"
    print("Тест 2 пройден - push и size работают корректно")

    # Тест 3: Проверка pop
    s = Stack()
    s.push(10)
    popped_value = s.pop()
    assert popped_value == 10, "Тест 3: pop должен вернуть последний добавленный элемент"
    assert s.size() == 0, "Тест 3: размер стека после pop должен уменьшиться"
    print("Тест 3 пройден - pop работает корректно")

    # Тест 4: Проверка нескольких операций
    s = Stack()
    s.push(20)
    s.push(30)
    s.push(40)
    assert s.size() == 3, "Тест 4: размер стека должен быть 3"
    assert s.peek() == 40, "Тест 4: peek должен вернуть 40"

    popped_value = s.pop()
    assert popped_value == 40, "Тест 4: первый pop должен вернуть 40"
    assert s.size() == 2, "Тест 4: размер стека должен быть 2 после pop"

    popped_value = s.pop()
    assert popped_value == 30, "Тест 4: второй pop должен вернуть 30"
    assert s.peek() == 20, "Тест 4: peek должен вернуть 20 после двух pop"
    print("Тест 4 пройден - последовательность операций работает корректно")

    # Тест 5: Проверка последовательности pop
    s = Stack()
    s.push(20)
    popped_value = s.pop()
    assert popped_value == 20, "Тест 5: pop должен вернуть 20"
    assert s.size() == 0, "Тест 5: стек должен быть пустым после pop"
    assert s.pop() is None, "Тест 5: pop из пустого стека должен возвращать None"
    print("Тест 5 пройден - поведение после полной очистки корректно")

    # Тест 6: Проверка повторного заполнения
    s = Stack()
    s.push(100)
    s.push(200)
    assert s.size() == 2, "Тест 6: размер стека должен быть 2"
    assert s.peek() == 200, "Тест 6: peek должен вернуть 200"
    print("Тест 6 пройден - повторное использование стека работает корректно")

    print("Тесты успешно пройдены!")

#3. Не запуская программу, скажите, как отработает такой цикл?
#Цикл:
# stack = Stack()
# while stack.size() > 0:
#     print(stack.pop())
#     print(stack.pop())
#Ответ:
# В консоль будут выводиться значения "вытолкнутых" из стека элементов начиная с последнего.
# Если элементы закончатся до окончания цикла (например при нечетном количестве элементов в стеке)
# То в консоль будет выводится None, согласно логике прописанной в методе pop()
# Когда выполнение print-ов завершится, и при очередной проверке size станет == 0, цикл завершится.

#4. Оцените меру сложности для операций pop и push.
# pop - O(n) тк создаем новый список каждый раз
# push - O(1) в среднем, а при необходимости расширения массива O(n), поэтому правильнее будет сказать что O(n)





