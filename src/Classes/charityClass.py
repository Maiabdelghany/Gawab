class cCharity:
    def __init__(self, charityID, name, email, phone, address, description, password):
        self.charityID = charityID
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.description = description
        self.password = password

    # getters
    def get_charityID(self):
        return self.charityID

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_address(self):
        return self.address

    def get_description(self):
        return self.description

    def get_password(self):
        return self.password

    # setters
    def set_charityID(self, charityID):
        self.charityID = charityID

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_phone(self, phone):
        self.phone = phone

    def set_address(self, address):
        self.address = address

    def set_description(self, description):
        self.description = description

    def set_password(self, password):
        self.password = password

    def __str__(self):
        return f"Charity(charityID={self.charityID}, name={self.name}, email={self.email}, phone={self.phone}, address={self.address}, description={self.description})"


class charityList:
    def __init__(self):
        self.charities = []

    def add_charity(self, charity: cCharity):
        self.charities.append(charity)

    def get_charities(self):
        return self.charities

    def remove_charity(self, charity: cCharity):
        self.charities.remove(charity)

    def search_charity_by_id(self, charityID):
        for charity in self.charities:
            if charity.get_charityID() == charityID:
                return charity
        return None