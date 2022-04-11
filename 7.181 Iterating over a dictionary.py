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

# for key in vehicles:
#     print(key)
# # if we run this will print the key, so the iterating is done via key
# # if you want to values, you have decide to index dictionary
#
# for key in vehicles:
#     print(key, vehicles[key], sep=", ")         #we use a sep

for key, value in vehicles.items():             # we use enumerate when iterating over sequences and items over dictionaries
    print(key, value, sep=", ")