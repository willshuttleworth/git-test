size = int(input('enter array size: '))
nums = []
for i in range(1, size + 1):
	nums.append(i)
print(nums)

sum = 0
for i in nums:
	sum = sum  + i
print('sum:', sum)
print("did you know that this sum is equal to n(n+1)/2? (where n is the array size)")
name = input("enter first name:")
