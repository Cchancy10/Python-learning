ownerID = input ("Enter your owner ID:")
dog_name = input ("Enter your dog's name:")
breed = input ("Enter your dog's breed:")
age = int(input ("Enter your dog's age:"))
weight = int(input ("Enter your dog's weight:"))

if weight < 15:
    fee = 55
elif weight <= 30:
    fee = 75
elif weight <= 80:
    fee = 105
else:
    fee = 125
print ("--- Dog Daycare Bill ---")
print ("Owner ID:", ownerID)
print ("Dog's Name:", dog_name)
print ("Breed:", breed)
print ("Age:", age, 'years')
print ("Weight:", weight, "pounds")
print ("Daycare Fee: $", fee)