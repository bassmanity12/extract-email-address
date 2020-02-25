import re
import csv

with open('hello.txt', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\n')
    regexforemail = re.compile(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)')
    for lines in spamreader:

        mo = regexforemail.search(str(lines))
        email =  str(mo)
        if (email!="None"):
            email = re.sub('.*match=', "", str(mo))
            email = re.sub('\'t', "", email)
            email = re.sub('\'>', "", email)

            f = open("results.txt", "a")
            f.write(email+"\n")

        print(str(mo))
        #
        #
        # print(lines)

