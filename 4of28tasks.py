#4. Стек

class Stack:
    def __init__(self):
        self.stack = []

#1. Подберите подходящую динамическую структуру данных для хранения стека. Реализуйте методы size(), pop(), push() и peek().
#Добавьте тесты для каждого из этих четырёх методов.
#Оцените меру сложности для операций pop и push. 
    def size(self):
        return len(self.stack)

    def pop(self):
        # ваш код
        return None # если стек пустой

    def push(self, value):
        # ваш код

    def peek(self):
        # ваш код
        return None # если стек пустой

#2. Переделайте реализацию стека так, чтобы она работала не с хвостом списка как с верхушкой стека, а с его головой. 


#3. Не запуская программу, скажите, как отработает такой цикл? 
while stack.size() > 0:
    print(stack.pop())
    print(stack.pop())

#4. Оцените меру сложности для операций pop и push. 


######################
stack = Stack()
stack.push(1)
stack.push("2")
stack.push(3.14)
while stack.size() > 0:
    stack.pop()
