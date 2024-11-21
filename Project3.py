#project 3
# make change

class Caregiver: 
    def __init__(self, name, phone, email,pay_rate, hours):
        self.name = name
        self.phone = phone
        self.email = email 
        self.pay_rate = pay_rate
        self.hours = hours 
        self.availability = "available" #since this is the default 

    #Availability
    def availability(self):
        
        #availabity for both shifts
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
                print(f"\n{shift.capitalize()} Shift ({time})")
                status = input(f"Enter availability for {shift} shift ('preferred', 'available', or 'unavailable'): ").lower()
                
                if status in valid_status:
                    #update availability dictionary
                    self.availability[shift] = status
                    break
                else:
                    print("Invalid input. Please enter 'preferred', 'available', or 'unavailable'.")

        #display updated availability
        print("\nUpdated Availability:")
        for shift, status in self.availability.items():
            print(f"{shift.capitalize()} Shift: {status}")
        
        return self.availability


    # def availability(self, Caregiver, shift, status):
    #     self.shift = {"morning": "7AM-1PM", "afternoon": "1PM-7PM"}
    #     self.status = ["preferred", "available", "unavailable"]
        
    #     # Get availability for the morning shift
    #     morning_shift = input("Morning shift (7:00AM - 1:00PM): Enter 'preferred', 'available', or 'unavailable': ").lower()
    #     if morning_shift in status:
    #         return self.availability
        
    #     # Get availability for the afternoon shift
    #     afternoon_shift = input("Afternoon shift (1:00PM - 7:00PM): Enter 'preferred', 'available', or 'unavailable': ").lower()
    #     if afternoon_shift in status:
    #         print(status)


class Schedule(Caregiver):
    #make caregiver objects 
    caregivers = [
    Caregiver("Sara", "510-678-7756","sara@gmail.com", 20,36 ),
    Caregiver("Brian", "510-568-7906","brian@gmail.com",20, 48 ),
    Caregiver("Hana", "510-234-6700","hana@gmail.com",20, 36 ),
    Caregiver("John", "510-128-1670","john@gmail.com",20, 36 ),
    Caregiver("Sally", "510-999-9956","sally@gmail.com",20, 36 ),
    Caregiver("Stephen", "510-248-8421","stephen@gmail.com",20, 36 ),

#family members, unpaid 
    Caregiver("Sara", "510-678-7756","sara@gmail.com", 0,48 ),
    Caregiver("Liz", "510-688-7566","liz@gmail.com", 0,48 )]