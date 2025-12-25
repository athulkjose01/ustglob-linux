celsius = [0, 10, 25, 37, 100]

fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print(fahrenheit)
