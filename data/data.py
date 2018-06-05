# Data modules
import pandas as pd
import re
import math
from definitions import ROOT_DIR


def get_data():
    # Read the data into pandas df
    accepted = pd.read_csv(ROOT_DIR + '/data/LoanStats_2018Q1.csv', skiprows = 1, header=0)
    rejected = pd.read_csv(ROOT_DIR + '/data/RejectStats_2018Q1.csv', skiprows = 1, header=0)

    # Variables we will use as inputs, found using set difference
    accepted_col_list = ['loan_amnt', 'title', 'dti', 'emp_length']
    rejected_col_list = ['Amount Requested', 'Loan Title', 'Debt-To-Income Ratio', 'Employment Length']

    accepted = accepted[accepted_col_list]
    rejected = rejected[rejected_col_list]
    # Rename columns to match
    rejected.columns = accepted_col_list

    # Drop dummy/invalid rows
    accepted.drop(accepted.tail(2).index,inplace=True)
    accepted = accepted.loc[accepted.emp_length > 0]
    accepted = accepted.loc[accepted.dti > 0]
    rejected = rejected.loc[rejected.emp_length > 0]

    rejected.title = rejected.title.apply(format_title)

    # Get same number of samples from both classes to avoid data skew
    rejected = rejected.sample(len(accepted))

    # Add the Y column
    rejected['accepted'] = 0
    accepted['accepted'] = 1

    # Put all the data together
    all_loans = pd.concat([rejected, accepted])

    # Shuffle all of the elements
    all_loans = all_loans.sample(frac=1).reset_index(drop=True)

    # Format the columns using helper functions
    all_loans.dti = all_loans.dti.apply(format_dti)
    all_loans.emp_length = all_loans.emp_length.apply(parse_employment_length)
    all_loans.loan_amnt = all_loans.loan_amnt.apply(scale_loan_amount)

    # One hot encode the loan titles
    one_hot = pd.get_dummies(all_loans.title)
    all_loans.drop('title',axis = 1, inplace =True)
    all_loans = all_loans.join(one_hot)

    X = all_loans.loc[:, all_loans.columns != 'accepted'].values
    Y = all_loans.loc[:, all_loans.columns == 'accepted'].values

    return X, Y


# Scaled to [0,1] by dividing by the max
# TODO: Change to use min/max scaler
def scale_loan_amount(s):
    return s/300000.0


def catch_nan(s):
    return type(s) == str or not math.isnan(s)


# Remove % sign from Debt to Income Ratio (rejected) and scale (assume range of 0-100%)
def format_dti(dti):
    if type(dti) == float:
        return dti/100
    return float(dti[:-1])/100


# Assumes the string contains a single integer at some point
# Extract int using regular expression, scale it to [0,1]
# TODO: try one-hot encoding
def parse_employment_length(s):
    if '<' in s:
        return 0.5/10
    return float(re.search(r'\d+', s).group())/10


# Change Loan Title strings to match accepted categories
# Rejects: Business Loan -> Business, other -> Other
def format_title(title):
    if title == 'Business Loan':
        return 'Business'
    if title == 'other':
        return 'Other'
    return title
