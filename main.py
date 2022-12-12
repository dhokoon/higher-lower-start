from art import logo
from game_data import data
import random

def format_data(account):
  """Format the account data into a printable format."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"
  
#Display art
print(logo)

#Generate a random account from the game data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
  account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}")
print(f"Compare B: {format_data(account_b)}")

#Ask user for a guess

#Check if user is correct

#Get follwe account of each account
#User if statement to check if user is correct

#Give user feedback on their guess

#Track score

#Make the game repeatable

#Making account at position B becime the next account at position A

#Clear the screen between rounds

