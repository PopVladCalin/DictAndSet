vehicles = {                                    # We use {} to create a dic
    'dream': 'Honda 250T',                      # dream is a key, and what is after ":" is the value
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

# Dictionaries don't have an append method, we assign the value to the dictionary, using it's key
# we uesed starfighter as an index into the dic and assign the value to it
vehicles["starfighter"] = "Lock F-104"
vehicles["learjet"] = "Ler 101"
vehicles["toy"] = "glider"
for key, value in vehicles.items():             # we use enumerate when iterating over sequences and items over dictionaries
    print(key, value, sep=", ")