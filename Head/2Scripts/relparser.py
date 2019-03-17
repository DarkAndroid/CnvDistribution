#coding=utf8

# Importing of libraries
import time
import timeit
import os
import sqlite3
import sys


"""
Хромосомы есть на гитхабе в body/1Raw/. 
Файл заархивированный с цифрой 02 в названии. 
Там каждая строка - одна CNV (делеция или дупликация) с ее координатами и имя человека (SampleID). 
С ними и надо играться. Давай подробности по Скайпу / телеграмме при разговоре
"""


# PARSE


# id                   "1"
# "SampleNameShort" "1000019"
# "Sample_Name" "batch_b071.1000019"
# "Chromosome" 9
# "Start_Position_bp" 5265826 
# "End_Position_bp" 5292743
# "Copy_Number" 1
# "Max_Log_BF" 17.48
# "Length_bp" 26917
# "No_Probes" 10
# "LRR_mean" 0.0154
# "LRR_median" 0
# "LRR_SD" 0.2233
# "BAF_mean" 0.4979
# "BAF_median" 0.5
# "BAF_SD" 0.0243
# "BAF_drift" 3.8e-05
# "WF" 0.0104
# "NumCNV" 4
# "Quality_Score" -0.166709908378597
# "MaleOrNot" 0
# "Age" 62





# ['1', '1000019', 'batch_b071.1000019', '9', '5265826', '5292743', '1', '17.48',
# '26917', '10', '0.0154', '0', '0.2233', '0.4979', '0.5', '0.0243', '3.8e-05', '0
# .0104', '4', '-0.166709908378597', '0', '62']
















con = sqlite3.connect('cnvdb_advance.sqlite')
cur = con.cursor()






# path = 'id.related'
# src = open(path,'r')


# #cur.execute('CREATE TABLE related (id INTEGER PRIMARY KEY, SampleNameShort VARCHAR(100))')
# #con.commit()



# pr=1

# while True: 
#     read = src.readline().strip()
#     if read=='':
#         break
    
#     print read

#     q = "INSERT INTO related (SampleNameShort) VALUES(%s)" % read
#     cur.execute(q)
#     #con.commit()


#     pr=pr+1

# con.commit()







# 1586458 -12.1725 5.39163 
# -1.28103 0.841765 -5.26521 
# -1.78657 3.10992 -2.63085 
# 2.39288 0.307537 3.3288 
# -1.9726 -0.6052 -2.04493 
# 0.548903 -3.5349 0.894739 
# -5.93925 1.00318 4.44252 
# -1.85249 -1.67193 -0.65523 
# -2.18364 0.897395 -0.274776 
# -1.37049 -1.26763 -0.872993 
# 2.37458 1.12258 0.0614056 
# -4.38268 0.526918 -2.47523 
# 2.26852 -1.17824 -4.45602 
# 2.24529 -3.55047



path = 'europeanID_pca.txt'
src = open(path,'r')



cur.execute('CREATE TABLE pca (id INTEGER PRIMARY KEY, r1 VARCHAR(100), r2 VARCHAR(100), r3 VARCHAR(100), r4 VARCHAR(100), r5 VARCHAR(100), r6 VARCHAR(100), r7 VARCHAR(100), r8 VARCHAR(100), r9 VARCHAR(100), r10 VARCHAR(100), r11 VARCHAR(100), r12 VARCHAR(100), r13 VARCHAR(100), r14 VARCHAR(100), r15 VARCHAR(100), r16 VARCHAR(100), r17 VARCHAR(100), r18 VARCHAR(100), r19 VARCHAR(100), r20 VARCHAR(100), r21 VARCHAR(100), r22 VARCHAR(100), r23 VARCHAR(100), r24 VARCHAR(100), r25 VARCHAR(100), r26 VARCHAR(100), r27 VARCHAR(100), r28 VARCHAR(100), r29 VARCHAR(100), r30 VARCHAR(100), r31 VARCHAR(100), r32 VARCHAR(100), r33 VARCHAR(100), r34 VARCHAR(100), r35 VARCHAR(100), r36 VARCHAR(100), r37 VARCHAR(100), r38 VARCHAR(100), r39 VARCHAR(100), r40 VARCHAR(100), r41 VARCHAR(100))')
con.commit()


pr=1

while True: 
    read = src.readline()
    if read=='':
        break

    cnv = read.strip().replace('"','').split(' ')

    
    q = "INSERT INTO pca (r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26, r27, r28, r29, r30, r31, r32, r33, r34, r35, r36, r37, r38, r39, r40, r41) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    cur.execute(q,(cnv))
    #con.commit()


    pr=pr+1

con.commit()



