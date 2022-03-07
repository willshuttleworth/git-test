size = int(input('enter array size: '))
nums = []
for i in range(1, size + 1):
	nums.append(i)
print(nums)

sum = 0
for i in nums:
	sum = sum  + i
print('sum:', sum)
