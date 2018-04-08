'''
	Creating for 2018 Google Code Jam Qualification Round.
	@author: Josh Snider
	@date: 2018/04/07
'''

def do_testcase():
	input()
	nums = [int(n) for n in input().split(' ')]
	nums = trouble_sort(nums)
	if is_sorted(nums):
		return 'OK'
	else:
		return first_unsorted_index(nums)

def first_unsorted_index(nums):
	''' Assumes nums is not sorted. '''
	for ind in range(len(nums) - 1):
		if nums[ind] > nums[ind + 1]:
			return ind

def is_sorted(nums):
	''' Let's do it the dumbest way possible because it's easier for me. '''
	return sorted(nums) == nums

def trouble_sort(nums):
	done = False
	while not done:
		done = True
		for i in range(len(nums) - 2):
			if nums[i] > nums[i+2]:
				done = False
				nums[i], nums[i+2] = nums[i+2], nums[i]
				#reverse the sublist from nums[i] to nums[i+2], inclusive
	return nums

def main():
	num_tests = int(input())
	for n in range(num_tests):
		ans = do_testcase()
		print("Case #{0}: {1}".format(n + 1, ans))
	
if __name__ == '__main__':
	main()