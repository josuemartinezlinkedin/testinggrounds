"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

l1 = [2,3,4]
l2 = [7,9,8]
def addTwoNumbers(l1, l2):
    string1 = "l"
    for i in l1:
        string1 += str(i)
    string1 = string1[1:]
    string2 = "l"
    for j in l2:
        string2 += str(j)
    string2 = string2[1:]
    first = int(string1[::-1])
    second = int(string2[::-1])
    answer = first + second
    return answer
addTwoNumbers(l1,l2)


#Online solution from youtube

#Declar pointers for traversal. Added for clarity.
p1 = l1
p2 = l2

#declare 
