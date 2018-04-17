def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])
    return sum%tablesize

"""Using a list of names, we go through and hash each one, giving it a slot in our table.
   Note that we get multiple names that are sent to the same slot and have some slots which are
   totally empty (2,3, and 7). This may seem odd, but it will still make searching much easier
   if we are just searching a slot with 2 items as opposed to a list of 7."""

familyNames = ["Rudi", "Tina", "James","Emily", "Wanda","Gary","Billie"]
tableSize = len(familyNames)
for item in familyNames:
    print(hash(item,tableSize))
    