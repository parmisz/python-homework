



menu={("coffee,120"),("latte,150"),("tea,100")}
while True:
    print("parmis cafe")
    print("coffee,120")
    print("latte,150")
    print("tea,100")
    print("exit")

    choice=input("choose ur order:")
    choice=int(choice)
    match choice:
        case 1:print("you choose coffee")
        case 2:print("choose latte")
        case 3 :print ("choose tea")
        case 4:print ("bye")

    if choice in menu:
        name,price=menu[choice]
        number=int(input("tedad vared konid"))
        if number > 0:
            total=price*number
            print("your order",name)
            print("total price:",total)
        elif number == 0
        print ("exit")
"