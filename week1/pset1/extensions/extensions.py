file_extension = input("File name: ").strip().lower()

if file_extension.endswith(".gif"):
    print("image/gif")

elif file_extension.endswith(".jpg") or file_extension.endswith(".jpeg"):
    print("image/jpeg")

elif file_extension.endswith(".png"):
    print("image/png")

elif file_extension.endswith(".pdf"):
    print("application/pdf")

elif file_extension.endswith(".txt"):
    print("text/plain")

elif file_extension.endswith(".zip"):
    print("application/zip")

else:
    print("application/octet-stream")