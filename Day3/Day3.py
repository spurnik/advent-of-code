# ----------------------------- #
# ---- Advent Of Code 2023 ---- #
# ---- Day 3: Gear Ratios  ---- #
# ----------------------------- #

import numpy as np

## Helper functions
def parse_input():
	input_data = []
	with open('./input.txt', 'r') as file:
		for line in file:
			input_data.append(list(line[:-1]))
	return np.array(input_data)

def get_row_numbers(arr):
	all_row_numbers = []
	for i in range(arr.shape[0]):

		# Get numbers in rows and their column index ranges (e.g. 401, (3, 5))
		this_row_numbers = []
		number, number_index_start, number_index_end = 0, None, None

		for j in range(arr.shape[1]):
			if arr[i, j].isdigit(): 
				number = number * 10 + int(arr[i, j])
				if number_index_start is None: number_index_start = j

			else: 
				if number_index_start is not None: 
					number_index_end = j - 1
					this_row_numbers.append((number, (number_index_start, number_index_end)))
					number, number_index_start, number_index_end = 0, None, None

		# edge number
		if number_index_start is not None: 
			number_index_end = j
			this_row_numbers.append((number, (number_index_start, number_index_end)))

		all_row_numbers.append(this_row_numbers)

	return all_row_numbers

def get_part_numbers(row_numbers, arr):
	part_numbers = []
	part_numbers_positions = []
	for i, row in enumerate(row_numbers):
		for row_number, j_range in row:
			neighbourhood = arr[max(i - 1, 0) : i + 2, max(j_range[0] - 1, 0): j_range[1] + 2]
			part_number_condition = np.any([char != '.' and not char.isdigit() for char in neighbourhood.ravel()])
			if part_number_condition: 
				part_numbers.append(row_number)
				part_numbers_positions.append((i, j_range))

	return part_numbers, part_numbers_positions

def get_gear_symbol_positions(arr):
	all_gear_symbol_positions = []
	for i in range(arr.shape[0]):
		for j in range(arr.shape[1]):
			if arr[i, j] == '*': all_gear_symbol_positions.append((i, j))
	return all_gear_symbol_positions

def get_gear_ratios(gear_symbol_positions, part_numbers, part_numbers_positions):
	gear_ratios = []
	for gear_i, gear_j in gear_symbol_positions:
		gear_part_count = 0
		gear_part_numbers = []
		for part_number, (i, j_range) in zip(part_numbers, part_numbers_positions):
			if (
				gear_i in range(max(i - 1, 0), i + 2) and 
				gear_j in range(max(j_range[0] - 1, 0), j_range[1] + 2)
			):	
				gear_part_count += 1
				gear_part_numbers.append(part_number)
		if gear_part_count == 2: gear_ratios.append(gear_part_numbers[0] * gear_part_numbers[1])
	return gear_ratios

## Main Program
if __name__ == "__main__":
	input_array = parse_input()
	row_numbers = get_row_numbers(input_array)
	part_numbers, part_numbers_positions = get_part_numbers(row_numbers, input_array)
	
	print("Sum of all engine schemation part numbers:")
	print(sum(part_numbers))

	gear_symbol_positions = get_gear_symbol_positions(input_array)
	gear_ratios = get_gear_ratios(gear_symbol_positions, part_numbers, part_numbers_positions)

	print("Sum of all gear ratios")
	print(sum(gear_ratios))