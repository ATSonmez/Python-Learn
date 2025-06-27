temp = 0
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is Hot outside")
    print("It is Sunny")
elif temp <= 0 and is_sunny:
    print("It is Cold outside")
    print("It is Sunny")
elif temp < 28 and temp > 0 and is_sunny:
    print("It is Warm outside")
    print("It is Sunny")
