from bank import value

def test_hello():
    # تست کلمه hello با حروف کوچک
    assert value("hello") == 0

def test_hello_uppercase():
    # تست case-insensitive بودن (حروف بزرگ)
    assert value("HELLO") == 0

def test_hello_phrase():
    # تست اینکه عبارت می‌تواند بیشتر از یک کلمه باشد
    assert value("Hello, Newman") == 0

def test_h():
    # تست کلماتی که با h شروع می‌شوند اما hello نیستند
    assert value("how you doing?") == 20

def test_h_uppercase():
    assert value("HOW YOU DOING?") == 20

def test_other():
    # تست کلماتی که با حروف دیگر شروع می‌شوند
    assert value("what's up?") == 100

def test_empty_string():
    # تست ورودی خالی
    assert value("") == 100
