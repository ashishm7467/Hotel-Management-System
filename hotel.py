guest ={}
rooms = {
    101: {"type": "Single", "occupancy": 1, "price": 2000, "food": 500, "bed": 700, "status": "Available",
          "facilities": ["AC", "TV", "Wi-Fi"], "complimentary": ["Welcome Drink"]},
    102: {"type": "Single", "occupancy": 1, "price": 2000, "food": 500, "bed": 700, "status": "Available",
          "facilities": ["AC", "TV", "Wi-Fi"], "complimentary": ["Welcome Drink"]},
    103: {"type": "Double", "occupancy": 2, "price": 3000, "food": 700, "bed": 800, "status": "Available",
          "facilities": ["AC", "TV", "Wi-Fi", "Mini Fridge"], "complimentary": ["Breakfast"]},
    201: {"type": "Deluxe", "occupancy": 2, "price": 4500, "food": 900, "bed": 1000, "status": "Available",
          "facilities": ["AC", "TV", "Wi-Fi", "Mini Bar", "Mini Fridge"], "complimentary": ["Breakfast", "Welcome Drink"]},
    202: {"type": "Deluxe", "occupancy": 2, "price": 4500, "food": 900, "bed": 1000, "status": "Available",
          "facilities": ["AC", "TV", "Wi-Fi", "Mini Bar", "Mini Fridge"], "complimentary": ["Breakfast", "Welcome Drink"]},
    301: {"type": "Suite", "occupancy": 2, "price": 7000, "food": 1200, "bed": 0, "status": "Available",
          "facilities": ["AC", "Smart TV", "Wi-Fi", "King Bed"],
          "complimentary": ["Breakfast", "Room Decoration"]} 
}

def available_rooms():
    print("\n====== Available Rooms =======")
    for number, room in rooms.items():
        if rooms[number]["status"] == "Available":
            print("\nRoom:", number)
            print("Type:", room["type"])
            print("Occupancy:", room["occupancy"])
            print("Price:", room["price"], "Per night")
            print("Food charge:", room["food"], "Per day")
            print("Aminites:", room["facilities"])
            print("Complimentries:", room["complimentary"])
            
            
        if room["bed"] > 0:
            print("Extra beds available = ", room["bed"], "Per night")
        else:
            print("")
            print("\n", "-" * 50)
            
def room_details():
    print("\n====== Room Details =======")
    for number, room in rooms.items():
        print("\nRoom:", number)
        print("Type:", room["type"])
        print("Occupancy:", room["occupancy"])
        print("Price:", room["price"] , "Per night" )
        print("Food charge:", room["food"], "Per day")
        print("Aminites:", room["facilities"])
        print("Complimentries:", room["complimentary"])

        if room["bed"] > 0:
            print("Extra beds available = ", room["bed"],"Per night")

        else :
            print("")
        print("\n","-" * 50) 

def check_in():
    global Number_of_people
    Number_of_people = int(input("How many persons are accomodating in that room - "))

    if Number_of_people > 3:
        print("\nSorry we can accomodate just 3 people at max in a room.\nWe suggest you to book another room for the next person as per your comfort.")
        return
    
    print("")
    Name = str(input("Enter your name - "))
    Age = int(input("Enter your age - "))
    Phone = int(input("Enter your phone number - "))
    Email_id = str(input("Enter your mail id - "))
    Id_proof = str(input("Which id do you want to provide? - "))
    Id_number = str(input("Enter your id number - "))
    print("")
    Date_and_time = input("Entre the date(DD:MM:YY) and time(HR:MIN(am/pm)) of check in - ")
            
    
    
    print("----- CUSTOMER DETAILS -----")

    print(Name)
    print(Age)
    print(Phone)
    print(Email_id)
    print(Id_proof)
    print(Id_number)
    print(Date_and_time)

    room_details()
    
    number = int(input("\nEnter room number: "))
    
    if number not in rooms:
        print("Invalid room number.")
        return
    
    if rooms[number]["status"] == "Booked":
        print("Room is already booked.")
        return
    
    nights = int(input("Number of nights: "))
    room = rooms[number]

    
    food_cost = 0
    a_choice = input("Include food? (yes/no): ")
        
    if a_choice.lower() == "yes" :
        food_cost = room["food"] * nights
    
    extra = 0
    extra_choice = input("Extra bed? (yes/no): ")
    
    if extra_choice.lower() == "yes" and room["bed"] > 0:
        extra = room["bed"] * nights
    
    room_cost = room["price"] * nights
    total = room_cost + food_cost + extra
    
    guest[number] = {
        "name": Name,
        "age": Age,
        "phone": Phone,
        "email": Email_id,
        "id_proof": Id_proof,
        "id_number": Id_number,
        "type": room["type"],
        "nights": nights,
        "food": food_cost,
        "room_cost": room_cost,
        "food_cost": food_cost,
        "extra": extra,
        "total": total,
        "Date n time": Date_and_time
    }
    
    rooms[number]["status"] = "Booked"
    
    print("\nBooking successful!")
    print("Guest: ", Name)
    print("Room: ", number)
    print("Total: ₹", total)
    print("Date n time: ", Date_and_time)
    print("if you want to book another room, \nplease select option 3 from the main menu.")

def guest_details():
    number = int(input("\n Entre room number : "))

    if number in guest:
        customer = guest[number]
        
        print("*" * 5, " Guest details ", "*" * 5)
        print("")
        print("Room number : ", number )
        print("Room type : ",customer["type"])
        print("Nights : ", customer["nights"])
        print("Date n time: ", customer["Date n time"])
        print(" ")
        for i in range(1 , Number_of_people + 1):
            print("-" * 34)
            print("Guest name : ", customer["name"])
            print("Age : ", customer["age"])
            print("Phone : ", customer["phone"])
            print("Email ID : ", customer["email"])
            print("ID : ", customer["id_proof"], customer["id_number"])
            print("Food included : ", customer["food"])
            print("Extra bed : ", customer["extra"])
            print(" ")
        print("-" * 34)

    else:
            print("No guest found.")

def bill():
    number = int(input("\nEnter room number: "))

    if number not in guest:
        print("No booking found.")
        return

    customer = guest[number]

    print("\n", "*" * 7, " HOTEL BILL ", "*" * 7)
    print("Guest name : ", customer["name"])
    print("Room : ", number, " - ", customer["type"])
    print("Room Charges : ₹", customer["room_cost"])
    print("Food Charges : ₹", customer["food_cost"])
    print("Extra Bed : ₹", customer["extra"])
    print("-------------------------------")
    print("TOTAL: ₹", customer["total"])

def check_out():
    number = int(input("\nEntre room number : "))

    if number not in guest:
        print("No booking found.")
        return

    print("Guest : ", guest[number]["name"])
    print("Final Bill : ₹", guest[number]["total"])

    confirm = input("Confirm Checkout ? (yes/no) : ")
    if confirm.lower() == "yes":
        rooms[number]["status"] = "Available"
        del guest[number]
        print("Checkout succesful.")

    else:
        print("Checkout cancelled")

def Booked_rooms():
    print("\n====== Booked Rooms =======")

    for number, room in rooms.items():
        if rooms[number]["status"] == "Booked":
            print("\nRoom:", number)
            print("Type:", room["type"])
            return
        
        else:
            print("\nNo rooms are booked at the moment.")
            break

while True:

    print("\n","=" * 34 )
    print(" ","*" * 8, "VIT's Paradise", "*" * 8)
    print("","=" * 34 )
    print("   ","1. Available Rooms")
    print("   ","2. Room details")
    print("   ","3. Book room")
    print("   ","4. Guest Details")
    print("   ","5. Generate bill")
    print("   ","6. Check-out")
    print("   ","7. Booked rooms")
    print("   ","8. Exit")
    print("", "=" * 34 )

    choice = int(input("Entre your choice : "))
    if choice == 1:
        available_rooms()
    elif choice == 2:
        room_details()
    elif choice == 3:
        check_in()
    elif choice == 4:
        guest_details()
    elif choice == 5:
        bill()
    elif choice == 6:
        check_out()
    elif choice == 7:
            Booked_rooms()
    elif choice == 8:
        print("Thank you for visiting VIT's Paradise \n     ___***Visit Again***___")
    else:
        print("Invalid choice")

