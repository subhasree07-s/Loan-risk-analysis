Loan Risk Analysis & Approval Prediction

A data-driven project that analyzes loan applicant data to identify key factors affecting loan approval and classify applicants into risk categories using statistical and exploratory analysis.


Overview

This project focuses on understanding loan approval behavior by analyzing applicant data such as income, credit history, employment status, and loan amount.


The goal is to:

* Identify patterns influencing loan approval
* Detect high-risk applicants
* Support better decision-making in financial systems 

Key Features

* Exploratory Data Analysis (EDA)
* Data Cleaning & Preprocessing
* Visualization using Seaborn & Matplotlib
* Statistical Testing (Chi-Square, Correlation)
* Risk Classification Model
* Insight generation for loan approval trends


Analysis Approach

Data Preprocessing

* Handled missing values (Mode & Median)
* Encoded categorical variables
* Removed irrelevant columns
* Converted inconsistent data formats 

Data Transformation

* Converted categorical values (e.g., `3+ → 3`)
* Encoded Loan Status (Y → 1, N → 0)
* Prepared clean dataset for analysis
  

Exploratory Analysis

The project analyzes key factors affecting loan approval:

* Gender
* Employment Status
* Credit History


Key Observations

* Gender has no significant impact on approval
* Employment status has minimal effect
* Credit history has a strong influence on loan approval 


Statistical Analysis

Chi-Square Test

* Gender vs Loan Approval → Not significant
* Credit History vs Loan Approval → Highly significant

Correlation Analysis

* Income vs Loan Amount → Moderate positive relationship (≈ 0.56) 

Risk Classification

Applicants are categorized based on:


Risk Categories

* Low Risk → Good credit + low ratio
* Medium Risk → Good credit + moderate ratio
* High Risk → Poor credit or high ratio 

Results

* Low Risk → ~79% approved
* High Risk → ~92% rejected
* Medium Risk → ~100% approved

Risk classification aligns closely with actual loan approval patterns 


Project Structure

loan-risk-analysis/
│
├── data/
├── src/
│   ├── cleaning.py
│   ├── analysis.py
│   ├── risk_analysis.py
│   ├── statistics_test.py
│
├── outputs/
├── requirements.txt
└── README.md




Key Insights

* Credit history is the **most important factor**
* Income has a **moderate influence**
* Gender & employment have **minimal impact**
* Risk grouping effectively predicts loan behavior 

My Contribution

* Performed data cleaning & preprocessing
* Conducted exploratory data analysis
* Implemented statistical testing (Chi-Square, Correlation)
* Designed risk classification model
* Generated insights & visualizations

 Future Improvements

* Apply machine learning models for prediction
* Use larger real-world datasets
* Build a web interface for user interaction
* Deploy as a financial decision-support tool



