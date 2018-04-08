'''
	Creating for 2018 Google Code Jam Qualification Round.
	@author: Josh Snider
	@date: 2018/04/07
'''

def do_testcase():
	return [['TODO'] * 3] * 3

def main():
	num_tests = int(input())
	for n in range(num_tests):
		ans = do_testcase()
		print("Case #{0}:".format(n + 1))
		for row in ans:
			print(' '.join(row))
	
if __name__ == '__main__':
	main()