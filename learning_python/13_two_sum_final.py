# 嘗試輸出所有符合條件的結果
def two_sum_sorted(nums, target):
    if not isinstance(nums, list) or not isinstance(target, int):
        return None
    for i in nums:
        if not isinstance(i, int):
            return None
    left = 0
    right = len(nums) - 1
    result = []
    while left < right:
        s = nums[left] + nums[right]
        if target < s:
            right = right - 1
        elif target == s:
            temp = (left, right)
            result.append(temp)
            left = left + 1
            right = right - 1
        elif target > s:
            left = left + 1
    return result

if __name__ == "__main__":
    nums = [0, 1, 1, 2, 2, 3]
    target = 3
    print(two_sum_sorted(nums, target))