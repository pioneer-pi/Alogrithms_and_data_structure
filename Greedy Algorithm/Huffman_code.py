class Node:
    def __init__(self,frequency,left = None,right = None):
        self.left = left
        self.right = right
        self.father = None
        self.frequency = frequency
    def is_left(self):
        return self.father.left == self

#统计字符出现频率，生成映射表
def count_frequency(text):
    chars = []
    ret = []
    for char in text:
        if char in chars:
            continue
        else:
            chars.append(char)
            ret.append((char,text.count(char)))

def create_nodes(frequecny_list):
    return [Node(frequency) for frequency in frequecny_list]


def create_huffman_tree(nodes):
    queue = nodes
    while len(queue) > 1:
        queue.sort(key=lambda item: item.frequency)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_left.frequency + node_right.frequency,node_left,node_right)
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)
    return queue[0]

def huffman_encoding(nodes,root):
    huffman_code = [''] * len(nodes)
    for i in range(len(nodes)):
        node = nodes[i]
        while node != root:
            if node.is_left():
                huffman_code[i] = '0' + huffman_code[i]
            else:
                huffman_code[i] = '1' + huffman_code[i]
            node = node.father
    return huffman_code
