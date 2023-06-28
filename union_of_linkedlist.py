''''
Given two linked lists, your task is to complete the function makeUnion(), that returns the union list of two linked lists. This union list should include all the distinct elements only and it should be sorted in ascending order.

Example 1:

Input:
L1 = 9->6->4->2->3->8
L2 = 1->2->8->6->2
Output: 
1 2 3 4 6 8 9
Explaination: 
All the distinct numbers from two lists, when sorted forms the list in the output. '''
#MY APPROACH...
class node:
    def __init__(self, data=0):
        self.data =data
        self.next = None
class Linkedlist:
    def __init__(self, head=None):
        self.head =head
    def push(self, data):
        current =self.head
        if current:
            while current.next:
                current = current.next
            current.next = node(data)
        else:
            self.head = node(data)
class solution:
    def union_of_linked_list(self, head1, head2):
        result = set()
        current = head1
        while current:
            result.add(current.data)
            current = current.next
        current = head2
        while current:
            result.add(current.data)
            current = current.next
        result = sorted(result)
        l1= Linkedlist()
        for elements in result:
            l1.push(elements)
        return l1.head
def show(head):
    current = head
    result_list = []
    while current:
        result_list.append(current.data)
        current = current.next
    print(result_list)
        
lst1 = [9,6,4,2,3,8]
lst2 = [1,2,8,6,2]
l1 = Linkedlist()
l2 = Linkedlist()
for element in lst1:
    l1.push(element)
for element in lst2:
    l2.push(element)
s = solution()
result_head = s.union_of_linked_list(l1.head, l2.head)
show(result_head)
