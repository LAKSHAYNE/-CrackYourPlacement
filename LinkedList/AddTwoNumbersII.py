# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=''
        num2=''
        while(l1):
            num1+=str(l1.val)
            l1=l1.next
        
        while(l2):
            num2+=str(l2.val)
            l2=l2.next
        
        ans=str(int(num1)+int(num2))
        li=ListNode(int(ans[0]))
        new=li
        for i in ans[1:]:
            li.next=ListNode(int(i))
            li=li.next
        
        return new
        