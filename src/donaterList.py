from .donaterClass import cDonater


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
    