def is_even(number):
    return number % 2 == 0
a = int(input("какое число надо проверить? = "))
print("число четное" if is_even(a) else "число нечетное")