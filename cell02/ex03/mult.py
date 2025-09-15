first_num = int(input("Enter the first number: "))
sec_num = int(input("Enter the second number: "))
ans = first_num * sec_num
print(str(first_num) + " x " + str(sec_num) + " = " + str(ans))

if ans > 0:
    print("The result is positive.")
elif ans < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")