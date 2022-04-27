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
csv_file = open('mobiles_summary.csv', 'w',newline='',encoding='utf-8')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Mobile Name','Summary'])

for link in rows:
    lst = []
    
    #print(link)
    
    source = requests.get(link).text
    soup = BeautifulSoup(source,'lxml')
    title = soup.find('div',class_='_thd _shins')
    summary = soup.find('div',class_='inc _pdsmry')
    lst.append(title.text)
    lst.append(summary.p.text)
    print(lst)
    csv_writer.writerow(lst)
    