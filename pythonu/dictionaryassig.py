my_vehicle={
    "model":"ford",
    "make":"explorer",
    "year": 2018,
    "mileage":40000
}
for x,y in my_vehicle.items():
    print(x,y)
vehicle2=my_vehicle.copy()
vehicle2["number_of_tires"]=4
vehicle2.pop("mileage")
for x,y in vehicle2.items():
    print(x,y)