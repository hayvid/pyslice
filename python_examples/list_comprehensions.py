
values_list = []
for i in range (10):
    i_squared = i**2
    if i_squared < 20:
        values_list.append(i_squared)
print(values_list)


values_list = [i**2 for i in range(10) if i**2 < 20 ]
print(values_list)

