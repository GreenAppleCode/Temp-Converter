def tempconverter():
    conv = input("Would you like to convert Fahrenheit to Celcius or Celcius to Fahrenheit?(f to c, c to f): ")
    if conv == "f to c":
        ftemp = input("enter temp in Fahrenheit: ")
        ftemp = float(ftemp)
        ctemp = ftemp - 32
        ctemp = ctemp * 5/9
        ftemp = str(ftemp)
        ctemp = str(ctemp)
        print(ftemp + " in F is " + ctemp + " in C")

    elif conv == "c to f":
        ctemp = input("enter temp in Celcius: ")
        ctemp = float(ctemp)
        ftemp = ctemp * 9/5
        ftemp = ftemp + 32
        ctemp = str(ctemp)
        ftemp = str(ftemp)
        print(ctemp + " in C is " + ftemp + " in F")

    else:
        print("Invalid Syntax, Closing Program...")
    yorn = input("Do you want to convert again?(y/n): ")
    if yorn == "y":
        tempconverter()
    elif yorn == "Y":
        tempconverter()
    elif yorn == "n":
        print("Alright, have a nice day!")
        exit()
    elif yorn == "N":
        print("Alright, have a nice day!")
        exit()
    else:
        print("Invalid Syntax, Closing Program...")
tempconverter()