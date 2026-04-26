# nums = [2,7,11,15], target = 9→ [0,1]
def two_sum(nums, target):
    if not isinstance(nums, list) or not isinstance(target, int):
        return None
    
    coordinate = []
    
    for i in range(0, len(nums)):
        x = target - nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] == x:
                coordinate.append(i)
                coordinate.append(j)
    return coordinate

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(two_sum(nums, target))