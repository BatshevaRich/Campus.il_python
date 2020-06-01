number = int(input("Enter three digits (each digit for one pig): "))

total = number %10 + number //10 %10 + number //100
print("total all: ", total)
print("equal: ", total //3)
print("mod left: ", total % 3)
print("equally divided? ", total % 3 == 0)