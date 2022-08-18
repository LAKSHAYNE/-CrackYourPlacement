class Solution:
    def sortList(self, head):
        if head == None or head.next == None:
            return head
        
        mid = self.midlist(head)
        left = self.sortList(head)
        right = self.sortList(mid)
            
        return self.merge(left, right)
    
    def midlist(self, head):
        slow = fast = head
            
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
        slow.next = None  #HERE WE ARE SEPREATING LEFT AND RIGHT PART
        
        return mid
    
    def merge(self, left, right): #SIMPLY JUST ADD TWO LISTS JUST LIKE WE DO IN MERGE SORT
        dummy = curr = ListNode()
        
        while left != None and right != None:
            if left.val < right.val:
                curr.next = left
                curr = curr.next
                left = left.next
                
            else:
                curr.next = right
                curr = curr.next
                right = right.next
                
                      
        while left != None:
            curr.next = left
            curr = curr.next
            left = left.next
            
        while right != None:
            curr.next = right
            curr = curr.next
            right = right.next
                
        return dummy.next 