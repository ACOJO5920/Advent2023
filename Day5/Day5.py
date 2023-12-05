
def main(filename):
    with open(filename) as file:
        seeds = file.readline()[6:].strip().split()
        for ix in range(len(seeds)):
            seeds[ix] = int(seeds[ix])

        smallest_location = None
        pairs = get_ends(seeds)
        mapping = get_maps()

        for pair in pairs:
            for x in range(pair[0], pair[1]):
                location = get_location(x, mapping)
                if smallest_location is None:
                    smallest_location = location
                elif location < smallest_location:
                    smallest_location = location
            print(smallest_location)

        return smallest_location


def get_ends(seeds):
    x = 0
    ranges = []
    while x < len(seeds)-1:
        start = seeds[x]
        end = seeds[x+1] + start
        ranges.append((start, end))
        x += 2
    return ranges


def get_maps():
    with open('Day5Input1.txt') as file:
        mapping = []
        for line in file.readlines():
            mapping.append(line)
    return mapping


def get_location(seed, mapping):
    seed_changed = False
    new_seed = seed
    for line in mapping:
        line = line.split()

        if len(line) == 3:
            if not seed_changed:
                new_seed = Mapping(line[0], line[1], line[2]).get_destination(int(seed))
                seed_changed = False if new_seed == seed else True
                seed = new_seed
        else:
            seed_changed = False
    return new_seed


class Mapping:

    def __init__(self, destination_start, source_start, common_range):
        self.destination_start = int(destination_start)
        self.source_start = int(source_start)
        self.common_range = int(common_range)
        self.difference = self.source_start - self.destination_start

    def get_destination(self, source):
        if source < self.source_start or source > self.source_start + self.common_range:
            return source

        return source - self.difference
