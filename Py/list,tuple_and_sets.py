# List, Tuple and sets

# l = ['bob', 'rolf', 'anne'] # (List) Changable 
# t = ('bob', 'rolf', 'anne') # (Tuples) It can not be changable and replacable and values can not be added
# s = {'bob', 'rolf', 'anne'} # (Set) In set values can not be replaced, but new values can be added using "add" function and will allow only unique values and also it is unordered

# l.append("smith")  # will add the values to the list
# l.remove("bob") # will remove the values from the list
# s.add('an') # to add a value to the set
# print(s)

# Advance set operations

# friends = {"Bob", "Rof", "Anne"}
# abroad = {"Bob", "Anne"}
# local = {"Rolf"}

# local_friends = friends.difference(abroad)
# local_friends1 = abroad.difference(friends)
# frnds = local.union(abroad)
# print(local_friends)
# print(local_friends1)
# print(frnds)

# art = {"Bob", "Jen", "Rolf", "Charlie"}
# science = {"Bob", "Jen", "Adam", "Anne"}

# both = art.intersection(science)
# print(both)