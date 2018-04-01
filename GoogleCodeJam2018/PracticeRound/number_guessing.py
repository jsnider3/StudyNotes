'''
	Solution to the number guessing problem of
	Google Code Jam Practice Session 2018.
	@author: Josh Snider
	@date: 3/31/2018
'''

def do_test():
	[low, high] = [int(s) for s in input().split(' ')]
	guesses = int(input())
	while True:
		guess = high
		if low + 1 == high:
			print(guess)
		else:
			guess = (high - low) // 2 + low
			print(guess)
		resp = input()
		if resp == 'CORRECT' or resp == 'WRONG_ANSWER':
			break
		elif resp == 'TOO_SMALL':
			low = guess
		elif resp == 'TOO_BIG':
			high = guess
			
	
def main():
	num_tests = int(input())
	for _ in range(num_tests):
		do_test()

if __name__ == '__main__':
	main()