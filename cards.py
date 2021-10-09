print("Welcome to BlackJack")
# create the classes
class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
    def show(self):
        print ("{} of {}".format(self.val, self.suit))
    
card = Card("Spades", 9)
card.show()

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Hearts", "Spades", "Diamonds", "Clubs"]:
            for v in range(1, 14):
                self.cards.append(Card(s,v))
    
    def show(self):
        for c in self.cards:
            c.show()

deck = Deck()
deck.show()


class Player(object):
    def __init__(self):
        pass
