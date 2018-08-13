"""Binary Tree.

Max two children.
Insertion - Left, Right at the first available spot in level order traversal.
"""
from collections import deque
from copy import deepcopy

class Node(object):
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = None
        self.left = None

        self.addright(right)
        self.addleft(left)

    def addright(self, right):
        if isinstance(right, Node):
            self.right = right
        elif isinstance(right, str):
            self.right = Node(right)

    def addleft(self, left):
        if isinstance(left, Node):
            self.left = left
        elif isinstance(left, str):
            self.left = Node(left)


class BinaryTree(object):
    """Binary Tree."""
    def __init__(self, root):
        self.root = Node(root)

    def printhelper(self, output, space):
        tabs = "\t" * 2 * space
        short = '\t' * space
        op = "{0}{1}".format(tabs, short.join(map(str, output)))
        print op

    def getlevelnodes(self, q):
        local = deepcopy(q)
        result = []
        while (len(local)>0):
            node = local.popleft()
            if node:
                result.append(node.value)
        return result

    def levelorder(self, root):
        """Return array of array containing each level elememts. 

        Encode empty or missing as None."""

        if not root:
            return

        result = []
        q = deque()
        q.append(root)

        while self._hasnodes(q):
            result.append(self.getlevelnodes(q))
            q = self.getnextlevel(q)

        print result

    def _hasnodes(self, q):
        local = deepcopy(q)
        if list(set(local)) == [None]:
            return False
        return True

    def getnextlevel(self, q):
        newq = deque()

        while (len(q)>0):
            node = q.popleft()

            if not node:
                # empty left
                newq.append(None)
                # empty right
                newq.append(None)
            else:
                newq.append(node.left)
                newq.append(node.right)

        return newq

    def pprint(self, root):
        h = self.height(root)

        buf = deque()
        output = []

        if not root:
            print '$'
        else:
            buf.append(root)
            count, nextCount = 1, 0

            while count:
                node = buf.popleft()

                if node:
                    output.append(node.value)
                    count -= 1

                    for n in (node.left, node.right):
                        if n:
                            buf.append(n)
                            nextCount += 1
                        else:
                            buf.append(None)
                else:
                    output.append('$')

                if not count:
                    self.printhelper(output, h)

                    output = []
                    count, nextCount = nextCount, 0
                    h -= 1

            # print the remaining all empty leaf node part
            output.extend(['$']*len(buf))
            self.printhelper(output, h)

    def preorder(self, root):
        if not root:
            return

        # Pre Order
        # Uses Stack

        # <root>    <left>     <right>

        # Root
        print "Node: {0}".format(root.value)

        # Recruse Left
        self.preorder(root.left)

        # Recurse Right
        self.preorder(root.right)

    def postorder(self, root):
        if not root:
            return

        # Post Order 
        # Uses Stack

        # <left>    <right>    <root>

        # Recurse Left
        self.postorder(root.left)

        # Recurse Right
        self.postorder(root.right)

        # Root
        print "Node: {0}".format(root.value)

    def inorder(self, root):
        if not root:
            return

        # Post Order 
        # Uses Stack

        # <left>    <root>    <right>

        # Recurse Left
        self.inorder(root.left)

        # Root
        print "Node: {0}".format(root.value)

        # Recurse Right
        self.inorder(root.right)

    def height(self, root):
        if not root:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return 1 + max(left_height, right_height)

    def insert(self, child):
        # create a child node
        if not isinstance(child, Node):
            childobj = Node(child)
        else:
            childobj = child

        # first spot available at level order traversal
        q = deque()

        # Start traversing from root
        q.append(self.root)

        while (len(q) > 0):
            # get the current node
            node = q.popleft()

            if not node.left:
                # Insert node
                node.left = childobj
                print("Inserted child {0} at left of {1}".format(childobj.value, node.value))
                return 
            else:
                # Add left node for traversal
                q.append(node.left)

            if not node.right:
                # Insert node
                node.right = childobj
                print("Inserted child {0} at right of {1}".format(childobj.value, node.value))
                return
            else:
                # Add right node for traversal
                q.append(node.right)