a = input("File name: ")
b = a.lower()

if '.gif' in b:
    print("image/gif")
elif '.jpg' in b:
    print("image/jpeg")
elif '.jpeg' in b:
    print("image/jpeg")
elif '.png' in b:
    print("image/png")
elif '.pdf' in b:
    print("application/pdf")
elif '.txt' in b:
    print("text/plain")
elif '.zip' in b:
    print("application/zip")
else:
    print("application/octet-stream")
