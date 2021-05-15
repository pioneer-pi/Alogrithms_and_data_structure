class StackNode:
    def __init__(self):
        self.data = None
        self.next = None

class TestBM:
    def BracketMatch(self, str1):
        self.head = StackNode()
        for i in str1:
                if i in ["{","("]:
                    node = StackNode()
                    node.data = i
                    node.next = self.head
                    self.head = node

                elif i in ["}",")"]:
                    find = False
                    l = []
                    while self.head != None and find == False:
                        if i == "}" and self.head.data =="{":
                            self.head = self.head.next
                            find = True
                        elif i == ")" and self.head.data =="(":
                            self.head = self.head.next
                            find = True
                        else:
                            node = self.head
                            l.append(node)
                            self.head = self.head.next
                    if  find == False:
                        print("False")
                        return

                    if len(l) != 0:
                        for j in l[::-1]:
                            node = j
                            node.next = self.head
                            self.head = node
        if self.head.data == None:
            print("True")
        else:
            print("False")

TBM = TestBM()
TBM.BracketMatch("{}{}")
TBM = TestBM()
TBM. BracketMatch("{ } { {( }} ) ")
TBM = TestBM()
TBM. BracketMatch("( ){() {}")

# standard answer
class StackNode:
    def __init__(self):
        self.data = None
        self.next = None
class LinkStack:
    def __init__(self):
        self.top = StackNode()
    '''判断链栈是否为空'''
    def IsEmptyStack(self):
        if self.top.next == None:
            iTop = True
        else:
            iTop = False
        return iTop
    '''进栈'''
    def PushStack(self,da):
        tStackNode = StackNode()
        tStackNode.data = da
        tStackNode.next = self.top.next
        self.top.next = tStackNode
    '''出栈'''
    def PopStack(self):
        if self.IsEmptyStack() == True:
            return
        else:
            tStackNode = self.top.next
            self.top.next = tStackNode.next
            return tStackNode.data
    '''获取栈顶元素'''
    def GetTopStack(self):
        if self.IsEmptyStack() == True:
            return
        else:
            return self.top.next.data
    '''反向输出链栈元素'''
    def ReverseStackTraverse(self):
        list1 = []
        tStackNode = self.top.next
        while tStackNode != None:
            result = self.PopStack()
            list1.append(result)
            tStackNode = tStackNode.next
class TestBM:
    def BracketMatch(self,str1):
        Ls = LinkStack()
        i = 0
        while i < len(str1):
            if str1[i] == '{':
                Ls.PushStack(str1[i])
                i = i+1
            elif str1[i] == '}':
                if Ls.GetTopStack() == '{':
                    Ls.PopStack()
                    i = i+1
                else:
                    Ls.PushStack(str1[i])
                    i = i+1
            else:
                 i = i+1
        if Ls.IsEmptyStack() == True:
            print("True")
        else:
            print("False")
            Ls.ReverseStackTraverse()