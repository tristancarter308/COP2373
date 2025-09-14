#Tristan Carter
#This program will prompt users to buy tickets and tell them how many tickets are left. When sold out it will
#show number of customers.

#Function to get input
def get_tickets(available_tickets):
    while True:
        try:
            #Get user input
            tickets_request = int(
                input(f"There are {available_tickets} remaining. Enter how many tickets you would like? "))
            #Check if the number is within range (1-4)
            if 1 <= tickets_request <= 4:
                #Check if enough tickets are available for purchase
                if tickets_request <= available_tickets:
                    return tickets_request
                else:
                    print(f"There are only {available_tickets} tickets left.")
            else:
                print("You can only buy up to 4 tickets.")
        except ValueError:
            #Handles if input is not a number
            print("Invalid input. Please enter a number.")


#Function to handle the ticket sales
def sell_tickets():

    available_tickets = 10
    sold_tickets = 0
    customers = 0

    #Loop until all tickets are sold
    while sold_tickets < available_tickets:
        #Calculate available tickets
        remaining_tickets = available_tickets - sold_tickets

        #Get and validate the user's ticket request
        tickets = get_tickets(remaining_tickets)

        #Update accumulators
        sold_tickets += tickets
        customers += 1

        #Output remaining tickets after the purchase
        print(f"Thank you for your purchase. {available_tickets - sold_tickets} tickets left.")

    #Display the total number of customers
    print("\nTickets are sold out!")
    print(f"Total number of customers: {customers}")


#Run the application
if __name__ == "__main__":
    sell_tickets()