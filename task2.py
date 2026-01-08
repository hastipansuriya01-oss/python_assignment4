user=input("enter a text and write to the file:")
with open("output.txt", "w") as f:
    f.write(user + "\n")
    print("data successfully written to file output.txt")
add_text=input("enter a additional text and write to the file:")
with open("output.txt", "a") as f:
    f.write(add_text + "\n")
    print("data successfully written to file output.txt")
with open("output.txt","r")as f:
    print("final content of the file")
    data=f.read()
    print(data)

