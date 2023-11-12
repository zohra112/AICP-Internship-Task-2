#Program to implement : A Ticketing System : Mountain Journey , An electric mountain railway
import datetime

journeys = {
    "09:00": {"up": {"seats": 80, "revenue": 0}},
    "10:00": {"down": {"seats": 80, "revenue": 0}},
    "11:00": {"up": {"seats": 80, "revenue": 0}},
    "12:00": {"down": {"seats": 80, "revenue": 0}},
    "13:00": {"up": {"seats": 80, "revenue": 0}},
    "14:00": {"down": {"seats": 80, "revenue": 0}},
    "15:00": {"up": {"seats": 80, "revenue": 0}},
    "16:00": {"down": {"seats": 80, "revenue": 0}}
}
#purchase tickets function
def purchase_tickets():
    journey_time = input("Enter the desired shift time (in HH:MM format): ")

    if journey_time not in journeys.keys():
        print("Invalid shift time.")
        return

    available_shifts = journeys[journey_time]
    shift = list(available_shifts.keys())[0]
    available_seats = available_shifts[shift]["seats"]

    num_passengers = int(input("Enter the number of passengers: "))

    if num_passengers > available_seats:
        print(f"Not enough seats available for the {shift} shift.")
        return

    price_per_ticket = 25
    total_price = num_passengers * price_per_ticket

    journey = journeys[journey_time][shift]
    journey["seats"] -= num_passengers
    journey["revenue"] += total_price

    print("Tickets purchased successfully.")
    print(f"Total amount paid: ${total_price}")

def display_available_shifts():
    print("Available shifts:")
    for journey_time, journey_shifts in journeys.items():
        for shift, shift_details in journey_shifts.items():
            seats_available = shift_details["seats"]
            print(f"{journey_time} ({shift.capitalize()}) : {seats_available} seats available")
#to show end of day report
def display_full_day_report():
    print("Full day report:")
    for journey_time, journey_shifts in journeys.items():
        for shift, shift_details in journey_shifts.items():
            seats_available = shift_details["seats"]
            revenue = shift_details["revenue"]
            print(f"{journey_time} ({shift.capitalize()})")
            print(f"Seats available: {seats_available}")
            print(f"Revenue generated: ${revenue}")
            print()

while True:
    print("Mountain Journey Ticketing System")
    print("---------------------------------")
    choice = input("Enter '1' to purchase tickets, '2' for full day report, or '3' to quit: ")

    if choice == '1':
        display_available_shifts()
        purchase_tickets()
    elif choice == '2':
        print("\nStart of Day")
        display_full_day_report()
    elif choice == '3':
        break
    else:
        print("Invalid choice.")
