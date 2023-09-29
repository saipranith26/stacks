class node :
    def __init__(self,value):
        self.data=value
        self.next=None

class stack:
    def __init__(self) :
        self.top=None

    def is_empty(self):
        return (self.top==None)
    def push(self,value):
        new_node=node(value)
        new_node.next =self.top
        self.top=new_node
    def traverse(self):
        current=self.top
        while current!= None:
            print(current.data)
            current=current.next
    def pop(self):
        if self.is_empty():
            return 'stack is empty'
        current=self.top
        self.top=current.next
        return current.data
    def peek(self):
        if self.is_empty():
            return 'stack is empty'
        else :
            return self.top.data
    


s=stack()
# # print(s.is_empty())
s.push(10)
s.push(20)
s.push(30)
# s.traverse()
# print('  ')
print(s.pop())
# print(s.peek())
# print(s.pop())
# print(s.peek())
# # print(s.pop())
# # print(s.pop())
# # print(s.is_empty())



