a = input("Greeting: ")

b = a.lower().strip()

if 'hello' in b:
    print("$0")
elif 'h' == b[0]:
    print("$20")
else:
    print("$100")
