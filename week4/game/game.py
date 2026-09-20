import random

def main():
    # دریافت سطح بازی از کاربر و اطمینان از مثبت بودن آن
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            pass

    # انتخاب یک عدد تصادفی بین ۱ تا سطح انتخاب شده
    number = random.randint(1, level)

    # حلقه حدس زدن
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue

        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
