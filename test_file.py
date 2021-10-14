import random

## features and needs

# a deck of cards, a player,  a dealer hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A"]
player_hand = []
dealers_hand = []


## Deal the cards
while len(dealers_hand) != 2:
    dealers_hand.append(random.randint(1, 11))
    if len(dealers_hand) == 2:
        print("Dealer has X &", dealers_hand[1] )


# add up the points in the hands
# def total(turn):
#     total = 0
#     face = ["J", "Q", "K"]
#     for card in turn:
#         if card in range(1, 11):
#             total += card
#         elif card in face:
#             total += 1
#         else:
#             if total > 11:
#                 total += 1
#             else:
#                 total += 11



# put it all together to play the game