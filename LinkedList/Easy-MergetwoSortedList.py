# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        li=ListNode(-100)
        root=li
        while(list1 and list2):
            if(list1.val<list2.val):
                li.next=list1
                list1=list1.next
                li=li.next
            else:
                li.next=list2
                list2=list2.next
                li=li.next
        while(list1):
            li.next=list1
            list1=list1.next
            li=li.next
        while(list2):
            li.next=list2
            list2=list2.next
            li=li.next
            
        return root.next