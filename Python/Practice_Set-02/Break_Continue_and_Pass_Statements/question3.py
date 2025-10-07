# Write a loop that goes through numbers 1 to 5, but does nothing for number 3 (use pass).

for i in range(1, 6):
    match i:
        case 1:
            print(1)
        case 2:
            print(2)
        case 3:
            pass
        case 4:
            print(4)
        case 5:
            print(5)    
        case _:
            print("Invalid number")
    