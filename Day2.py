def main():
    with open('Day2Input1.txt') as file:
        bag = {"red": 12, "green": 13, "blue": 14}
        id_sum = 0
        for game in file:
            invalid = False
            game_id, bundles = clean_game(game)

            for bundle in bundles:
                colour_values = count_colours(bundle)
                if check_if_invalid(colour_values, bag):
                    invalid = True

            if not invalid:
                id_sum += game_id

    return id_sum


def clean_game(game):
    game = game.replace('\n', '')
    sets = game.split(';')
    game_id = sets[0].split(':')[0].split(' ')[1]
    sets.insert(0, sets[0].split(':')[1])
    sets.remove(sets[1])
    return int(game_id), sets


def count_colours(bundle):
    colours = bundle.split(',')
    colour_values = {"red": 0, "green": 0, "blue": 0}
    for colour in colours:
        colour = colour.strip()
        colour = colour.split(' ')

        num = colour[0]
        value = colour[1]
        colour_values[value] = int(num)

    return colour_values


def check_if_invalid(colour_values, bag):
    for colour in colour_values.keys():
        if colour_values[colour] > bag[colour]:
            return True

    return False
