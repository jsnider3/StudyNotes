'''
	@author: Josh Snider
'''

def expand(sol, i, j):
	rl = i
	rr = i + 1
	cl = j
	cr = j + 1
	# Expand left
	while cl > 0 and all(sol[r][cl - 1] == '?' for r in range(rl, rr)):
		cl -= 1
	# Expand up
	while rl > 0 and all(sol[rl - 1][c] == '?' for c in range(cl, cr)):
		rl -= 1
	# Expand right
	while cr < len(sol[0]) and all(sol[r][cr] == '?' for r in range(rl, rr)):
		cr += 1
	# Expand down
	while rr < len(sol) and all(sol[rr][c] == '?' for c in range(cl, cr)):
		rr += 1
	for c in range(cl, cr):
		for r in range(rl, rr):
			sol[r][c] = sol[i][j]

def solve(test_case):
	if not any('?' in row for row in test_case):
		return test_case
	sol = [list(l) for l in test_case]
	for i in range(len(test_case)):
		for j in range(len(test_case[0])):
			if test_case[i][j] != '?':
				#print("# TODO Expand {0} at {1},{2}".format(test_case[i][j], i, j))
				expand(sol, i, j)
	return sol

def read_input(fname):
	with open(fname) as f:
		lines = f.readlines()
		num_tests = int(lines[0])
		test_cases = []
		line = 1
		for _ in range(num_tests):
			[r, c] = [int(n) for n in lines[line].split(' ')]
			line += 1
			test_cases.append([list(line.strip('\n')) for line in lines[line:line+r]])
			line += r
		return test_cases

def main():
	test_cases = read_input('A-small-practice.in')
	cnt = 1
	for test_case in test_cases:
		print('Case #{0}:'.format(cnt))
		sol = solve(test_case)
		for row in sol:
			print(''.join(row))
		cnt += 1

if __name__ == '__main__':
	main()