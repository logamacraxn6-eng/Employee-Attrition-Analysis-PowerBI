# Employee Attrition Analysis & Prediction

## Project Overview
This project analyzes employee attrition patterns and builds a simple classification model to identify factors associated with employee turnover. The project is designed for **Power BI + Python** and is suitable for a data analytics / data science internship portfolio.

The dataset contains **1,470 employee records** and includes demographic, job, compensation, satisfaction, travel, overtime and tenure attributes.

> **Dataset note:** This project package uses a reproducible synthetic HR dataset generated for portfolio/learning purposes, modeled on the structure of the widely used IBM HR Analytics Employee Attrition dataset. It does not claim to contain real employee records.

## 🎯 Objectives
- Measure overall employee attrition.
- Identify departments and job roles with higher turnover.
- Analyze the relationship between overtime, salary, satisfaction and attrition.
- Create an interactive Power BI HR dashboard.
- Build a Logistic Regression model as a baseline attrition classifier.
- Provide practical HR retention recommendations.

## 🛠️ Tools
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Microsoft Power BI
- DAX

## 📁 Project Structure
```text
Employee_Attrition_PowerBI_Project/
├── data/
│ └── employee_attrition.csv
├── notebooks/
│ └── employee_attrition_analysis.ipynb
├── powerbi/
│ ├── DAX_Measures.md
│ └── POWER_BI_BUILD_GUIDE.md
├── reports/
│ └── model_metrics.csv
└── README.md
```

## 📊 Key Dashboard KPIs
- Total Employees
- Employees Left
- Attrition Rate
- Average Age
- Average Monthly Income
- Average Tenure

## 🤖 Model Evaluation
The baseline model is Logistic Regression with one-hot encoding, scaling and balanced class weights.

| Metric | Score |
|---|---:|
| Accuracy | 0.789 |
| Precision | 0.065 |
| Recall | 0.500 |
| F1 Score | 0.114 |
| ROC-AUC | 0.661 |

These scores are included as a baseline demonstration; they should not be interpreted as a production HR decision system.

## 💡 Business Insights
The analysis is intended to help HR teams:
1. Identify employee groups with elevated attrition.
2. Monitor overtime-related turnover.
3. Examine early-tenure retention.
4. Compare attrition across departments and job roles.
5. Review salary and satisfaction patterns before designing retention actions.

## 🚀 How to Use
### Python
```bash
pip install pandas numpy scikit-learn matplotlib jupyter
jupyter notebook notebooks/employee_attrition_analysis.ipynb
```

### Power BI
Follow `powerbi/POWER_BI_BUILD_GUIDE.md` to create the dashboard and save the final `.pbix` file.

## ⚠️ Responsible Use
Employee attrition predictions should support—not replace—human judgment. Avoid using demographic attributes as the sole basis for employment decisions. Treat employee data as confidential and use appropriate privacy controls.

## 📚 Dataset Context
The dashboard design is inspired by common HR analytics questions around attrition, distance from home, job role, compensation and employee satisfaction. The popular IBM HR Analytics dataset has 1,470 records and 35 columns and is described as a fictional dataset created by IBM data scientists. See the project references below.

## References
- IBM HR Analytics dataset context: https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset
- Power BI reference implementation examples can be found on GitHub.
