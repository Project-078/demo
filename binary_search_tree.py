class User:
    def __init__(self, username, name, gmail):
        self.username = username
        self.name = name
        self.gmail = gmail
    
    def __repr__(self):
        return "User(username='{}', name = '{}', gmail = '{}')".format(self.username, self.name, self.gmail)

    def __str__(self):
        return self.__repr__()

user4 = User('jane', 'Jane Doe', 'jane@doe.com')
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

class BSTnode:
    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def BSTinsert(node, key, value):
    if node is None:
        node = BSTnode(key, value)
    elif node.key > key:
        node.left = BSTinsert(node.left, key, value)
        node.left.parent = node
    else:
        node.right = BSTinsert(node.right, key, value)
        node.right.parent = node
    return node

bst = BSTnode(vishal.username, vishal)
BSTinsert(bst, biraj.username, biraj)
BSTinsert(bst, hemanth.username, hemanth)
BSTinsert(bst, jadhesh.username, jadhesh)
BSTinsert(bst, siddhant.username, siddhant)
BSTinsert(bst, sonaksh.username, sonaksh)

def find(node, key):
    if node is None:
        return None
    elif node.key == key:
        return node
    elif node.key < key:
        return find(node.right, key)
    else:
        return find(node.left,key)

def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value

def list_All(node):
    if node is None:
        return []
    return (list_All(node.left)+[(node.key, node.value)]+(list_All(node.right)))

    


def is_bst_tree(node):
    if node is None:
        return True, 0
    else:
        bst_tree_l, height_L = is_bst_tree(node.left)
        bst_tree_r, height_r = is_bst_tree(node.right)
        bst = bst_tree_l and bst_tree_r and abs(height_L-height_r) <=1
        height = 1+ max(height_L, height_r)
    return bst, height

# t = is_bst_tree(bst)
# print(t)


def make_bst(data, parent = None):
    if not data:
        return None
    mid = len(data)//2
    key, value = data[mid]
    node = BSTnode(key, value)
    node.parent = parent
    node.left = make_bst(data[:mid], node)
    node.right = make_bst(data[mid+1:], node)
    return node

def make_bst_tree(node):
    data = list_All(node)
    return make_bst(data)

# b = make_bst_tree(bst)
# f = is_bst_tree(b)
# print(f)
# update(bst, siddhant.username, User('siddhant', 'Siddhant Simha', 'siddhant@example.com'))
# node1 = find(bst, siddhant.username)
# print(node1.value)
# print(list_All(bst))


