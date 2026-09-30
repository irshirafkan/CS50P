from twttr import shorten

# ۱. تست حروف کوچک (Lowercase)
def test_shorten_lowercase():
    assert shorten("hello") == "hll"
    assert shorten("aeiou") == ""

# ۲. تست حروف بزرگ (Uppercase)
def test_shorten_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("AEIOU") == ""

# ۳. تست حروف بزرگ و کوچک ترکیب شده (Mixed case)
def test_shorten_mixed_case():
    assert shorten("HeLLo") == "HLL"
    # در اینجا Twitter به Twttr تبدیل می‌شود که کاملا درست است
    assert shorten("Twitter") == "Twttr"

# ۴. تست اعداد (Numbers)
def test_shorten_numbers():
    assert shorten("12345") == "12345"
    assert shorten("h3ll0") == "h3ll0"

# ۵. تست علائم نگارشی و فاصله‌ها (Punctuation and Whitespace)
def test_shorten_punctuation():
    assert shorten("hello, world!") == "hll, wrld!"
    assert shorten("what's up?") == "wht's p?"