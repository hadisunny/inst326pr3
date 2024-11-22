import calendar
from collections import defaultdict

# caregiver class that has attributes such as name, phone, email, pay_rate, and hours
class Caregiver: 
    def __init__(self, name, phone, email, pay_rate, hours):
        self.name = name
        self.phone = phone
        self.email = email 
        self.pay_rate = pay_rate
        self.hours = hours
        self.availability = {
            "Morning": "Available",
            "Afternoon": "Available"  # default values
        }
    
    def weekly_pay(self):
        # calculate weekly pay based on hours and pay rate
        pay = self.hours * self.pay_rate
        return pay
    
    def avail(self):
        # Predefined shifts and status options
        shifts = {
            "Morning": "7AM-1PM",
            "Afternoon": "1PM-7PM"
        }
        avail_status = ["Preferred", "Available", "Unavailable"]

        print(f"\nSetting availability for {self.name}")

        # update availability for each shift
        for shift, time in shifts.items():
            while True:
                print(f"\n{shift} Shift ({time})")
                status = input(f"Enter availability for {shift} shift ('preferred', 'available', or 'unavailable'): ").lower()  # take input
                
                if status in avail_status:
                    # update availability dictionary
                    self.availability[shift] = status
                    break
                else:
                    print("Invalid input. Please enter 'preferred', 'available', or 'unavailable'.")

        # display updated availability
        print("\nUpdated Availability:")
        for shift, status in self.availability.items():
            print(f"{shift} Shift: {status}")

# create objects 
caregivers = [ 
    Caregiver("Sara", "510-678-7756", "sara@gmail.com", 20, 36),
    Caregiver("Brian", "510-568-7906", "brian@gmail.com", 20, 48),
    Caregiver("Hana", "510-234-6700", "hana@gmail.com", 20, 36),
    Caregiver("John", "510-128-1670", "john@gmail.com", 20, 36),
    Caregiver("Sally", "510-999-9956", "sally@gmail.com", 20, 36),
    Caregiver("Stephen", "510-248-8421", "stephen@gmail.com", 20, 36),

    # family members, unpaid 
    Caregiver("Alison", "510-678-7756", "alison@gmail.com", 0, 48),
    Caregiver("Liz", "510-688-7566", "liz@gmail.com", 0, 48)
]

# schedule class to assign shifts and generate reports
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
                # Find caregivers who are available, prioritize preferred
                available_caregivers = [
                    caregiver for caregiver in self.caregivers if caregiver.availability[shift] in ["preferred", "available"]
                ]
                
                preferred_caregivers = [caregiver for caregiver in available_caregivers if caregiver.availability[shift] == "preferred"]
                selected = preferred_caregivers[0] if preferred_caregivers else (available_caregivers[0] if available_caregivers else None)

                if selected:
                    # Select the first available caregiver (highest priority)
                    self.schedule[day][shift] = selected.name
                    selected.hours -= 6  # Deduct 6 hours after assigning a shift
    
    def make_calendar(self): 
        """Generate and save the schedule as an HTML file."""
        html_schedule = f"""
        <html>
        <head>
            <title>Work Schedule for {calendar.month_name[self.month]} {self.year}</title>
            <style>
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 20px 0;
                }}
                th, td {{
                    border: 1px solid black;
                    padding: 10px;
                    text-align: center;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
                td {{
                    height: 100px;
                    vertical-align: top;
                }}
            </style>
        </head>
        <body>
            <h1>Work Schedule for {calendar.month_name[self.month]} {self.year}</h1>
            <table>
                <tr>
                    <th>Mon</th>
                    <th>Tue</th>
                    <th>Wed</th>
                    <th>Thu</th>
                    <th>Fri</th>
                    <th>Sat</th>
                    <th>Sun</th>
                </tr>
        """

        # Get the first weekday of the month and the total days
        first_weekday, num_days = calendar.monthrange(self.year, self.month)

        # fill in days of the month
        current_day = 1
        for week in range((num_days + first_weekday) // 7 + 1):
            html_schedule += "<tr>"
            for day in range(7):
                if (week == 0 and day < first_weekday) or current_day > num_days:
                    html_schedule += "<td></td>"  # Empty cell for days outside the month
                else:
                    # add the day and the assigned shifts
                    shifts_for_day = self.schedule.get(current_day, {})
                    morning_shift = shifts_for_day.get("morning", "N/A")
                    afternoon_shift = shifts_for_day.get("afternoon", "N/A")

                    html_schedule += f"<td>{current_day}<br><b>AM:</b> {morning_shift}<br><b>PM:</b> {afternoon_shift}</td>"
                    current_day += 1
            html_schedule += "</tr>"

        # close html 
        html_schedule += """
            </table>
        </body>
        </html>
        """

        # write to file 
        with open(f"work_schedule_{self.year}_{self.month}.html", "w") as file:
            file.write(html_schedule)

        print(f"HTML work schedule for {calendar.month_name[self.month]} {self.year} generated successfully!")
    
    def pay_report(self):
        """Generate a pay report as a text file."""
        total_weekly_pay = 0 
        total_monthly_pay = 0
        report = "" 
        with open("pay_report.txt", "w") as f:
            for caregiver in self.caregivers:
                weekly_pay = caregiver.weekly_pay()
                total_weekly_pay += weekly_pay
                total_monthly_pay += weekly_pay
                report += f"{caregiver.name}: ${weekly_pay:.2f}\n"  # rounds to 2 decimals since it's money
            report += f"Total Weekly Pay: ${total_weekly_pay:.2f}\n"
            report += f"Total Monthly Pay: ${total_monthly_pay:.2f}\n"
            f.write(report)
        print("text file created")

# set availability for each caregiver
for caregiver in caregivers:
    caregiver.avail()

# display schedule, generate pay report 
year = 2024
month = 11
schedule = Schedule(year, month, caregivers)
schedule.assign_shifts()
schedule.make_calendar()
schedule.pay_report()
