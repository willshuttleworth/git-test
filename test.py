size = int(input('enter array size'))
nums = []
for i in range(size):
	nums.append(i)
print(nums)

sum = 0
for i in nums:
	sum = sum  + nums[i]
print('sum:', sum)
