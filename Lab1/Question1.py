class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linked_List:
    def __init__(self):
        self.head = None

    def initlist(self, data_list):
        self.data_list = data_list

    def reverse(self):
        length = len(self.data_list)
        for i in range(length):
            node = Node(self.data_list[i])
            node.next = self.head
            self.head = node
    def print_list(self):
        linked_list = []
        current = self.head
        while current != None:
            linked_list.append(current.data)
            current = current.next
        print("lined_list:")
        print(linked_list)

l = Linked_List()
l.initlist([1,2,3,4,5,6,7,8,9,10])
l.reverse()
l.print_list()

# standard answer
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linked_List:
    def __init__(self):
        self.head = None
    def initlist(self,data_list):    #链表初始化函数
        self.head=Node(data_list[0])   #创建头结点
        temp=self.head
        for i in data_list[1:]: #逐个为 data 内的数据创建结点, 建立链表
            node=Node(i)
            temp.next=node
            temp=temp.next
    def is_empty(self):  #判断链表是否为空
        if self.head.next==None:
            print("Linked_list is empty")
            return True
        else:
            return False
    def get_length(self):  #获取链表的长度
        temp=self.head #临时变量指向队列头部
        length=0 #计算链表的长度变量
        while temp!=None:
            length=length+1
            temp=temp.next
        return length #返回链表的长度
    def insert(self,key,value): #链表插入数据函数
        if key<0 or key>self.get_length()-1:
            print("insert error")
        temp=self.head
        i=0
        while i<=key: #遍历找到索引值为 key 的结点后, 在其后面插入结点
            pre=temp
            temp=temp.next
            i=i+1
        node=Node(value)
        pre.next=node
        node.next=temp
    def print_list(self):   #遍历链表，并将元素依次打印出来
        print("linked_list:")
        current=self.head
        new_list=[]
        while current is not None:
            new_list.append(current.data)
            current=current.next
        print(new_list)
    def remove(self,key):  #链表删除数据函数
        if key<0 or key>self.get_length()-1:
            print("insert error")
        i=0
        temp=self.head
        while temp !=None:  #遍历找到索引值为 key 的结点
            pre=temp
            temp=temp.next
            i=i+1
            if i==key:
                pre.next=temp.next
                temp=None
                return True
        pre.next=None
    def reverse(self): #将链表反转
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
