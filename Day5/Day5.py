
def main(filename):
    with open(filename) as file:
        mapping = file.read().split('\n\n')[1:]

    with open(filename) as file:
        seeds = file.readline()[6:].strip().split()
        seeds = list(map(int, seeds))
        seeds = get_ends(seeds)

        blocks = mapping
        for block in blocks:
            ranges = []
            for line in block.splitlines()[1:]:
                ranges.append(list(map(int, line.split())))

            new_seeds = []
            while len(seeds) > 0:
                seed_start, seed_end = seeds.pop()
                for a, b, c in ranges:
                    overlap_start = max(seed_start, b)
                    overlap_end = min(seed_end, b + c)
                    if overlap_start < overlap_end:
                        new_seeds.append((overlap_start - b + a, overlap_end - b + a))
                        if overlap_start > seed_start:
                            seeds.append((seed_start, overlap_start))
                        if seed_end > overlap_end:
                            seeds.append((overlap_end, seed_end))
                        break
                else:
                    new_seeds.append((seed_start, seed_end))

            seeds = new_seeds

        return min(seeds)[0]


def get_ends(seeds):
    x = 0
    ranges = []
    while x < len(seeds)-1:
        start = seeds[x]
        end = seeds[x+1] + start
        ranges.append((start, end))
        x += 2
    return ranges
