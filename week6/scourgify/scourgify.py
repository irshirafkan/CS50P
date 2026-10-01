import sys
import csv

def main():
    # ۱. بررسی تعداد آرگومان‌ها
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # ۲. بررسی پسوند فایل‌ها
    if not input_file.endswith(".csv"):
        sys.exit(f"Could not read {input_file}")
    if not output_file.endswith(".csv"):
        sys.exit(f"Could not write {output_file}")

    # ۳. خواندن، پردازش و نوشتن فایل
    try:
        with open(input_file, "r") as infile:
            reader = csv.DictReader(infile)

            with open(output_file, "w", newline="") as outfile:
                # تعریف هدرهای فایل خروجی
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)

                # نوشتن هدرها در فایل خروجی
                writer.writeheader()

                # پردازش هر ردیف
                for row in reader:
                    # جدا کردن نام و نام خانوادگی (مثلا از "Luna, Lovegood" به "Luna" و "Lovegood")
                    last, first = row["name"].split(", ")

                    # نوشتن ردیف جدید در فایل خروجی
                    writer.writerow({
                        "first": first,
                        "last": last,
                        "house": row["house"]
                    })

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()
