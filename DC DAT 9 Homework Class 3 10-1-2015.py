# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 20:42:33 2015
Class: DC Data Science DAT9
Assignment: Chipotle Python Data Class #3
Date: due October 1, 2015
Author: Tim Yang
Github: tyang123
email: tian1.yang@gmail.com
Address: 8th Floor, 1133 15th St NW, Washington, DC 20005
"""

"""************************************************************
BASIC LEVEL PART 1: Read in the data with csv.reader() and 
store it in a list of lists called 'data'. 
Hint: This is a TSV file, and csv.reader() needs to be told 
how to handle it. https://docs.python.org/2/library/csv.html
Outcome: List of lists store in 'data'
************************************************************"""

#import csv File from relative /data directory, then process tsv file by delineating on '\t'
import csv
with open('DAT-DC-9/data/chipotle.tsv', 'rb') as inputFile:
    tsvReader=csv.reader(inputFile,delimiter='\t')

    #data is the full list. itemRow is one row stored in a list.
    #the counter will be used to store the first row in a separate header list
    data=[]
    itemRow=[]
    counter=0
    
    #iterate by row in TSVreader, and store each row into a list, then append to the chipotleData List
    for row in tsvReader:
        itemRow=row
        data.append(itemRow)
        print itemRow
    
"""************************************************************
"BASIC LEVEL PART 2: Separate the header and data into two different lists.
Answer: Outcome: header stored in "headerRow', data stored in "chipotleData"
************************************************************"""

#import csv File from relative /data directory, then process tsv file by delineating on '\t'
import csv
with open('DAT-DC-9/data/chipotle.tsv', 'rb') as inputFile:
    tsvReader=csv.reader(inputFile,delimiter='\t')

    #chipotleData is the full dictionary. itemRow is one row stored in a list.
    #the counter will be used to store the first row in a separate header list
    chipotleData=[]
    headerRow=[]
    itemRow=[]
    counter=0
    
    #iterate by row in TSVreader, and store each row into a list, then append to the chipotleData List
    for row in tsvReader:
        if counter == 0:
            headerRow=row
            counter=counter+1
        else:
            itemRow=row
            chipotleData.append(itemRow)
        #print itemRow

#confirms the Header is a separate list
print headerRow
#confirms the Chipotle Data is 4623-1=4622 items long
print len(chipotleData)
print chipotleData
        
"""************************************************************
"INTERMEDIATE LEVEL PART 3: Calculate the average price of an order. 
Hint: Examine the data to see if the 'quantity' column is relevant 
to this calculation. Hint: Think carefully about the simplest way 
to do this!
Outcome: $39,237 Total OrderDollars / 1,834 orders = $21.39 dollars/order
************************************************************"""

#Calculate Largest Order ID number    
for rowItem in chipotleData:
    if int(rowItem[0])>maxOrderID:
        maxOrderID=int(rowItem[0])
    print "Row Item" + rowItem[0] + "Max ID" + str(maxOrderID)

print maxOrderID
    
#Iterate from 1 to maxOrderID=1833, total up order price for each orderID
orderTotal = 10000
orderTotal = 0
orderPriceList=[]

# for each order K in the datafile
for k in range(maxOrderID+1):
    #we total up the price*quantity for each orderID in the dataset
    for row in chipotleData:
        if int(row[0])==k:
            #Order Total is the sum of the price*quantity for all matching orderIDs
            orderTotal= orderTotal + float(row[1]) * float(row[4][1:50])
            print "for order#"+str(k) + "quantity: " + row[1] + "price: "+ row[4] + "Total order price:" + str(orderTotal)
            
    #for a given k, write the orderID and final Order Total to a new list
    orderPriceList.append([k,orderTotal])        
    #reset Order Total to 0 for the next orderID
    orderTotal=0
    
# Print out sum of order Totals, then divide by # of Orders
    TotalOrderRevenue=10000
    TotalOrderRevenue=0
    
    for orderRow in orderPriceList:
        TotalOrderRevenue =TotalOrderRevenue + orderRow[1]
    
    AverageOrderCost=TotalOrderRevenue/len(orderPriceList)
    print AverageOrderCost
    #Answer is $39,237.02/1,834 orders = $21.39 dollars/order
    
    
"""************************************************************
INTERMEDIATE LEVEL PART 4: Create a list (or set) of all unique sodas and soft 
drinks that they sell. Note: Just look for 'Canned Soda' and 'Canned Soft Drink',
and ignore other drinks like 'Izze’.
Outcomes: Set with list of sodas, 9 in total: 

Lemonade, Dr. Pepper, Diet Coke, Nestea, Mountain Dew, Diet Dr. Pepper, 
Coke, Coca Cola, Sprite
************************************************************"""

#Create Blank list of sodas for the soft drink
        sodaList=[]

#iterate across entire dataset
for row in chipotleData:
       #if item name has has Canned Soda or Soft Drink
            if row[2]=="Canned Soda" or row[2] == "Canned Soft Drink":
           #Append the Choice Description to the soda List
                sodaList.append(row[3])

#Run a set, which takes the unique non-duplicate values into a sodaList
print set(sodaList)

#Answer: Lemonade, Dr. Pepper, Diet Coke, Nestea, Mountain Dew, Diet Dr. Pepper, 
#Coke, Coca Cola, Sprite


"""************************************************************
ADVANCED LEVEL PART 5: Calculate the average number of toppings per burrito. 
Note: Let's ignore the 'quantity' column to simplify this task. 
Hint: Think carefully about the easiest way to count the number of toppings!
Outcome: ToppingFrequency List contains list of orderID and Count of Toppings.
6,323 Toppings Total
1,172 Burritos
-------------------------
5.395 Toppings/Burrito
************************************************************"""
#Create Blank list of sodas for the soft drink
toppingFrequencyList=[]

#iterate across entire dataset
for row in chipotleData:
       #if item name contains Burrito
            if "Burrito" in row[2]:
           #Append OrderID, Topping String, and # of Commas for Topping Count
                toppingFrequencyList.append([row[0], row[3],row[3].count(",")])
                    #print "orderID: "+ row[0] + " toppings: " + row[3] + " # toppings: " + str(row[3].count(",")+1)

#Parse through the Topping List to accurately extract the count of toppings
totalToppings=0.00
averageToppingsPerOrder=0.00

for row in toppingFrequencyList:
    #Count of toppings equals # of commas + 1
    totalToppings=totalToppings+row[2]+1
    

averageToppingsPerOrder=totalToppings/len(toppingFrequencyList)
print totalToppings #There are 6,323 toppings used
print str(len(toppingFrequencyList))     #There are 1172 burritos
print averageToppingsPerOrder           #Average of 5.395 topping/burrito

"""************************************************************
ADVANCED LEVEL PART 6: Create a dictionary in which the keys represent 
chip orders and the values represent the total number of orders. 
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... } 
Note: Please take the 'quantity' column into account! 
Optional: Learn how to use 'defaultdict' to simplify your code.
Result: Dictionary chipDict with chip category as key, order total as value.
Answers:
('Chips and Roasted Chili-Corn Salsa', 18)
('Chips and Mild Fresh Tomato Salsa', 1)
('Chips and Tomatillo-Red Chili Salsa', 25)
('Chips and Guacamole', 506)
('Chips and Fresh Tomato Salsa', 130)
('Side of Chips', 110)
('Chips and Tomatillo-Green Chili Salsa', 33)
('Chips and Tomatillo Red Chili Salsa', 50)
('Chips and Roasted Chili Corn Salsa', 23)
('Chips', 230)
('Chips and Tomatillo Green Chili Salsa', 45)
************************************************************"""


#Create Blank list of chips and order types
        chipNameList=[]

#iterate across entire dataset
for row in chipotleData:
       #if item name contains Chip, add to dataset
            if "Chips" in row[2]:
           #Append the Choice Description to the chip list
                chipNameList.append(row[2])

#Run a set, which takes the unique non-duplicate values into a ChipList
#print chipNameList
print set(chipNameList)

chipTypeCount=0
chipList = []

for item in set(chipNameList):
    for row in chipotleData:
        if row[2] == item:
            chipTypeCount=chipTypeCount+int(row[1])
            #print "item: "+str(row[2])+" quantity: "+str(row[1])+" running chipTotal: "+str(chipTypeCount)

    chipList.append([item,chipTypeCount])
    chipTypeCount=0        

chipDict=dict(chipList)
    
for p in chipDict.items():
    print p
    