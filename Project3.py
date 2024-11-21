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
