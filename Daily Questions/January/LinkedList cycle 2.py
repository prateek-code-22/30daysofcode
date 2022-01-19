def detectCycle(head):

    slow = head
    fast = head
        
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        #check loop is present
        if slow==fast:
            collide = slow

            #start moving from start and from collision point
            while head!=collide:
                head = head.next
                collide = collide.next
                    
            return head
            
    return None