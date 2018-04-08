'''
	Creating for 2018 Google Code Jam Qualification Round.
	@author: Josh Snider
	@date: 2018/04/07
'''

def do_testcase():
	inp = input()
	#print(inp)
	[slimit, commands] = inp.split(' ')
	#print(slimit, commands)
	if commands.count('S') > int(slimit):
		return 'IMPOSSIBLE'
	else:
		swaps = 0
		while get_damage(commands) > int(slimit):
			commands = swap_commands(commands)
			swaps = swaps + 1 #'TODO'
			#break
		return str(swaps)

def get_damage(commands):
	tot = 0
	dam = 1
	for c in commands:
		if c == 'C':
			dam = dam * 2
		else:
			tot = tot + dam
	return tot

def swap_commands(commands):
	''' Find last CS and swap it. '''
	for ind in reversed(range(len(commands) - 1)):
		if commands[ind] == 'C' and commands[ind+1] == 'S':
			swapped = list(commands)
			swapped[ind], swapped[ind+1] = swapped[ind+1], swapped[ind]
			#print(swapped)
			return ''.join(swapped)
	return commands
	
def main():
	num_tests = int(input())
	#print(num_tests)
	for n in range(num_tests):
		swaps = do_testcase()
		print("Case #{0}: {1}".format(n + 1, swaps))
	
if __name__ == '__main__':
	main()