#from wsgiref.validate import header_re


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def insert_node(self,item):
        new_node=Node(item)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
def deleteDuplicates(head):
    current=head
    while current and current.next:
        if current.data==current.next.data:
            current.next=current.next.next
        else:
            current=current.next
    return head
def disp_list(result,sep):
    current=result
    while current:
        print(current.data,end=sep)
        current=current.next


if __name__=='__main__':
    head_coun t=int(input().strip())
    head=SinglyLinkedList()
    for _ in range(head_count):
        item=int(input().strip())
        head.insert_node(item)
    result=deleteDuplicates(head.head)
    disp_list(result,'\n')



