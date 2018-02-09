'''
	Designed to solve https://www.hackerrank.com/challenges/botclean.
	@Author: Josh Snider
'''

GRID_SIZE = 5

def find_all(grid, char):
	''' Find the (row, col) coordinates of all matching
		characters in a grid. '''
	matches = set([])
	for row in range(len(grid)):
		for col in range(len(grid)):
			if grid[row][col] == char:
				matches.add((row, col))
	return matches

def manhattan_distance(start, end):
	[x1, y1] = start
	[x2, y2] = end
	return (abs(x2 - x1) + abs(y1 - y2))

def move_to_clean(bot, spot):
	#print(bot, spot)
	br, bc = bot
	sr, sc = spot
	if br > sr:
		print("UP")
	elif br < sr:
		print("DOWN")
	elif bc < sc:
		print("RIGHT")
	elif bc > sc:
		print("LEFT")
	else:#		if bot == spot:
		print("CLEAN")

def next_move(posr, posc, board):
	messes = find_all(board, 'd')
	closest = list(sorted(messes, key=lambda x: manhattan_distance((posr, posc), x)))[0]
	move_to_clean((posr, posc), closest)
	
def main():
	pos = [int(i) for i in input().strip().split()]
	board = [[j for j in input().strip()] for i in range(GRID_SIZE)]
	next_move(pos[0], pos[1], board)
	
if __name__ == '__main__':
	main()