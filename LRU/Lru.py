class CDLLNode:
    def __init__(self,key,value):
        self.k = key
        self.v = value
        self.prev = None
        self.next = None

class CDLL:
    def __init__(self):
        self.head = None
    
    def InsertAtBegin(self,key,value):
        nn = CDLLNode(key,value)
        nn.next = nn
        nn.prev = nn
        if self.head == None:
            self.head = nn
        else:
            last = self.head.prev
            nn.next = self.head
            self.head.prev = nn
            nn.prev = last 
            last.next = nn
            self.head = nn
        return self.head
        
    def printAll(self):
        if self.head == None:
            return 
        last = self.head.prev
        temp = self.head
        while(True):
            print(temp.k,temp.v)
            if(temp.next!=last):
                temp = temp.next
            else:
                temp = temp.next
                print(temp.k,temp.v)
                break

    def deleteLast(self):
        if self.head == None:
            return -1
        last = self.head.prev
        if(self.head == last):
            self.head = None
        else:
            last.prev.next = self.head
            self.head.prev = last.prev
        return last.k

    def moveNodeToStart(self,nodeToMove):
        if(self.head == nodeToMove):
            return # nothing to move
        nodeToMove.prev.next = nodeToMove.next
        nodeToMove.next.prev = nodeToMove.prev
        last = self.head.prev
        nodeToMove.next = self.head
        self.head.prev = nodeToMove
        nodeToMove.prev = last
        last.next = nodeToMove
        self.head = nodeToMove

class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.ll = CDLL()
        self.mp = dict()
    
    def get(self,key):
        if key in self.mp:
            node = self.mp[key]
            self.ll.moveNodeToStart(node)
            return node.v
        else:
            return -1
        
    def put(self,key,value):
        if key in self.mp:
            node = self.mp[key]
            node.v = value
            self.ll.moveNodeToStart(node)
        else:
            if(self.size < self.capacity):   # can insert without deletion
                node = self.ll.InsertAtBegin(key,value)
                self.mp[key] = node
                self.size+=1
            else:     # deletion of last node required as the capacity is full
                deletedKey = self.ll.deleteLast()
                self.mp.pop(deletedKey)
                node = self.ll.InsertAtBegin(key,value)
                self.mp[key] = node

if __name__ == '__main__':
   
    lru_cache = LRUCache(capacity=4)

    lru_cache.put(1, 1)  
    lru_cache.put(2, 2) 
    lru_cache.put(3, 3)  
    lru_cache.put(4, 4)  
    print("Initial cache state:")
    lru_cache.ll.printAll()  

    print("Access key 2. Value:", lru_cache.get(2)) 

    lru_cache.ll.printAll() 

    lru_cache.put(5, 5)
    print("After inserting new key")
    lru_cache.ll.printAll() 

    lru_cache.put(2, 22) 
    print("Access key 2 after updating its value to 22:")
    lru_cache.ll.printAll() 
    

    print("Access non-existent key 6. Value:", lru_cache.get(6))  

    print("Final cache state:")
    lru_cache.ll.printAll()