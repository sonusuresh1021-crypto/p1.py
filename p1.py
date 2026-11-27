vehicle = input("Enter vehicle type: ") 
hours = int(input("Enter parking hours: ")) 
if vehicle == "two-wheeler":   
     fee = hours * 20 
elif vehicle == "four-wheeler":   
     fee = hours * 50 
elif vehicle == "heavy vehicle":  
      fee = hours * 100 
else:    fee = 0   
print("Invalid vehicle type")
print("Vehicle Type:", vehicle) 
print("Parking Hours:", hours)
print("Total Fee: Rs.", fee)