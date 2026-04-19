room_monitor_name = input("Room monitor name: ")
room_number = input("Room number: ")
print("======================================")
print("DORM ROOM - CHORE LIST")
print("======================================")
chore_list=[["1.",  "Sweeping/Mopping ", "[Daily]"],
            ["2.",  "Dishwashing      ", "[After meals]"],
            ["3.",  "Taking out trash ", "[Every other day]"],
            ["4.",  "Cleaning bathroom", "[Weekly]"],
            ["5.",  "Buying groceries ", "[Weekly]"]]
for row in chore_list:
    for item in row:
        print(item, end=" ")
    print(" ")
print("======================================")
    
