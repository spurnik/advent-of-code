# ----------------------------- #
# ---- Advent Of Code 2023 ---- #
# --- Day 2: Cube Conundrum --- #
# ----------------------------- #

## Helper functions
def parse_input():
	input_data = []
	with open('./input.txt', 'r') as file:
		for line in file:
			input_data.append(line[:-1])
	return input_data

def parse_game_data(game_data):
	game = { 'id': -1, 'sets': [] }

	game_id_data, game_sets_data = game_data.split(':')
	game['id'] = int(game_id_data[5:])

	for game_set_data in game_sets_data.split(';'):
		game_set = { 'red': 0, 'green': 0, 'blue': 0 }

		for game_subset_data in game_set_data.split(','):
			for cube_type in ['red', 'green', 'blue']:
				if cube_type in game_subset_data:
					game_set[cube_type] = int(game_subset_data.split(cube_type)[0])

		game['sets'].append(game_set)

	return game

## Entities
class Game:
	def __init__(self, id, sets):
		self.id = id
		self.sets = []
		for set_of_cubes_data in sets:
			self.sets.append( SetOfCubes(**set_of_cubes_data) )

	def is_possible(self):
		for set_of_cubes in self.sets:
			if (
				set_of_cubes.red > 12 or 
				set_of_cubes.green > 13 or 
				set_of_cubes.blue > 14
			): return False
		return True
	
	def minimum_set(self):
		minimum_red = max(set_of_cubes.red for set_of_cubes in self.sets)
		minimum_green = max(set_of_cubes.green for set_of_cubes in self.sets)
		minimum_blue = max(set_of_cubes.blue for set_of_cubes in self.sets)
		return SetOfCubes(minimum_red, minimum_green, minimum_blue)

class SetOfCubes:
	def __init__(self, red, green, blue):
		self.red = red
		self.green = green
		self.blue = blue

	def power(self): 
		return self.red * self.green * self.blue

## Main Program
if __name__ == "__main__":
    
	games = []
	for game_data in parse_input():
		games.append( Game( **parse_game_data(game_data) ) )

	print("Sum of possible games IDs:")
	print(sum(game.id for game in games if game.is_possible()))

	print("Sum of minimum game set's powers")
	print(sum(game.minimum_set().power() for game in games))