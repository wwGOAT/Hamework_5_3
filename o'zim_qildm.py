# Generator funksiya
# Bu dastur sonlarni kubini hisoblaydi va 0 dan n gacha bo'lgan sonlar kublarini qaytaradi.


def kubi_soni(n):
    i = 0
    while i < n:
        yield i ** 3
        i += 1


n = int(input("Enter a number: "))
# Generator dan foydalanish
for son in kubi_soni(n):
    print(son)
