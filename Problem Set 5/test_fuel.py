import pytest

def main():
    fraction = input("Fraction: ")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)

def convert(fraction):
    while True:
        try:
            numerator, denominator = fraction.split("/")
            new_numerator = int(numerator)
            new_denominator = int(denominator)
            f = new_numerator / new_denominator
            if  f <= 1:
                p = int(f * 100)
                return p
            else:
                fraction = input('Fraction: ')
                pass
        except (ValueError,ZeroDivisionError):
            raise
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()


#this is my test code
from fuel import convert, gauge


def main():
    test_correct_input()
    test_zero_division()
    test_value()

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_correct_input():
    assert convert('1/2') == 50 and gauge(50) == "50%"
    assert convert('1/100')== 1 and gauge(1) == "E"
    assert convert('99/100')== 99 and gauge(99) == "F"


if __name__ == '__main__':
    main()
