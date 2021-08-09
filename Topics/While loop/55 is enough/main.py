number = 0
counter = 0
sum_of_numbers = 0
average = 0.0

while number != 55:
    sum_of_numbers += number
    counter += 1
    average = sum_of_numbers / counter
    number = int(input())
print(counter - 1)
print(sum_of_numbers)
print(round(average))
