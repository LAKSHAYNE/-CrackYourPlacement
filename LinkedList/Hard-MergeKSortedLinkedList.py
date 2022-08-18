# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp=ListNode(0)
        re=temp
        n=len(lists)
        k=[]
        i=0
        c=0
        while(i<n):
            if(lists[i] and lists[i]!=None):
                k.append((lists[i].val,i))
            i+=1
        heapq.heapify(k)
        nk=len(k)
        while(c<nk):
            a=heapq.heappop(k)
            temp.next=ListNode(a[0])
            temp=temp.next        
            lists[a[1]]=lists[a[1]].next
            if(lists[a[1]]==None):
                c+=1
            else:
                heapq.heappush(k,(lists[a[1]].val,a[1]))
        return re.next