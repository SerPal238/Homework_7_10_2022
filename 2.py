a = int(input("Первый катет "))
b = int(input("Второй катет "))
с = int(input("Гипотенуза "))
if a ** 2 + b ** 2 == с ** 2:
    print( a + b + с, a * b / 2)
else:
    print("Введите корректные значения")