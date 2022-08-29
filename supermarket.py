from datetime import date
from datetime import datetime
name=input("Enter your name:")
lists='''
Rice           Rs 45 per kg
Sugar          Rs 40 per kg
Salt           Rs 20 per kg
oil            Rs 180 per lit
Dal            Rs 120 per kg
Chilli Powder  Rs 180 per kg
maggi          Rs 40 per pack
Biscuits       Rs 60 per pack
toothpaste     Rs 65 per unit
soaps          Rs 30 per unit
'''
Price=0
Pricelist=[]
Totalprice=0
Finalprice=0
ilist=[]
qlist=[]
plist=[]


items={'Rice:45','sugar:40','salt:20','oil:180','dal:120','chilli powder:180','maggi:40','biscuits:60','toothpaste:65','soaps:30'}
option=int(input("for list of items press 1"))
if option==1:
    print("lists")
for i in range(len(items)):
    inp1=int(input('if you want to buy press1 or 2 for exit:'))
    if inp1==2:
        break
    if inp1==1:
        item=input('enter your items:')
        quantity=int(input("Enter Quantity"))   
        if item in items.keys():
            price=quantity*(items[item])
            Pricelist.append((item,quantity,items,price))
            Totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            Finalprice=gst+Totalprice
        else:
            print("item you entered is not available")
    else:
        print("you enterd wrong number")
    inp=input("can I bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamout!=0:
            print(20*"=","Kumar supermarket",20*"=")
            print(25*" ","Mahabubnagar")
            print("Name:",name,30*" ","Date:",datatime.now())
            print(80*"-")
            print("sno",8*" ",'items',8*" ","Quantity",5*" ",'price')
            for i in range(len(pricelist)):
                print('i,8*' ',8*' ',ilist[i],5*' ',qlist[i],plist[i]')
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',Totalprice)    
            print("gst amount",50*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'FinalAmount:','Rs',Finalprice)
            print(75*"-")
            print(50*" ","Thanks for visiting")
            print(75*"-")
