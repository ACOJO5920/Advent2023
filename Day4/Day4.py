
def main(filename):
    with open(filename) as file:
        cards = []
        nums = []
        ix = 0
        for line in file.readlines():
            ix += 1
            card, num_line = line.split('|')
            cards.append(Card(ix, enumerate_card(card)))
            nums.append(enumerate_nums(num_line))

        total_score = 0
        for ix in range(len(cards)):
            card, num_set = cards[ix], nums[ix]
            card_numbers = card.get_numbers()
            print(card_numbers)
            score = 0
            for number in card_numbers:
                if number.isdigit():
                    if number in num_set and score == 0:
                        score = 1
                    elif number in num_set:
                        score *= 2
            total_score += score
    return total_score


def main_2(filename):
    with open(filename) as file:
        cards = []
        nums = []
        ix = 0
        for line in file.readlines():
            ix += 1
            card, num_line = line.split('|')
            cards.append(Card(ix, enumerate_card(card)))
            nums.append(enumerate_nums(num_line))

        total_score = 0
        for ix in range(len(cards)):
            card, num_set = cards[ix], nums[ix]
            card_numbers = card.get_numbers()
            print(card_numbers)

            won = True
            copy_cards = []
            while won:

                score = 0
                won = False
                for number in card_numbers:
                    if number.isdigit():
                        if number in num_set:
                            score += 1
                            won = True

                for x in range(score):
                    copy_cards.append(cards[x])

                print(copy_cards)



            total_score += score
    return total_score


def enumerate_nums(num_line):
    num_line = num_line.strip(' \n')
    num_set = num_line.split(' ')
    return num_set

def enumerate_card(card):
    card = card.split(':')[1]
    card = card.strip(' \n')
    card = card.split(' ')
    return card


class Card:

    def __init__(self, value, numbers):
        self.value = value
        self.numbers = numbers

    def get_numbers(self):
        return self.numbers