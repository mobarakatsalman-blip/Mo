import math  # استدعاء مكتبة الرياضيات للعمليات المتقدمة

def calculator():
    print("--- Advanced Calculator ---")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (**)")
    print("6. Square Root (sqrt)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")

    choice = input("Enter choice (1-9): ")

    # العمليات التي تتطلب رقمين (جمع، طرح، ضرب، قسمة، أس)
    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
            else:
                print("Error! Division by zero.") # خطأ القسمة على صفر
        elif choice == '5':
            result = math.pow(num1, num2)
            print(f"Result: {num1} ^ {num2} = {result}")

    # العمليات التي تتطلب رقماً واحداً (جذر، جا، جتا، ظا)
    elif choice in ['6', '7', '8', '9']:
        num = float(input("Enter the number: "))

        if choice == '6':
            if num >= 0:
                result = math.sqrt(num)
                print(f"Square Root of {num} = {result}")
            else:
                print("Error! Negative numbers have no real square root.") # خطأ جذر عدد سالب
        elif choice == '7':
            # تحويل الدرجات لراديان لأن المكتبة تتعامل بالراديان
            result = math.sin(math.radians(num))
            print(f"Sin({num}) = {result}")
        elif choice == '8':
            result = math.cos(math.radians(num))
            print(f"Cos({num}) = {result}")
        elif choice == '9':
            result = math.tan(math.radians(num))
            print(f"Tan({num}) = {result}")
    
    else:
        print("Invalid Input!") # إدخال غير صحيح

# تشغيل الآلة الحاسبة
if __name__ == "__main__":
    calculator()
