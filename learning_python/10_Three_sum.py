# nums = [-1, 0, 1, 2, -1, -4], target = 0
# python list slicing:
# x = list(range(10))
# x[0:5] --> [0, 1, 2, 3, 4]
def two_sum(slicing, target):
    my_dict = {}
    for i, element in enumerate(slicing):
        x = target - element
        if x in my_dict:
            return[my_dict[x], i]
        my_dict[element] = i
    return None

def juadge_index(slicing, index):
    output = []
    for i in slicing:
        if i >= index:
            i = i + 1 
            output.append(i)
        else:
            output.append(i)
    return output

def three_sum(nums, target):
    if not isinstance(nums, list) or not isinstance(target, int):
        return None
    for j in nums:
        if not isinstance(j, int):
            return None 
    my_dict = {}
    for i, element in enumerate(nums):
        x = target - element
        slicing = nums[:i] + nums[i+1:]
        result = two_sum(slicing, x)
        if result != None:
            result = juadge_index(result, i)
            result.append(i)
            return result
        my_dict[element] = i
    pass

if __name__ == "__main__":
    # nums = [2,7,11,15]
    # target = 8
    # print(two_sum(nums, target) == None)
    nums = [-1, 0, 1, 2, -1, -4]
    target = 0
    print(three_sum(nums, target))