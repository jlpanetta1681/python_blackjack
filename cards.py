import random

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

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    
    def draw(self):
        return self.cards.pop()


# deck = Deck()
# deck.shuffle()
# # deck.show()
# card = deck.draw()
# card.show()

class Player(object):
    def __init__(self):
        self.hand = []
    
    def draw(self, deck):
        self.hand.append(deck.drawCard())
    
    
    def showHand(self):
        for card in self.hand:
            card.show()    

