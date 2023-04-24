numitems = int(input("Please enter the amount of items: "))

mylist = []

for i in range(numitems):
    num = int(input(f"Please enter integer {i+1}: "))
    mylist.append(num)

print("List: ", mylist)

mylist.insert(1, 99)
print("Updated list with 99 at position 1: ", mylist)

mylist[mylist.index(99)] = 100
print("Updated list with 100 instead of 99: ", mylist)

secondlist = [500, 600, 700, 800, 900]
print("Second list: ", secondlist)

mylist.extend(secondlist)
print("First list extended with second list: ", mylist)

mylist.remove(800)
print("First list with 800 removed: ", mylist)

del mylist[2]
print("First list with third item removed: ", mylist)

grades = ["A", "B", "C", "A", "A", "C"]

numgrades = grades.count("A")
print("Number of A grades: ", numgrades)

indexgrade = grades.index("B")
print("Index of first B grade: ", indexgrade)

if "F" not in grades:
    print("F is not in the list")

secondlist.clear()
print("Second list cleared: ", secondlist)

del secondlist

players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

players.sort()
print("Sorted list of players: ", players)

players2 = players.copy()
print("Copy of list of players: ", players2)

players2.reverse()
print("Reversed players2: ", players2)
print("Original players: ", players) 