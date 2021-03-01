german_data = credit
german_data.head()

#Cleaning data
german_data.chk_acct.replace(['A11','A12','A13','A14'],['little', 'moderate','rich', 'no checking account'], inplace = True)
german_data.credit_his.replace(['A30','A31','A32','A33','A34'],['no credits taken',
                                                               'all credits paid duly',
                                                               'existing credits paid duly',
                                                               'delay in paying off in the past',
                                                               'other credits existing'], inplace=True)
german_data.purpose.replace(['A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A410'], 
                            ['car (new)','car (used)', 'furniture/equipment','radio/television',
                             'domestic appliances','repairs', 'education', 'vacation', 'retraining',
                             'business', 'others'], inplace=True)
german_data.saving_acct.replace(['A61','A62','A63','A64','A65'], 
                                ['little', 'moderate', 'rich','quite rich','no savings account'], inplace=True)
german_data.present_emp.replace(['A71','A72','A73','A74','A75'], 
                                ['unemployed', '< 1yr', '>=1yr & <4yr', '>=4yr & <7yr','>=7yr'], inplace=True)
german_data.sex.replace(['A91','A92','A93','A94','A95'], 
                        ['male : divorced', 'female : divorced/married', 
                         'male : single', 'male : married/widowed', 'female : single'], inplace=True)
german_data.other_debtor.replace(['A101','A102','A103'], 
                                 ['none', 'co-applicant', 'guarantor'], inplace=True)
german_data.property.replace(['A121','A122','A123','A124'],
                             ['real estate', 'building/life insurance', 'car/others',
                             'unknown/no property'], inplace=True)
german_data.other_install.replace(['A141','A142','A143'],['bank', 'stores', 'none'], inplace=True)
german_data.housing.replace(['A151','A152','A153'],['rent','own','free'], inplace=True)
german_data.job.replace(['A171','A172','A173','A174'],
                        ['unskilled - non-resident', 'unskilled - resident', 
                         'skilled employee', 'self-employed'],inplace=True)
german_data.telephone.replace(['A191','A192'],['none', 'yes'], inplace=True)
german_data.foreign.replace(['A201','A202'],['yes','no'], inplace=True)
german_data.response.replace([1,2], [1,0], inplace=True)

#Checking the data
german_data.head()


#Checking missing values in the data 
print("Missing values in each column:\n{}".format(german_data.isnull().sum()))


