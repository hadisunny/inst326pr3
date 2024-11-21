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
        self.availability = "available" #since this is the default 
    
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
        Caregiver("Alison", "510-678-7756","sara@gmail.com", 0,48 ),
        Caregiver("Liz", "510-688-7566","liz@gmail.com", 0,48 )]



class Schedule():
    def __init__(self, year, month, caregivers):
        self.year = year
        self.month = month
        self.caregivers = caregivers  
        self.schedule = defaultdict(dict) 

    def assign_shifts(self):
        """Assign shifts based on caregiver availability and hours."""
        num_days = calendar.monthrange(self.year, self.month)[1] 

        for day in range(1, num_days + 1):
            for shift in ["AM", "PM"]:
                # Find caregivers who are available
                available_caregivers = [
                    caregiver for caregiver in self.caregivers if caregiver.availability == "available"
                ]
                # Assign the first available caregiver (you can enhance this logic)
                if available_caregivers:
                    selected_caregiver = available_caregivers[0]  # Simple selection
                    self.schedule[day][shift] = selected_caregiver.name
                    # Decrease their hours to simulate working the shift
                    selected_caregiver.hours -= 6

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
        for day, shifts in self.schedule.items():
            for shift, caregiver in shifts.items():
                html_calendar = html_calendar.replace(
                    f">{day}<", 
                    f">{day}<br>{shift}: {caregiver}<br>"
                )
        return html_calendar