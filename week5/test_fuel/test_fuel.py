import pytest
from fuel import convert, gauge

# تست‌های تابع convert
def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75

def test_convert_full():
    assert convert("1/1") == 100

def test_convert_value_error():
    # اگر صورت از مخرج بزرگتر باشد
    with pytest.raises(ValueError):
        convert("3/1")
    # اگر ورودی عدد صحیح نباشد
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_convert_zero_division():
    # اگر مخرج صفر باشد
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

# تست‌های تابع gauge
def test_gauge_E():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_F():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_percentage():
    assert gauge(50) == "50%"
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"
