def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # باید بین 2 تا 6 کاراکتر باشد
    if len(s) < 2 or len(s) > 6:
        return False

    # دو کاراکتر اول باید حرف باشند
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # فقط حروف و اعداد مجاز هستند
    if not s.isalnum():
        return False

    # بررسی اعداد
    for i in range(len(s)):
        if s[i].isdigit():
            # اولین عدد نباید 0 باشد
            if s[i] == "0":
                return False

            # بعد از شروع اعداد، دیگر نباید حرف بیاید
            if not s[i:].isdigit():
                return False

            break

    return True

if __name__ == "__main__":
    main()
