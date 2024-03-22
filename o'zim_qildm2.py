# Bu dastur kvadratlar(x) chaqirilganda 0 dan x gacha bo'lgan
# kvadratlar ketma-ketligini generatsiya qiladi va shu kvadratlar
# ketma-ketligini ekranga chiqaradi.

def kvadratlar(top_limit):
    for i in range(top_limit):
        yield i ** 2


x = int(input("Enter a number: "))
# Generatorni chaqirish
generator = kvadratlar(x)

# Generatorni elementlarini o'qish
for element in generator:
    print(element)
