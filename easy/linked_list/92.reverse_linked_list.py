class Node:
    def __init__(self,val):
        self.val = val
        self.next = next 


def reverseBetween(head, left, right):
    if not head:
        return head 
    
    dummy = Node(0)
    dummy.next = head 
    prev = dummy 

    for _ in range(left -1):
        prev = prev.next 

    start = prev.next 
    then = start.next 

    for _ in range(right - left):
        start.next = then.next 
        then.next = prev.next 
        prev.next = then 
        then =  start.next 
    
    return dummy.next