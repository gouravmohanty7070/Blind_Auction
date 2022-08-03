from replit import clear
import art

print(art.logo)
print("Welcome to the secret auction program.")

auction = {}

again = False

while again != True:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  auction[name] = bid

  yes_or_no = input("Are there any other bidders? Type 'yes' or 'no'.\n")

  if yes_or_no == 'no':
    again = True
    clear()
  else:
    clear()

maxBid = 0
maxName= ""

for name in auction:
  bid_amount = auction[name]
  if bid_amount > maxBid:
    maxBid = bid_amount
    maxName = name

print(f"The winner is {maxName} with a bid of ${maxBid}")
