from bs4 import BeautifulSoup
import requests
import csv

#Get the URL of the mobile phones
file = open("mobiles.csv")
csvreader = csv.reader(file)
#header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row[0])
file.close()

#Create a csv file to store the image links
csv_file = open('images.csv', 'w',newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['mobile_names', 'img_links', 'best_buy_links'])

#parse and create html tree for each mobile
for link in rows:
    r = requests.get(link)
    soup = BeautifulSoup(r.content,'html.parser',from_encoding="iso-8859-1")
    #scrape image links
    image=soup.find('div',class_='_pdmimg __arModalBtn _flx')
    img_link = image.img['src']
    img_link = img_link.split('?')[0]
    img_alt=image.img['alt']
    #print(img_link)
    #scrape best buy links
    try:
        best_buy=soup.find('div',class_='_trtwgt')
        best_buy_link=best_buy.a['href']
        #print(best_buy_link)
    except:
        pass
    csv_writer.writerow([img_alt, img_link, best_buy_link])



