waiting_room = []


while True:
   name = input("Enter patient name (or 'done' if finished): ")
   if name == 'done':
    break
   waiting_room.append(name)

print(f"Total number of patients waiting: {len(waiting_room)}" )

for name in waiting_room:
    print(f"Calling: {name}")



