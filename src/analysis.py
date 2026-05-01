import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("data/cleaned_loan_data.csv")

print("First rows of dataset:")
print(df.head())


# Approval rate by Gender
print("\nApproval Rate by Gender:")
gender_approval = df.groupby("Gender")["Loan_Status"].value_counts(normalize=True).unstack()
print(gender_approval)

sns.countplot(x="Gender", hue="Loan_Status", data=df,palette=["purple","pink"])
plt.title("Loan Approval by Gender")
plt.show()


# Approval rate by Employment
print("\nApproval Rate by Employment:")
employment_approval = df.groupby("Self_Employed")["Loan_Status"].value_counts(normalize=True).unstack()
print(employment_approval)

sns.countplot(x="Self_Employed", hue="Loan_Status", data=df,palette=["purple","pink"])
plt.title("Loan Approval by Employment")
plt.show()


# Approval rate by Credit History
print("\nApproval Rate by Credit History:")
credit_approval = df.groupby("Credit_History")["Loan_Status"].value_counts(normalize=True).unstack()
print(credit_approval)

sns.countplot(x="Credit_History", hue="Loan_Status", data=df,palette=["purple","pink"])
plt.title("Loan Approval by Credit History")
plt.show()
