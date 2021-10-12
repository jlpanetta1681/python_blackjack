import random
from typing import no_type_check

values = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "Jack":10, "Queen":10, "King":10, "Ace":1}


class Card(object):
    def __init__(self, suit, val, rank):
        self.suit = suit
        self.rank = rank
        
    def show(self):
        print ("{} of {}".format(self.rank, self.suit))
    


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Hearts", "Spades", "Diamonds", "Clubs"]:
            for v in [2.3,3,4,5,6,7,8,9,10,"jack","Queen","King", "Ace"]:
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


class Player(object):
    def __init__(self, score):
        self.hand = []
        self.score = 0

    def draw(self, deck):
        self.hand.append(deck.drawCard())
    
    def showHand(self):
        for card in self.hand:
            card.show()  

    def discard(self):
        return self.hand.pop()


def deal(deck):
    hand = []
    for i in range(2):
        card = deck.pop()
        hand.append(card)
       
    print(deal(deck))