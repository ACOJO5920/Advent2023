
def main(filename):
    with open(filename) as file:

        seeds = file.readline()[6:].strip().split()

        for line in file.readlines():

            line = line.split()

            if len(line) == 3:

                for ix in range(len(seeds)):
                    new_seed = Mapping(line[0], line[1], line[2]).get_destination(int(seeds[ix]))
                    if new_seed is not None:
                        seeds[ix] = new_seed

        for ix in range(len(seeds)):
            if ix == 0:
                smallest = seeds[ix]
            elif seeds[ix] < smallest:
                smallest = seeds[ix]

        return smallest







class Mapping:

    def __init__(self, destination_start, source_start, common_range):
        self.destination_start = int(destination_start)
        self.source_start = int(source_start)
        self.common_range = int(common_range)
        self.difference = self.source_start - self.destination_start

    def get_destination(self, source):
        if source < self.source_start or source > self.source_start + self.common_range:
            return None

        return source - self.difference
