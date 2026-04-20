# 定義節點
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 建立 Linked List
def build_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


# 反轉 Linked List（Iterative）
def reverseList(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next   # 先存下一個
        curr.next = prev        # 反轉指標
        prev = curr             # prev 往前移
        curr = next_node        # curr 往前移

    return prev


# 印出 Linked List
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# 主程式
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]

    # 建立 linked list
    head = build_list(arr)

    print("原始:")
    print_list(head)

    # 反轉
    new_head = reverseList(head)

    print("反轉後:")
    print_list(new_head)
    

