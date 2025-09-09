# 2. Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who like to
# buy LP record albums. The store rents new videos for $3.00 a night, and oldies for $2.00 a
# night. Write a program that the clerks at Five Star Retro Video can use to calculate the total
# charge for a customer’s video rentals. The program should prompt the user for the number
# of each type of video and output the total cost.
def switch_case_option(opt):
    # Prices for VHS and DVDs
    PriceVHStapes = 3.00
    PriceDVDs = 2.00

    # VHS and DVD rental logic
    if opt == "1":
        VHStapes = int(input("How many VHS tapes do you want to rent? "))
        nighttorentforVHS = int(input("How many nights do you want to rent the VHS tapes? "))
        totalcostofVHSTapes = VHStapes * nighttorentforVHS * PriceVHStapes
        print("Total cost for VHS tapes: $", totalcostofVHSTapes)

    elif opt == "2":
        DVDs = int(input("How many DVDs do you want to rent? "))
        nighttorentforDVDs = int(input("How many nights do you want to rent the DVDs? "))
        totalcostofDVDs = DVDs * nighttorentforDVDs * PriceDVDs
        print("Total cost for DVDs: $", totalcostofDVDs)

    elif opt == "3":
        print("Logging out... Thank you for visiting Five Star Retro Video!")
        return
    else:
        print("Invalid option. Please select a valid option.")

def main():
    # Prompt the user for the initial option
    opt = input("What do you want to buy?\n1. VHS Tapes\n2. DVDs\n3. Log out\nEnter your choice: ")
    switch_case_option(opt)
main()
