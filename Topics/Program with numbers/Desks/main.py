class_1 = abs(int(input()))
class_2 = abs(int(input()))
class_3 = abs(int(input()))

number_of_desks = 0

classes_list = [class_1, class_2, class_3]

for i in classes_list:
    if i % 2 == 0:
        number_of_desks += i / 2
    else:
        number_of_desks += (i + 1) / 2

print(int(number_of_desks))