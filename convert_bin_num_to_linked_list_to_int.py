'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.
Example:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
'''
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
class Solution:
    def getDecimalValue(self, head) -> int:
            current = head
            len =0
            sum = 0
            while current:
                len+=1
                current = current.next
            print(len)
            current = head
            i = len-1
            while current:
                sum =sum+ current.data * 2**i
                current = current.next
                i-=1
            return sum
def show(head):
    current = head
    result_list = []
    while current:
        result_list.append(current.data)
        current = current.next
    print(result_list)
bin = [1,0,1]
l1 = Linkedlist()
for i in bin:
    l1.push(i)
show(l1.head)
s = Solution()
result = s.getDecimalValue(l1.head)
print(result)
