# Visszaadja az legnagyobb elemet a listából

# l = [1, 2, 4]

# print(max(l))

# Második legkisebb elem

# l = [1, 2, 3, 0, -5, -4]

# smallest = l[0]
# smallest_2 = l[1]

# if smallest > smallest_2:
#     smallest = l[1]
#     smallest_2 = l[0]

# for item in l[2:]:
#     if item < smallest:
#         smallest_2 = smallest
#         smallest = item
#     if smallest < item and item < smallest_2:
#         smallest_2 = item

# print(smallest_2)

# smallest = min(l)
# l.remove(smallest)
# smallest = min(l)

# print(smallest)

# Csináljon egy olyan listát amiben csak az 1x előforduló elemek vannak benne
# l1 = [0,1,1,1,1,2,3, 5, 10, 12, 11]
# l2 = [0,1,2,3,4, 7, 9, 9, 10]

# longer = l1
# smaller = l2
# if len(l1) < len(l2):
#     longer = l2
#     smaller = l1

# unique = []
# copy = longer[:]
# print(copy.extend(smaller))
# print(copy)
# for item in copy:
#     if item not in smaller:
#         longer.remove(item)
#         if item not in longer:
#             if item not in unique:
#                 unique.append(item)

# for item in smaller[:]:
#     if item not in longer:
#         smaller.remove(item)
#         if item not in smaller:
#             if item not in unique:
#                 unique.append(item)

# print(unique)

# Buborékos rendezés 1,3,4,5,6,2

list = [64, 34, 25, 12, 22, 11, 90]

for darab in range(len(list)):
    for index in range(len(list) - darab - 1):
        elobbi = list[index]
        utobbi = list[index + 1]
        if elobbi > utobbi:
            print(elobbi, ">", utobbi, "csere kell")
            list[index] = utobbi
            list[index + 1] = elobbi

print('Növekvőbe rendezve', list)

def csere(list, index):
    print(elobbi, "<", utobbi, "csere kell")
    list[index] = utobbi
    list[index + 1] = elobbi
    import random
    random.randint(1, 10)

for darab in range(len(list)):
    for index in range(len(list) - darab - 1):
        elobbi = list[index]
        utobbi = list[index + 1]
        if elobbi < utobbi:
            csere(list, index)

print(list)
