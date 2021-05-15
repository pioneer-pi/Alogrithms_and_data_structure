class QueueNode():
    def __init__(self):
        self.data = None
        self.next = None


class LinkQueue():
    def __init__(self):
        tQueueNode = QueueNode()
        self.front = tQueueNode
        self.rear = tQueueNode


class TestJP():
    def Josephus(self, n, k):
        first_node = QueueNode()
        first_node.data = 1
        current = first_node
        for i in range(2,n+1):
            node = QueueNode()
            node.data = i
            current.next = node
            current = current.next
        current.next = first_node
        Queue = LinkQueue()
        Queue.front = first_node
        Queue.rear = current

        killed_list = []
        while (Queue.front != Queue.rear):
            for i in range(k-1):
                Queue.front = Queue.front.next
                Queue.rear = Queue.rear.next
            killed_list.append(Queue.front.data)
            Queue.rear.next = Queue.front.next
            Queue.front = Queue.front.next
        killed_list.append(Queue.front.data)
        for i in killed_list:
            print(i,end = " ")

t = TestJP()
t.Josephus(7,3)


# standard answer
class QueueNode():
    def __init__(self):
        self.data = None
        self.next = None


class LinkQueue():
    def __init__(self):
        tQueueNode = QueueNode()
        self.front = tQueueNode
        self.rear = tQueueNode

    '''判断是否为空'''

    def IsEmptyQueue(self):
        if self.front == self.rear:
            iQueue = True
        else:
            iQueue = False
        return iQueue

    '''进队列'''

    def EnQueue(self, da):
        tQueueNode = QueueNode()
        tQueueNode.data = da
        self.rear.next = tQueueNode
        self.rear = tQueueNode

    '''出队列'''

    def DeQueue(self):
        if self.IsEmptyQueue():
            print("队列为空")
            return
        else:
            tQueueNode = self.front.next
            self.front.next = tQueueNode.next
            if self.rear == tQueueNode:
                self.rear = self.front
            return tQueueNode.data

    '''遍历顺序队列内的所有元素'''

    def QueueTraverse(self):
        if self.IsEmptyQueue():
            return
        else:
            tQueueNode = self.front.next
            while tQueueNode != self.rear:
                print(tQueueNode.data, end=" ")
                tQueueNode = tQueueNode.next
            print(tQueueNode.data, end=" ")

    '''链式队列长度'''

    def GetQueueLength(self):
        if self.IsEmptyQueue():
            return
        else:
            tQueueNode = self.front
            num = 0
            tQueueNode = self.front.next
            while tQueueNode != self.rear:
                num = num + 1
                tQueueNode = tQueueNode.next
            num = num + 1
            return num


class TestJP():
    def Josephus(self, n, k):
        qu = LinkQueue()
        i = 1
        while i <= n:
            qu.EnQueue(i)
            i = i + 1
        # qu.QueueTraverse()
        count = 0
        while qu.GetQueueLength() > 1:
            iNum = 1
            while iNum != k:
                tData = qu.DeQueue()
                qu.EnQueue(tData)
                iNum = iNum + 1
            print(qu.DeQueue(), end=" ")
            count = count + 1
        print(qu.DeQueue())