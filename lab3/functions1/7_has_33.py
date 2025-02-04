def has_33(nums):
    return any(nums[i] == 3 and nums[i + 1] == 3 for i in range(len(nums) - 1))

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3]))  
