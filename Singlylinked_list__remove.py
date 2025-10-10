class SinglyLinkedListNode:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None

    def insert_node(self,data):
        node=SinglyLinkedListNode(data)
        if self.head is None:
            self.head=node
        else:
            self.tail.next=node
        self.tail=node

def print_singly_linked_list(node,sep):
        while node:
            print(node.data,end=sep)
            node=node.next

def removeKthNodeFromEnd(head,k):

    if head is None or k<0:
        return head

    dummy=SinglyLinkedListNode(0)
    dummy.next=head
    fast=slow=dummy
    # move first pointer k+1 steps
    for _ in range(k+1):
        if not fast.next:
            return head
        fast=fast.next

    #move both pointers till first reaches end
    while fast.next:
        fast=fast.next
        slow=slow.next

    #delete the kth node
    slow.next=slow.next.next
    return dummy.next

if __name__=='__main__':
    head_count=int(input().strip())
    head=SinglyLinkedList()

    for _ in range(head_count):
        head_item=int(input().strip())
        head.insert_node(head_item)
    k=int(input().strip())
    result=removeKthNodeFromEnd(head.head,k)
    print_singly_linked_list(result,'\n')
    print()


