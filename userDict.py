customerList = []

while True :
    name = input ("Enter your name \n")
    cellNo = input ("Enter your phone number \n")
    flag = input ("Add another customer? (Y/N) \n");
    if flag.lower() == "y":
        customerList.append({cellNo :name})
    else :
        break


print ("----------------------")
print ("Customer List: \n")
print (customerList)
print ("----------------------")
