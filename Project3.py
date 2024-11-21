#project 3

import calendar
from collections import defaultdict

class Schedule:
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
