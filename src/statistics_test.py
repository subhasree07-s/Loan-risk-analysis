import pandas as pd
from scipy.stats import chi2_contingency

# Load dataset
df = pd.read_csv("data/cleaned_loan_data.csv")


# Chi-square test: Gender vs Loan Approval
print("\nChi-square Test: Gender vs Loan Approval")

table = pd.crosstab(df["Gender"], df["Loan_Status"])

chi2, p, dof, expected = chi2_contingency(table)

print("Chi2:", chi2)
print("p-value:", p)

if p < 0.05:
    print("Gender and Loan Approval are related")
else:
    print("No significant relationship")


# Chi-square test: Credit History vs Loan Approval
print("\nChi-square Test: Credit History vs Loan Approval")

table2 = pd.crosstab(df["Credit_History"], df["Loan_Status"])

chi2, p, dof, expected = chi2_contingency(table2)

print("Chi2:", chi2)
print("p-value:", p)

if p < 0.05:
    print("Credit History significantly affects Loan Approval")
else:
    print("No significant relationship")


# Correlation test: Income vs Loan Amount
print("\nCorrelation: Income vs Loan Amount")

correlation = df["ApplicantIncome"].corr(df["LoanAmount"])

print("Correlation value:", correlation)