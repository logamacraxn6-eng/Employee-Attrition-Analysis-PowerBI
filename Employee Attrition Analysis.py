# Employee Attrition Analysis & Prediction
# Power BI + Python portfolio project

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"E:\11524040264\Employee Attrition Analysis\data\employee_attrition.csv")
df.head()

# Data Overview
print(df.shape)
print(df.isna().sum().sum(), 'missing values')
print(df['Attrition'].value_counts())

# Exploratory Data Analysis
df.groupby('Department')['Attrition_Flag'].mean().sort_values(ascending=False)
df.groupby('OverTime')['Attrition_Flag'].mean().sort_values(ascending=False)
df.groupby('Salary_Slab')['Attrition_Flag'].mean().sort_values(ascending=False)
   
# Logistic Regression Model

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
X = df.drop(columns=['Attrition','Attrition_Flag'])
y = df['Attrition_Flag']
cat = X.select_dtypes(include=['str','category']).columns.tolist()
num = [c for c in X.columns if c not in cat]
pre = ColumnTransformer([('cat',OneHotEncoder(handle_unknown='ignore'),cat),('num',StandardScaler(),num)])
model = Pipeline([('pre',pre),('clf',LogisticRegression(max_iter=1000,class_weight='balanced'))])
Xtr,Xte,ytr,yte = train_test_split(X,y,test_size=.2,random_state=42,stratify=y)
model.fit(Xtr,ytr)
pred=model.predict(Xte); prob=model.predict_proba(Xte)[:,1]
print('Accuracy:',accuracy_score(yte,pred))
print('Precision:',precision_score(yte,pred))
print('Recall:',recall_score(yte,pred))
print('F1:',f1_score(yte,pred))
print('ROC-AUC:',roc_auc_score(yte,prob))


