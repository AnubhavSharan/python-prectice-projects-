import time

class New_User:
    def __init__(self,name,address,mob_number,username,password,DOB):
        self.name=name
        self.address=address
        self.mob_number=mob_number
        self.username=username
        self.password=password
        self.DOB=DOB
        
Clients=[]

def app():
    user=input(f"Please enter 1 for sign up\nplease enter 2 for sign in\nplease enter 3 to exit\n")
    if user=='1':
        user_registration()
    elif user=='2':
            login()
    elif user=='3':
        print("thankyou for using this app")
        exit()
    else:
        print("please enter the valid input")

def user_registration():        
        name=input("please enter your name :")
        address=input("please enter your address or press enter to skip :")
        mob_number=input("please enter your mobile number :")
        while not (mob_number[0]=='0' and len(mob_number)==10): 
            print("the mobile number should start with 0 and should contain 10 digtits")
            mob_number=input("please start again : ")
        username=input("please enter your username :")
        password=input("please enter your password :")
        notpass=True
        if ('@' in password or '#' in password or '$' in password):
            index=0
            if('@' in password):
                      index=password.index('@')
            elif '#' in password:
                      index=password.index('#')
            elif '$' in password:
                      index=password.index('$')
            if (password[0:index].isalpha() and password[index+1:len(password)].isnumeric()):
                      notpass=False
        while(notpass):
                print("Invalid password provided. The Password must initiate with alphabets followed by either one of @,#, $ and ending with numeric. (For Example: Sam@0125)")
                password=input("please try again")
                if ('@' in password or '#' in password or '$' in password):
                    index=0
                    if('@' in password):
                            index=password.index('@')
                    elif '#' in password:
                            index=password.index('#')
                    elif '$' in password:
                            index=password.index('$')
                    if (password[0:index].isalpha() and password[index+1:len(password)].isnumeric()):
                            notpass=False
        confirm_pass=input("please confirm your password : ")
        while not (password==confirm_pass):
                        print("the password is not matching")
                        confirm_pass=input("please try again : ")
         
        DOB=input("please enter your Date of birth :")
        notdate=True
        try:
            valid_date = time.strptime(DOB, '%d/%m/%Y')
            notdate=False
        except ValueError:
            print("the date of birth should be in format DD/MM/YYYY")
        
        while (notdate):
            DOB = input('Please try again: ')
            try:
                valid_date = time.strptime(DOB, '%d/%m/%Y')
                notdate=False
            except ValueError:
                print('the date of birth should be in format DD/MM/YYYY')
        if (2024-valid_date.tm_year < 21):
            print("Sorry you must be atleat 21 years old")
        else:
            student=New_User(name,address,mob_number,username,password,DOB)
            Clients.append(student)
            print("the User is successfully Signed Up")
            app()

def login():
    uname=input("Please enter your username (Mobile number) : ")
    found_user = None
    for user in Clients:
        if uname == user.username or uname == user.mob_number:
            found_user = user
            break
    if found_user is None:
        print("User or mobile number not found.")
        login()
    upass = input("Please enter your password: ")
    while True:
        if upass != found_user.password:
            print("Incorrect password.")
            upass=input("please enter valid password : ")
        else:
            print("You have successfully signed in.")
            print(f"Welcome {found_user.name}")
            print("please enter 2.1 to start ordering\nplease enter 2.2 to print stastistics\nplease enter 2.3 for logout")
            ord=input()
            noodles=[]
            sandwich=[]
            dumpling=[]
            muffins=[]
            pasta=[]
            pizza=[]
            coffee=[]
            cold_coffee=[]
            shake=[]
            if ord=='2.1':
                    cond=True
                    print("please enter 1 for dine in\nplease enter 2 for Order Online\nplease enter 3 to go to login page")
                    dine=input()
                    
                    if dine=='1':
                            dine_date=input("please enter the date of booking in dine : ")
                            dine_time=input("please enter the time of booking in dine : ")
                            members=int(input("please enter the number of persons  : "))
                            print("thankyou for entering the details, your booking is confirmed")
                            while cond:
                                print("Enter 1 for Noodles  Price AUD 2\nEnter 2 for Sandwich Price AUD 4\nEnter 3 for Dumpling Price AUD 6\nEnter 4 for Muffins  Price AUD 8\nEnter 5 for Pasta    Price AUD 10\nEnter 6 for Pizza    Price AUD 20\nEnter 7 for Drinks Menu :")
                                e=input()
                                amount=1
                                if e=='1':
                                    noodles.append(amount)
                                elif e=='2':
                                    sandwich.append(amount)
                                elif e=='3':
                                    dumpling.append(amount)
                                elif e=='4':
                                    muffins.append(amount)
                                elif e=='5':
                                    pasta.append(amount)
                                elif e=='6':
                                    pizza.append(amount)
                                elif e=='7':
                                    print("Enter 1  for coffee  Price AUD 2\nEnter 2  for cold coffee  Price AUD 4\nEnter 3  for shake  Price AUD 6\nEnter 4 for checkout : ")
                                    f=input()
                                    if f=='1':
                                        coffee.append(amount)
                                    elif f=='2':
                                        cold_coffee.append(amount)
                                    elif f=='3':
                                        shake.append(amount)
                                    elif f=='4':
                                        print("please enter Y to proceed with the payment or\nenter N to cancel the Order : ")
                                        i=input()
                                        if i=='N' or i=='n':
                                            noodles.clear()
                                            sandwich.clear()
                                            dumpling.clear()
                                            muffins.clear()
                                            pasta.clear()
                                            pizza.clear()
                                            coffee.clear()
                                            cold_coffee.clear()
                                            shake.clear()
                                            break
                                        elif i=='Y' or i=='y':
                                            a_noodles=len(noodles)*2
                                            b_sandwich=len(sandwich)*4
                                            c_dumpling=len(dumpling)*6
                                            d_muffins=len(muffins)*8
                                            e_pasta=len(pasta)*10
                                            f_pizza=len(pizza)*20
                                            g_coffee=len(coffee)*2
                                            h_cold_coffee=len(cold_coffee)*4
                                            i_shake=len(shake)*6
                                  
                                        total=(a_noodles+b_sandwich+c_dumpling+d_muffins+e_pasta+f_pizza+g_coffee+h_cold_coffee+i_shake)
                                        service_tax=0.15*total
                                        bill_total=service_tax+total
                                        print(f"your total payable amount is : {bill_total} incuding AUD {service_tax} for service charges")
                                        exit()
                    elif dine=='2':
                            condi=True
                            deliver=input("enter 1 for self pickup\nenter 2 for Home delivery\nenter 3 to go to previous menu : ")
                            if deliver=='1':
                                while condi:
                                    print("Enter 1 for Noodles  Price AUD 2\nEnter 2 for Sandwich Price AUD 4\nEnter 3 for Dumpling Price AUD 6\nEnter 4 for Muffins  Price AUD 8\nEnter 5 for Pasta    Price AUD 10\nEnter 6 for Pizza    Price AUD 20\nEnter 7 for Drinks Menu :")
                                    a=input()
                                    amount=1
                                    if a=='1':
                                        noodles.append(amount)
                                    elif a=='2':
                                        sandwich.append(amount)
                                    elif a=='3':
                                        dumpling.append(amount)
                                    elif a=='4':
                                        muffins.append(amount)
                                    elif a=='5':
                                        pasta.append(amount)
                                    elif a=='6':
                                        pizza.append(amount)
                                    elif a=='7':
                                        print("Enter 1  for coffee  Price AUD 2\nEnter 2  for cold coffee  Price AUD 4\nEnter 3  for shake  Price AUD 6\nEnter 4 for checkout : ")
                                        c=input()
                                        if c=='1':
                                            coffee.append(amount)
                                        elif c=='2':
                                            cold_coffee.append(amount)
                                        elif c=='3':
                                            shake.append(amount)
                                        elif c=='4':
                                            print("please enter Y to proceed with the payment or\nenter N to cancel the Order : ")
                                            d=input()
                                            if d=='N' or d=='n':
                                                noodles.clear()
                                                sandwich.clear()
                                                dumpling.clear()
                                                muffins.clear()
                                                pasta.clear()
                                                pizza.clear()
                                                coffee.clear()
                                                cold_coffee.clear()
                                                shake.clear()
                                                break
                                            elif d=='Y' or d=='y':
                                                j_noodles=len(noodles)*2
                                                k_sandwich=len(sandwich)*4
                                                l_dumpling=len(dumpling)*6
                                                m_muffins=len(muffins)*8
                                                n_pasta=len(pasta)*10
                                                o_pizza=len(pizza)*20
                                                p_coffee=len(coffee)*2
                                                q_cold_coffee=len(cold_coffee)*4
                                                r_shake=len(shake)*6
                                                total=(j_noodles+k_sandwich+l_dumpling+m_muffins+n_pasta+o_pizza+p_coffee+q_cold_coffee+r_shake)
                                            
                                                p_date=input("Please enter date of pickup : ")
                                                p_time=input("Please enter time of pickup : ")
                                                p_person=input("Please enter the name of person : ")
                                                print("thankyou for entering the details, your booking is confirmed")
                                                print(f"your total payable amount is : {total}")
                                            exit()
                            elif deliver=='2':
                                while condi:
                                    print("Enter 1 for Noodles  Price AUD 2\nEnter 2 for Sandwich Price AUD 4\nEnter 3 for Dumpling Price AUD 6\nEnter 4 for Muffins  Price AUD 8\nEnter 5 for Pasta    Price AUD 10\nEnter 6 for Pizza    Price AUD 20\nEnter 7 for Drinks Menu :")
                                    g=input()
                                    amount=1
                                    if g=='1':
                                        noodles.append(amount)
                                    elif g=='2':
                                        sandwich.append(amount)
                                    elif g=='3':
                                        dumpling.append(amount)
                                    elif g=='4':
                                        muffins.append(amount)
                                    elif g=='5':
                                        pasta.append(amount)
                                    elif g=='6':
                                        pizza.append(amount)
                                    elif g=='7':
                                        print("Enter 1  for coffee  Price AUD 2\nEnter 1  for cold coffee  Price AUD 4\nEnter 1  for shake  Price AUD 6\nEnter 4 for checkout : ")
                                        h=input()
                                        if h=='1':
                                            coffee.append(amount)
                                        elif h=='2':
                                            cold_coffee.append(amount)
                                        elif h=='3':
                                            shake.append(amount)
                                        elif h=='4':
                                            print("please enter Y to proceed with the payment or\nenter N to cancel the payment : ")
                                            d=input()
                                            if d=='Y' or d=='y':
                                                if found_user.address != '':
                                                    s_noodles=len(noodles)*2
                                                    t_sandwich=len(sandwich)*4
                                                    u_dumpling=len(dumpling)*6
                                                    v_muffins=len(muffins)*8
                                                    w_pasta=len(pasta)*10
                                                    x_pizza=len(pizza)*20
                                                    y_coffee=len(coffee)*2
                                                    z_cold_coffee=len(cold_coffee)*4
                                                    ab_shake=len(shake)*6
                                                    total=(s_noodles+t_sandwich+u_dumpling+v_muffins+w_pasta+x_pizza+y_coffee+z_cold_coffee+ab_shake)
                                                    print(f"your total payable amount is : {total} and there will be an additional charges for delivery")
                                                    print("A fix charges for Delivery based on the distance\nMore than 0 to 4 Kms $3\nMore than 4 to 8 Kms $6\nMore than 8 to 12 Kms $10\nMore than 12 Kms No Delivery provided")
                                                    del_date = input("Please enter the Date of Delivery:")
                                                    del_tem = input("Please enter the Time of Delivery:")
                                                    d_dis =int(input("Please enter the Distance from the restaurant:"))

                                                    if d_dis <= 4 and d_dis >= 0:
                                                            print(f"Your total payable amount is : {total + 3} including delivery charge")
                                                            print("thank you for ordering, your order has been confirmed")
                                                            exit()
                                                    elif d_dis >= 4 and d_dis <= 8:
                                                            print(f"Your total payable amount is : {total + 6} including delivery charge")
                                                            print("thank you for ordering, your order has been confirmed")
                                                            exit()
                                                    elif d_dis >= 8 and d_dis <=12 :
                                                            print(f"Your total payable amount is : {total + 10} including delivery charge")
                                                            print("thank you for ordering, your order has been confirmed")
                                                            exit()
                                                    elif d_dis > 12:
                                                            print("No delivery can be done")
                                                            exit()
                                                elif d=='N' or d=='n':
                                                    noodles.clear()
                                                    sandwich.clear()
                                                    dumpling.clear()
                                                    muffins.clear()
                                                    pasta.clear()
                                                    pizza.clear()
                                                    coffee.clear()
                                                    cold_coffee.clear()
                                                    shake.clear()
                                                    break
                                            
                                                else:
                                                    print("You have not mentioned your address, while signing up.\nPlease Enter Y if you would to enter your address.\nEnter N if you would like to select other mode of order.")
                                                    Y_N = str(input())
                                                    if Y_N == "Y" or Y_N == "y":
                                                        add = input("Please Enter your Address:")
                                                        s_noodles=len(noodles)*2
                                                        t_sandwich=len(sandwich)*4
                                                        u_dumpling=len(dumpling)*6
                                                        v_muffins=len(muffins)*8
                                                        w_pasta=len(pasta)*10
                                                        x_pizza=len(pizza)*20
                                                        y_coffee=len(coffee)*2
                                                        z_cold_coffee=len(cold_coffee)*4
                                                        ab_shake=len(shake)*6
                                                        total=(s_noodles+t_sandwich+u_dumpling+v_muffins+w_pasta+x_pizza+y_coffee+z_cold_coffee+ab_shake)
                                                        print(f"your total payable amount is : {total} and there will be an additional charges for delivery")
                                                        print("A fix charges for Delivery based on the distance\nMore than 0 to 4 Kms $3\nMore than 4 to 8 Kms $6\nMore than 8 to 12 Kms $10\nMore than 12 Kms No Delivery provided")
                                                        del_date = input("Please enter the Date of Delivery:")
                                                        del_tem = input("Please enter the Time of Delivery:")
                                                        d_dis =int(input("Please enter the Distance from the restaurant:"))

                                                        if d_dis <= 4 and d_dis >= 0:
                                                                print(f"Your total payable amount is : {total + 3} including delivery charge")
                                                                print("thank you for ordering, your order has been confirmed")
                                                                exit()
                                                        elif d_dis >= 4 and d_dis <= 8:
                                                                print(f"Your total payable amount is : {total + 6} including delivery charge")
                                                                print("thank you for ordering, your order has been confirmed")
                                                                exit()
                                                        elif d_dis >= 8 and d_dis <=12 :
                                                                print(f"Your total payable amount is : {total + 10} including delivery charge")
                                                                print("thank you for ordering, your order has been confirmed")
                                                                exit()
                                                        elif d_dis > 12:
                                                                print("No delivery can be done")
                                                                exit()
                                                    elif Y_N == "N" or Y_N == "n":
                                                            print("Select another mode of order.")
                                                            break
                                            elif d=='N' or d=='n':
                                                    noodles.clear()
                                                    sandwich.clear()
                                                    dumpling.clear()
                                                    muffins.clear()
                                                    pasta.clear()
                                                    pizza.clear()
                                                    coffee.clear()
                                                    cold_coffee.clear()
                                                    shake.clear()
                                                    break
                            elif deliver=='3':
                                login()
            elif ord=='2.2':
                print("\nOrder ID\tDate\t\t\tTotal Amount Paid\tType of Order\t")
                print("\n12334\t\t12/12/2000\t\t35.5 AUD\t\tHome Dilivery")
 
                print("\nOrder ID\tDate\t\t\tTotal Amount Paid\tType of Order\t")
                print("\n12335\t\t01/01/2001\t\t20.00 AUD\t\tSelf Pick-Up")
 
                print("\nTotal Amount Spend on all orders AUD: 57.5")
                exit()
            

            elif ord=='2.3':
                print("logged out successfully")
                exit()

                



app()