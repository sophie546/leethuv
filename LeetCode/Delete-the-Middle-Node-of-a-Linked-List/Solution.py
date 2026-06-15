1class Solution:
2    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
3        if not head.next: return None
4
5        slow = head
6        fast = slow.next.next
7
8        while fast and fast.next:
9            slow = slow.next
10            fast = fast.next.next
11
12        slow.next = slow.next.next
13        return head