import random
from art import logo
from art import vs
from game_data import data


play = True
correct_answers = 0
banner = ""


while play:
    dict1 = random.choice(data)
    dict2 = random.choice(data)

    while dict1 == dict2:
        dict2 = random.choice(data)

    print(logo)

    print(banner)
    print(f"Compare A: {dict1['name']}, a {dict1['description']} from {dict1['country']}")
    print(vs)
    print(f"Against B: {dict2['name']}, a {dict2['description']} from {dict2['country']}")

    if dict1['follower_count'] > dict2['follower_count']:
        answer = 'a'
    else:
        answer = 'b'

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    while guess != 'a' and guess != 'b':
        guess = input("Invalid input, please type 'A' or 'B': ")

    if guess == answer:
        correct_answers += 1
        banner = f"You're right! Current score: {correct_answers}"
    else:
        play = False
print(f"Sorry, that's wrong. Final score: {correct_answers}")

