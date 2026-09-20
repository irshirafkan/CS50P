import sys
import random
from pyfiglet import Figlet

def main():
    # ساخت شیء از کلاس Figlet
    figlet = Figlet()

    # بررسی آرگومان‌های خط فرمان
    if len(sys.argv) == 1:
        # اگر هیچ آرگومانی داده نشد، فونت تصادفی انتخاب کن
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)

    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        # اگر آرگومان‌ها درست بودند، فونت را اعمال کن
        try:
            figlet.setFont(font=sys.argv[2])
        except Exception:
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")

    # دریافت متن از کاربر
    text = input("Input: ")

    # چاپ متن با فونت انتخاب شده (دقت کنید دقیقا renderText نوشته شده است)
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
    
