# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import chardet
import sys
sns.set_style('whitegrid',{'font.sans-serif':['simhei','Arial']})
filename = 'C:/Users/john/Desktop/JobRequirementAnalysis-master/cache/position_final2.csv'
data = pd.read_csv(filename)
# ---------------第一部分--------------
# print(data['city'].unique())
# print(data[data['city']=='北京'].shape[0])
city_name = data['city'].unique()
# city_job_count = []
# for name in city_name:
#     city_job_count.append(data[data['city'] == name].shape[0])
# print(city_name)
# print(city_job_count)
# city_info = dict(zip(city_name, city_job_count))
# frame = pd.DataFrame([city_info])
# plt.figure(figsize=(10,10))
# sns.barplot(city_name,city_job_count)
# plt.show()
# ----------------------------------
# -----------------第二部分---------------
# print(data['financeStage'].unique())
company_financeStage_name=data['financeStage'].unique()
company_financeStage_count=[]
for name in company_financeStage_name:
    company_financeStage_count.append(data[data['financeStage']==name].shape[0])
plt.figure(figsize=(20,20))
sns.factorplot(x='workYear',kind='count',data=data,col='financeStage',col_wrap=2,legend=True)
plt.show()
