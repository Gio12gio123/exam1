#your accaunt username and password👇 Step 1

accaunt=input("plese enter your username")
password=input("plese enter your password")

if accaunt == "Gio izoria" and password == "giovar12" :
    print( "you have loged in","balance:",80000)

else: 
    print("try again")

#your balance👇

balance = 80000

#how much would you like to deposit👇 Step two or three
deposit = int(input("plese enter how much u want to deposit"))

new_balance = balance + deposit

print("you have sucsefully deposited money")

#how much you want to withdraw👇 step two or three
withdraw = int(input("please enter how much u want to withdraw:"))

newer_balance = balance - withdraw

print("you have sucsefully withdrawed money")

#enter if you want to exit or not👇 and step 4
exit = input("plese enter if you want to leave or not")

if exit == "yes":
    print("you have sucsefully left the account")

else:
    print("you stayed")