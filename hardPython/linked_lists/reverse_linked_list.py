from turtle import clear


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    curr = head
    previous = None
    while True:
        tmp_curr = curr.next
        curr.next = previous
        previous = curr
        if tmp_curr == None:
            return curr
        else:
            curr = tmp_curr




