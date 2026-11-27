from fastapi import FastAPI

from src.Classes import donaterClass

gawab = FastAPI()

donater_list = donaterClass.donaterList()





@gawab.get("/")
def root():  
    return {"message": "Hello World"}



@gawab.post("/signup")
def create_donater(userID: str, name: str, email: str, phone: str, nationalID: str, address: str, password: str):
    donater = donaterClass.cDonater(userID, name, email, phone, nationalID, address, password)
    donater_list.add_donater(donater)
    return {"message": "Donater created successfully"}

@gawab.get("/donaters")
def get_donaters():
    return donater_list.get_donaters()
