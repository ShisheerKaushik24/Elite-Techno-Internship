import json
import time



def menuDisplay():
       
    print('============================================================')
    print('*****************Inventory Management Menu *****************')
    print('============================================================')
    print('(1) Add New Item to Inventory')

    print('(2) Remove Item from Inventory')

    print('(3) Search Item in Inventory')
    
    print('(4) purchase Product')

    print('(5) Print Inventory Report')

    print('(99) Quit')

    CHOICE = int(input("Enter choice: "))

    menuSelection(CHOICE)



def menuSelection(CHOICE):

    if CHOICE == 1:

        addInventory()

    elif CHOICE == 2:

        removeInventory()

    elif CHOICE == 3:

        searchInventory()

    elif CHOICE == 4:
        
        purchaseInventry()
        
    elif CHOICE == 5:
    	
    	printInventory() 	

    elif CHOICE == 99:

        exit()
        
def addInventory():
       
       print('*ADD NEW ITEM TO INVENTRY*')
       print('===================')
       fd = open("inventry record.json",'r')
       r = fd.read()
       fd.close()
       inventry_record = json.loads(r)
       prod_id = str(input("Enter product id:"))
       name = str(input("Enter product  name:"))
       pr = int(input("Enter product price:"))
       qn = int(input("Enter quantity:"))
       inventry_record[prod_id] = {'name': name, 'pr': pr, 'qn': qn}
       js = json.dumps(inventry_record)
       fd = open("inventry record.json",'w')
       fd.write(js)
       fd.close()
       CHOICE = int(input('Enter 98 to continue or 99 to exit: '))

       if CHOICE == 98:

            menuDisplay()

       else:

        exit()
      

def removeInventory():

    print("REMOVING ITEMS FROM INVENTRY")

    print("==================")
    fd = open("inventry record.json",'r')
    r = fd.read()
    fd.close()
    inventry_record = json.loads(r)
    product_id=str(input("Enter produt id for removing:"))
    if product_id in inventry_record:
    	del inventry_record[product_id]
    else:
     	print("product not found")
    js = json.dumps(inventry_record)
    fd = open("inventry record.json",'w')
    fd.write(js)
    fd.close()
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))

    if CHOICE == 98:
     	menuDisplay()
    else:
     	exit()
 
def searchInventory():

    print('SEARCHING ITEM IN INVENTRY')

    print('===================')
    fd = open("inventry record.json",'r')
    r = fd.read()
    fd.close()
    inventry_record = json.loads(r)
    product_id=str(input("Enter produt id to search:"))
    if product_id in inventry_record:
    	print(inventry_record[product_id])
    else:
    	print("Product Not Found")
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))

    if CHOICE == 98:
     	menuDisplay()
    else:
     	exit()

 
def purchaseInventry():

    print('PURCHASE ITEM TO INVENTRY')

    print('===================')
    fd = open("inventry record.json",'r')
    r = fd.read()
    fd.close()
    
    inventry_record = json.loads(r)
    ui_prod  = str(input("Enter the product_Id: "))
    ui_quant = int(input("Enter the quantity: "))
    if ui_prod in inventry_record:
    	print("Product: ", inventry_record[ui_prod]['name'])
    	print("Price: ", inventry_record[ui_prod]['pr'])
    	print("Billing Amount: ",inventry_record[ui_prod]['pr'] * ui_quant)
    	inventry_record[ui_prod]['qn'] = inventry_record[ui_prod]['qn'] - ui_quant
    	js = json.dumps(inventry_record)
    	fd = open("inventry record.json",'w')
    	fd.write(js)
    	fd.close()
    	fd = open("Sales.json",'r')
    	r = fd.read()
    	fd.close()
    	sales= json.loads(r) 
    	sales[ui_prod] ={'qn' : ui_quant, 'amount': inventry_record[ui_prod]['pr'] * ui_quant}
    	sale = json.dumps(sales)
    	fd = open("Sales.json",'w')
    	fd.write(sale)
    	fd.close()
    else:
    	print("Product Not Available")
    	
   
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))

    if CHOICE == 98:
     	menuDisplay()
    else:
     	exit()  
    
 
def printInventory():

    print('PRINT ITEM IN INVENTRY')
    print('===================')
    fd = open("inventry record.json",'r')
    r = fd.read()
    fd.close()
    inventry_record = json.loads(r)  
    print(inventry_record)      

menuDisplay()
