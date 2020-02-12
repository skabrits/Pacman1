from pprint import pprint
class Tree:

    def __init__(self, x, is_test = False):
        self.testTree = [4,
                [2,
                 [1,
                  [0,
                   [-1, None, None],
                   None],
                  None],
                 [3, None, None]],
                [6,
                 [5, None, None],
                 [7, None, None]]]
        if is_test:
            self.val = self.testTree
        else:
            self.val = x

    def find(self, x):
        import copy

        t = copy.copy(self.val)
        while not (t[0] == x or (t[0] > x and t[1] == None) or (t[0] <= x and t[2] == None)):
            if t[0] > x:
                t = t[1]
            else:
                t = t[2]
        if t[0] == x:
            return t
        else:
            return None

    def __add__(self, other):
        t = self.val
        x = other
        while not ((t[0] > x and t[1] == None) or (t[0] <= x and t[2] == None)):
            if t[0] > x:
                t = t[1]
            else:
                t = t[2]
        if t[0] > x:
            t[1] = [x, None, None]
        else:
            t[2] = [x, None, None]
        return self.val

    def count_depth(self, tree = 0):
        if (tree == 0):
            tree = self.val
        length = 0
        if tree is not None:
            length = length + 1 + max(self.count_depth(tree[1]), self.count_depth(tree[2]))
        return length

    def convert_to_array(self, tree = 0):
        arr = list()
        if (tree == 0):
            tree = self.val
        arr.append(tree[0])
        if (tree[1] is not None):
            arr = self.convert_to_array(tree[1]) + arr
        if (tree[2] is not None):
            arr = arr + self.convert_to_array(tree[2])

        return arr

    def bal(self, arr, l, r):
        if r<l:
            return None
        else:
            m = (l+r)//2
            node = [arr[m], self.bal(arr, l, m-1), self.bal(arr, m+1, r)]
            return node

    def balance(self, tree = 0):
        if(tree == 0):
            tree = self.val
        arr = self.convert_to_array(tree)
        n = len(arr)
        self.val = self.bal(arr, 0, n-1)
        return self.val

    def show(self):
        self.__add__(1)
        pprint(self.count_depth())
        pprint(self.val, width = 30)
        self.balance()
        pprint(self.count_depth())
        pprint(self.val, width = 30)

Tree(1, is_test = True).show()
