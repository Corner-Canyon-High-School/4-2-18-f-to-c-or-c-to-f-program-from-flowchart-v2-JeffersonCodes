
temp = int(input("Enter the temperature: "))
type = int(input("Type 1 for Fahrenheit-to-Centigrade. Type 2 for Centigrade-to-Fahrenheit "))
if type == 2:
    C = ((5*(temp-32))/9)
    print(C, "degrees Centigrade")
if type == 1:
    F = (9*temp + (32 * 5))/5
    print(F, "degrees Fahrenheit")