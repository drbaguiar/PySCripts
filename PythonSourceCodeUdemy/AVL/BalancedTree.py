from AVL.Node import Node;

class BalancedTree(object):
    
    def __init__(self):
        self.rootNode = None;
        
    def insert(self,data):
        
        parentNode = self.rootNode;
        
        if( self.rootNode == None ):
            parentNode = Node(data, None);
            self.rootNode = parentNode;
        else:
            parentNode = self.rootNode.insert(data, self.rootNode);
            
        self.rebalanceTree(parentNode);
        
            
    def getMax(self):
        
        maxNode = self.rootNode;
        
        while maxNode.rightChild:
            maxNode = maxNode.rightChild;
            
        return maxNode.data;
    
    def getMin(self):
        
        minNode = self.rootNode;
        
        while minNode.leftChild:
            minNode = minNode.leftChild;
            
        return minNode.data; 
            
    def traverseInOrder(self):
        if self.rootNode:
            self.rootNode.traverseInOrder();
            
    def rebalanceTree(self, parentNode):
        
        self.setBalance(parentNode);
        
        if( parentNode.balance < -1 ):
            if( self.height(parentNode.leftChild.leftChild) >= self.height(parentNode.leftChild.rightChild)):
                parentNode = self.rotateRight(parentNode);
            else:
                parentNode = self.rotateLeftRight(parentNode);
        elif( parentNode.balance > 1 ):
            if( self.height(parentNode.rightChild.rightChild) >= self.height(parentNode.rightChild.leftChild)):
                parentNode = self.rotateLeft(parentNode);
            else:
                parentNode = self.rotateRightLeft(parentNode);
        
        if( parentNode.parentNode is not None ):
            self.rebalanceTree(parentNode.parentNode);
        else:
            self.rootNode = parentNode;
        
        
    def rotateLeftRight(self, node):
        print("Rotation left then right...\n");
        node.leftChild = self.rotateLeft(node.leftChild);
        return self.rotateRight(node);
        
    def rotateRightLeft(self, node):
        print("Rotation right then left...\n");
        node.rightChild = self.rotateRight(node.rightChild);
        return self.rotateLeft(node);
    
    def rotateLeft(self, node):
        print("Left rotation...\n");

        b = node.rightChild;
        b.parentNode = node.parentNode;
        
        node.rightChild = b.leftChild;
        
        if( node.rightChild is not None ):
            node.rightChild.parentNode = node;
            
        b.leftChild = node;
        node.parentNode = b;
        
        if( b.parentNode is not None ):
            if( b.parentNode.rightChild == node ):
                b.parentNode.rightChild = b;
            else:
                b.parentNode.leftChild = b;
                
        self.setBalance(node);
        self.setBalance(b);
        
        return b;
        
    def rotateRight(self, node):
        print("Right rotation...\n");

        b = node.leftChild;
        b.parentNode = node.parentNode;
        
        node.leftChild = b.rightChild;
        
        if( node.leftChild is not None ):
            node.leftChild.parentNode = node;
            
        b.rightChild = node;
        node.parentNode = b;
        
        if( b.parentNode is not None ):
            if( b.parentNode.rightChild == node ):
                b.parentNode.rightChild = b;
            else:
                b.parentNode.leftChild = b;
                
        self.setBalance(node);
        self.setBalance(b);
        
        return b;
    
        
    def setBalance(self, node):      
        node.balance = (self.height(node.rightChild) - self.height(node.leftChild) );
        
    def height(self, node):
        
        if( node == None ):
            return -1;
        
        return 1 + max( self.height(node.leftChild) , self.height(node.rightChild)  );
        
        
        
