class cDonater:
    def __init__(self, userID, name, email, phone, nationalID, address, password):
        self.userID = userID
        self.name = name
        self.email = email
        self.phone = phone
        self.nationalID = nationalID
        self.address = address
        self.password = password

    #getters
    def get_userID(self):
        return self.userID
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def get_phone(self):
        return self.phone
    def get_nationalID(self):
        return self.nationalID
    def get_address(self):
        return self.address
    def get_password(self):
        return self.password
    
    #setters
    def set_userID(self, userID):
        self.userID = userID
    def set_name(self, name):
        self.name = name
    def set_email(self, email):
        self.email = email    
    def set_phone(self, phone):
        self.phone = phone
    def set_nationalID(self, nationalID):
        self.nationalID = nationalID
    def set_address(self, address):
        self.address = address
    def set_password(self, password):
        self.password = password   
    
    
    def __str__(self): #string representation of the object
        return f"Donater(userID={self.userID}, name={self.name}, email={self.email}, phone={self.phone}, nationalID={self.nationalID}, address={self.address}, password={self.password})"
    
    
    def post(self): #initialize the post method
        pass
    

class donaterList:
    def __init__(self):
        self.donaters = []

    def add_donater(self, donater: cDonater):
        self.donaters.append(donater)
    
    def get_donaters(self):
        return self.donaters
    
    def remove_donater(self, donater: cDonater):
        self.donaters.remove(donater)
        
    def search_donater_by_id(self, userID):
        for donater in self.donaters:
            if donater.get_userID() == userID:
                return donater
        return None
        
        