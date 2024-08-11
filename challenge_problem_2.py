# CHALLENGE PROBLEM 2
# SORTING AN ARRAY

# You have an array of maximum size of 100 with DISTINCT integers. 
# Write a algorithm and produce a flow chart that sorts this array from smallest to largest. 

# EXAMPLE:
# [1, 4, 5, 66, 3, 84, 11, 198] 
# SORTED:
# [1, 3, 4, 5, 11, 66, 84, 198]

nums = [ 1, 4, 1, 5, 66, 3, 84, 11, 198]
nums = list(set(nums))
print(f"The unordered list of distinct numbers is {nums}.")
n = len(nums)
for i in range (n -1):
	for j in range (n - i - 1):
		if nums[j] > nums[j+1]:
			nums[j], nums[j+1] = nums[j+1], nums[j]
print(f"The sorted list of distinct numbers is {nums}.")

