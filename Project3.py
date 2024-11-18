#project 3

##requirements

#sun, mon, tues, wed, thurs, fri, sat
#shift 1 = 7am - 1pm
#shift 2 = 1pm - 7pm

#caregivers 
#name, phone, email, pay, hours

#calender
#pay calculator
#pay report with weekly and monthly totals 

import calendar
from datetime import datetime, timedelta

class Caregiver:
    def __init__(self, name, phone, email, pay_rate):
        self.name = name
        self.phone = phone
        self.email = email
        self.pay_rate = pay_rate
        self.availability = {'AM': 'available', 'PM': 'available'}
        self.hours = {'AM': 0, 'PM': 0}

    def set_availability(self, shift, status):
        self.availability[shift] = status

    def log_hours(self, shift, hours):
        self.hours[shift] += hours

    def calculate_pay(self):
        total_hours = sum(self.hours.values())
        return total_hours * self.pay_rate