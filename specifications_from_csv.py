import pandas as pd 
import csv
csv_file = open('specifications.csv','w',newline='',encoding='utf-8')
csv_writer = csv.writer(csv_file)

df = pd.read_csv("mobiles_specifications.csv")

category=['Alternate names','Brand','Model','Price in India','Release date','Launched in India','Form factor','Thickness','Body type',
'Dimensions (mm)','Weight (g)','IP rating','Battery capacity (mAh)','Removable battery','Fast charging','Wireless charging','Colours',
'SAR value','Refresh Rate','Screen size (inches)','Touchscreen','Resolution','Protection type','Aspect ratio','Pixels per inch (PPI)',
'Processor','Processor make','RAM','Internal storage','Expandable storage','Expandable storage type','Expandable storage up to (GB)',
'Dedicated microSD slot','Rear camera','No. of Rear Cameras','Rear autofocus','Rear flash','Front camera','No. of Front Cameras',
'Front autofocus','Front flash','Pop-Up Camera','Operating system','Skin','Face unlock','3D face recognition',
'Fingerprint sensor','In-Display Fingerprint Sensor','Compass/ Magnetometer','Proximity sensor','Accelerometer',
'Ambient light sensor','Gyroscope','Barometer','Temperature sensor','Wi-Fi','Wi-Fi standards supported',
'GPS','Bluetooth','NFC','Infrared','USB OTG','USB Type-C','Micro-USB','Lightning','Headphones','FM','Number of SIMs',
'Wi-Fi Direct','Mobile High-Definition Link (MHL)','Active 4G on both SIM cards','SIM 1 SIM Type','GSM/CDMA','3G','4G/ LTE',
'5G','Supports 4G in India (Band 40)','SIM 2 SIM Type']
csv_writer.writerow(category)
count = 0
#print(len(category))
names = list(df['Mobile Name'])
general = list(df['General'])
display = list(df['Display'])
hardware = list(df['Hardware'])
camera = list(df['Camera'])
software = list(df['Software'])
connectivity = list(df['Connectivity'])
sensors = list(df['Sensors'])
categories = []
temp=[]
for (i,j,k,l,m,n,o) in zip(general,display,hardware,camera,software,connectivity,sensors):
    string = str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)
    categories.append(string)

for value in categories:
    lst = []
    for parameter in category:
        
        string = parameter+" : "
        if string in value:
            temp = value.split(string)
            temp1 = temp[1].split(';')
            lst.append(temp1[0])
        else:
            lst.append("-")
    
        
    csv_writer.writerow(lst)

    

    
    
    


