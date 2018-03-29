'''
	Solution for Standing Ovation practice problem.
	@author: Josh Snider
'''

def read_input(fname):
	test_cases = []
	with open(fname) as f:
		lines = f.readlines()
		lines = lines[1:]
		for line in lines:
			line = line.strip('\n ')
			line = line.split(' ')[1]
			test_cases.append([int(d) for d in line])
	return test_cases

def solve(test_case):
	additions = 0
	standing = 0
	for ind in range(len(test_case)):
		if standing <= ind:
			additions += ind - standing
			standing = ind
		standing += test_case[ind]
	return additions

def main():
	test_cases = read_input('A-small-attempt0.in')
	cnt = 1
	for case in test_cases:
		people = solve(case)
		print('Case #{0}: {1}'.format(cnt, people))
		cnt += 1

if __name__ == '__main__':
	main()