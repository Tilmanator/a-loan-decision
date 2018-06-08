import pandas as pd
import matplotlib.pyplot as plt


def explore():
    # Read the data into pandas df
    accepted = pd.read_csv('LoanStats_2018Q1.csv', skiprows=1, header=0)
    rejected = pd.read_csv('RejectStats_2018Q1.csv', skiprows=1, header=0)

    # Loan Title
    f = plt.figure(1)
    accepted['title'].value_counts().plot(kind='bar')
    f.show()

    g = plt.figure(2)
    rejected['Loan Title'].value_counts().plot(kind='bar')
    g.show()

    # Visually comparing these two, we see some similar trends
    # Most people want debt consolidation; this is the highest category in both accepted and rejected loans
    # "Other" categories seem much more likely to be rejected however...
    raw_input()

    # Employment Length
    f = plt.figure(1)
    accepted['emp_length'].value_counts().plot(kind='bar')
    f.show()

    g = plt.figure(2)
    rejected['Employment Length'].value_counts().plot(kind='bar')
    g.show()

    # This is very clearly highly related to getting your loan approved
    raw_input()

    # Let's see what percentage of rejected loans happen when employed under 1 year:
    pct = 100.0*len(rejected[rejected['Employment Length'] == '< 1 year'].index)/rejected['Employment Length'].count()
    print "%.2f%% of rejections are employed < 1 year" % (pct)


if __name__ == '__main__':
    explore()