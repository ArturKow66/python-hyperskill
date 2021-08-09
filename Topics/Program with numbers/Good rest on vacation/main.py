duration = int(input())
daily_food = int(input())
one_way_flight = int(input())
accommodation = int(input())

print(daily_food * duration + one_way_flight * 2 + accommodation * (duration - 1))
