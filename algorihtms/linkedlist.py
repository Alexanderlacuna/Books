class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,val):
        if self.head == None:
            self.head = Node(val)
        else:
            current = self.head
            while (current.next!=None):
                current = current.next

            current.next = Node(val)

    def __str__(self):
        nodes = []
        current = self.head
        while current!=None:
            nodes.append(str(current.value))
            current = current.next
        return "->".join(nodes)

    def delete_head(self):
        if self.head !=None:
            self.head.next = self.head

    def delete(self,val):
        if self.head !=None:
            prev = None
            current = self.head
            while (current!=None):
                if current.value == val:
                    if prev  == None:
                        self.head = current.next

                    else:
                        prev  = current
                        prev.next = current.next
                    break
                else:
                    prev = current
                    current = current.next

                    
            
                


            
