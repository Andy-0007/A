class listNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def MergeTwoList(List1,List2):
    dummy=ListNode(-1)      
    current=dummy
    while List1 and List2:
        if List1.val<List2.val:
            current.next=List1
            List=List.next  
        else:
            current
        
