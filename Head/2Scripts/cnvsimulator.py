#coding=utf8

# Importing of libraries
import os 
import sqlite3
#from StringIO import StringIO
import sys
import random

import numpy as np
import matplotlib.pyplot as plt


path = 'cnvdb.sqlite'


outpath=("newdawn.csv")
out = open(outpath, "w")
out.write("id;SampleNameShort;Sample_Name;Chromosome;Start_Position_bp;End_Position_bp;Copy_Number;Max_Log_BF;Length_bp;No_Probes;LRR_mean;LRR_median;LRR_SD;BAF_mean;BAF_median;BAF_SD;BAF_drift;WF;NumCNV;Quality_Score;MaleOrNot;Age\n")

# Connection to DB
con = sqlite3.connect(path)
cur = con.cursor()

dbsize=2316640
ppltn=10000

dwn=1
upn=99

ad=39
au=73

statarr=[]

for p in range(ppltn):

    n=random.randrange(dwn,upn+1)
    sex=random.randrange(0,1+1)
    age=random.randrange(ad,au+1)

    statarr.append([n,sex])

    for i in range(n):
        r=random.randrange(dbsize+1)
        q = ("SELECT * FROM cnvs WHERE id=%s" % (r))
        cur.execute(q)
        f=cur.fetchall() 
        if len(f)!=0:  
            print ("%s: chr%s %s-%s\n" % (p+1,f[0][3],f[0][4],f[0][5]))
            out.write("%s;nd%s;new_dawn_%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (p+1, p+1, p+1, f[0][3], f[0][4], f[0][5], f[0][6], f[0][7], f[0][8], f[0][9], f[0][10], f[0][11], f[0][12], f[0][13], f[0][14], f[0][15], f[0][16], f[0][17], n, f[0][19], sex, age))
            
        # Проверка что такая уже есть в этом человеке
        # Проверка на перекрытие
        

stat = np.array(statarr)                
    
fig = plt.figure()


# Histogram
plt.hist(stat,100)
plt.title('CNV Nums')
plt.grid(True)
plt.savefig('cnvhist.png', dpi = 300)


#x = stat[:,0]
#y = stat[:,1]


# DotPlot
# plt.scatter(x=x, y=y, marker='o', c='r', edgecolor='b')
# plt.title('Sim%s: $pop:%s$ $gnm:%s$ $sel:%s$ $mtrt:%s$' % (n,p,g+1,e*j,m))
# plt.xlabel('$Population$ $(every$ $hundredth)$')
# plt.ylabel('$Average$ $number$ $of$ $mutations$')
# plt.savefig('sim%sdot.png' % n, dpi = 300)
# plt.close()



# LinePlot
# plt.plot(x, y, lw = 1, color = '#539caf', alpha = 1)
# plt.title('Sim%s: $pop:%s$ $gnm:%s$ $sel:%s$ $mtrt:%s$' % (n,p,g+1,e,m))
# plt.xlabel('$Population$ $(every$ $hundredth)$')
# plt.ylabel('$Average$ $number$ $of$ $mutations$')
# plt.savefig('sim%s_pop%s_gnm%s_sel%s_mtrt%s.png' % (n,p,g+1,e,m), dpi = 300)
# plt.close() 