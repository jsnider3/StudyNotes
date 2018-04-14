'''
	Creating for 2018 Google Code Jam Round 1A.
	@author: Josh Snider
	@date: 2018/04/13
'''

def do_testcase():
	[rows, cols, hcuts, vcuts] = [int(n) for n in input('').split(' ')]
	grid = []
	for _ in range(rows):
		grid.append(input(''))
	print(grid)
	return 'POSSIBLE'

def main():
	num_tests = int(input())
	for n in range(num_tests):
		ans = do_testcase()
		print("Case #{0}: {1}".format(n + 1, ans))
	
if __name__ == '__main__':
	main()
