import random
from art import logo
from art import vs
from game_data import data
from replit import clear
def format_data(account):
  """formats the account data into a printable format"""
  account_name = account["name"]
  about_person = account["description"]
  home = account["country"]
  return (f"{account_name} ,a {about_person}, from {home}")

def check_answer(guess, a_followers, b_followers):
  """takes the user guess and follower counts and returns if they got it right"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess ==  "b"

print(logo)

score = 0 
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
  account_a = account_b
  account_b = random.choice(data)

  if account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()


  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  clear()
  print(logo)

  if is_correct:
    score +=1 
    print(f"you are right. your current score is {score}")
  else:
    game_should_continue = False
    print(f"sorry, that is wrong. Final score:{score}")
