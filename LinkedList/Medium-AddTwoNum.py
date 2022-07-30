# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3=[]
        l4=[]
        while(l1):
            l3.append(l1.val)
            l1=l1.next
        while(l2):
            l4.append(l2.val)
            l2=l2.next
        l3=[str(i) for i in l3[::-1]]
        l3n=int("".join(l3))
        l4=[str(i) for i in l4[::-1]]
        l4n=str(int("".join(l4))+l3n)[::-1]
        result = ListNode(0)
        result_tail=result
        for i in l4n:
            result_tail.next = ListNode(int(i))
            result_tail = result_tail.next
        return result.next