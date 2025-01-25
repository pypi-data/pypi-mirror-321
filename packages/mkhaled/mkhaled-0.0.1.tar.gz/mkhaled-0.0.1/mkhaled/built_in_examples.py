def load_built_in_examples(code_manager):
    """Load updated examples into the code manager."""

    # Example: deb
    deb_code = '''
import gradio as gr
import pandas as pd

def predict(age, bmi, blood_pressure, pa, fh, ss):
    try:
        input_data = pd.DataFrame(
            {
                "": [],  # Fill in column names
            }
        )
        for col in ['', '']:  # Add appropriate column names
            input_data[col] = le[col].transform(input_data[col])

        input_data[scale_cols] = scaler.transform(input_data[scale_cols])

        prediction = dt.predict(input_data)
        if prediction[0] == 1:
            return "Prediction: Positive"
        else:
            return "Prediction: Negative"
    except Exception as e:
        return str(e)

gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Age"),
        gr.Dropdown(choices=['Yes', 'No'], label="Example Dropdown"),
        # Add other inputs here
    ],
    outputs=gr.Textbox(label="Prediction Output")
).launch()
'''
    code_manager.save_code("deb", deb_code)

    # Example: gred
    gred_code = '''
from sklearn.model_selection import GridSearchCV

grid_param = {'max_iter': [23, 35, 50]}  # Define your parameters
grid_search_model = GridSearchCV(lo, grid_param, cv=5)
grid_search_model.fit(x_train, y_train)

print("Best Parameters:", grid_search_model.best_params_)
print("Best Score:", grid_search_model.best_score_)
'''
    code_manager.save_code("gred", gred_code)

    # Example: eval
    eval_code = '''
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("Accuracy =", accuracy_score(y_test, y_pred_lo))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_lo))
print("Classification Report:")
print(classification_report(y_test, y_pred_lo))
'''
    code_manager.save_code("eval", eval_code)

    # Example: char
    char_code = '''
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 8))
sns.histplot(df[''], color="Red", kde=True)  # Add column name
plt.title("Distribution of ...")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")

plt.figure(figsize=(5, 5))
sns.scatterplot(x=df[''], y=df[''])  # Add column names
plt.title("Scatterplot Title")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
'''
    code_manager.save_code("char", char_code)

    # Example: encode
    encode_code = '''
from sklearn.preprocessing import LabelEncoder

le = {}
for col in encode_cols:  # Add your encode_cols list
    le[col] = LabelEncoder()
    data[col] = le[col].fit_transform(data[col])
'''
    code_manager.save_code("encode", encode_code)

    # Example: scale
    scale_code = '''
from sklearn.preprocessing import StandardScaler

scale_Cols = ['col1', 'col2', 'col3', 'col4', 'col5']  # Replace with your column names
scaler = StandardScaler()
df[scale_Cols] = scaler.fit_transform(df[scale_Cols])

print("Scaled Data:")
print(df[scale_Cols].head())
'''
    code_manager.save_code("scale", scale_code)
    #m1
    m1 = '''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df=pd.read_csv('/content/sample_data/mission1_data.csv')
df.head()
df.info()
df.isnull().sum()
df.duplicated().sum()

df['Test Preparation Course']=df['Test Preparation Course'].fillna('Not Complete')
df['Total Score']=df['Math Score']+df['Reading Score']+df['Writing Score']

#char
plt.figure(figsize=(10,5))
sns.histplot(x='Math Score',kde=True,data=df)

plt.figure(figsize=(10,5))
sns.scatterplot(x='Total Score',y='Math Score',data=df)

plt.figure(figsize=(10,5))
sns.barplot(x='Study Time',y='Reading Score',data=df)

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse

#encode
encode_cols=['Gender','Parental Education Level','Lunch Type','Test Preparation Course']
le = {}
for col in encode_cols:
  le[col] = LabelEncoder()
  df[col] = le[col].fit_transform(df[col])

x=df.drop(['Total Score'],axis=1)
y=df['Total Score']

#scale
scale_Cols = ['Study Time', 'Absences', 'Math Score', 'Reading Score', 'Writing Score']
scaler = StandardScaler()
df[scale_Cols] = scaler.fit_transform(df[scale_Cols])

X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

dt=DecisionTreeRegressor()
dt.fit(X_train,y_train)

dt.score(X_test,y_test)

y_pred=dt.predict(X_test)

mse(y_test,y_pred)

rf=RandomForestRegressor()
rf.fit(X_train,y_train)
rf.score(X_test,y_test)

y_pred_fr=rf.predict(X_test)

#GridSearchCV
from sklearn.model_selection import GridSearchCV , RandomizedSearchCV
dt_param={'max_depth':[3,5,10,None] , 'max_leaf_nodes':[2,5,7]}
grid_search_CV = GridSearchCV(dt,dt_param,cv=5)
grid_search_CV.fit(X_train,y_train)
print(grid_search_CV.best_params_)
df['Test Preparation Course'].value_counts()

#Deploy
!pip install gradio
import gradio as gr

def Predict_total_score(Gender, Parental_Education_Level, Lunch_Type, Test_Preparation_Course, Study_Time, Absences, Math_Score, Reading_Score, Writing_Score):
  try:
    input_data = pd.DataFrame({
        'Gender': [Gender],
        'Parental Education Level': [Parental_Education_Level],
        'Lunch Type': [Lunch_Type],
        'Test Preparation Course': [Test_Preparation_Course],
        'Study Time': [Study_Time],
        'Absences': [Absences],
        'Math Score': [Math_Score],
        'Reading Score': [Reading_Score],
        'Writing Score': [Writing_Score]
    })
    for col in encode_cols:
      input_data[col] = le[col].transform(input_data[col])
    input_data[scale_Cols] = scaler.transform(input_data[scale_Cols])
    # Predict
    prediction = rf.predict(input_data)
    return f"Predicted Total Score: {prediction[0]:,.2f}"
  except Exception as e:
    return f"Error: {str(e)}"

gr.Interface(
    fn=Predict_total_score,
    inputs=[
        gr.Radio(label="Gender", choices=["Female", "Male"]),
        gr.Dropdown(choices=['High School', 'Some High School', 'Bachelor', 'Master'], label='Parental Education Level'),
        gr.Dropdown(choices=['Free/Reduced', 'Standard'], label='Lunch Type'),
        gr.Dropdown(choices=['Complete', 'Not Complete'], label='Test Preparation Course'),
        gr.Number(label='Study Time'),
        gr.Number(label='Absences'),
        gr.Number(label='Math Score'),
        gr.Number(label='Reading Score'),
        gr.Number(label='Writing Score')
    ],
    outputs=gr.Textbox(label="Predicted Total Score"),
    title="Student Performance Prediction",
    description="Predict a student's total score based on various factors"
).launch()
'''
    code_manager.save_code("m1", m1)
