inventory = {
    'gold' : [500],
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

#Adding pocket as a key and values of it
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

#Sorting the values under backpack key
inventory['backpack'].sort()

#Remove dagger from the backpack key
inventory['backpack'].remove('dagger')

#Adding 50 under the gold key
inventory['gold'].append(50)


