import re
import csv

with open('hello.txt', newline='') as csvfile: #opening the file with text as a csvfile
    spamreader = csv.reader(csvfile, delimiter='\n')
    regexforemail = re.compile(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)') #regex to catch all the emails
    for lines in spamreader:

        mo = regexforemail.search(str(lines))
        email =  str(mo)
        if (email!="None"):
            email = re.sub('.*match=', "", str(mo))
            email = re.sub('\'t', "", email)
            email = re.sub('\'>', "", email)

            f = open("results.txt", "a")
            f.write(email+"\n") #appending all the emails

        print(str(mo))
    

