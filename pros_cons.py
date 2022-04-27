
from bs4 import BeautifulSoup
import requests
import csv

#Create a csv file to store the image links
csv_file = open('pros_cons.csv', 'w',newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['mobile_names', 'Pros', 'Cons'])

#Get the URL of the mobile phones
file = open("mobiles.csv")
csvreader = csv.reader(file)
#header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row[0])
file.close()

for link in rows:
    r = requests.get(link)
    htmlContent=r.content
    soup = BeautifulSoup(htmlContent,'html.parser')

    title = soup.find('div',class_='_thd _shins')
    title = title.h1.text

    #scrape pros and cons
    try:
        div=soup.find('div',{"class":'_flx _pdqty'})
        uls=div.find_all('ul')

        good=uls[0]
        bad=uls[1]

        good_li=good.find_all("li")
        bad_li=bad.find_all("li")
        good_li=good_li[1:]
        bad_li=bad_li[1:]
        pros=""
        cons=""
        for li in good_li:
            pros=pros+li.text.strip()+" ;"
        for li in bad_li:
            cons=cons+li.text.strip()+" ;"
        #print(pros)
        #print(cons)

        csv_writer.writerow([title, pros, cons])
    except:
        csv_writer.writerow([title,'-','-'])




        



