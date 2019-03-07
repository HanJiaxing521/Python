class Node():
    def __init__(self, data=0):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head = self.tail

    def create_head(self, l):
        for i in range(len(l)):
            self.add_head(l[i])

    def add_head(self, data):
        tmp = Node(data)
        tmp.setNext(self.head.getNext())
        self.head.setNext(tmp)

    def create_tail(self, l):
        for i in range(len(l)):
            self.add_tail(l[i])

    def add_tail(self, data):
        tmp = Node()
        self.tail.setNext(tmp)
        self.tail = tmp

    def search(self, data):
        current = self.head
        Found = False
        while current != None and not Found:
            if current.getData() == data:
                Found = True
            else:
                current = current.getNext()
        print("Found:" + str(Found))

    def insert(self, n, data):
        tmp = Node(data)
        current = self.head
        for i in range(1, n):
            current = current.getNext()
        tmp.setNext(current.getNext())
        current.setNext(tmp)

    def remove(self, data):
        current = self.head
        previous = None
        Found = False
        while current != None and not Found:
            if current.getData() == data:
                Found = True
            else:
                previous = current
                current = current.getNext()
        if Found:
            previous.setNext(current.getNext())
            del current
        else:
            print("Remove: Not found!")

    def reverse(self):
        pre = None
        self.head = self.head.getNext()
        while self.head:
            nex = self.head.getNext()
            self.head.setNext(pre)
            pre = self.head
            self.head = nex
        self.head = Node(0)
        self.head.setNext(pre)

    def display(self):
        p = self.head.getNext()
        while p:
            print(p.getData())
            p = p.getNext()


if __name__ == '__main__':
    list = UnorderedList()
    list.create_head(['你', '是', '心', '中', '的', '爱', '恋'])
    print("正向创建链表并输出：")
    list.display()
    print("\n")
    print("将链表反向并输出：")
    list.reverse()
    list.display()
