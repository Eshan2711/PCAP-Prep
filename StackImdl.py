stack=[]
def push(num):
    stack.append(num)
def pop():
    del stack[-1]
def top():
    return stack[-1]
push(1)
pop()
push(10)
top()
print(stack)
class Stack():
    def __init__(self):
        self.__stack_list = []
    def stack_len(self):
        return (len(self.__stack_list))

stack_object=Stack()
print(stack_object.stack_len())
