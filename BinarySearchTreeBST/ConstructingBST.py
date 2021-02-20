'''
nodes > parent node go to the right
nodes <= parent node got to the left

*attention - some people say no duplicate values but in our case we will put them to the left

Three main parts to focus on for a BST
Insetion
Searching
Deletion

Insertion
call insertion method.
start by comparing the value to the first value.
then we know which direction to go in.
insertion number > or <= to first node. if > then go right
if <= go left
We keep going by halves to find the locaion of the node we want to put in.

Searching
same concept as before but to find a value

Deletion
same concept but a few extra steps
grab smallest value in the right sub tree and we keep track of that value
Then we replace the value we want to delete with that value
Reason is that smallest/left most value in the right subtree is smaller than
all values to its right and greater than all values to it's left

time and space will be average case and worst case
all three have O(log(N))
Average:
Time = O(log(N))
space = O(log(N)) - recursive
space = O(1) - Iterative
worst:
Time = O(N)
space = O(N) - recursive
space = O(1) - Iterative
 '''

 #Code walk through solution 1
 class BST:
     def __init__(self,value):
         self.value = value
         self.left = None
         self.right = None

     #Average: o(log(n)) time | O(log(n)) space
     #worst: O(n) time | O(n) space
     def insert(self, value):
         if value < self.value:
             if self.left is None:
                 self.left = BST(value)
             else:
                 self.left.insert(value)
         else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    #Average: o(log(n)) time | O(log(n)) space
    #worst: O(n) time | O(n) space
    def contains(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
            else:
                return True
    #Average: o(log(n)) time | O(log(n)) space
    #worst: O(n) time | O(n) space

    def remove(self, value, parent=None):
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value, self)
            else:
                if self.left is not None and self.right is not None:
                    self.value = self.right.getMinValue()
                    self.right.remove(self.value, self)
                elif parent is None:
                    if self.left is not None:
                        self.value = self.left.value
                        self.right = self.left.right
                        self.left = self.left.left
                    elif self.right is not None:
                        self.value = self.right.value
                        self.left = self.right.right
                    else:
                        # This is a single-node tree; do nothing.
                        pass
                elif parent.left == self:
                    parent.left = self.left if self.left is not None else self.right
                elif parent.right == self:
                    parent.right = self.left if self.left is not None else self.right
            return self
        def getMinValue(self):
            if self.left is None:
                return self.value
            else:
                return self.left.getMinValue()

#code walk through solution 2
class BST2:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
            return self

    def contains(self,value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False

    def remove(self,value, parentNode = None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode= currentNode
                currentNode= currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNodeis None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        #this is a single-node tree; do nothing
                        pass
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode is not None else currentNode.right
                    break
            return self

        def getMinValue(self):
            currentNode = self
            while currentNode.left is not None:
                currentNode = currentNode.left
            return currentNode.value


#Now with video explanation and typing side by side with Iterative solution
class BST3:
    def __init__(self,value):
        #every node has a value with a left and a right
        self.value = value
        #left and right defaulted to none
        self.left = None
        self.right = None

    #insert, contains, and remove methods. Each take in a value as a parameter
    def insert(self,value):
        #first initialize a variable to keep track of position
        currentNode = self
        while True: #untill we have a break or use return statement
        #questions to ask, is the node value we want to insert
        #greater than, equal to, or less than the current value?
        #if insert value > current go to the right
        #if it is less than the current than we go to the left
        #if it is eual to then we break because it is already there or right
            if value < currentNode.value:
                #since insert value is < current we want to go to the left
                #check if there left node is end of a branch where
                #we can just insert it or if we need to continue checking
                if currentNode.left is None:
                    currentNode.left = BST3(value)
                    break
                else:
                    #if not none then we make current the left value
                    currentNode = currentNode.left
            else: #eles in this case means if value >= currentNode.value
                if currentNode.right is None:
                    currentNode.right = BST3(value)
                    break
                else:
                    #if not none then we make current the right value
                    currentNode = currentNode.right
        return self
        #This is done so that we can chain these calls for test cases
        #for example testBST.insert(1).insert(5).insert(12)
        #other than that retur self isn't needed for the algorithm

        #Now for time and space complexity we have
        #Average: O(Log(n)) time | = O(1) space
        #worst: O(n) time | O(1) space

        #space explanation
        #Reason for the consstant space is because we are not storing much
        #We are only keeping track of the currentNode variable so constant space
        #We implemented this iteratively and never called function recursively

    #checking to see if value is located in the tree
    def contains(self,value):
        #similar to Insertion
        #start by creating variable for the currentNode value
        currentNode = self
        while currentNode is not None: #if None then no values in three
            #ask question is value we are checking for greater than,
            #equal to, or less than the currentNode
            if value < currentNode.value:
                #if value is less than currentNode then we go left
                currentNode = currentNode.left
            elif value > currentNode.value:
                #if greater than or equal to go to the right
                currentNode = currentNode.right
            else:
                #we found the value in the tree
                return True
        return False
        #This means that we ended up at a node that is null
        #we broke out of the while loop and return False since value not in tree

        #same time and space as before
        #Average: O(Log(n)) time | = O(1) space
        #worst: O(n) time | O(1) space


    #has a specific parentNode value
    #here we are trying to remove a value given
    #Keeping track of the parentNode is important to track to know
    #what the value before the new currentNode is
    def remove(self, value, parentNode=None):
        #first thing to do is declare the currentNode
        currentNode = self
        #if currentNode is not none then we can start comparing values
        #removing is a two step process, first find then remove
        while currentNode is not None:
            #checking if the value is either in the right or left
            if value < currentNode.value:
                #if value to remove is < current then go left
                #then keep track of the node now and before
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                #if value to remove is > current then go right
                #also keeping track of both new current node and old
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                #a few subcases when we find the values
                #first case is when dealing with a node with two children nodes
                if currentNode.left is not None and currentNode.right is not None:
                    #above we are saying found value and another one so two nodes
                    currentNode.value = currentNode.right.getMinValue()
                    # we are calling the getMinValue method which we'll make
                    #this will give us the smallest value of the right subtree
                    currentNode.right.remove(currentNode.value, currentNode)
                    #Then above we are saying .remove function pass in
                    #currentNode.value and the parentNode
                #Here we are checking to make sure that parentNodeis not none
                #Reason being that if
                elif parentNode is None:
                    #dealing with a root node who's parentNode is None
                    if currentNode.left is not None:
                        #Here we are manually replacing the values
                        #replacing values with left node value
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                        #we assign left at the end since we need it for
                        #all the previously
                    #here we are doing the same if it's on the right side
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                        #here we set the right last for the same reason
                    else:
                        #here root node has no children nodes
                        #edge case and you are essentially deleting the BST
                        #currentNode.value = None
                        pass
                #next case if there are not two nodes
                #We then have two cases

                elif parentNode.left == currentNode:
                    #Here we check if parentNode left is the one we want to remove
                    #if it is then we replace it with currentNode.left but only if it isn't null
                    #if it is null then replace with currentNode.right
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    #Here we are checking if parentNode.right is the one we want to remove
                    #if it isn't null then replace with currentNode.left
                    # if it is Null then we replace with currentNode.right
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self

    def getMinValue(self):
        currentNode = self
        print("getMinValue")
        print("self", currentNode.value)
        while currentNode.left is not None:
            print("currentNode.left",currentNode.left.value)
            print("--")
            print("--")
            print("--")
            print("currentNode.value", currentNode.value)
            currentNode = currentNode.left
            print("currentNode.left after ", currentNode.left.value)
            print("currentNode.value after", currentNode.value)
        return currentNode.value

FirstTree = BST3(10)
FirstTree.insert(5).insert(2).insert(12).insert(6).insert(13)
FirstTree.contains(5)
FirstTree.insert(11).insert(22).insert(27).insert(30).insert(4).insert(8)
FirstTree.remove(10)

FirstTree.insert(10)
print(FirstTree.getMinValue())


def remove(self, value, parent=None):
    current = self
    while current is not None:
        if value < current.value:
            parent = current
            current = current.left
        elif value > current:
            parent = current
            current = current.right
        else:
            if current.left is None and current.right is None:
                #current is the one to remove
                #so we go right and find the smallest to replace it with
                #getMin we make and will return the smallest value from self
                #therefore we give it the right subtree as the argument value
                current.value = current.right.getMin()
                #with above we have removed the initial value
                #Now we have a new value to remove and so we start looking again
                #this time we start from that right subtree with the parent
                #recorded and the smallest value to look for and remove
                current.right.remove(self=current.right,current.value = value to remove ,parent=current which equals the value we want to remove initially)






listone = [0,2,3,4,5,6,1,8]
listtwo = [9,10]
FirstTree.right.remove(0,10)
FirstTree.contains(0)
FirstTree.contains(10)
