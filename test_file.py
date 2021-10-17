import random

## features and needs

# a deck of cards, a player,  a dealer hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A"]
player_hand = []
dealers_hand = []


## Deal the cards

# Dealers hand
while len(dealers_hand) != 2:
    dealers_hand.append(random.randint(1, 11))
    if len(dealers_hand) == 2:
        print("Dealer has X &", dealers_hand[1] )
# player_hand
while len(player_hand) != 2:
    player_hand.append(random.randint(1, 11))
    if len(player_hand) == 2:
        print("you have ", player_hand)


# add up the points in the hands
# first the dealer tota;
if sum(dealers_hand) == 21:
    print("Dealer has BlacKjack abd wins!!")
elif sum(dealers_hand) > 21:
    print("Dealer has over 21, Bust. You winn!!")

# now the player totals
while sum(player_hand) < 21:
    decision = str(input("Do you want to hit or stay? "))
    if decision =="hit":
        player_hand.append(random.randint(1, 11))
        print("you have a total of " + str(sum(player_hand)) + " from these cards ", player_hand)
    else:
        print("The dealer has a total of " + str(sum(dealers_hand)) + " with ", dealers_hand)
        print("you have a total of " + str(sum(player_hand)) + " from these cards ", player_hand)
        if sum(dealers_hand) > sum(player_hand):
            print("Dealer wins!!")
        else:
            print("You win!!")
        break

#