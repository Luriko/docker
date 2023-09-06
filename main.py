from typing import Union
from schemas import *
from config import *
from fastapi import FastAPI
import psycopg2

app = FastAPI()

con = psycopg2.connect(dbname=DB_NAME, user=DB_USER,password=DB_PASS, host=DB_HOST)
cursor = con.cursor()

@app.post('/create_client')
def create_client(item: Client):
    cursor.execute(f"""INSERT INTO "public"."Clients"("First_name", "Middle_name", "Last_name", "Address", "Number") 
                    VALUES ('{item.Last_name}','{item.First_name}','{item.Middle_name}','{item.Address}','{item.Number}')""")
    con.commit()
    return "success"

@app.get('/get_all_clients')
def get_all_clients():
    cursor.execute(f""" SELECT * FROM "public"."Clients" """)
    fet = cursor.fetchall()
    output_List = []
    for client in fet:
        output_List.append({'id':client[0],'First_name':client[1],'Middle_name':client[2],'Last_name':client[3], 'Address':client[4],'Number':client[5]})
    return output_List

@app.post('/create_car')
def create_car(item: Car):
    cursor.execute(f"""INSERT INTO "public"."Cars"("Car_mark", "Car_type", "Car_price", "Rental_price", "IsRented") 
                    VALUES ('{item.Car_mark}','{item.Car_type}','{item.Car_price}','{item.Rental_price}','{item.Is_Rented}')""")
    con.commit()
    return "success"

@app.get('/get_all_cars')
def get_all_cars():
    cursor.execute(f""" SELECT * FROM "public"."Cars" """)
    fet = cursor.fetchall()
    output_List = []
    for car in fet:
        output_List.append({'id':car[0],'Car_mark':car[1],'Car_type':car[2],'Car_price':car[3], 'Rental_price':car[4],'IsRented':car[5]})
    return output_List

@app.post('/apply_lease')
def create_car(item: Lease):
    cursor.execute(f"""INSERT INTO "public"."Car_Client"("car_id", "client_id") 
                    VALUES ('{item.Car_id}','{item.Client_id}');
                    
                    UPDATE public."Cars"
                    SET "IsRented" = true
                    WHERE id = {item.Car_id}""")
    con.commit()
    return "success"

@app.get('/get_all_leases')
def get_all_cars():
    cursor.execute(f""" SELECT "Last_name","First_name","Middle_name","Car_mark","lease_date","lease_end"
                        FROM public."Car_Client" cc
                        LEFT JOIN public."Cars" cs ON cc.car_id = cs.id
                        LEFT JOIN public."Clients" cl ON cc.client_id = cl.id; """)
    fet = cursor.fetchall()
    output_List = []
    for Car_Client in fet:
        output_List.append({'Last_name':Car_Client[0],'First_name':Car_Client[1],'Middle_name':Car_Client[2], 'Car_mark':Car_Client[3],'lease_date':Car_Client[4],'lease_end':Car_Client[5]})
    return output_List

@app.patch("/Change_car_info_{id}")
def Change_info(item: Car,id):
    cursor.execute(f"""UPDATE public."Cars" 
                    SET "Car_mark" = '{item.Car_mark}', "Car_type" = '{item.Car_type}', "Car_price" = '{item.Car_price}', "Rental_price" = '{item.Rental_price}', "IsRented" = '{item.Is_Rented}'
                    WHERE id = {id}""")
    con.commit()
    return "success"

@app.patch("/Change_client_info_{id}")
def Change_info(item: Client,id):
    cursor.execute(f"""UPDATE "public"."Clients" 
                    SET "First_name" = '{item.First_name}', "Middle_name" = '{item.Middle_name}', "Last_name" = '{item.Last_name}', "Address" = '{item.Address}', "Number" = '{item.Number}'
                    WHERE id = {id}""")
    con.commit()
    return "success"