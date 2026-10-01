import sys
from PIL import Image, ImageOps

def main():
    # بررسی تعداد آرگومان‌ها
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # بررسی پسوندهای مجاز
    valid_extensions = (".jpg", ".jpeg", ".png")
    if not input_file.lower().endswith(valid_extensions) or not output_file.lower().endswith(valid_extensions):
        sys.exit("Invalid input")

    # بررسی اینکه پسوند فایل ورودی و خروجی یکسان باشد
    input_ext = input_file.lower().rsplit('.', 1)[-1]
    output_ext = output_file.lower().rsplit('.', 1)[-1]
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    # باز کردن فایل‌ها، تغییر اندازه، قرار دادن پیراهن و ذخیره
    try:
        # باز کردن عکس پیراهن و عکس ورودی کاربر
        shirt = Image.open("shirt.png")
        photo = Image.open(input_file)

        # برش دادن و تغییر اندازه عکس کاربر دقیقاً به اندازه عکس پیراهن
        photo = ImageOps.fit(photo, shirt.size)

        # چسباندن پیراهن روی عکس کاربر (آرگومان دوم برای شفافیت پیکسل‌های خالی است)
        photo.paste(shirt, shirt)

        # ذخیره عکس نهایی
        photo.save(output_file)

    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
