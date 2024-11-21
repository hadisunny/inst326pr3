#project 3
# make change
import calendar
from collections import defaultdict

class Caregiver: 
    def __init__(self, name, phone, email,pay_rate, hours):
        self.name = name
        self.phone = phone
        self.email = email 
        self.pay_rate = pay_rate
        self.hours = hours 
    
    def weekly_pay(self):
        pay =  self.hours * self.pay_rate
        return pay


caregivers = [ Caregiver("Sara", "510-678-7756","sara@gmail.com", 20,36 ),
        Caregiver("Brian", "510-568-7906","brian@gmail.com",20, 48 ),
        Caregiver("Hana", "510-234-6700","hana@gmail.com",20, 36 ),
        Caregiver("John", "510-128-1670","john@gmail.com",20, 36 ),
        Caregiver("Sally", "510-999-9956","sally@gmail.com",20, 36 ),
        Caregiver("Stephen", "510-248-8421","stephen@gmail.com",20, 36 ),

    #family members, unpaid 
        Caregiver("Alison", "510-678-7756","alison@gmail.com", 0,48 ),
        Caregiver("Liz", "510-688-7566","liz@gmail.com", 0,48 )]



class Schedule:
    def __init__(self, year, month, caregivers):
        self.year = year
        self.month = month
        self.caregivers = caregivers  
        self.schedule = defaultdict(dict)  # Holds the schedule for each day
    
    def assign_shifts(self):
        """Assign shifts based on caregiver availability and hours."""
        num_days = calendar.monthrange(self.year, self.month)[1]  # Number of days in the month
        
        for day in range(1, num_days + 1):
            for shift in ["morning", "afternoon"]:
                # Find caregivers who are available and prioritize those with 'preferred' status
                available_caregivers = [
                    caregiver for caregiver in self.caregivers if caregiver.availability[shift] in ["preferred", "available"]
                ]
                
                # Sort caregivers by preference (those who are 'preferred' come first)
                available_caregivers.sort(key=lambda x: x.availability[shift] == "preferred", reverse=True)
                
                if available_caregivers:
                    # Select the first available caregiver (highest priority)
                    selected_caregiver = available_caregivers[0]
                    self.schedule[day][shift] = selected_caregiver.name
                    # Deduct 6 hours for the shift assigned
                    selected_caregiver.hours -= 6  # Deduct 6 hours after assigning a shift

    def display_schedule(self):
        """Print the schedule."""
        for day, shifts in self.schedule.items():
            print(f"Day {day}:")
            for shift, caregiver in shifts.items():
                print(f"  {shift}: {caregiver}")
        print()

    def generate_html_calendar(self):
        """Generate an HTML calendar with assigned shifts."""
        cal = calendar.HTMLCalendar()
        html_calendar = cal.formatmonth(self.year, self.month)
        
        # Add the shift assignments to the HTML calendar
        for day, shifts in self.schedule.items():
            for shift, caregiver in shifts.items():
                html_calendar = html_calendar.replace(
                    f">{day}<", 
                    f">{day}<br>{shift.capitalize()}: {caregiver}<br>"
                )
        return html_calendar
        self.availability = "available" #since this is the default 

    #Availability
    def availability(self):
        
        #default availabity for both shifts
        self.availability = {
            "morning": "available",
            "afternoon": "available"
        }
        
        #predefined shifts and status options
        shifts = {
            "morning": "7AM-1PM",
            "afternoon": "1PM-7PM"
        }
        valid_status = ["preferred", "available", "unavailable"]

        print(f"\nSetting availability for {self.name}")

        #update availability for each shift
        for shift, time in shifts.items():
            while True:
                print(f"\n{shift} Shift ({time})")
                status = input(f"Enter availability for {shift} shift ('preferred', 'available', or 'unavailable'): ").lower() #take input
                
                if status in valid_status:
                    #update availability dictionary
                    self.availability[shift] = status
                    break
                else:
                    print("Invalid input. Please enter 'preferred', 'available', or 'unavailable'.")

        #display updated availability
        print("\nUpdated Availability:")
        for shift, status in self.availability.items():
            print(f"{shift} Shift: {status}")
        
        return self.availability

