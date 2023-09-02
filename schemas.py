from pydantic import BaseModel

class Client(BaseModel):
    First_name: str 
    Middle_name: str
    Last_name: str
    Address: str
    Number: str

class Car(BaseModel):
    Car_mark: str
    Car_type: str
    Car_price: int
    Rental_price: int
    Is_Rented: bool = 'false'

class Lease(BaseModel):
    Car_id: int
    Client_id: int