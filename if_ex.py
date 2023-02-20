try:
    gross_income = int(input("Enter your salary: "))
    children = int(input("Enter the number of children: "))
    if ( gross_income < 1000 ) and ( children < 1 ):
        tax = 10
    elif ( gross_income < 1000) and ( children <2):
        result = gross_income * 0.91
        print (result)
    elif (gross_income < 2000) and (children < 1):
        result = gross_income * 0.88
        print(result)
    elif (gross_income < 4000) and (children < 1):
        result = gross_income * 0.86
    else:

net = gross_income - tax

print(net)


except:
    print("Error")