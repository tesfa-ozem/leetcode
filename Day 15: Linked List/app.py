class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 

    def display(self,head):
        current = head
        while current:
            # print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        if not head:
            head = Node(data)
            return head
        current = head
        while current.next:
            print(current.data)
            current = current.next
        current.next = Node(data)

        return head
    def insert_head(self,head, data):
        ...

# mylist= Solution()
# T= 7
# head=None
# for i in range(T):
#     data=i+1
#     head=mylist.insert(head,data)    
# mylist.display(head); 
print(__name__)	