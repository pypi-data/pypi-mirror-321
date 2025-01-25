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
I love You Ya Moza

'''
    code_manager.save_code("m1", m1)

    #m2
    m2 = '''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("/content/sample_data/mission 2.csv")
data.head(10)

data.isna().sum()

#Encoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

data['Location'] =  le.fit_transform(data['Location'])
data.info()

#Scaler
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
data[['Size (sqft)',  'Bedrooms', 'Bathrooms', 'Year Built', 'Condition']] = sc.fit_transform(
    data[['Size (sqft)',  'Bedrooms', 'Bathrooms', 'Year Built', 'Condition']])
data.columns
data.head()

data.describe()
#char
plt.figure(figsize=(10,10))
sns.histplot(data['Price'], color="green", kde=True)
plt.title = 'Price Distribution'
plt.xlable = "Price"
plt.ylable= "Frequency"
plt.show()

plt.figure(figsize=(10,10))
sns.scatterplot(x=data['Price'], y= data['Size (sqft)'], color="green")
plt.title = 'Price & Size Relation'
plt.xlable = "Price"
plt.ylable= "Size"
plt.show()

plt.figure(figsize=(10,10))
sns.barplot(x=data['Location'],y=data['Price'], color="blue")
plt.title = 'impact of location on price'
plt.xlable = "location"
plt.ylable= "Price"
plt.show()

#model and evl
from sklearn.model_selection import train_test_split
x = data.drop('Price', axis=1)
y =data['Price']
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
lr = LinearRegression()
dt = DecisionTreeRegressor()
rf = RandomForestRegressor()
lr.fit(x_train, y_train)
dt.fit(x_train, y_train)
rf.fit(x_train, y_train)

y_predict_lr = lr.predict(x_test)
y_predict_dt = dt.predict(x_test)
y_predict_rf = rf.predict(x_test)

print("Linear Regression MSE:", mean_squared_error(y_test, y_predict_lr))
print("DecisionTreeRegressor MSE:", mean_squared_error(y_test, y_predict_dt))
print("Random Forest MSE:", mean_squared_error(y_test, y_predict_rf))

print("Linear Regression MSE:", mean_absolute_error(y_test, y_predict_lr))
print("DecisionTreeRegressor MSE:", mean_absolute_error(y_test, y_predict_dt))
print("Random Forest MSE:", mean_absolute_error(y_test, y_predict_rf))

print("r2_score Linear Regression:", r2_score(y_test, y_predict_lr))
print("r2_score DecisionTreeRegressor:", r2_score(y_test, y_predict_dt))
print("r2_score Random Forest:", r2_score(y_test, y_predict_rf))

plt.figure(figsize=(10, 8))
plt.scatter(y_test, y_predict_lr, color='blue', label='Linear Regression')
plt.scatter(y_test, y_predict_dt, color='green', label='Decision Tree')
plt.scatter(y_test, y_predict_rf, color='red', label='Random Forest')
plt.show()

#Gridsearch
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
# using Gridsearch
gird_params = {
    "max_depth": [5,15,10,20,30], "max_leaf_nodes": [10,20,30,50,15,5,7]
}
grid_search_model = GridSearchCV(estimator=DecisionTreeRegressor(), param_grid=gird_params, cv=5)
grid_search_model.fit(x_train, y_train)
grid_search_model.best_params_

grid_y_predict = grid_search_model.best_estimator_.predict(x_test)
print("r2_score GridSearch:", r2_score(y_test, grid_y_predict))
print("MSE GridSearch:", mean_squared_error(y_test, grid_y_predict))
print("MAE GridSearch:", mean_absolute_error(y_test, grid_y_predict))

random_params = {
    'max_depth': [5,15,10,20,30], "n_estimators": [100,200,300,400,500]
}

ranom_model = RandomizedSearchCV(estimator=RandomForestRegressor(), param_distributions=random_params, cv=5)
ranom_model.fit(x_train, y_train)
ranom_model.best_params_

random_y_predict = ranom_model.best_estimator_.predict(x_test)
print("r2_score Random Search:", r2_score(y_test,random_y_predict))
print("MSE Random Search:", mean_squared_error(y_test, random_y_predict))
print("MAE Random Search:", mean_absolute_error(y_test, random_y_predict))

#DEploy
pip install gradio

import gradio as gr
def predict_house_price(Location, Size, Bedrooms, Bathrooms, YearBuilt, Condition):
  # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'Location': [Location],
        'Size (sqft)': [Size],
        'Bedrooms': [Bedrooms],
        'Bathrooms': [Bathrooms],
        'Year Built': [YearBuilt],
        'Condition': [Condition]
    })

    # Encode the categorical column
    input_data['Location'] = le.transform(input_data['Location'])

    # Scale the numerical columns (assume scaling_cols contains the numeric column names)
    scaling_cols = ['Size (sqft)', 'Bedrooms', 'Bathrooms', 'Year Built', 'Condition']
    input_data[scaling_cols] = sc.transform(input_data[scaling_cols])

    # Predict the house price
    prediction = rf.predict(input_data)
    return f"Predicted House Price: ${prediction[0]:,.2f}"
gr.Interface(
    fn=predict_house_price,
    inputs=[
        gr.Dropdown(
            ["Suburban", "Urban", "Rural"], label="Location"),

        gr.Number(label="Size (sqft)"),
        gr.Number(label="Bedrooms"),
        gr.Number(label="Bathrooms"),
        gr.Number(label="Year Built"),
        gr.Number(label="Condition (1-5)")
    ],
    outputs="text",
    title="House Price Prediction"
).launch()

I love You Ya Moza

'''
    code_manager.save_code("m2", m2)

    #m4
    m4 = '''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/content/mission 4.csv')
data.head()
data.isna().sum()
data.columns

from sklearn.preprocessing import LabelEncoder
encode_cols = ['Brand', 'Processor Type', 'Operating System']
le = {}
for col in encode_cols:
  le[col] = LabelEncoder()
  data[col] = le[col].fit_transform(data[col])
data.head()

scale_Cols = ['RAM Size (GB)', 'Storage (GB)', 'Screen Size (inches)']
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data[scale_Cols] = scaler.fit_transform(data[scale_Cols])
data.head()

data.describe()

#char
plt.figure(figsize=(10, 8))
sns.histplot(data['Price ($)'], kde=True, color="red")
plt.xlabel('Price ($)')
plt.ylabel('Frequency')
plt.title('Distribution of Laptop Prices')
plt.show()

plt.figure(figsize=(10,8))
sns.scatterplot(x=data['RAM Size (GB)'], y=data['Price ($)'], color='Blue')
plt.xlabel('Ram')
plt.ylabel('Price')
plt.title('RAM and Price Relationship')

plt.figure(figsize=(10,8))
sns.barplot(x=data['Brand'], y=data['Price ($)'], color='Green')
plt.xlabel('Brand')
plt.ylabel('Price')
plt.title('Brand Impact on Price ')

#model and evl
from sklearn.model_selection import train_test_split
x = data.drop('Price ($)', axis=1)
y = data['Price ($)']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
lr = LinearRegression()
lr.fit(x_train, y_train)
dt = DecisionTreeRegressor()
dt.fit(x_train, y_train)
rf = RandomForestRegressor()
rf.fit(x_train, y_train)
y_pred_lr = lr.predict(x_test)
y_pred_dt = dt.predict(x_test)
y_pred_rf = rf.predict(x_test)
print("Linear Regression:")
print("Mean Squared Error:", mean_squared_error(y_test, y_pred_lr))
print("R-squared:", r2_score(y_test, y_pred_lr))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred_lr))

print("Decision Tree Regression:")
print("Mean Squared Error:", mean_squared_error(y_test, y_pred_dt))
print("R-squared:", r2_score(y_test, y_pred_dt))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred_dt))

print("Random Forest Regression:")
print("Mean Squared Error:", mean_squared_error(y_test, y_pred_rf))
print("R-squared:", r2_score(y_test, y_pred_rf))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred_rf))


#GraidsearchCV
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
random_params = {
    'n_estimators': [50, 100, 200, 250,300],
    'max_depth': [None, 10, 20, 30,35,40],

}
random_model = RandomizedSearchCV(RandomForestRegressor(), random_params, cv=5)
random_model.fit(x_train, y_train)
print("Best Parameters:", random_model.best_params_)
print("Best Score:", random_model.best_score_)


#deploy
pip install gradio
import gradio as gr
def predict_laptop_price(brand, processor_type, ram_size, storage, screen, os):
  try:
    input_data = pd.DataFrame(
        {
            'Brand': [brand],
            'Processor Type': [processor_type],
            'RAM Size (GB)': [ram_size],
            'Storage (GB)': [storage],
            'Screen Size (inches)': [screen],
            'Operating System': [os]

        }
    )

    for col in encode_cols:
      input_data[col] = le[col].transform(input_data[col])
    input_data[scale_Cols] = scaler.transform(input_data[scale_Cols])
    prediction = random_model.best_estimator_.predict(input_data)
    return prediction[0]
  except Exception as e:
    return str(e)
gr.Interface(
      inputs=[
          gr.Dropdown(choices=list(data['Brand'].unique()), label='Brand'),
          gr.Dropdown(choices=list(data['Processor Type'].unique()), label='Processor Type'),
          gr.Number(label='RAM Size (GB)'),
          gr.Number(label='Storage (GB)'),
          gr.Number(label='Screen Size (inches)'),
          gr.Dropdown(choices=list(data['Operating System'].unique()), label='Operating System')
      ]
      , outputs=gr.Textbox(label='Predicted Price ($)'),
      fn=predict_laptop_price,
      title='Laptop Price Prediction',
      description='Enter the details of the laptop to predict its price.'
  ).launch()

I love You Ya Moza

'''
    code_manager.save_code("m4", m4)

    #m7
    m7 = '''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv(r"C:\Users\MKank\Downloads\Holestic\mission7.csv")
df

df['Thrives']=df['Thrives'].map({'Yes':1,'No':0})
df.info()

#encode
encode_cols= ['Soil Type'	, 'Plant Species']
le = {}
for col in encode_cols:
    le[col] = LabelEncoder()
    df[col] =  le[col].fit_transform(df[col])

#Scale
cs = StandardScaler()
df[['Sunlight (hours/day)', 'Water Supply (liters/week)',	'Temperature (Â°C)',	'pH Level']]=cs.fit_transform(df[['Sunlight (hours/day)', 'Water Supply (liters/week)',	'Temperature (Â°C)',	'pH Level']])	

#char 
plt.figure(figsize=(10,8))
sns.scatterplot(x=df['Sunlight (hours/day)'], y=df['Water Supply (liters/week)'], color="yellow")

#Model 
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,accuracy_score

x=df.drop('Thrives',axis=1)
y=df['Thrives']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

rf=RandomForestClassifier()
rf.fit(x_train,y_train)

y_pre=rf.predict(x_test)
confusion_matrix(y_test,y_pre)
accuracy_score(y_test,y_pre)

pram={'max_depth':[20,40,15,10,5]}
pream_g=GridSearchCV(rf,pram,cv=5)
pream_g.fit(x_train,y_train)

#Deploy
!pip install gradio
import gradio as gr

def er(so,su,wa,te,ph,pl):
  try:
    input_data=pd.DataFrame({
        'Soil Type':[so],
        'Sunlight (hours/day)':[su],
        'Water Supply (liters/week)':[wa],
        'Temperature (Â°C)':[te],
        'pH Level':[ph],
        'Plant Species':[pl]
    })
    for col in le_col:
      input_data[col]=le[col].transform(input_data[col])
    input_data[std_col]=std.transform(input_data[std_col])
    pri=rf.predict(input_data)
    if pri ==[0]:
      return "No"
    else:
      return "yes"
  except Exception as e:
    return str(e)
gr.Interface(
    fn=er,
    inputs=[
        gr.Dropdown(label='Soil Type', choices=['Clay','Sandy','Loamy']),
        gr.Number(label='Sunlight (hours/day)'),
        gr.Number(label='Water Supply (liters/week)'),
        gr.Number(label='Temperature (Â°C)'),
        gr.Number(label='pH Level'),
        gr.Dropdown(label='Plant Species',choices=['Lily','Fern','Cactus','Rose','Oak'])
    ],
    outputs=gr.Textbox(label='pridict')
).launch()

I love You Ya Moza
'''
    code_manager.save_code("m7", m7)