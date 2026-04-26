# nums = [2,7,11,15]
# target = 9
# --> [0,1]
# Two Pointers（雙指針）
def two_sum_sorted(nums, target):
    if not isinstance(nums, list) or not isinstance(target, int):
        return None
    for i in nums:
        if not isinstance(i, int):
            return None
    left = 0
    right = len(nums) - 1
    while left < right:
        gap = target - (nums[left] + nums[right])
        if gap < 0:
            right = right - 1
        elif gap == 0:
            return [left, right]
        elif gap > 0:
            left = left + 1
    return None

if __name__ == "__main__":
    nums = [2, 7,11,15]
    target = 9
    print(two_sum_sorted(nums, target))