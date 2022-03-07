name = input('enter your name: ')
age = int(input('how old are you? '))
print(name, 'is', age, 'years old')
nums = []
for i in range(10):
	nums.append(i)
print(nums)

sum = 0
for i in nums:
	sum = sum  + nums[i]
print('sum:', sum)
