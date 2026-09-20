import sys
import requests

def main():
    # بررسی اینکه کاربر دقیقا یک آرگومان وارد کرده باشد
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # بررسی قابل تبدیل بودن آرگومان به عدد اعشاری (float)
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # کلید API خود را از سایت CoinCap دریافت کرده و جایگزین کنید
    api_key = "YOUR_API_KEY_HERE"

    # آدرس API نسخه 3 برای دریافت اطلاعات بیت کوین
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

    try:
        # ارسال درخواست به سرور
        response = requests.get(url)

        # بررسی اینکه آیا درخواست موفق بوده است (کد 200)
        response.raise_for_status()

        # تبدیل اطلاعات دریافت شده به فرمت JSON
        data = response.json()

        # استخراج قیمت بیت کوین (قیمت به صورت متن/string است، پس باید به float تبدیل شود)
        price_usd = float(data["data"]["priceUsd"])

        # محاسبه قیمت کل
        amount = n * price_usd

        # چاپ خروجی با فرمت خواسته شده (4 رقم اعشار و جداکننده هزارگان)
        print(f"${amount:,.4f}")

    except requests.RequestException:
        # مدیریت خطاهای مربوط به ارتباط با شبکه و API
        sys.exit("Error fetching data from API")

if __name__ == "__main__":
    main()
