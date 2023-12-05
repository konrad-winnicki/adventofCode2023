from functools import reduce

from read_file import read_file


class Card:
    def __init__(self, card_number, winning_numbers, user_numbers):
        self.card_number = card_number
        self.winning_numbers = winning_numbers
        self.user_numbers = user_numbers
        self.won_numbers = self.find_won_numbers()


    def find_won_numbers(self):
        set_of_winning_numbers = set(self.winning_numbers)
        set_of_user_numbers = set(self.user_numbers)
        won_numbers = set_of_winning_numbers.intersection(set_of_user_numbers)
        return list(won_numbers)





    def __str__(self):
        return 'ala'









data = read_file('test4-small.txt')

def prepare_cards(data):
    cards = []
    for row in data:
        card_name, numbers = row.split(':')
        card_number = int(card_name.split()[1])
        winning_numbers, user_numbers = numbers.split('|')
        cards.append(Card(card_number, winning_numbers.split(), user_numbers.split() ))

    return cards


class Node:
    def __init__(self, card: Card, cards):
        self.card = card
        self.cards = cards
        self.children = self.produce_children()

    def produce_children(self):
        won_count = len(self.card.won_numbers)
        if won_count == 0:
            return
        card_number = self.card.card_number
        following_card = card_number + 1
        children = []
        for index in range(following_card, following_card + won_count):
            children.append(Card(self.cards[index], self.cards[index].winning_numbers, self.cards[index].winning_numbers))
            return children





cards = prepare_cards(data)
print(cards)
suma = 0
nodes = []
for card in cards:
    nodes.append(Node(card, cards))

print(suma)

