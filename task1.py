try:
    print("reading file")
    with open("simple.txt", "r") as f:
        line_no=1
        for line in f:
            print(f"line {line_no}: {line.strip()}")
            line_no+=1
except FileNotFoundError:
    print("file not found")