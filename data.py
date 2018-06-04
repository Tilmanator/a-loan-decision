# Data modules
import pandas as pd
import re


# Can add scaling in here? Or do it using MinMaxScaler
# Assumes the string contains a single integer at some point
# Extract int using regular expression
def parse_int_in_string(s):
    if '<' in s:
        return 0.5
    return int(re.search(r'\d+', s).group())


# Read the data into pandas df
accepted = pd.read_csv('LoanStats_2018Q1.csv', skiprows = 1, header=0)
# Efficient way to drop last 2 dummy columns
accepted.drop(accepted.tail(2).index,inplace=True)
rejected = pd.read_csv('RejectStats_2018Q1.csv', skiprows = 1, header=0)

# Playing with the data
print accepted.purpose.unique()
print accepted.pymnt_plan.unique()
parse = accepted.emp_length.head(10)

print map(parse_int_in_string, parse.values)

# Preparing data for simple reject/approval model
# Loan Title, DTI, Employment Length, Amount Requested
#set(rejected['Loan Title'].unique()) - set(accepted.title.unique())

# Loan Title
# Rejects: Business Loan -> Business
#           other -> Other
# accepted: nan -> REMOVE

# loan_amnt = Amount Requested
# title = Loan Title
# dti = Debt to Income Ratio
# emp_length - Employment Length

