# ----------------------------- #
# ---- Advent Of Code 2023 ---- #
# ---- Day 4: Scratchcards ---- #
# ----------------------------- #

## Helper functions
def parse_input():
	input_data = []
	with open('./input', 'r') as file:
		for line in file:
			input_data.append(line[:-1])
	return input_data

def parse_card(card_data):
    card = { 'id': None, 'winning_numbers': [], 'card_numbers': [] }
    card_id_data, card_lists_data = card_data.split(':')
    card['id'] = int(card_id_data[5:])

    card_winning_numbers_data, card_numbers_data = card_lists_data.split('|')
    card['winning_numbers'] = [ int(chars) for chars in card_winning_numbers_data.split(' ') if chars]
    card['card_numbers'] = [ int(chars) for chars in card_numbers_data.split(' ') if chars]
    return card

## Entities
class ScrathCard:
	def __init__(self, id, winning_numbers, card_numbers):
		self.id = id
		self.winning_numbers = winning_numbers
		self.card_numbers = card_numbers

	def matches(self):
		return len([x for x in self.card_numbers if x in self.winning_numbers])

	def worth_points(self):
		matches = self.matches()
		if not matches: return 0
		return 2**(matches - 1)

class OriginalDeck:
    def __init__(self, original_cards):
        self.scratchcards = { card.id : (card, 1) for card in original_cards }

    def count_repeats(self):
        # Iteratively count how many repeats do you have!
        for id in self.scratchcards.keys():
            card, repeats = self.scratchcards[id]
            for i in range(card.matches()):
                next_card, next_card_repeats = self.scratchcards[id + i + 1]
                self.scratchcards[id + i + 1] = (next_card, next_card_repeats + repeats)
        return sum(repeats for _, repeats in self.scratchcards.values())
    
## Main Program
if __name__ == "__main__":
    
	scratchcards = []
	for card_data in parse_input():
		scratchcards.append( ScrathCard( **parse_card(card_data) ) )
        
	print("Sum of all cards worth points:")
	print(sum(card.worth_points() for card in scratchcards))

	my_deck = OriginalDeck( scratchcards )

	print("Total number of scratchcards:")
	print(my_deck.count_repeats())
