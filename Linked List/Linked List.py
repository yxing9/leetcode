# Linked List (Singly)

# Bacics
'''
A linked list is a collection of nodes.

Node: an element of a linked list that has two different fields
    1. Data: the value to be stored in the list
    2. Next or next node: a pointer/reference to the next node

Head: the first node of a linked list
    - used as the starting point for any iteration through the list, ... = self.head

Last node pointing to None. 
'''

# Use Cases
'''
1. queue
    - insert at end
    - delete from beginning

2. stack
    - insert at end
    - delete from end

3. graph
    - implement Directed Acyclic Graph (DAG) using adjacency list, a list of linked list
    - each vertex of the graph has a linked list of vertices

    Vertex              Linked List of Vertices
    1                   2 -> 3 -> None
    2                   4 -> None
    3                   None
    4                   5 -> 6 -> None
    5                   6 -> None
    6                   None

    - also using dictionary, value is implemented using linked list

    graph = {
        1: [2, 3, None],
        2: [4, None],
        3: [None],
        4: [5, 6, None],
        5: [6, None],
        6: [None]
    }

4. lifecycle management for an operating system application
'''

# Methods:
'''
1. traverse/print list
2. search O(n)
3. insert O(1)
    - insert at the beginning
    - insert at the end 
    - insert in the middle
4. delete/remove O(n)
5. length/size O(n)
'''

# Implementation
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next # next is short for next_node, the next node

    def __repr__(self): # Optional: for better representation of the objects
        return self.data

    def get_data(self): # Optional: return the stored data
        return self.data

    def get_next(self): # Optional: return the next node
        return self.next

    def set_next(self, new_next): # Optional: reset the pointer to a new node
        self.next = new_next

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def __repr__(self): # Optional: for better representation of the objects
        node = self.head
        nodes = []
        while node:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)
        
    def print_list(self):
        print_data = self.head
        while print_data:
            print(print_data.data)
            print_data = print_data.next

    def insert(self, data): # This is insert at the beginning
        new = Node(data) # new is short for new_node, the new node
        new.next = self.head # this is easier to understand compared to new.set_next(self.head)
        #new.set_next(self.head) # point the head to the next node?
        self.head = new # This is initialization of a new empty linked list, so head points to the new node

    def insert_at_end(self, data): 
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        laste = self.head
        while laste.next:
            laste = laste.next
        laste.next = new

    def insert_at_middle(self, middle_node, data):
        if middle_node is None:
            print('The mentioned node is absent.')
            return
        new = Node(data)
        new.next = middle_node.next
        middle_node.next = new

    def get_count(self, head): # 1st approach to find the length of a linked list
        current = head
        count = 0
        while current:
            count += 1
            current = current.next # I prefer this approach because there is no .get_next()
        return count

    def size(self): # 2nd approach to find the length of a linked list
        current = self.head # start at the head node
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data == data:
                found = True
                # return current # I add this line to return the found data
            else:
                current = current.get_next()
        if current is None:
            raise ValueError('Data not in the linked list.')
        return current # Optional?

    def delete(self, data): # This is the 1st approach to delete a node/datum
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else: # if there is no match, 
                previous = current # remember the last node it visits
                current = current.get_next()
        if current is None:
            raise ValueError('Data not in the linked list.')
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next()) # reset the last visited node's pointer to the next next node, leaving the deleted node in between

    def remove(self, data): # This is the 2nd approach to delete a node/datum
        head = self.head
        if head:
            if head.data == data:
                self.head = head.next
                head = None
                return
        while head:
            if head.data == data:
                break
            previous = head
            head = head.next
        if head == None:
            return
        previous.next = head.next
        head = None


# Tests
# Test 1
lst = LinkedList()
lst.head = Node('Mon')
n2 = Node('Tue')
n3 = Node('Wed')

lst.head.next = n2
n2.next = n3

#lst.print_list()

#lst.insert('Sun')
#lst.print_list()

lst.insert_at_end('Thu')
#lst.print_list()

lst.insert_at_middle(lst.head.next, 'After Tue')
lst.insert_at_middle(lst.head.next.next.next, 'After Wed')
#lst.print_list()

lst.remove('After Wed')
lst.print_list()

# Test 2
# has better representation because of __repr__
llist = LinkedList()
print(llist)

first_node = Node('a')
llist.head = first_node
print(llist)

second_node = Node('b')
third_node = Node('c')
first_node.next = second_node
second_node.next = third_node
print(llist)

# Logic of Implementation
'''
search:
    - traverse the entire list to find the deleted node

insert:
    - insert at the beginning 
        - create a new node
        - point the head to the new node

delete:
    - traverse the entire list to find the deleted node
    - the previous node -> the to-be-deleted node -> the next node
'''

# Reference
'''
https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/
https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
https://realpython.com/linked-lists-python/
'''