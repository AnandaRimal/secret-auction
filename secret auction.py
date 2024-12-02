import os

from art import logo

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)
bidding = True
bidding_list = {}

while bidding:
    name = input("Enter the name: ")
    bid = int(input("Enter the bid price: ₹"))
    bidding_list[name] = bid

    others = input("Type 'yes' if others are remaining for bids, or 'no' to end: ").lower()
    if others == "yes":
        clear_screen()
        print(logo)
    else:
        bidding = False

highest_bid = 0
winner = ""

for name in bidding_list:
    if bidding_list[name] > highest_bid:
        highest_bid = bidding_list[name]
        winner = name

clear_screen()
print("The auction is over!")
print(f"The highest bid is ₹{highest_bid}, and it was placed by {winner}.")
