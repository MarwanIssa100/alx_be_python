size = int(input("Enter the size of the pattern: "))
limit = size
while limit > 0 :
    for i in range(0, size-1):
        print("*", end = "")
    print("*")
    limit -= 1

        