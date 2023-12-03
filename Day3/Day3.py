import string


def main(filename):
    with open(filename) as file:
        iy = 0
        items = []
        adjacent_locations = []
        for line in file.readlines():
            items.extend(get_nums(line, iy))
            adjacent_locations.extend(get_adjacent_locations(line, iy))
            iy += 1
    return calculate_sum(items, adjacent_locations)


def get_nums(line, iy):
    tracking_num = False
    items = []
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
            items.append(Item(int(super_value), super_locations))
            super_value = ""
            super_locations = []

    return items


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

    def get_data(self):
        return self.value

    def get(self):
        return self.value, self.locations
