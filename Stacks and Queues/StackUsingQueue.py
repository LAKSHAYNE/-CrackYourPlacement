class MyStack:

    def __init__(self):
        self.li=[]

    def push(self, x: int) -> None:
        self.li.append(x)

    def pop(self) -> int:
        return self.li.pop()

    def top(self) -> int:
        return self.li[-1]

    def empty(self) -> bool:
        return True if(len(self.li)==0) else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()