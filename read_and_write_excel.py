import csv
import pandas as pd
#import matplotlib as plot

f = open(r'C:\Users\RaunakKothiyal\Downloads\emplist\emplist.csv')
r = csv.reader(f)

for row in r:
    print (row[1])
    print (row[2])

#f = open(r'C:\Users\RaunakKothiyal\Downloads\emplist\emplist.csv')
r = csv.reader(open(r'C:\Users\RaunakKothiyal\Downloads\emplist\emplist.csv'))

name = []
job= []
age = []

for jt in r:
         name.append(jt[0])
         job.append(jt[1])
         age.append(jt[2])

print(name)
print(job)
print(age)

#df = pd.read_csv(r'C:\Users\RaunakKothiyal\Downloads\emplist\emplist.csv')
#df.to_csv('raunak_test.csv')

#plot(arange(10))


    
