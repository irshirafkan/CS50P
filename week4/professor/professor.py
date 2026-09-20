import random

def main():
    # دریافت سطح بازی از کاربر
    level = get_level()

    score = 0

    # پرسیدن ۱۰ سوال
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        # کاربر ۳ فرصت برای پاسخ دارد
        for attempts in range(3):
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == correct_answer:
                    score += 1
                    break # پاسخ درست است، به سوال بعدی برو
                else:
                    print("EEE")
            except ValueError:
                # اگر کاربر به جای عدد، حروف وارد کرد
                print("EEE")
        else:
            # اگر حلقه for بدون break تمام شود (یعنی ۳ بار اشتباه زد)
            print(f"{x} + {y} = {correct_answer}")

    # چاپ امتیاز نهایی
    print(f"Score: {score}")


def get_level():
    # گرفتن سطح معتبر از کاربر (فقط 1، 2 یا 3)
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    # تولید عدد تصادفی بر اساس سطح
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        # اگر سطح غیرمعتبر باشد، باید ارور ValueError بدهد
        raise ValueError


if __name__ == "__main__":
    main()
