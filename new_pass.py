import random

letters = "qwertyuiopasdfghjklzxcvbnm"
Letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
sumbols = "!@#$%^&*()"
numbers = "1234567890"
entry = (input("Введите число - длину нового пароля (минимум 8 символов)\n"))
if entry.isdigit() == False or int(entry) < 8:
    entry = input("Ошибка ввода, попробуйте еще раз")
else:
    entry = int(entry)
    password = random.sample(letters, entry//4) + random.sample(Letters, entry//4) + random.sample(sumbols, entry//4) + random.sample(
    numbers, entry - entry//4 * 3)
    random.shuffle(password)
    new_password = "".join(password)
print(new_password)
print(entry - entry//4 *4 )