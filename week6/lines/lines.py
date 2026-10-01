import sys

def main():
    # 1. بررسی تعداد آرگومان‌ها
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # 2. بررسی پسوند فایل
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    # 3. بررسی وجود فایل و شمارش خطوط
    try:
        line_count = 0
        with open(sys.argv[1], "r") as file:
            for line in file:
                # حذف فاصله‌های اضافی ابتدا و انتهای خط
                stripped_line = line.strip()

                # نادیده گرفتن خطوط خالی و کامنت‌ها
                if stripped_line == "" or stripped_line.startswith("#"):
                    continue

                # اگر خط خالی یا کامنت نبود، آن را بشمار
                line_count += 1

        print(line_count)

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
