import csv
import os
import random as r
import pandas as pd


stats = []
uid_range = 10
iid_range = 10
ratings_range = 5


# edit it to desired folder name
path = ""
# headers for interaction CSVs
headers = ['uid','iid','ratings']
# header for stats
stats_headers = ['file_size','time_taken']


for i in [x*x for x in range(1,10**2) if x%10==0]:
    pd.DataFrame([[str(r.randrange(int(uid_range+i/50))),str(r.randrange(int(iid_range+i/80))),str(r.randrange(ratings_range))] for each in range(i)],columns=headers).to_csv('the_data/input'+str(i)+'.csv',index=False)
    stats.append([os.path.getsize(path+'/input'+str(i)+'.csv'),0])
    
pd.DataFrame(stats,columns = stats_headers).to_csv(path+"/stats.csv",index=False)