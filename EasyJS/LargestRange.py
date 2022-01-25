def largestRange(array):
    # Write your code here.
	best = []
	longest = 0
	nums = {}
	for num in array:
		nums[num] = True
	for num in array:
		if nums[num] != True:
			continue
		current = 1
		left = num -1
		right = num +1
		while right in nums:
			nums[right] = False
			right +=1
			current+=1
		while left in nums:
			nums[left] = False
			left -=1
			current+=1
		if current > longest:
			longest = current
			best = [left+1,right-1]
	return best
    
