'''
	Creating for 2018 Google Code Jam Qualification Round.
	@author: Josh Snider
	@date: 2018/04/07
'''

import sys

#test_file = open('sample_in_testing.txt', 'w')

def do_testcase():
	sz = int(input())
	#print(sz, file=test_file)
	[m, n] = [2, 2]
	print('{0} {1}'.format(m, n))
	prepared = set()
	[a, b] = get_two_ints()
	prepared.add((a,b))
	#print(str([a, b]), file=test_file)
	cnt = 0
	while [a, b] != [0,0] and [a, b] != [-1, -1] and cnt < 1000:
		print('{0} {1}'.format(m, n))
		[a, b] = get_two_ints()
		prepared.add((a,b))
		#print(str([a, b]), file=test_file)
		cnt = cnt + 1
		if has_all_neighbors(prepared, m, n):
			m += 3
	#print('DONE 23', file=test_file)
	#print(prepared, file=test_file)
	#test_file.flush()
	return [a, b]

		
def get_two_ints():
	resp = input()
	return [int(n) for n in resp.split(' ')]

def has_all_neighbors(prepared, x, y):
	return ((x,y) in prepared and (x-1,y) in prepared and (x+1,y) in prepared and
			(x,y-1) in prepared and (x-1,y-1) in prepared and (x+1,y-1) in prepared and
			(x,y+1) in prepared and (x-1,y+1) in prepared and (x+1,y+1) in prepared)
	
def main():
	num_tests = int(input())
	#print(num_tests, file=test_file)
	for _ in range(num_tests):
		ans = do_testcase()
		#print('DONE 35', file=test_file)
		if ans == [-1, -1]:
			break
		#print("Case #{0}: {1}".format(n + 1, ans))
	#test_file.close()
	
if __name__ == '__main__':
	main()