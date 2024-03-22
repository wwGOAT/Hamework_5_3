# Foydalanuvchidan generatsiya qilinadigan sonlar orasidagi oraliqni kiritish
# Ushbu dastur yuqoridagi funksiyalardan foydalanib foydalanuvchidan
# boshlang'ich va oxirgi sonlarni olib, ular orasidagi toq sonlarni
# ekranga chiqaradi.
def generate_numbers(start, end):
    for num in range(start, end + 1):
        yield num


# Berilgan sonlarning toqini generatsiya qilish
def filter_odd_numbers(numbers):
    for num in numbers:
        if num % 2 != 0:
            yield num

# Berilgan sonlarning toqini ko'rsatish


def main():
    start = int(input("Boshlang'ich sonni kiriting: "))
    end = int(input("Oxirgi sonni kiriting: "))

    numbers = generate_numbers(start, end)
    odd_numbers = filter_odd_numbers(numbers)

    print(f"{start} dan {end} gacha bo'lgan toq sonlar:")
    for num in odd_numbers:
        print(num)


if __name__ == "__main__":
    main()
