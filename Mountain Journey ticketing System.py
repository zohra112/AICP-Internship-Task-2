#Program to implement : A Ticketing System : Mountain Journey , An electric mountain railway

import datetime

# Task1: Start of the day
journeys = {
    "09:00": {"up": 0, "down": 0, "revenue": 0},
    "11:00": {"up": 0, "down": 0, "revenue": 0},
    "13:00": {"up": 0, "down": 0, "revenue": 0},
    "15:00": {"up": 0, "down": 0, "revenue": 0}
}

# Task2: Purchasing tickets
def purchase_tickets():
    journey_time = input("Enter the journey time (in HH:MM format): ")
    num_passengers = int(input("Enter the number of passengers: "))
    
    #this chunk will check if the journey time is valid
    if journey_time not in journeys.keys():
        print("Invalid journey time.")
        return
    
    journey = journeys[journey_time]
    
    # To check if there are enough tickets available
    if num_passengers * 2 > 80 * 6:
        print("Not enough seats available.")
        return
    
    # To calculate the total price including group discount
    price_per_ticket = 25
    total_price = num_passengers * price_per_ticket
    
    if num_passengers >= 10 and num_passengers <= 80:
        free_tickets = num_passengers // 10
        total_price -= free_tickets * price_per_ticket
    
    # to update the screen display and the data for the totals
    journey["up"] += num_passengers
    journey["revenue"] += total_price
    
    print("Tickets purchased successfully.")
    print(f"Total amount paid: ${total_price}")

# Task3: End of the day report
def end_of_day():
    total_passengers = 0
    total_revenue = 0
    max_passengers = 0
    max_journey_time = ""
    
    print("End of the day report:")
    
    for journey_time, journey in journeys.items():
        total_passengers += journey["up"]
        total_revenue += journey["revenue"]
        
        print("Journey Time:", journey_time)
        print("Passengers:", journey["up"])
        print("Revenue collected:", journey["revenue"])
        print("---------------------------------")
        
        if journey["up"] > max_passengers:
            max_passengers = journey["up"]
            max_journey_time = journey_time
    
    print("Total passengers for the day:", total_passengers)
    print("Total revenue collected for the day: $", total_revenue)
    print("Journey with the most passengers:", max_journey_time, "with", max_passengers, "passengers.")

# Main 
print("Start of the day.")

print("Journey times:")
for journey_time in journeys.keys():
    print(journey_time)

while True:
    choice = input("Enter '1' to purchase tickets, '2' to end day, or 'q' to quit: ")
    
    if choice == '1':
        purchase_tickets()
    elif choice == '2':
        end_of_day()
        break
    elif choice.lower() == 'q':
        break
    else:
        print("Invalid choice.")
