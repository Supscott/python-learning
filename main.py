import random

def main():
    number = random.randint(1, 100)
    attempts = 0

    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        guess = input("Введи число: ")

        if not guess.isdigit():
            print("Введите именно число!")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Слишком маленькое.")
        elif guess > number:
            print("Слишком большое.")
        else:
            print(f"Угадал! Это {number}. Попыток: {attempts}")
            break

main()
