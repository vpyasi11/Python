
productOpen = open("products.csv","r")
invoiceID = 101101
f= open("invoice.csv",'r')
f.readline()
for i in f.readlines():
    invoiceID=i[0]
invoiceID += 1

print(invoiceID)

productInfo = []
j=0

productOpen.readline()
print("\n\n\tWELCOME to our Store")
print("\n\n*************************************")
print("Choose Products from below : ")
print("*************************************\n")
for i in productOpen.readlines():
    productInfo.append(i.split(","))
    productInfo[j].pop()
    j+=1
productOpen.close()

for i in range(0,len(productInfo)) :
    print(productInfo[i][0]+ ". " + productInfo[i][1] + " " + productInfo[i][2])
print("\n///////////////////////////////////////////\n")        

name = input("Please Enter your Name : ")
number = input("Please Enter contact number : ")
print("\n")

x=[invoiceID, name, number]
f.close()

f = open("invoice.csv","a")
f.write("\n")
for i in x:
    f.write(str(i)+",")
f.close()

ans = True

while (ans == True):
    id = int(input("Enter Product ID : "))
    qty = int(input("Enter Quantity for product : "))

    details = [invoiceID, id, qty]
    details.append(productInfo[id-1][2])
    details.append(int(productInfo[id-1][2])*qty)

    d = open("details.csv","a")
    d.write("\n")
    for i in details :
        d.write(str(i) +",")
    d.close()

    inputAns = input("Do you wish to buy another item ? (Y/N) : ")  
    if inputAns.lower() == 'y':
        ans=True
    else:
        ans=False

    print("\nHey ! "+ x[1] + "!\n")
    print("Invoice :",x[0])
    print("Contact : "+ x[2])
    print("\nYou need to pay : " , details[4])


print(details)
print(x)
print(productInfo)