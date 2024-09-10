num = int(input("Enter a number to check = "))

if num > 1:
    for i in range(2, (num//2)+1):
s
        if (num % i ) == 0:
            print(num, "is Not a Prime Number")
            break
        
    else:
        print(num, "Is a Prime Number")

else:
    print(num, "is Not a prime Number")