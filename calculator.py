

print("--- Digital Calculator ---")
print("Instructions: Exit karne ke liye 'off' likhein")

while True:
    # 1. User se input lena
    choice = input("\nCalculation shuru karein? (Enter dabayein ya band karne ke liye 'off' likhein): ").lower()
    
    if choice == 'off':
        print("Calculator band ho raha hai. Bye!")
        break

    try:
        num1 = float(input("Pehla Number: "))
        op = input("Sign (+, -, *, /) chunein: ")
        num2 = float(input("Dusra Number: "))

        # 2. If-Else Logic (Main Part)
        if op == '+':
            result = num1 + num2
            print(f"Total: {result}")

        elif op == '-':
            result = num1 - num2
            print(f"Total: {result}")

        elif op == '*':
            result = num1 * num2
            print(f"Total: {result}")

        elif op == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"Total: {result}")
            else:
                print("Galti: Zero (0) se divide nahi kar sakte!")
        
        else:
            print("Galti: Galat sign lagaya hai!")

    except ValueError:
        print("Galti: Sirf numbers hi likhein!")

    print("-" * 25)