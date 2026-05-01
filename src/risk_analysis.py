import pandas as pd

df = pd.read_csv("data/cleaned_loan_data.csv")
print("Dataset Loaded Successfully\n")


# Create Loan to Income Ratio
df["Loan_Income_Ratio"] = df["LoanAmount"] / df["ApplicantIncome"]
print("Loan to Income Ratio Created\n")

# Define Risk Groups
def classify_risk(row):

    if row["Credit_History"] == 1 and row["Loan_Income_Ratio"] < 0.2:
        return "Low Risk"

    elif row["Credit_History"] == 1 and row["Loan_Income_Ratio"] < 0.5:
        return "Medium Risk"

    else:
        return "High Risk"

df["Risk_Group"] = df.apply(classify_risk, axis=1)
print("Risk Groups Assigned\n")


# Risk Group Distribution

print("Borrower Distribution by Risk Group:")
print(df["Risk_Group"].value_counts())


# Loan Approval by Risk Group

print("\nLoan Approval Rate by Risk Group:")
approval_by_risk = pd.crosstab(df["Risk_Group"], df["Loan_Status"], normalize="index")
print(approval_by_risk)


# Rejection Rate Analysis

print("\nRejection Rate by Risk Group:")
rejection_rate = 1 - approval_by_risk[1]
print(rejection_rate)

# Income and Loan Summary

print("\nAverage Income and Loan Amount by Risk Group:")
summary = df.groupby("Risk_Group")[["ApplicantIncome", "LoanAmount"]].mean()
print(summary)