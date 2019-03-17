#coding=utf8

# Importing of libraries
import os 
import sqlite3
#from StringIO import StringIO
import sys
import random

import numpy as np
import matplotlib.pyplot as plt


from statistics import median 


path = 'cnvdb_round_plus.sqlite'


outpath=("vector.csv")
out = open(outpath, "w")
out.write("epoch;cnvnum;cnvlen\n")

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






# ВЫбрать только те где по одному CNV на хромосоме


# создать новую таблицу

con = sqlite3.connect('cnvdb_round_plus.sqlite')
cur = con.cursor()

for n in range(1,1001):
    print (n)

    cur.execute('CREATE TABLE cnvs1%s (id INTEGER PRIMARY KEY, SampleNameShort VARCHAR(100),Sample_Name VARCHAR(100),Chromosome VARCHAR(100),Start_Position_bp VARCHAR(100),End_Position_bp VARCHAR(100),Copy_Number VARCHAR(100),Max_Log_BF VARCHAR(100),Length_bp VARCHAR(100),No_Probes VARCHAR(100),LRR_mean VARCHAR(100),LRR_median VARCHAR(100),LRR_SD VARCHAR(100),BAF_mean VARCHAR(100),BAF_median VARCHAR(100),BAF_SD VARCHAR(100),BAF_drift VARCHAR(100),WF VARCHAR(100),NumCNV VARCHAR(100),Quality_Score VARCHAR(100),MaleOrNot VARCHAR(100),Age VARCHAR(100))' % n)
    

   
    # q = ("SELECT * FROM cnvs1%s" % (n-1))
    # cur.execute(q)
    # f=cur.fetchall() 
    # if len(f)!=0:  
    #     #print ("%s: chr%s %s-%s\n" % (p+1,f[0][3],f[0][4],f[0][5]))
    #     for fa in f:
    #         p=random.randrange(1,10001)
    #         cnv = [p, p, fa[3], fa[4], fa[5], fa[6], fa[7], fa[8], fa[9], fa[10], fa[11], fa[12], fa[13], fa[14], fa[15], fa[16], fa[17], 0, fa[19], 0, 0]
    #         q = "INSERT INTO cnvs1%s (SampleNameShort, Sample_Name, Chromosome, Start_Position_bp, End_Position_bp, Copy_Number, Max_Log_BF, Length_bp, No_Probes, LRR_mean, LRR_median, LRR_SD, BAF_mean, BAF_median, BAF_SD, BAF_drift, WF, NumCNV, Quality_Score, MaleOrNot, Age) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" % n
    #         cur.execute(q,(cnv))

    q = ("INSERT INTO cnvs1%s SELECT * FROM cnvs1%s" % (n, n-1))
    cur.execute(q)

    q = ("SELECT * FROM cnvs1%s" % (n))
    cur.execute(q)
    f=cur.fetchall() 
    if len(f)!=0:  
        #print ("%s: chr%s %s-%s\n" % (p+1,f[0][3],f[0][4],f[0][5]))
        for fa in f:
            p=random.randrange(1,10001)
            q=("UPDATE cnvs1%s SET SampleNameShort = %s  WHERE id = %s" % (n,p,fa[0]))
            cur.execute(q)




    # посчитать зарактеристики



    narr=[]
    larr=[]

    for i in range(1,10001):
        q = ("SELECT * FROM cnvs1%s WHERE SampleNameShort=%s" % (n, i))
        cur.execute(q)
        f=cur.fetchall() 
        if len(f)!=0:  
            #print ("%s: chr%s %s-%s\n" % (p+1,f[0][3],f[0][4],f[0][5]))
            ncnv=0.0
            lcnv=0.0
            for t in f:
                
                ncnv = ncnv + 1
                lcnv = lcnv + int(t[8])

            narr.append(ncnv)
            larr.append(lcnv)

            
    

    
    out.write("%s;%f;%f\n" % (n,median(narr),median(larr)))
            


    # удалить старую таблицу





con.commit()
con.close()














path = 'cnvdb_round_plus.sqlite'


outpath=("vector22.csv")
out = open(outpath, "w")
out.write("epoch;cnvnum;cnvlen\n")

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




# ВЫбрать только те где по одному CNV на хромосоме


# создать новую таблицу

con = sqlite3.connect('cnvdb_round_plus.sqlite')
cur = con.cursor()

for n in range(1,1001):
    print (n)

    cur.execute('CREATE TABLE cnvs2%s (id INTEGER PRIMARY KEY, SampleNameShort VARCHAR(100),Sample_Name VARCHAR(100),Chromosome VARCHAR(100),Start_Position_bp VARCHAR(100),End_Position_bp VARCHAR(100),Copy_Number VARCHAR(100),Max_Log_BF VARCHAR(100),Length_bp VARCHAR(100),No_Probes VARCHAR(100),LRR_mean VARCHAR(100),LRR_median VARCHAR(100),LRR_SD VARCHAR(100),BAF_mean VARCHAR(100),BAF_median VARCHAR(100),BAF_SD VARCHAR(100),BAF_drift VARCHAR(100),WF VARCHAR(100),NumCNV VARCHAR(100),Quality_Score VARCHAR(100),MaleOrNot VARCHAR(100),Age VARCHAR(100))' % n)
    

   
    # q = ("SELECT * FROM cnvs1%s" % (n-1))
    # cur.execute(q)
    # f=cur.fetchall() 
    # if len(f)!=0:  
    #     #print ("%s: chr%s %s-%s\n" % (p+1,f[0][3],f[0][4],f[0][5]))
    #     for fa in f:
    #         p=random.randrange(1,10001)
    #         cnv = [p, p, fa[3], fa[4], fa[5], fa[6], fa[7], fa[8], fa[9], fa[10], fa[11], fa[12], fa[13], fa[14], fa[15], fa[16], fa[17], 0, fa[19], 0, 0]
    #         q = "INSERT INTO cnvs1%s (SampleNameShort, Sample_Name, Chromosome, Start_Position_bp, End_Position_bp, Copy_Number, Max_Log_BF, Length_bp, No_Probes, LRR_mean, LRR_median, LRR_SD, BAF_mean, BAF_median, BAF_SD, BAF_drift, WF, NumCNV, Quality_Score, MaleOrNot, Age) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" % n
    #         cur.execute(q,(cnv))

    q = ("INSERT INTO cnvs2%s SELECT * FROM cnvs1%s" % (n, n-1))
    cur.execute(q)

    q = ("SELECT * FROM cnvs2%s" % (n))
    cur.execute(q)
    f=cur.fetchall() 
    if len(f)!=0:  
        #print ("%s: chr%s %s-%s\n" % (p+1,f[0][3],f[0][4],f[0][5]))
        for fa in f:
            p=random.randrange(1,10001)
            q=("UPDATE cnvs2%s SET SampleNameShort = %s  WHERE id = %s" % (n,p,fa[0]))
            cur.execute(q)




    # посчитать зарактеристики



    narr=[]
    larr=[]

    for i in range(1,10001):
        q = ("SELECT * FROM cnvs2%s WHERE SampleNameShort=%s" % (n, i))
        cur.execute(q)
        f=cur.fetchall() 
        if len(f)!=0:  
            #print ("%s: chr%s %s-%s\n" % (p+1,f[0][3],f[0][4],f[0][5]))
            ncnv=0.0
            lcnv=0.0
            for t in f:
                
                ncnv = ncnv + 1
                lcnv = lcnv + int(t[8])
            narr.append(ncnv)
            larr.append(lcnv)

            
    

    
    out.write("%s;%f;%f\n" % (n,median(narr),median(larr)))
            


    # удалить старую таблицу





con.commit()
con.close()












# stat = np.array(statarr)                
    
# fig = plt.figure()


# # Histogram
# plt.hist(stat,100)
# plt.title('CNV Nums')
# plt.grid(True)
# plt.savefig('cnvhist.png', dpi = 300)


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