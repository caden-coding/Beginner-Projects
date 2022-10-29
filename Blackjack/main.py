# Program that allows the user to play blackjack vs a computer.
# Author:cadencoding

import random
from art import logo

def deal_card():
    random_num = random.randint(0, length - 1)
    card = cards[random_num]
    return card


def calculate_score(a_list):
    if 11 in a_list and 10 in a_list and len(a_list) == 2:
        score = 0
        return score
    if 11 in a_list:
        score = sum(a_list)
        if score > 21:
            a_list.remove(11)
            a_list.append(1)
            score = sum(a_list)
            return score
    return sum(a_list)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It is a draw"
    if user_score == 0:
        return "Blackjack! You win!"
    if computer_score == 0:
        return "Blackjack! The house wins!"
    if user_score > 21:
        return "You went over! The house wins!"
    if computer_score > 21:
        return "The house went over! You win!"
    if user_score > computer_score:
        return "You win!"
    if computer_score > user_score:
        return "You lost!"


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

length = len(cards)

play = True

while play:
    user_score = 0
    computer_score = 0
    user_cards = []
    computer_cards = []

    user_turn = True
    computer_turn = True

    user_bust = False

    print(logo)

    for i in range(0, 2):
        user_cards.append(deal_card())
    user_score = calculate_score(user_cards)
    computer_cards.append(deal_card())

    computer_score = calculate_score(computer_cards)

    if user_score == 0:
        print(f"Your cards: {user_cards}    Score: {user_score}")
        user_turn = False

    while user_turn:
        print(f"Your cards: {user_cards}    Score: {user_score}")
        print(f"Computer's first card: {computer_cards}\n")
        choice = input("Would you like another card? Type 'y' for yes or 'n' for no:").lower()
        print("---------------------------------------------------------------")
        while choice != 'y' and choice != 'n':
            choice = input("Invalid input, please try again: ")
        if choice == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            if user_score > 21:
                user_turn = False
                user_bust = True
        if choice == 'n':
            user_turn = False

    if not user_bust:
        while computer_turn:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

            if computer_score < 17:
                computer_turn = True
            else:
                computer_turn = False

    winner = compare(user_score, computer_score)
    print(f"Your final cards: {user_cards}     Score: {user_score}")
    print(f"Computer's final cards: {computer_cards}     Score: {computer_score}")
    print(winner)
    print("---------------------------------------------------------------")
    choice = input("Play again? Type 'y' or 'n': ").lower()
    while choice != 'y' and choice != 'n':
        choice = input("Invalid input, please try again: ")
    if choice == 'n':
        play = False
    print("---------------------------------------------------------------")
print("Thanks for playing!")
