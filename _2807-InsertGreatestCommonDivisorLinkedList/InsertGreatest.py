class Solution(object):

    def GcD(self,a,b):
        if(a==b):
            return b
        elif(b>a):
            return self.GcD(a,b-a)
        else:
            return self.GcD(a-b,b)

    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res=ListNode(0)
        curr= res
            
        while(head and head.next):
            num1 = head.val
            num2=head.next.val
            gcd = self.GcD(num1,num2)
            curr.next=ListNode(head.val)
            curr.next.next = ListNode(gcd)
            head=head.next
            curr=curr.next.next


        curr.next = ListNode(head.val)
        return res.next