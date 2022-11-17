products=[]
invoiceID = 0
sum=0
bill =[]
with open("products.csv") as product:
    product.readline()
    for row in product:
         temp = row.split(",")
         products.append(temp)
    
print("\n\n"+"*"*44+"\n\t    WELCOME to our Store\n"+"*"*44,"\n")

name = input("Please Enter your Name : ")
number = input("Please Enter contact number : ")


with open("invoice.csv") as inv:
    inv.readline()
    for i in inv:
        temp1 = i.split(",")
        invoiceID = temp1[0]

invoiceID=int(invoiceID)+1



invoice_file = [invoiceID, name, number]

with open("invoice.csv",'a') as inv:
    inv.write("\n")
    for item in invoice_file:
        inv.write(str(item)+",")
        
ans = True

while (ans == True):
    #print("-"*44,"\n")
    print("\n"+"*"*44)
    print("Choose Products from below : ")
    print("*"*44,"\n")
    print("Product ID\tProduct Name\tUnit Price")
    print("-"*44,"\n")
    for i in range(len(products)):
        print("   ",products[i][0],'\t\t'+products[i][1],"     \t"+products[i][2],"\n")
    print("-"*44)

    id = int(input("\nEnter Product ID : "))
    qty = int(input("Enter Quantity for product : "))
    print("-"*44,"\n")

    details = [invoiceID, id, qty]
    details.append(products[id-1][2])
    details.append(int(products[id-1][2])*qty)

    with open("details.csv","a") as d:
        d.write("\n")
        for item in details:
            d.write(str(item) +",")
 
    print("Hey, "+ invoice_file[1] + "!")
    print("="*44,"\n"+"Bill Summary \n"+"="*44,"\n")
    print("Product Name  Unit Price  Quantity  Total")
    print("-"*44,"\n")
    bill.append([products[id-1][1],details[3],details[2],details[4]])
    
    for i in range(len(bill)):
        print("  ",bill[i][0],'\t ',bill[i][1],"\t   ",bill[i][2],"\t   ",bill[i][3],"\n")
    print("="*44)
    sum += details[4]
    print("You need to pay : ", sum)
    
    print("="*44,"\n")

    inputAns = input("Do you wish to buy another item ? (Y/N) : ")  
    if inputAns.lower() == 'y':
        ans=True
    else:
        ans=False


   