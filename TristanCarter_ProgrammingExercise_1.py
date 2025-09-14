#Tristan Carter
#This program will prompt users to buy tickets and tell them how many tickets are left. When sold out it will
#show number of customers.

#Function to get input
def get_tickets(available_tickets):
    while True:
        try:
            #Get user input
            tickets_request = int(
                input(f"Tickets remaining: {available_tickets}. How many tickets would you like to buy (MAX:4)? "))
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

    total_available = 20
    total_sold = 0
    total_customers = 0

    #Loop until all tickets are sold
    while total_sold < total_available:
        #Calculate available tickets
        remaining_tickets = total_available - total_sold

        #Get and validate the user's ticket request
        tickets = get_tickets(remaining_tickets)

        #Update accumulators
        total_sold += tickets
        total_customers += 1

        #Output remaining tickets after the purchase
        print(f"Thank you for your purchase. {total_available - total_sold} tickets left.")

    #Display the total number of customers
    print("\nTickets are sold out!")
    print(f"Total number of customers: {total_customers}")


#Run the application
if __name__ == "__main__":
    sell_tickets()