class Solution:
    def searchKey(self, head, key):
        if head is None:
            return False

        while head is not None:
            if head.data == key:
                return True
            head = head.next

        return False
