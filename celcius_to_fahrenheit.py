celsius_temperatures = [25, 30, 15, 10, 20]
def fahrenheit(i):
    return i*(9/5)+32
a=list(map(fahrenheit,celsius_temperatures))
print(a)
