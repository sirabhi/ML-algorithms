# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 18:40:13 2018

@author: admin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


""""df=pd.read_csv("csv_result-weather.csv")
a= df.head()

print a

d=pd.read_csv("csv_result-weather2.csv",delim_whitespace=',',dtype=None)
ab= d.head()
print ab
plt.bar(d['humidity'],d['temperature'])
plt.show()

"""

""""
p=[]
q=[]

with open('csv_result-weather.csv','r') as csvFile:
    a=csv.reader(csvFile,delimiter=',')
    for row in a:
        #print row
        p.append((row[2]))
        q.append((row[3]))
p.sort()
q.sort()        
plt.plot(p,q,label='Loaded from file!')
plt.xlabel('p')
plt.ylabel('q')
plt.legend()
plt.show()        
        
csvFile.close()        
        

x=[]
y=[]

with open('csv_result-weather2.csv','r') as csvFile:
    a=csv.reader(csvFile,delimiter=',')
    for row in a:
        #print row
        if row[3]==" ":
            row[3]=85
        x.append((row[2]))
        y.append((row[3]))
        
x.sort()
y.sort()       
plt.plot(x,y,label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()        
        
csvFile.close()        
    
  
"""

df=pd.read_csv("csv_result-weather.csv")

plt.scatter(df['id'],df['humidity'])
plt.xlabel('id')
plt.ylabel('humidity')
plt.show()
"""
df=pd.read_csv("csv_result-weather.csv")
print df['hu'].isnull()
plt.axis([-100,700,-100,700])
plt.bar(df['temperature'],df['humidity'])
plt.show()
"""

df=pd.read_csv("csv_result-weather2.csv")
plt.scatter(df['id'],df['humidity'])   
plt.xlabel('id')
plt.ylabel('humidity')
plt.show()
print df
print "\n\n"
print "checking missing values for humidity"
print df['humidity'].isnull()
print "\n\n"
print "checking missing values for humidity"
print df['temperature'].isnull()
#plt.axis([-100,700,-100,700])
#plt.bar(df['temperature'],df['humidity'])
#df['humidity'].fillna(85,inplace=True)
#print df

#replacing negativr values with expected value=80
nc=0
for n in df['humidity']:
    if n<0:
        nc=nc+1;
print "number of negative values are" ,nc  

counth=0
for n in df.humidity:
    counth=counth+1
    if n<0:
        df.loc[counth-1,'humidity']=80
print df        

#filing mean at null places
mean=df['humidity'].mean()
print "MEAN",mean
df['humidity'].fillna(mean,inplace=True)
print df


#similarly for temperature
#expecred value=85
m=0
for g in df['temperature']:
    if g<0:
        m=m+1;
print "Number of negative values are:" ,m  

countt=0
for n in df.temperature:
    countt=countt+1
    if n<0:
        df.loc[countt-1,'temperature']=80
print df   

print"\n"
#filing mean at null places
mean=df['temperature'].mean()
print "MEAN",mean
df['temperature'].fillna(mean,inplace=True)
print df     


print"\n"
for pl in df['play']:
    try:
        i=float(pl)
        print"false"
    except(ValueError,TypeError):
        print "true"
        
print"\n"
z=0
for pl in df['play']:
    z=z+1
    try:
        if(float(pl)):
            
            df.loc[z-1,'play']="no"
    except(ValueError,TypeError)  :
        df.loc[z-1,'play']=pl
        
            
print df 
print "\n"
#for outlook

print"\n"
zq=0
for plp in df['outlook']:
    zq=zq+1
    try:
        if(int(plp)):
            
            df.loc[zq-1,'outlook']="rainy"
    except(ValueError,TypeError)  :
        df.loc[zq-1,'outlook']=plp
           
print df         
        
   
plt.scatter(df['id'],df['humidity'])   
plt.show()



