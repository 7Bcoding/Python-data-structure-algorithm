
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Linklist(object):
    def __init__(self, none=None):
        self.headnode = none

    def is_empty(self):

        if self.headnode is None:
            return 1
        else:
            return 0

    def length(self):

        count = 0
        node = self.headnode
        while node is not None:
            count += 1
            node = node.next
        return count

    def travel(self):

        node = self.headnode
        nodelist = ''
        while node is not None:
            nodelist += str(node.val) + '-->' + ' '
            node = node.next
        print(nodelist + 'end')

    def add(self, value):
        node = Node(value)
        node.next = self.headnode
        self.headnode = node

    def append(self, value):

        node = Node(value)
        if self.is_empty():
            self.headnode = node
        else:
            p = self.headnode
            while p.next is not None:
                p = p.next
            p.next = node

    def insert(self, pos, value):
        node = Node(value)
        if pos < 0:
            self.add(value)
        elif pos > (self.length()-1):
            self.append(value)
        else:
            count = 0
            p = self.headnode
            while count >= pos-1:
                p = p.next
            node.next = p.next
            p.next = node

    def remove(self, value):
        p = self.headnode
        pre = None
        while p is not None:
            if p.val == value:
                if p == self.headnode:
                    self.headnode = p.next
                    break
                else:
                    pre.next = p.next
                    break
            else:
                pre = p
                p = p.next

    def search(self, item):
        cur = self.head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    linklist = Linklist()
    for i in range(5):
        linklist.append(i)
    linklist.travel()
    linklist.insert(3, 7)
    linklist.travel()
    print(linklist.search(4))
    linklist.remove(7)
    linklist.travel()




