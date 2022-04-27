from bs4 import BeautifulSoup
import requests
import csv
file = open("mobiles.csv")
csvreader = csv.reader(file)
#header = next(csvreader)
#print(csvreader)
rows = []
for row in csvreader:
    #print(row[1])
    rows.append(row[0])
#print(rows)
file.close()
csv_file = open('mobile_key_specs.csv', 'w',newline='',encoding='utf-8')
headings = ['Mobile Name','Display','Processor','Front Camera','Rear Camera','RAM','Storage','Battery Capacity','OS']
csv_writer = csv.writer(csv_file)
csv_writer.writerow(headings)
for link in rows:
    lst=[]
    source = requests.get(link).text
    soup = BeautifulSoup(source,'lxml')
    #print(soup)
    title = soup.find('div',class_='_thd _shins')
    title = title.h1.text
    lst.append(title)
    #count = 1
    #for item in soup.find_all('div',class_='_pdsd'):
        #one,two = item.find_all('span')
        #if(one.text==headings[count]):
        #    lst.append(two.text)
        #else:
        #    lst.append("-")
        
        #count+=1
    for item in soup.find_all('div',class_='_pdsd'):
        lst.append(item.text)
        
            
            
           
         
    print(lst)
    csv_writer.writerow(lst)
    