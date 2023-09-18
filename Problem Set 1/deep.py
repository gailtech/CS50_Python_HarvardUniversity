a = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

#def input_yes(y):
    #y = d("42", "forty-two", "forty two")

if a.strip() == "42":
    print("Yes")
elif a.lower().strip() == "forty-two":
    print("Yes")
elif a.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")
