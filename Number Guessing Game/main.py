from art import logo
import random

def intro():
	print("--------------------------------------------------------------------------------------")
	print(logo)
	print("--------------------------------------------------------------------------------------")
	print("Welcome to High/Low!")
	print("I am thinking of a number between 1 and 100...")


def guesses_remaining(guess_amount):
	if guess_amount < 1:
		return False
	return True

play = True

intro()
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

while difficulty != "easy" and difficulty != "hard":
	difficulty = input("Invalid input. Type 'easy' or 'hard': ")

if difficulty == "easy":
	guess_amount = 10
else:
	guess_amount = 5

random_num = random.randint(1, 100)

while play:
	if guess_amount == 1:
		print("This is your last chance to guess the number.")
	else:
		print(f"Print you have {guess_amount} attempts remaining to guess the number.")
	guess = int(input("Make a guess: "))
	if guess > random_num:
		print("Too high!")
		guess_amount -= 1
		if not guesses_remaining(guess_amount):
			print("Out of guesses, you lose!")
			break
	elif guess < random_num:
		print("Too low!")
		guess_amount -= 1
		if not guesses_remaining(guess_amount):
			print("Out of guesses, you lose!")
			break
	else:
		print("You win!")
		break
print(f"The number was {random_num}")		
print("--------------------------------------------------------------------------------------")
print("Thanks for playing!")