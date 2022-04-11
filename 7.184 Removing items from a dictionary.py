vehicles = {                                    # We use {} to create a dic
    'dream': 'Honda 250T',                      # dream is a key, and what is after ":" is the value
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'BMW R11001',                   # doar asta va fi afisat dar pe pozitia 2, unde e prima data roadster, pentru ca un key isi pastreaza ordersul
}
#info: se patreaza locul de insertie in dictionare

# Dictionaries don't have an append method, we assign the value to the dictionary, using it's key
# we uesed starfighter as an index into the dic and assign the value to it
vehicles["starfighter"] = "Lock F-104"
vehicles["learjet"] = "Ler 101"
vehicles["toy"] = "glider"

# upgrade virago
# the keys are unique, if you change a key will change the value
vehicles["virago"] = "yamaha xv535"             # isi pastreaza pozitia

#2 variants of delling from a dic

del vehicles["starfighter"]
# del vehicles["f1"]                             # If the key doesn't exist will crash the program

result = vehicles.pop("f1", None)                # pop method removes the key from a dictionary and returns the value
print(result)                                    # the program won't crash because fi has the value None


result = vehicles.pop("f1", "You wish!")
print(result)
plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "not present")     #Here is displayed the value from dic, because it exist
                                                # the default value is only returned when the key doesn't exist in the dic
print(bike)
print()

for key, value in vehicles.items():              # we use enumerate when iterating over sequences and items over dictionaries
    print(key, value, sep=", ")