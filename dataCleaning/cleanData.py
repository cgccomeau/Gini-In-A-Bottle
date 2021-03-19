import csv
import os
import pandas as pd 



# with open('2011data.csv', 'w', newline='') as csvfile:

    # fieldnames = ['CountryName', 'GiniCoff', 'IncomePerPeerson', 'InvestmentShareOfGDP', 'TaxShareOfGDP']
    # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # writer.writeheader()

    # with open('combined_final_last_10_years.csv', newline='') as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         # print(row['country'])
    #         if row['year'] == '2011':
    #             # print(row['country'])
    #             writer.writerow({'CountryName': row['country'], 
    #                             'GiniCoff': row['gini_index'], 
    #                             'IncomePerPeerson': row['income_per_person'], 
    #                             'InvestmentShareOfGDP': row['invest_%_gdp'], 
    #                             'TaxShareOfGDP': row['tax_%_gdp']})
    



# for filename in os.listdir('./rawSets'):
#     f = open('./rawSets/' + filename,'r')
#     reader = csv.DictReader(f)
#     ncol = len(next(reader))
#     if ncol == 4:
#         f.seek(0)
#         header = reader.fieldnames
#         print(header[3])
#         with open('temp.csv', 'w', newline='') as tempfile:  
#             fieldnames = ['CountryName', header[3]]
#             writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
#             writer.writeheader()
#             for row in reader:
#                 if row['Year'] == '2011':
#                     writer.writerow({'CountryName': row['Entity'], 
#                                 header[3]: row[header[3]]})
#         data1 = pd.read_csv('2011data.csv',engine='python') 
#         data2 = pd.read_csv('temp.csv',engine='python')   
            
#         output4 = pd.merge(data1, data2,  
#                 on='CountryName',  
#                 how='outer') 
#         # print(output4)
#         output4.to_csv('2011data.csv',index=False)



count = 0
with open('2011data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        trash = ["UN Population Division (Median Age) (2017)", 
                "Estimated average age at marriage, women",
                "Number of people employed in agriculture  (Herrendorf et al. data)",
                "Tax Revenue (Piketty (2014))",
                "Public Expenditure on Education (Tanzi & Schuktnecht (2000))",
                "Income share held by highest 10%"]
        headers = [ele for ele in headers if ele not in trash] 
        for row in reader:
            # ncol = len(next(reader))
            # print(ncol)
            temp = True
            for i in range(len(headers)):
                if row[headers[i]] == '':
                    temp = False
            if temp == True:
                count += 1
    
print(count)
