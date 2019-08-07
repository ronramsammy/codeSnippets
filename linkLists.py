class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.start_node = None
        
    def traverse_list(self):
        if self.start_node is None:
            print("The list has no elements")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.ref


    def insert_at_start(self,data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node


    def insert_at_end(self,data):
        new_node = Node(data)        
        if self.start_node is None:
            self.start_node = new_node
            return        
        n = self.start_node
        while n.ref is not None:
            n = n.ref        
        n.ref = new_node
            
        
    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List has no elements...Unable to insert")
            return
        
        n = self.start_node
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print(f"Item {x} is not in the list...Cannot Insert After")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


        
    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List has no elements")
            return

        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return

        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

            
nll = LinkedList()
nll.insert_at_start(99)

nll.insert_at_end(20)
nll.insert_at_start(2)
nll.insert_after_item(5,11)

nll.insert_before_item(99,92)
nll.traverse_list()
            
        
        
