# -------------------------------------- #
# -------- Advent Of Code 2023 --------- #
# Day 5: If You Give A Seed A Fertilizer #
# -------------------------------------- #

## Helper functions
def parse_input():
    seeds, seeds_as_ranges, maps = [], [], []
    with open('./input', 'r') as file:
        for i, line in enumerate(file):

            # Retrieve first line for seeds
            if i == 0: 
                seeds = [ int(number) for number in line[6:-1].split() ]
                seeds_as_ranges = [ Range(seeds[i], seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

            # Start new map
            elif 'map' in line: maps.append([])
            
            # Append numbers on last map
            elif len(line) > 1:
                dest, source, _range = [int(number) for number in line.split()]
                maps[-1].append( Range(dest, source, _range) )

    maps = [Map(map_ranges) for map_ranges in maps]

    # Return the list of initial seeds and all the maps
    return seeds, seeds_as_ranges, maps

## Entities
class Map:
    def __init__(self, map_ranges):
        self.map_ranges = map_ranges

    def __getitem__(self, key):
        if isinstance(key, list) and len(key) > 0 and isinstance(key[0], Range): 
            return self.__getitem_for_ranges(key)
        if isinstance(key, Range): return self.__getitem_for_ranges([key])
        for map_range in self.map_ranges:
            if key in map_range: return map_range[key]
        return key

    def __getitem_for_ranges(self, initial_key_ranges):
        non_mapped_key_ranges = initial_key_ranges
        mapped_key_ranges = []

        for map_range in self.map_ranges:
            new_non_mapped_key_ranges = []
            for key_range in non_mapped_key_ranges:
                for result_range in map_range[ key_range ]:
                    if result_range.mapped: mapped_key_ranges.append( result_range )
                    else: new_non_mapped_key_ranges.append( result_range )

            # try mapping the non-mapped key ranges with the rest of iterations
            non_mapped_key_ranges = new_non_mapped_key_ranges

        # return all the mapped ranges and all the non-mapped ranges (defaultly self-mapped)
        return mapped_key_ranges + non_mapped_key_ranges

    def __repr__(self): return repr(self.map_ranges)
        
class Range:

    def __init__(self, dest, source, _range, mapped = False):
        self.range = _range
        self.source = (source, source + _range)
        self.dest = (dest, dest + _range)
        self.mapped = mapped

    def __eq__(self, __o: object):
        return ( 
            self.dest[0] == __o.dest[0] and 
            self.source[0] == __o.source[0] and
            self.range == __o.range 
        )

    def __contains__(self, key):

        # overlapping ranges
        if isinstance(key, self.__class__):
            return (
                key.dest[0] in self or 
                key.dest[1] - 1 in self or 
                key.dest[0] <= self.source[0] and self.source[1] < key.dest[1]
            )

        # single element
        return self.source[0] <= key & key < self.source[1]

    def __getitem__(self, key):

        # Map source -> dest ranges through this range map
        if isinstance(key, self.__class__): return self.__map_range(key) 

        if key in self:
            diff = key - self.source[0]
            return self.dest[0] + diff

        raise KeyError(f"Key {key} is not in {self}")

    def __repr__(self):
        return '(' + str(self.source[0]) + ', ' + str(self.dest[0]) + ', ' + str(self.range) + ', ' + str(self.mapped) + ')'

    def __map_range(self, other_range):
        source0, source1 = other_range.source
        dest0, dest1 = other_range.dest
        _range = other_range.range

        # The whole range of destination values can be mappped using this range
        if dest0 in self and dest1 - 1 in self:
            return [ Range(self[dest0], source0, _range, True) ]

        # The destination range mapping breaks in two, the first subset being mapped
        if dest0 in self:
            offset = self.source[1] - dest0
            mapped_subrange = Range(self[dest0], source0, offset, True)
            non_mapped_subrange = Range(dest0 + offset, source0 + offset, _range - offset, False)
            return [ mapped_subrange, non_mapped_subrange ]

        # The destination range mapping breaks in two, the second subset being mapped
        if dest1 - 1 in self:
            offset = self.source[0] - dest0
            non_mapped_subrange = Range(dest0, source0, offset, False)
            mapped_subrange = Range(self[dest0 + offset], source0 + offset, _range - offset, True)
            return [ non_mapped_subrange, mapped_subrange ]

        # The destination range mapping breaks in three, the middle subset being mapped
        if dest0 <= self.source[0] and self.source[1] < dest1:
            offset = self.source[0] - dest0
            left_non_mapped_subrange = Range(dest0, source0, offset, False)
            middle_mapped_subrange = Range(self[dest0 + offset], source0 + offset, self.range, True)
            right_non_mapped_subrange = Range(dest0 + offset + self.range, source0 + offset + self.range, _range - offset - self.range, False)
            return [ left_non_mapped_subrange, middle_mapped_subrange, right_non_mapped_subrange ]

        # The ranges do not overlap, return the original range as non-mapped
        return [ Range(dest0, source0, _range, False) ]

## Main Program
if __name__ == "__main__":
	
    seeds, seeds_as_ranges, maps = parse_input()

    print('seeds')
    print(seeds)

    print('\nseeds as ranges')
    print(seeds_as_ranges)

    print('\nmaps')
    print(maps[0])
    print(maps[-1])

    seed_locations = []
    for seed in seeds:
        source = seed
        print('\n\nTransforming seed:', seed)
        for map in maps:
            dest = map[source]
            print('\t', source, '==>', dest)
            source = dest
        print("\nSeed Location:", dest)
        seed_locations.append(dest)

    print('\n\nLowest Location Number corresponding to any of the initial seeds:')
    print(min(seed_locations))

    seed_location_ranges = []
    for seed_range in seeds_as_ranges:
        source_ranges = [ seed_range ]
        print('\n\nTransforming seed range:', seed_range)
        for map in maps:
            dest_ranges = map[source_ranges]
            print('\t', source_ranges, '==>', dest_ranges)
            source_ranges = dest_ranges
        print("\nSeed range locations:", dest_ranges)
        seed_location_ranges += dest_ranges

    sorted_seed_location_ranges = sorted(seed_location_ranges, key = lambda location: location.dest[0])
    print("\n\nFinal seed location ranges:")
    print(sorted_seed_location_ranges)

    print('\n\nLowest Location Number corresponding to any of the initial seeds (but this time, as ranges):')
    print(min(seed_location_ranges, key = lambda location: location.dest[0] ))
