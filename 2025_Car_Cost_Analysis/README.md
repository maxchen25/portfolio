# Excel Basics: 2025 Car Cost Analysis

## Project Overview

This project was created to help my dad figure out which new car to buy by comparing total ownership costs across various models and powertrains.

## Questions Being Answered

- What car should we buy?
- Which type of vehicle (Gas, Hybrid, EV) offers the best value over time?

## Data Source

- I gathered the data myself from the following websites:
  - [Honda](https://www.honda.com/)
  - [Toyota](https://www.toyota.com/)
  - [Tesla](https://www.tesla.com/)
  - [Hyundai](https://www.hyundaiusa.com/)
  - [Ford](https://www.ford.com/)
  - [FuelEconomy.gov](https://www.fueleconomy.gov/)
  - [Edmunds TCO Tool](https://www.edmunds.com/tco.html)
- Missing data was estimated using **Gemini 2.0**

## Tools and Skills Used

- **Tool**: Microsoft Excel

**Skills Applied**:

- Pivot Tables
- Slicers
- Conditional Formatting (Heatmaps)
- Charting & Visualization
- Functions: `FILTER`, `CHOOSECOLS`, `IFERROR`, and more

## Project Workflow

1. Gathered and manually entered car data into Excel
2. Performed data cleaning and structuring
3. Built pivot tables and applied filters/slicers
4. Created visualizations to analyze trends
5. Highlighted cost drivers using heatmaps

## Key Insights

- **MSRP strongly predicts 5-Year TCO**: R² = 0.9077
- **Fuel costs** are a small portion of 5-Year TCO and don’t significantly affect overall cost
- **Gas cars** are generally the cheapest, followed by hybrids, then EVs
- **Hybrid and EVs** offer much better MPG (or MPGe)
- **Tesla** vehicles have the highest depreciation by far
- **Tax credits** can greatly reduce or eliminate 5-Year ownership costs, especially for EVs

## Question Answered

To save money, buying a **gas or hybrid car** is the best option. **EVs are expensive**, especially when considering depreciation. Used hybrids are likely the best value, as they balance fuel savings with lower upfront cost. Ultimately, **MSRP is the strongest factor** in predicting long-term cost.

## Visuals

![Screenshot](./project_screenshot)

## What I Learned

- How to build and use Pivot Tables
- How to apply Conditional Formatting (Heatmaps)
- How to use slicers for interactive filtering
- How to write and use common Excel functions
- How to manually gather, input, and analyze real-world data
