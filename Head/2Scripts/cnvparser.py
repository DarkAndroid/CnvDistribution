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




path = '002.AllCnvsUnrelatedEuropeans.txt'
src = open(path,'r')


con = sqlite3.connect('cnvdb.sqlite')
cur = con.cursor()
cur.execute('CREATE TABLE cnvs (id INTEGER PRIMARY KEY, SampleNameShort VARCHAR(100),Sample_Name VARCHAR(100),Chromosome VARCHAR(100),Start_Position_bp VARCHAR(100),End_Position_bp VARCHAR(100),Copy_Number VARCHAR(100),Max_Log_BF VARCHAR(100),Length_bp VARCHAR(100),No_Probes VARCHAR(100),LRR_mean VARCHAR(100),LRR_median VARCHAR(100),LRR_SD VARCHAR(100),BAF_mean VARCHAR(100),BAF_median VARCHAR(100),BAF_SD VARCHAR(100),BAF_drift VARCHAR(100),WF VARCHAR(100),NumCNV VARCHAR(100),Quality_Score VARCHAR(100),MaleOrNot VARCHAR(100),Age VARCHAR(100))')
con.commit()


columns = src.readline().strip().replace('"','').split(' ')
pr=1

while True: 
    read = src.readline()
    if read=='':
        break

    cnv = read.strip().replace('"','').split(' ')
    print pr
    print cnv[2]
    
    q = "INSERT INTO cnvs (id, SampleNameShort, Sample_Name, Chromosome, Start_Position_bp, End_Position_bp, Copy_Number, Max_Log_BF, Length_bp, No_Probes, LRR_mean, LRR_median, LRR_SD, BAF_mean, BAF_median, BAF_SD, BAF_drift, WF, NumCNV, Quality_Score, MaleOrNot, Age) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    cur.execute(q,(cnv))
    #con.commit()


    pr=pr+1

con.commit()

# try:
#     os.mkdir(dirpath)
# except OSError:
#     print ("FOUND directory is exist")
# else:
#     print ("FOUND directory created")

















# SQLITE


# PERMUTATION