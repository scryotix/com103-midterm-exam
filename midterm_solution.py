# --- 1. ASK FOR ROOM MONITOR NAME AND ROOM NUMBER ---
valid_monitor = False
while not valid_monitor:
    monitor_name = input("Room monitor name: ")
    if " " in monitor_name or monitor_name == "":
        print("Invalid input. Name cannot contain whitespace or be empty.")
    else:
        valid_monitor = True

valid_room = False
while not valid_room:
    room_num = input("Room number: ")
    if " " in room_num or room_num == "":
        print("Invalid input. Room number cannot contain whitespace or be empty.")
    elif room_num[0] == "-":
        print("Invalid input. Room number cannot be negative.")
    else:
        valid_room = True

# --- 2. PRINT DORM CHORE LIST ---
print("\n==========================================")
print("   DORM ROOM -- CHORE LIST")
print("==========================================")
print(" 1. Sweeping / Mopping    [Daily]")
print(" 2. Dishwashing           [After meals]")
print(" 3. Taking Out Trash      [Every other day]")
print(" 4. Cleaning Bathroom     [Weekly]")
print(" 5. Buying Groceries      [Weekly]")
print("==========================================\n")

chore_descriptions = [
    "", # padding for 1-based indexing
    "Sweeping / Mopping    [Daily]",
    "Dishwashing           [After meals]",
    "Taking Out Trash      [Every other day]",
    "Cleaning Bathroom     [Weekly]",
    "Buying Groceries      [Weekly]"
]

# --- 3 & 4. ASK FOR FOUR CHORE ASSIGNMENTS ---
assigned_nums = []
assigned_names = []
assigned_statuses = []
invalid_name_chars = [" ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", "|", "\\", ":", ";", '"', "'", "<", ">", ",", ".", "/", "?", "`", "~", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for i in range(1, 5):
    print(f"--- CHORE {i} ---")
    
    valid_chore = False
    while not valid_chore:
        c_num_str = input("Chore number (0 to skip): ")
        if c_num_str in ["0", "1", "2", "3", "4", "5"]:
            valid_chore = True
        else:
            print("Invalid chore number. Must be between 0 and 5.")
            
    if c_num_str == "0":
        print()
        continue
        
    c_num = int(c_num_str)
    
    valid_mate = False
    while not valid_mate:
        mate_name = input("Roommate name: ")
        if mate_name == "":
            print("Name cannot be empty.")
            continue
            
        has_symbol = False
        for char in invalid_name_chars:
            if char in mate_name:
                has_symbol = True
                
        if has_symbol:
            print("Invalid input. Name can only be letters, no whitespace or symbols.")
        else:
            valid_mate = True
            
    valid_status = False
    while not valid_status:
        status_in = input("Status (done/not done): ")
        if status_in in ["done", "not done"]:
            valid_status = True
        else:
            print("Invalid status. Must be 'done' or 'not done'.")
            
    assigned_nums.append(c_num)
    assigned_names.append(mate_name)
    assigned_statuses.append(status_in)
    print()

# --- 5. WEEKLY CHORE REPORT ---
print("=============================================")
print(f"     ROOM {room_num} -- WEEKLY CHORE REPORT")
print("=============================================")
print(f"Room Monitor : {monitor_name}")
print("---------------------------------------------")

total_assigned = 0
total_done = 0

for idx in range(len(assigned_nums)):
    total_assigned += 1
    c_num = assigned_nums[idx]
    c_name = assigned_names[idx]
    c_stat = assigned_statuses[idx]
    
    if c_stat == "done":
        total_done += 1
        
    print(f"[{total_assigned}] {chore_descriptions[c_num]}")
    print(f"    Roommate : {c_name}")
    print(f"    Status   : {c_stat}")
    print()

print("---------------------------------------------")
if total_assigned == 0:
    print("Completed      : 0 out of 0 assigned")
    print("Completion Rate: 0%")
    print("Room Status    : No chores assigned.")
else:
    completion_rate = int((total_done / total_assigned) * 100)
    print(f"Completed      : {total_done} out of {total_assigned} assigned")
    print(f"Completion Rate: {completion_rate}%")
    
    if completion_rate == 100:
        room_status = "Room is very clean!"
    elif completion_rate > 50:
        room_status = "Almost there!"
    elif completion_rate > 0:
        room_status = "Ongoing"
    else:
        room_status = "Needs work!"
        
    print(f"Room Status    : {room_status}")
print("=============================================")