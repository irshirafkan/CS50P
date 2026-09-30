from plates import is_valid

# 1. تست‌های طول پلاک (Length checks)
def test_length_valid():
    assert is_valid("HELLO") == True
    assert is_valid("CS50") == True

def test_length_invalid():
    assert is_valid("A") == False       # کمتر از ۲ کاراکتر
    assert is_valid("OUTATIME") == False # بیشتر از ۶ کاراکتر

# 2. تست شروع با حروف (Beginning alphabetical checks)
def test_start_with_letters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False       # دومین کاراکتر عدد است
    assert is_valid("2A") == False       # اولین کاراکتر عدد است
    assert is_valid("22") == False       # هر دو کاراکتر عدد هستند

# 3. تست placement اعداد (Number placement)
def test_numbers_at_end():
    assert is_valid("AAA50") == True     # اعداد در انتها
    assert is_valid("AAA50A") == False   # عدد در وسط پلاک
    assert is_valid("AA12AA") == False

# 4. تست شروع اعداد با صفر (Zero placement)
def test_no_leading_zero():
    assert is_valid("CS05") == False     # اولین عدد صفر است
    assert is_valid("CS50") == True      # اولین عدد صفر نیست

# 5. تست کاراکترهای مجاز (Alphanumeric checks)
def test_alphanumeric_only():
    assert is_valid("PI3.14") == False   # دارای نقطه
    assert is_valid("PI 14") == False     # دارای فاصله
    assert is_valid("PI!14") == False    # دارای علامت تعجب
    assert is_valid("CS50") == True      # فقط حرف و عدد
