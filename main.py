from art import logo, vs
from game_data import data
import random
from replit import clear

# Select random item from the dictionary
def select_random_account():
  '''Get data from a random account'''
  return random.choice(data)
  
# Print the chosen item
def format_data(account):
  '''Format account into printable format: name, description and country'''
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

# Compare the followers
def compare_followers(guess, a_followers, b_followers):
  '''Checks followers against user's guess and returns True if they got it right pr,
      False if they got it wrong.'''
  if a_followers > b_followers:
    return guess == "A"
  else:
    return guess == "B"

def game():
  print(logo)
  score = 0
  game_continue = True
  
  a = select_random_account()
  b = select_random_account()
 
  while game_continue:
    a = b
    b = select_random_account()

    while a == b:
      b = select_random_account()

    print(f"⭐ Compare A: {format_data(a)}")
    print(vs)
    print(f"⭐ Compare B: {format_data(b)}")
    
    # Ask the user to choose
    guess = input("\nWho has more followers? Type 'A' or 'B': ")
    print(guess)
    
    a_followers = a['follower_count']
    b_followers = b['follower_count']
    is_correct = compare_followers(guess, a_followers, b_followers)
    
    clear()
    print(logo)
    if is_correct:
      score += 1
      print("-------------------------------------")
      print(f"You are right 😀. Current score is {score}.")
      print("-------------------------------------")
    else:
      game_continue = False
      print("---------------------------------------------")
      print(f"Oops! You got it wrong 😥. Final score is {score}.")
      print("---------------------------------------------")
  
game()
