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

my_car = vehicles['fiesta']                     # We use [] to retrieve a value
                                                # if the key don't match well receive an eerror
print(my_car)

computer = vehicles['virago']
print(computer)

# get method. We provide the key for the item we want
learner = vehicles.get("er5")                   # the key must match exactly, strings are case sensitive
                                                # If doesn't match, there will be no error, only none
print(learner)

#it looks like indexing but we use the key as the index rather than position.