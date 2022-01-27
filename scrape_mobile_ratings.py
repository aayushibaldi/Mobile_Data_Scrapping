from bs4 import BeautifulSoup
import requests
import csv
import re
file = open("mobiles.csv")
csvreader = csv.reader(file)
header = next(csvreader)
#print(header)
rows = []
for row in csvreader:
    #print(row[1])
    rows.append(row[1])
#print(rows)
file.close()
csv_file = open('mobiles_ratings.csv', 'w',newline='')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['mobiles', 'design','display','software','performance','battery life','camera','value for money','Price'])

for link in rows:
    source = requests.get(link).text
    soup = BeautifulSoup(source,'lxml')
    
    ch = 'r'
    try:
        lst = []
        element = soup.find('ul',class_='_flx _rwrtng _ovfhide')
        #print(element)
        title = soup.find('div',class_='_thd _shins')
        price = soup.find('div',class_='_trtwgt')
        title = title.h1.text
        price = price.a.text
        price = price[1:]
        price = price.lstrip()
        price = price.replace(',','')
        #print(type(price))
        lst.append(title)
        for data in element.find_all('i'):
            temp = data['class'][1].lstrip(ch)
            #print(temp)
            lst.append(temp)
            
        lst.append(price)   
        csv_writer.writerow(lst)
        print(lst) # this list is to be written in the csv file mobile_ratings.csv

        
        #print(title)
    except:
        pass
#    num = num + 1
#print(num)

#print(data)




  




