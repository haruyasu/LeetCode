# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        current = head
        while current:
            copied = RandomListNode(current.label)
            copied.next = current.next
            current.next = copied
            current = copied.next

        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        dummy = RandomListNode(0)
        copied_current = dummy
        current = head
        while current:
            copied_current.next = current.next
            current.next = current.next.next
            copied_current = copied_current.next
            current = current.next

        return dummy.next


head = RandomListNode(1)
head.next = RandomListNode(2)
head.random = head.next
result = Solution().copyRandomList(head)
print(result.label)
print(result.next.label)
print(result.random.label)
