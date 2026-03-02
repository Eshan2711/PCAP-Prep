class Stack():
    def __init__(self):
        self.__stack_list = []
    def push(self,num):
        self.__stack_list.append(num)
    def pop(self):
        a=self.__stack_list[-1]
        del self.__stack_list[-1]
        return a
    def top(self):
        return self.__stack_list[-1]
    def is_empty(self):
        return len(self.__stack_list) == 0
class Adding_stack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
    def push(self, num):
        self.__sum += num
        Stack.push(self,num)
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
    def get_sum(self):
        return self.__sum
s=Adding_stack()
for x in range(5):
    if s.is_empty():
        print("Nothing")
    else:
        s.pop()
for x in range (5):
    s.push(x)
print(s.get_sum())


