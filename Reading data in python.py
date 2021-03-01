url = "https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data"
credit = pd.read_csv(url, sep= " ", names = ["chk_acct", "duration", "credit_his", "purpose","amount", 
                                             "saving_acct", "present_emp", "installment_rate", "sex", 
                                             "other_debtor", "present_resid", "property", "age", 
                                             "other_install", "housing", "n_credits", "job", "n_people", 
                                             "telephone", "foreign","response"])

credit.head()

credit.info()
