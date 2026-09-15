class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)

print("Total nodes:", count_nodes(root))




def height(root):
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height (root.right)

    return 1 + max(left_height, right_height)
print("Height:", height(root))



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def level_order(root):
    if root is None:
        return

    queue = [root]

    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level Order Traversal:")
level_order(root)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return 1 + max(left_height, right_height)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Height of Binary Tree:", height(root))


def has_cycle(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True

        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True

    return False


graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

if has_cycle(graph):
    print("Cycle exists")
else:
    print("No cycle")
    
    
    class Graph:
    def __init__(self, vertices): 
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        x = self.find(parent, x)
        y = self.find(parent, y)

        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def kruskal(self):
        self.edges.sort()

        parent = list(range(self.V))
        rank = [0] * self.V

        mst = []
        total = 0

        for weight, u, v in self.edges:
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                mst.append((u, v, weight))
                total += weight
                self.union(parent, rank, x, y)

        print("Minimum Spanning Tree:")

        for u, v, weight in mst:
            print(u, "-", v, ":", weight)

        print("Total weight:", total)


g = Graph(4)

g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskal()


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)

print("Total nodes:", count_nodes(root))

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)

print("Total nodes:", count_nodes(root))



def height(root):
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height (root.right)

    return 1 + max(left_height, right_height)
print("Height:", height(root))


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Create the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)


# Inorder traversal
print("Inorder Traversal:")
inorder(root)



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Create the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)


# Postorder traversal
print("Postorder Traversal:")
postorder(root)

def move_zeroes(arr):
    pos=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[pos],arr[i]=arr[i],arr[pos]
            pos+=1
    return arr
arr=[0,1,0,3,12]
print(move_zeroes(arr))


def string_reverse(str):
    return str[::-1]
while True:
    str= input("Enter the string:")
    reverse_str=string_reverse(str)
    print(reverse_str)
    continue_choice= input("want to reverse the another string?(yes the continue, no to exit:)" ).strip().lower()
if continue_choice!="yes":
    print("Existing the string reverse.....Goodbye!")
    break


def fibonacci(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n]=fibonacci(n-1,memo)+ fibonacci(n-2,memo)
    return memo[n]
n=7
print("fibonacci:",fibonacci(n))