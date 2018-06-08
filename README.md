# a-loan-decision
Analyzing and making predictions about loan data

# Can I get a loan?

## The Idea

Can we predict whether or not you will be given a loan based on some metrics?
Current (handpicked) metrics:
1.  Loan Type
2.  Amount Requested
3.  Debt to Income Ratio
4.  Employment Length

## The Models

1.  Neural Network (3 layers)
2.  Random Forest

## The Result

Achieving consistent 93% - 95% accuracy on test set, the Random Forest (mostly) sees employment length as the most important feature

## The Data
Lending Club, 2018 Q1
[Download files from here](https://www.lendingclub.com/info/download-data.action)

Copy the csv files into the data directory or curl/wget:

```bash
cd data
curl https://resources.lendingclub.com/LoanStats_2018Q1.csv.zip -o LoanStats_2018Q1.csv.zip
curl https://resources.lendingclub.com/RejectStats_2018Q1.csv.zip -o RejectStats_2018Q1.csv.zip
```

## Further setup
From root directory,
```bash
make
```
This will install the required packages.
You can now run
```bash
python run.py
```
or to see what arguments can be passed in:
```bash
python run.py -h
```

## Testing
Testing in test directory. Set up Travis in future, for now from root directory:
```bash
make test
```
or

```bash
pytest
```