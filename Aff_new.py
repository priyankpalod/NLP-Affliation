import xml.etree.ElementTree as ET
import unicodedata

country_list = ["Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegowina", "Botswana", "Bouvet Island", "Brazil", "British Indian Ocean Territory", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Congo", "Congo, the Democratic Republic of the", "Cook Islands", "Costa Rica", "Cote d'Ivoire", "Croatia (Hrvatska)", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands (Malvinas)", "Faroe Islands", "Fiji", "Finland", "France", "France, Metropolitan", "French Guiana", "French Polynesia", "French Southern Territories", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Heard and Mc Donald Islands", "Holy See (Vatican City State)", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran (Islamic Republic of)", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, Democratic People's Republic of", "Korea, Republic of", "Kuwait", "Kyrgyzstan", "Lao People's Democratic Republic", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libyan Arab Jamahiriya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia, The Former Yugoslav Republic of", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia, Federated States of", "Moldova, Republic of", "Monaco", "Mongolia", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russian Federation", "Rwanda", "Saint Kitts and Nevis", "Saint LUCIA", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Seychelles", "Sierra Leone", "Singapore", "Slovakia (Slovak Republic)", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Georgia and the South Sandwich Islands", "Spain", "Sri Lanka", "St. Helena", "St. Pierre and Miquelon", "Sudan", "Suriname", "Svalbard and Jan Mayen Islands", "Swaziland", "Sweden", "Switzerland", "Syrian Arab Republic", "Taiwan, Province of China", "Tajikistan", "Tanzania, United Republic of", "Thailand", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "United States Minor Outlying Islands", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Viet Nam", "Virgin Islands (British)", "Virgin Islands (U.S.)", "Wallis and Futuna Islands", "Western Sahara", "Yemen", "Yugoslavia", "Zambia", "Zimbabwe"]

US_States = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District Of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

Exceptional_names = ["MSN", "KU Leuven", "INSEAD", "ESCP Europe", "Sciences Po Paris", "Ecole Centrale de Paris", "ETH Zurich", "EPFL"]



def isAffiliation(y,fs):
    x=y.strip()                                         
    x=x.strip(',')
    #print x
    if fs == max_fs:            #If in Title (Biggest Font Size) it can't be affiliation.
        #print x
        return "0"              #Done to prevent cases when "Research" comes in title (often)
    if x.find("Universit")!=-1 or x.find(" Labs")!=-1 or x.find("Laboratories")!=-1 or x.find("Institut")!=-1 or x.find("Research")!=-1 or x.find("College")!=-1 or x.find("Corporat")!=-1 or x.find("Academy")!=-1 or x.find("Normale")!=-1 or x.find("Polytechnique")!=-1 or x.find("Politecnic")!=-1 or x.find("Universidad")!=-1 or x in Exceptional_names:
        t = x.split(' ')
        countsmall = 0
        countall = 0
        for word in t:
            countall += 1
            if word == word.lower():
                countsmall += 1
        #print str(countall) + " " + str(countsmall)  
        if countsmall > 3:
                return "0"
        #print "Yes " + word
        return "1"
    return "0"

a_file = "/users/user/Desktop/Palod/pdfs/chi2.xml"
AffiliationOutputFile = open(a_file.split(".")[0]+'_parse.txt','w')
AffiliationOutputFile.write("0\t0\t0\n")
'''
def FindAffiliation(stri,fs):
    l = []
    a = []
    stri = ((((((((((stri.strip('1')).strip('2')).strip('3')).strip('4')).strip('5')).strip('6')).strip('7'))).strip('8')).strip('9')).strip('0')
    #print stri
    t = stri.split(',')
    aff = "0"
    for j in t:
        j = j.strip()
        #print j
        if aff == "1" and isAffiliation(j,fs) == "0":
            if (j.split(' '))[0] is "":
                continue
            if ((j.split(' '))[0])[0].isupper():
                aff = "1"
            else:
                aff = "0"
        else:
            aff = isAffiliation(j,fs)
        #print aff
        x = j.split(' ')
        for i in x:
            if len(i) > 0:
                if(aff!="0"):
                    AffiliationOutputFile.write((i+"\t").encode("utf-8"))
                    AffiliationOutputFile.write(aff + "\t")
                    AffiliationOutputFile.write(("0\n").encode("utf-8"))
'''
def FindAffiliation(stri,fs):
    l = []
    a = []
    stri = ((((((((((stri.strip('1')).strip('2')).strip('3')).strip('4')).strip('5')).strip('6')).strip('7'))).strip('8')).strip('9')).strip('0')
    #print stri
    t = stri.split(',')
    aff = "0"
    flag = "0"
    for j in t:
        if flag == "1":
            break
        j = j.strip()
        #print j
        p = isAffiliation(j,fs)
        if p == "1" or aff == "1":
            aff = "1"
            x = j.split(' ')
            for i in x:
                if len(i)>0:
                    AffiliationOutputFile.write((i+"\t").encode("utf-8"))
                    AffiliationOutputFile.write(("1\t").encode("utf-8"))
                    AffiliationOutputFile.write(("0\n").encode("utf-8"))
                    if p == "0" and (i in country_list or i in US_States):
                        flag = "1"
                        break


tree = ET.parse(a_file)
root = tree.getroot()
max_fs = 0
for pages in root.findall('PAGE'):
    for texts in pages.findall('TEXT'):
        for tokens in texts.findall('TOKEN'):
            if(float(tokens.attrib['font-size'])>max_fs):
                max_fs=float(tokens.attrib['font-size'])

stringForAff = ""
count = 0
for pages in root.findall('PAGE'):
    count+=1
    if count>2:
        break
    texts = pages.findall('TEXT')
    for i  in range(len(texts)):
        tokens = texts[i].findall('TOKEN')
        for j in range(len(tokens)):
            if type(tokens[j].text) is not str:
                continue            
            if type(tokens[j].text) is unicode:
                stringForAff += unicodedata.normalize('NFKD', tokens[j].text).encode('ascii','ignore')
            else:
                stringForAff += tokens[j].text
            stringForAff += " "
        if(count<=2):
            FindAffiliation(stringForAff,float(tokens[j].attrib['font-size']))
            stringForAff = ""
            AffiliationOutputFile.write("0\t0\t0\n")
            
