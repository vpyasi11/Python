#Opeing the products file
ProductfileRead = open('Products.csv')
invoiceID=0

#Generating Invoice ID
f= open("invoice.csv",'r')
# f.readline()
# for i in f.readlines():
#     invoiceID=i[0]
# invoiceID += 1
# print(invoiceID)
# lines = file.readlines()

# for i, line in enumerate(lines):
#     print("Line {}: {}".format(i, line.strip()))
    
# file.close()


#Variables controling the flow
productInfo=[] #2D array to store the input file data
details = [] #details to write in output file
count = 0 #controlling variable


print("\nChoose the products from below: \n" )
#exclude the headers
print(ProductfileRead.readline())

#loop to store the input file as 2D array
for i in ProductfileRead.readlines():  
    productInfo.append(i.split(','))
    productInfo[count].pop()
    print(i,'\t')
    count +=1

inputName = input("Enter the your name: ")
inputPhone = input("Enter the phone number: ")
ans = True
x=[invoiceID, inputName, inputPhone]
f.close()
f = open("invoice.csv","a")
f.write("\n")
for i in x:
    f.write(str(i)+",")

f.close()

while(ans == True):
    inputId = int(input("Enter the product ID: "))
    inputQty = int(input("Enter the Quantity: "))
    
    details = [invoiceID, inputId, inputQty]

    #appends the unit price
    details.append(productInfo[inputId - 1][2])

    #appends the total price
    details.append(int(productInfo[inputId - 1][2]) * inputQty)

    #Opening the files to write the details
    detailsFileWrite = open('Details.csv', 'a')
    detailsFileWrite.write('\n')
    for i in details:
        detailsFileWrite.write(str(i) + ",")

    #closing details file
    detailsFileWrite.close()

        
    inputAns = input("Do you wish to buy another item ? (Y/N) : ")  
    if inputAns.lower() == 'y':
        ans=True
    else:
        ans=False

    

#closing products file
ProductfileRead.close()


#print("Hey", details[0],"you need to pay", details[5], "for", productInfo[inputId - 1][1])