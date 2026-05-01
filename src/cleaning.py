import pandas as pd
import numpy as np

df = pd.read_csv("data/train.csv")

print(df.isnull().sum())

# categorical columns
df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
df['Married'] = df['Married'].fillna(df['Married'].mode()[0])
df['Dependents'] = df['Dependents'].fillna(df['Dependents'].mode()[0])
df['Self_Employed'] = df['Self_Employed'].fillna(df['Self_Employed'].mode()[0])

# numeric columns
df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())
df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].median())

# credit history
df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].mode()[0])

# fix dependents column
df['Dependents'] = df['Dependents'].replace('3+', 3).astype(int)

# convert target variable
df['Loan_Status'] = df['Loan_Status'].map({'Y':1, 'N':0})

# drop unnecessary column
df = df.drop("Loan_ID", axis=1)

# save cleaned dataset
df.to_csv("data/cleaned_loan_data.csv", index=False)