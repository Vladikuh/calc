#Python калькулятор 
print("Ноль в качестве знака операции"
      "\nзавершит работу программы")
while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y+z))
        elif s == '-':
            print("%.2f" % (x-y-z))
        elif s == '*':
            print("%.2f" % (x*y*z))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y/z))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")