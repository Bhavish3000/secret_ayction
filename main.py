"""_Secret Auction_
    """
from art import logo
from welcome import welcome
print(welcome)
print(logo)

def finding_highest_bid(bidding_record):
    """_checking the highest bidder to declare as a winner_

    Args:
        bidding_record (_dictionary_): _key = name $$ value = amount_
    """
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bid:
            highest_bid = bidding_record[bidder]
            winner= bidder
    print(f"The Winner is {winner} with a Bid of {highest_bid} $")
BIDDING_FINISHED = False
auction={}
while not BIDDING_FINISHED:
    Name = input("Please Enter your Name: ")
    Bid = int(input("Please Enter your Bidding Ammount $: "))
    auction[Name]= Bid
    SHOULD_CONTINUE = input("Are there any others bidders. TYPE yes (or) no: ")
    if SHOULD_CONTINUE == "no":
        BIDDING_FINISHED = True
        finding_highest_bid(auction)
    else:
        SHOULD_CONTINUE = "yes"
        print(auction)
        print("\n" *100)
        print(welcome)
        print(logo)
