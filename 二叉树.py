
#  python class 定义二叉树
class Node(object):
  pass

class Tree(object):
    pass
    def add(self, elem):
        node = Node(elem)
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

#  2  函数实现二叉树先序遍历
def perorder(self, root):
    if root == Node:
        return
    print(root.elem)
    self.foo(root.lchild)
    self.foo(root.rchild)

# 3 广度优先遍历
def breadth_travel(self, root):
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.elem)
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)

