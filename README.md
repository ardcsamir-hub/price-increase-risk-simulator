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

## Key Results

The churn-based pricing simulator evaluated price increase scenarios from 0% to 15%.

| Price Increase | Avg. Churn Risk | Expected Revenue | High-Risk Customers |
|---:|---:|---:|---:|
| 0% | 26.6% | $316,162 | 982 |
| 3% | 26.8% | $324,687 | 1,010 |
| 5% | 26.9% | $330,338 | 1,024 |
| 8% | 27.0% | $338,767 | 1,039 |
| 10% | 27.1% | $344,353 | 1,049 |
| 15% | 27.4% | $358,206 | 1,078 |

## Best Scenario

The 15% price increase scenario generated the highest expected revenue:

- Expected revenue: $358,206
- Incremental revenue vs. baseline: $42,044
- Average churn risk: 27.4%
- Churn risk increase vs. baseline: +0.8 percentage points
- Additional high-risk customers: +96

## Segment-Level Findings

The strongest candidates for price increases were loyal customers with one-year or two-year contracts, especially those with low predicted churn risk.

Examples of low-risk segments identified by the simulator:

| Contract | Tenure Segment | Price Segment | Internet Service | Customers | Avg. Churn Risk | Price Increase | Recommendation |
|---|---|---|---|---:|---:|---:|---|
| Two year | Loyal | High price | Fiber optic | 386 | 7.4% | 15% | Apply increase |
| Two year | Loyal | Mid-high price | DSL | 270 | 2.1% | 15% | Apply increase |
| Two year | Loyal | Mid-low price | DSL | 244 | 1.5% | 15% | Apply increase |
| Two year | Loyal | Low price | No | 463 | 0.5% | 15% | Apply increase |
| One year | Loyal | High price | Fiber optic | 383 | 19.1% | 15% | Apply increase |

## Business Recommendation

The analysis suggests that price increases should be applied selectively rather than uniformly.

Loyal customers with one-year or two-year contracts show lower churn risk and are stronger candidates for higher price increases. New customers and month-to-month customers should be treated more carefully, using control groups or retention actions before applying aggressive price increases.

The recommended strategy is to prioritize price increases for low-risk loyal segments while testing moderate increases in medium-risk groups.

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