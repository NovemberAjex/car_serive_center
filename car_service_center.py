# file = open("Car_service",'x')
# file2 = open("car_oil_change","x")
# file3 = open("car_maintainence","x")
def car_serivce():
    car_name = input("Please enter the name of the car:  ")
    car_model = input("Please enter the model of the car:  ")
    car_in_time = input("Please enter the time in the for HH:MM  ")
    with open("car_service","a") as f:
        print(car_name,car_model,car_in_time,file =f)
        f.close()
def car_oil_change():
    car_name = input("Please enter the name of the car:  ")
    car_model = input("Please enter the model of the car:  ")
    car_oil_name = input("Please enter the name of the oil:  ")
    car_oil_quantity  =input("Please enter the oil quantity of the oil in liters:  ")
    car_oil_change_cost = int(input("Please enter the cost of the oil change:  "))
    car_in_time = input("Please enter the time in the form HH:MM  ")
    with open("car_oil_change","a") as f:
        print(car_name,car_model,car_oil_change_cost,car_in_time,car_oil_name,car_oil_quantity,file = f)
        f.close()
def car_tuning():
    car_name  = input("Please enter the name of the car:  ")
    car_model  = input("Please enter the model of the car:  ")
    car_in_time  = input("Please enter the car in time in the form HH:MM  ")
    car_parts_change = int(input("Please enter the parts that are change in the car:  "))
    car_parts_change_list = []
    for x in range(0,car_parts_change):
        car_parts_change_input = float(input("Please enter the price of every part:  "))
        car_parts_change_list.append(car_parts_change_input)
    for y in range(0,len(car_parts_change_list)):
        car_parts_change_total = car_parts_change_total+car_parts_change_list[y]
    with open("car_maintainence","a") as f:
        print(car_name, car_model, car_in_time, car_parts_change, car_parts_change_total, file =f)
        f.close()
user_function = int(input("""Please enter which function you want to choose  
press 1 to enter car service
press 2 to car oil change
press 3 to car tunning\n
"""))
if user_function==1:
    car_serivce()
elif user_function==2:
    car_oil_change()
elif user_function==3:
    car_tuning()
elif user_function>3:
    print("Plese try again")