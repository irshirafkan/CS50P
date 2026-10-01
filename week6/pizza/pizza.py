import sys
import csv
from tabulate import tabulate

def main():
    # ۱. بررسی تعداد آرگومان‌ها
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_path = sys.argv[1]

    # ۲. بررسی پسوند فایل
    if not file_path.lower().endswith(".csv"):
        sys.exit("Not a CSV file")

    # ۳. خواندن فایل و چاپ جدول
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            # تبدیل داده‌های فایل به یک لیست از لیست‌ها
            data = list(reader)

            # جدول‌بندی و چاپ (ردیف اول به عنوان هدر)
            print(tabulate(data[1:], headers=data[0], tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
