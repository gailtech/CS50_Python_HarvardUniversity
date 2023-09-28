def main():
    a = fraction("Fraction: ")

    a = int(a[0]) / int(a[1]) * 100
    a = round(a)
    if a >= 99:
        print("F")
    elif a <= 1:
        print("E")
    else:
        print(f"{a}%")

def fraction(prompt):
    while True:
        x = input(prompt)
        try:

            x = x.split("/")
            int(x[0]) / int(x[1])
            int(x[0]) < int(x[1])
        except(ValueError, ZeroDivisionError):
            pass
        else:
            #please end me
            if int(x[0]) <= int(x[1]):
                return x
            else:
                pass

main()
