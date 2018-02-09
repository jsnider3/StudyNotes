'''
	Designed to solve https://www.hackerrank.com/challenges/saveprincess.
	@Author: Josh Snider
'''

def get_xy(grid, char):
	''' Find the x-y coordinates of a character
		in a square grid. '''
	x, y = None, None
	for idx in range(len(grid)):
		for idy in range(len(grid)):
			if grid[idx][idy] == char:
				x = idx
				y = idy
	return x, y

def displayPathtoPrincess(size, grid):
	start = get_xy(grid, 'm')
	end = get_xy(grid, 'p')
	sy, sx = start
	ey, ex = end
	xdiff = ex - sx
	ydiff = ey - sy
	while xdiff < 0:
		print("LEFT")
		xdiff += 1
	while xdiff > 0:
		print("RIGHT")
		xdiff -= 1
	while ydiff < 0:
		print("UP")
		ydiff += 1
	while ydiff > 0:
		print("DOWN")
		ydiff -= 1
	
def main():
	size = int(input(''))
	grid = []
	for _ in range(size):
		grid.append(list(input('')))
	displayPathtoPrincess(size, grid)
	#print(grid)

if __name__ == '__main__':
	main()