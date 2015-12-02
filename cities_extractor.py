f = open('Cities.txt','r')
f1 = open('All_Cities.txt','w')
#import xml.etree.ElementTree as ET
#tree = ET.parse(f)
#root = tree.getroot()
#for option in root.findall('option'):
#    f1.write("\"")
#    f1.write(option.text)
#    f1.write("\", ")
lines = f.readlines()
for line in lines:
    if line.find("//")==0 or len(line)<=1:
        continue
    print len(line)
    line = line.split('= \'')[1]
    line = line.split(';')[0]
    line = line.split('|')
    for city in line:
        city.strip("\n")
        city = city.strip("\\")
        city = city.strip("\'")
        if city!="":
            f1.write("\"")
            f1.write(city)
            f1.write("\", ")
f.close()
f1.close()
