from bs4 import BeautifulSoup
import requests
import csv
file = open("mobile_links.csv")
csvreader = csv.reader(file)
header = next(csvreader)
#print(csvreader)
rows = []
for row in csvreader:
    #print(row[1])
    rows.append(row[0])
#print(rows)
file.close()
csv_file = open('mobiles_specifications.csv', 'w',newline='',encoding='utf-8')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Mobile Name','General','Display','Hardware','Camera','Software','Connectivity','Sensors'])

for link in rows:
    lst = []
    
    #print(link)
    source = requests.get(link).text
    soup = BeautifulSoup(source,'lxml')
    title = soup.find('div',class_='_thd _shins')
    title = title.h1.text
    lst.append(title)
    for item in soup.find_all('div',class_='_gry-bg _spctbl _ovfhide'):
        temp = ""
        count=0
        for element in item.find_all('td'):
            if(temp==''):
                temp+=element.text+" : "
            elif(count%2!=0 and element.text!='SIM 1' and element.text!='SIM 2'):
                temp+=element.text+" : "
                count+=1
            elif(count%2==0 and element.text!='SIM 1' and element.text!='SIM 2'):
                temp+=element.text+" ; "
                count+=1
            else:
                temp+=element.text+" "
           
        #print(temp)       
        #print("\n")
        #item = item.text.strip()
        #item = item.replace('  ',';')
        #item = item.replace(';;;',';')
        temp.strip()
        lst.append(temp)
        #print(item)
    
    print(lst)
    csv_writer.writerow(lst)
    #break