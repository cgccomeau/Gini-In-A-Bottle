import csv
import os
import pandas as pd 


# clean gini file
# with open('MultiYearData.csv', 'w', newline='') as csvfile:

#     fieldnames = ['CountryName', 'Year', 'GiniCoff', 'IncomePerPeerson', 'InvestmentShareOfGDP', 'TaxShareOfGDP']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()

#     with open('combined_final_last_10_years.csv', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             # print(row['country'])
#             writer.writerow({'CountryName': row['country'],
#                                 'Year': row['year'], 
#                                 'GiniCoff': row['gini_index'], 
#                                 'IncomePerPeerson': row['income_per_person'], 
#                                 'InvestmentShareOfGDP': row['invest_%_gdp'], 
#                                 'TaxShareOfGDP': row['tax_%_gdp']})
    


# # clean files from our world in data
# for filename in os.listdir('./rawSets'):
#     f = open('./rawSets/' + filename,'r')
#     reader = csv.DictReader(f)
#     # print(filename)
#     if filename[-4:-1] == '.cs':
#         ncol = len(next(reader))
        
#         if ncol == 4:
#             f.seek(0)
#             header = reader.fieldnames
#             print(header[3])
#             with open('temp.csv', 'w', newline='') as tempfile:  
#                 fieldnames = ['CountryName', 'Year', header[3]]
#                 writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
#                 writer.writeheader()
#                 for row in reader:
#                     # print(row)
#                     if row['Entity'] != 'Entity':
#                         writer.writerow({'CountryName': row['Entity'],
#                                     'Year': row['Year'],
#                                     header[3]: row[header[3]]})
                
#             data1 = pd.read_csv('MultiYearData.csv',engine='python') 
#             data2 = pd.read_csv('temp.csv',engine='python')   
#             # data2.drop('Entity')
                
#             output4 = pd.merge(data1, data2,  
#                     on=['CountryName', 'Year'],  
#                     how='left') 
#             # print(output4)
#             output4.to_csv('MultiYearData.csv',index=False)



# count effective number of countries
# result: 102
# count = 0
# with open('2011data.csv', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         headers = reader.fieldnames
#         trash = ["UN Population Division (Median Age) (2017)", 
#                 "Estimated average age at marriage, women",
#                 "Number of people employed in agriculture  (Herrendorf et al. data)",
#                 "Tax Revenue (Piketty (2014))",
#                 "Public Expenditure on Education (Tanzi & Schuktnecht (2000))",
#                 "Income share held by highest 10%",
#                 "Pupil-teacher ratio in primary education (headcount basis)"]
#         headers = [ele for ele in headers if ele not in trash] 
#         for row in reader:
#             # ncol = len(next(reader))
#             # print(ncol)
#             temp = True
#             for i in range(len(headers)):
#                 if row[headers[i]] == '':
#                     temp = False
#             if temp == True:
#                 count += 1
    
# print(count)



# clean Multi
# df = pd.read_csv('2011data.csv')
# df.to_csv('cleaned2011data.csv')

lines = list()
with open('MultiYearData.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    headers = reader.fieldnames
    trash = ['UN Population Division (Median Age) (2017)', 
            'Estimated average age at marriage, women',
            'Number of people employed in agriculture  (Herrendorf et al. data)',
            'Tax Revenue (Piketty (2014))',
            'Public Expenditure on Education (Tanzi & Schuktnecht (2000))',
            'Income share held by highest 10%',
            'Pupil-teacher ratio in primary education (headcount basis)']
    headers = [ele for ele in headers if ele not in trash] 
    with open('allFilledMultiYearData.csv', 'w') as writeFile:
        writer = csv.DictWriter(writeFile, reader.fieldnames)
        writer.writeheader()
        for row in reader:
            
            temp = True
            for i in range(len(headers)):
                if row[headers[i]] == '':
                    temp = False
            if temp == True:
                # print(row)
                # lines.append(row)
                writer.writerow(row)
                # writer.writerows({reader.fieldnames[i]:row[reader.fieldnames[i]] for i in range(len(reader.fieldnames))})
# print(lines)

    


newdf = pd.read_csv('allFilledMultiYearData.csv')
newdf.drop(['UN Population Division (Median Age) (2017)', 
    'Estimated average age at marriage, women',
    'Number of people employed in agriculture  (Herrendorf et al. data)',
    'Tax Revenue (Piketty (2014))',
    'Public Expenditure on Education (Tanzi & Schuktnecht (2000))',
    'Income share held by highest 10%',
    'Pupil-teacher ratio in primary education (headcount basis)'],axis=1,inplace=True) 
newdf.to_csv('allFilledMultiYearData.csv')
