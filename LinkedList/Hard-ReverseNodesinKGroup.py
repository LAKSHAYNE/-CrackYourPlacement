# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        li=[]
        temp=ListNode()
        re=temp
        i=0
        while(head):
            if(i%k==0):
                li.append([])
                li[-1].append(head.val)
            else:
                li[-1].append(head.val)
            i+=1
            head=head.next
        
        for i in li:
            if(len(i)!=k):
                for x in i:
                    temp.next=ListNode(x)
                    temp=temp.next
                break
            for x in i[::-1]:
                temp.next=ListNode(x)
                temp=temp.next
            
        return re.next