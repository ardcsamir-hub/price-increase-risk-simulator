# Price Increase Risk Simulator: Churn-Based Pricing Strategy

## Business Problem

Companies often need to increase prices, but applying the same increase to all customers can increase churn risk. This project simulates different price increase scenarios and identifies which customer segments can tolerate higher prices with lower churn risk.

## Objective

Build a churn-based pricing simulator to estimate the impact of price increases on customer churn risk and expected revenue.

## Dataset

Telco Customer Churn dataset.

Main variables used:

- Customer tenure
- Monthly charges
- Total charges
- Contract type
- Payment method
- Internet service
- Tech support
- Churn

## Methodology

1. Data cleaning and preprocessing
2. Exploratory churn analysis
3. Customer segmentation by price and tenure
4. Churn prediction model using Logistic Regression
5. Price increase simulation from 0% to 15%
6. Segment-level pricing recommendations

## Tools

- Python
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- Jupyter Notebook

## Key Deliverables

- Churn prediction model
- Price increase scenario simulation
- Segment-level pricing recommendations
- Executive business insights

## Business Recommendation

Price increases should not be applied uniformly. Loyal customers with long-term contracts are better candidates for higher increases, while month-to-month and new customers should receive retention actions before any pricing change.

## Repository Structure

```text
price-increase-risk-simulator/
│
├── data/
├── notebooks/
├── outputs/
├── README.md
├── requirements.txt
└── .gitignore