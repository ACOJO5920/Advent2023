import string


def main(filename):
    with open(filename) as file:
        iy = 0
        nums = []
        adjacent_locations = []
        for line in file.readlines():
            nums.extend(get_items(line, iy)[0])
            adjacent_locations.extend(get_adjacent_locations(line, iy))
            iy += 1
    return calculate_sum(nums, adjacent_locations)


def main_2(filename):
    with open(filename) as file:
        iy = 0
        nums = []
        gears = []
        adjacent_locations = []
        for line in file.readlines():
            line_nums, line_gears = get_items(line, iy)
            nums.extend(line_nums)
            gears.extend(line_gears)
            adjacent_locations.extend(get_adjacent_locations(line, iy))
            iy += 1

    total_sum = 0
    for gear in gears:
        total_sum += calculate_gear_ratio(gear, nums)

    return total_sum


def get_items(line, iy):
    tracking_num = False
    gears = []
    nums = []
    super_value = ""
    super_locations = []
    for ix in range(len(line)):
        value = line[ix]
        if value.isdigit() and not tracking_num:
            super_value = value
            super_locations.append((ix, iy))
            tracking_num = True
        elif value.isdigit() and tracking_num:
            super_value += value
            super_locations.append((ix, iy))
        elif not value.isdigit() and tracking_num:
            tracking_num = False
            nums.append(Item(int(super_value), super_locations))
            super_value = ""
            super_locations = []
            if value == "*":
                gears.append((ix, iy))
        elif value == "*":
            gears.append((ix, iy))

    return nums, gears


def calculate_gear_ratio(gear, nums):
    ix, iy = gear
    adjacent_locations = [(ix - 1, iy - 1), (ix, iy - 1), (ix + 1, iy - 1), (ix - 1, iy), (ix + 1, iy),
                          (ix - 1, iy + 1), (ix, iy + 1), (ix + 1, iy + 1)]
    close_nums = 0
    total_sum = 1

    for num in nums:
        num_locations = num.get_locations()
        num_found = False
        for num_location in num_locations:
            if num_location in adjacent_locations and not num_found:
                total_sum *= num.get_data()
                num_found = True
                close_nums += 1

    if close_nums == 2:
        return total_sum

    return 0


def get_adjacent_locations(line, iy):
    adjacent_locations = []
    for ix in range(len(line)):
        value = line[ix]
        if value in string.punctuation and value != ".":
            adjacent_locations.append((ix-1, iy-1))
            adjacent_locations.append((ix, iy-1))
            adjacent_locations.append((ix+1, iy-1))
            adjacent_locations.append((ix-1, iy))
            adjacent_locations.append((ix+1, iy))
            adjacent_locations.append((ix-1, iy+1))
            adjacent_locations.append((ix, iy+1))
            adjacent_locations.append((ix+1, iy+1))
    return adjacent_locations


def calculate_sum(items, adjacent_locations):
    total_sum = 0
    for item in items:
        item_locations = item.get_locations()
        item_summed = False
        for item_location in item_locations:
            if item_location in adjacent_locations and not item_summed:
                total_sum += item.get_data()
                item_summed = True
    return total_sum


class Item:
    def __init__(self, value, locations):
        self.value = value
        self.locations = locations

    def get_locations(self):
        return self.locations

    def get(self):
        return self.value, self.locations
