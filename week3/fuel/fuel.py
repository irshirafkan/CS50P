def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")

            break

        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, y = fraction.split("/")

    x = int(x)
    y = int(y)

    if x > y:
        raise ValueError

    return round((x / y) * 100)


if __name__ == "__main__":
    main()
