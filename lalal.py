import calendar
from collections import defaultdict

# Part 1: Caregiver Class
class Caregiver:
    def __init__(self, name, phone, email, pay_rate, hours):
        self.name = name
        self.phone = phone
        self.email = email
        self.pay_rate = pay_rate
        self.hours = hours
        self.availability = defaultdict(lambda: {"AM": "available", "PM": "available"})  # Default availability
    
    def update_availability(self, day, shift, status):
        """
        Update availability for a specific day and shift.
        Args:
            day (str): The day of the week (e.g., "Monday").
            shift (str): The shift ("AM" or "PM").
            status (str): The availability status ("preferred", "available", "unavailable").
        """
        if day in self.availability and shift in ["AM", "PM"]:
            self.availability[day][shift] = status


# Part 2: Pay Report Class
class PayReport:
    def __init__(self, caregivers):
        self.caregivers = caregivers

    def calculate_pay(self):
        """
        Calculate weekly pay for each caregiver.
        Returns:
            dict: A dictionary with caregiver names and their pay amounts.
        """
        weekly_pay = {}
        for caregiver in self.caregivers:
            weekly_pay[caregiver.name] = caregiver.hours * caregiver.pay_rate
        return weekly_pay

    def generate_report(self, filename="pay_report.txt"):
        """
        Generate a text-based pay report and save it to a file.
        Args:
            filename (str): The name of the file to save the report.
        """
        weekly_totals = self.calculate_pay()
        total_weekly_pay = sum(weekly_totals.values())
        total_monthly_pay = total_weekly_pay * 4  # Assuming 4 weeks in a month

        with open(filename, "w") as file:
            file.write("Caregiver Weekly Pay Report\n")
            file.write("=" * 30 + "\n")
            for name, pay in weekly_totals.items():
                file.write(f"{name}: ${pay:.2f}\n")
            file.write("\n")
            file.write(f"Total Weekly Pay: ${total_weekly_pay:.2f}\n")
            file.write(f"Total Monthly Pay: ${total_monthly_pay:.2f}\n")

        print(f"Pay report generated: {filename}")


# Part 3: Schedule Class
class Schedule:
    def __init__(self, caregivers):
        """
        Initialize the Schedule class with a list of caregivers.
        Args:
            caregivers (list): A list of Caregiver objects.
        """
        self.caregivers = caregivers
        self.schedule = defaultdict(lambda: {"AM": None, "PM": None})  # Default empty schedule

    def assign_shifts(self):
        """
        Assign caregivers to shifts based on their availability and preferences.
        """
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for day in days:
            # Assign caregivers to the AM shift
            for caregiver in sorted(self.caregivers, key=lambda c: c.availability[day]["AM"]):
                if caregiver.availability[day]["AM"] in ["preferred", "available"]:
                    self.schedule[day]["AM"] = caregiver.name
                    break

            # Assign caregivers to the PM shift
            for caregiver in sorted(self.caregivers, key=lambda c: c.availability[day]["PM"]):
                if caregiver.availability[day]["PM"] in ["preferred", "available"]:
                    self.schedule[day]["PM"] = caregiver.name
                    break

    def display_schedule(self):
        """
        Display the schedule for the week.
        """
        print("Caregiver Schedule")
        print("=" * 30)
        for day, shifts in self.schedule.items():
            print(f"{day}: AM - {shifts['AM']}, PM - {shifts['PM']}")
        print("=" * 30)

    def export_html_calendar(self, year, month):
        """
        Export the schedule as an HTML calendar.
        Args:
            year (int): The year for the calendar.
            month (int): The month for the calendar.
        """
        cal = calendar.HTMLCalendar()
        html_schedule = cal.formatmonth(year, month)

        # Replace the calendar cells with the schedule
        for day, shifts in self.schedule.items():
            day_index = list(calendar.day_name).index(day)
            html_schedule = html_schedule.replace(
                f"<td class=\"{calendar.day_abbr[day_index]}\">",
                f"<td>{day}: AM - {shifts['AM']}, PM - {shifts['PM']}"
            )

        with open("schedule.html", "w") as file:
            file.write(html_schedule)

        print("HTML schedule exported as 'schedule.html'.")


# Part 4: Main Function
def main():
    # Create caregivers
    caregivers = [
        Caregiver("Sara", "510-678-7756", "sara@gmail.com", 20, 36),
        Caregiver("Brian", "510-568-7906", "brian@gmail.com", 20, 48),
        Caregiver("Hana", "510-234-6700", "hana@gmail.com", 20, 30),
        Caregiver("John", "510-128-1670", "john@gmail.com", 20, 42),
        Caregiver("Liz", "510-688-7566", "liz@gmail.com", 0, 48),  # Family member (unpaid)
    ]

    # Update caregiver availability
    caregivers[0].update_availability("Monday", "AM", "preferred")
    caregivers[1].update_availability("Monday", "PM", "preferred")
    caregivers[2].update_availability("Tuesday", "AM", "preferred")
    caregivers[3].update_availability("Wednesday", "PM", "unavailable")

    # Create and assign schedule
    schedule = Schedule(caregivers)
    schedule.assign_shifts()
    schedule.display_schedule()

    # Export schedule as HTML calendar
    schedule.export_html_calendar(2024, 11)

    # Generate pay report
    pay_report = PayReport(caregivers)
    pay_report.generate_report()


if __name__ == "__main__":
    main()
