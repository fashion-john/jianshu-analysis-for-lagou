# -*- coding: UTF-8 -*-
import pandas as pd
filename = 'C:/Users/john/Desktop/JobRequirementAnalysis-master/cache/position_after_cleaning.csv'
outputfile = 'C:/Users/john/Desktop/JobRequirementAnalysis-master/cache/position_final2.csv'
# data = pd.read_csv(filename,encoding='utf8',header=None)
# print(data)
content = []
data = open(filename, encoding='utf8')
for i in data.readlines():
    i = i.strip().split(' ')
    content.append(i)
final = {}
positionId = []
city = []
industyField = []
companyShortName = []
companySize = []
financeStage = []
education = []
workYear = []
positionName = []
salary = []
requirement = []
for content_one_by_one in content:
    positionId.append(content_one_by_one[0].replace('"', ''))
    city.append(content_one_by_one[1].replace('"', ''))
    industyField.append(content_one_by_one[2].replace('"', ''))
    companyShortName.append(content_one_by_one[3].replace('"', ''))
    companySize.append(content_one_by_one[4].replace('"', ''))
    financeStage.append(content_one_by_one[5].replace('"', ''))
    education.append(content_one_by_one[6].replace('"', ''))
    workYear.append(content_one_by_one[7].replace('"', ''))
    positionName.append(content_one_by_one[8].replace('"', ''))
    salary.append(content_one_by_one[9].replace('"', ''))
    requirement.append(content_one_by_one[10].replace('"', ''))
final = {'positionId': positionId, 'city': city, 'industyField': industyField, 'companyShortName': companyShortName,
         'companySize': companySize, 'financeStage': financeStage, 'education': education, 'workYear': workYear,
         'positionName': positionName, 'salary': salary, 'requirement': requirement}
frame = pd.DataFrame(final)
frame.to_csv(outputfile,encoding='utf8')
