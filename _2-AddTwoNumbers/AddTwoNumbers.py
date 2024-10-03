# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        num1=0
        mul=1
        
        while(l1):
            num1 = num1 + mul*l1.val

            mul=mul*10
            l1=l1.next
        
        num2 =0 
        mul=1
        while(l2):
            num2 = num2 + mul*l2.val
            mul=mul*10
            l2=l2.next

        num2 = num2+num1

        l3 = ListNode(str(num2)[0])
        for i in str(num2)[1:len(str(num2))]:
            l3 = ListNode(i,l3)
        
        return l3
            

