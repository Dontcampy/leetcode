# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3head = None
        isCarry = False
        while l1:
            # l1.len > l2.len
            if l2:
                val = l1.val + l2.val
                if isCarry:
                    val += 1
                    isCarry = False
                # 进位检测
                if val >= 10:
                    isCarry = True
                    val = val - 10

                if not l3head:
                    # first Node
                    l3 = ListNode(val)
                    l3head = l3
                else:
                    l3.next = ListNode(val)
                    l3 = l3.next
                l1 = l1.next
                l2 = l2.next
            else:
                val = l1.val
                if isCarry:
                    val += 1
                    isCarry = False
                # 进位检测
                if val >= 10:
                    isCarry = True
                    val = val - 10
                l3.next = ListNode(val)
                l3 = l3.next
                l1 = l1.next
        while l2:
            # l1.len < l2.len
            val = l2.val
            if isCarry:
                val += 1
                isCarry = False
            # 进位检测
            if val >= 10:
                isCarry = True
                val = val - 10
            l3.next = ListNode(val)
            l3 = l3.next
            l2 = l2.next
        # 最后补位检测
        if isCarry:
            l3.next = ListNode(1)
        return l3head
