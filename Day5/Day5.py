# -------------------------------------- #
# -------- Advent Of Code 2023 --------- #
# Day 5: If You Give A Seed A Fertilizer #
# -------------------------------------- #

## Helper functions
def parse_input():
    seeds, maps = [], []
    with open('./input', 'r') as file:
        for i, line in enumerate(file):

            # Retrieve first line for seeds
            if i == 0: seeds = [ int(number) for number in line[6:-1].split() ]

            # Start new map
            elif 'map' in line: maps.append([])
            
            # Append numbers on last map
            elif len(line) > 1:
                dest, source, _range = [int(number) for number in line.split()]
                maps[-1].append( Range(dest, source, _range) )

    maps = [Map(map_ranges) for map_ranges in maps]

    # Return the list of initial seeds and all the maps
    return seeds, maps

## Entities
class Map:
    def __init__(self, map_ranges):
        self.map_ranges = map_ranges

    def __getitem__(self, key):
        if isinstance(key, Range): return self.__getitem_for_range(key)
        for map_range in self.map_ranges:
            if key in map_range: return map_range[key]
        return key

    def __getitem_for_range(self, key_range):
        pass

    def __repr__(self): return repr(self.map_ranges)
        
class Range:
    def __init__(self, dest, source, _range):
        self.range = _range
        self.source = (source, source + _range)
        self.dest = (dest, dest + _range)

    def __contains__(self, key):
        return self.source[0] <= key & key < self.source[1]

    def __getitem__(self, key):

        # Map source -> dest ranges through this range map
        if isinstance(key, self.__class__): return self.__map_range(key) 

        if self.__contains__(key):
            diff = key - self.source[0]
            return self.dest[0] + diff
        raise KeyError(key)

    def __repr__(self):
        return '(' + str(self.source[0]) + ', ' + str(self.dest[0]) + ', ' + str(self.range) + ')'

    def __map_range(self, other_range):
        source0, source1 = other_range.source
        dest0, dest1 = other_range.dest
        _range = other_range.range

        # The whole range of destination values can be mappped using this range
        if dest0 in self and dest1 in self:
            return [ Range(self[dest0], source0, _range) ]

        # The destination range mapping breaks in two, the first subset being mapped
        if dest0 in self:
            offset = self.source[1] - dest0
            mapped_subrange = Range(self[dest0], source0, offset)
            non_mapped_subrange = Range(dest0 + offset, source0 + offset, _range - offset)
            return [ mapped_subrange, non_mapped_subrange ]

        # The destination range mapping breaks in two, the second subset being mapped
        if dest1 in self:
            offset = self.source[0] - dest0
            non_mapped_subrange = Range(dest0, source0, offset)
            mapped_subrange = Range(self[dest0 + offset], source0 + offset, _range - offset)
            return [non_mapped_subrange, mapped_subrange]

        # The ranges do not overlap, no mapping at all
        return other_range


## Main Program
if __name__ == "__main__":
	
    seeds, maps = parse_input()

    print('seeds')
    print(seeds)

    print('maps')
    print(maps[0])
    print(maps[-1])

    seed_locations = []
    for seed in seeds:
        source = seed
        print('\nTransforming seed:', seed)
        for map in maps:
            dest = map[source]
            print('\t', source, '==>', dest)
            source = dest
        print("Seed Location:", dest)
        seed_locations.append(dest)

    print('Lowest Location Number corresponding to any of the initial seeds:')
    print(min(seed_locations))