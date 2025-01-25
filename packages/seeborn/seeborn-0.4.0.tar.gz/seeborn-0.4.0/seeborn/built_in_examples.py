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

    # Example: deb2
    deb2_code = '''
import gradio as gr
import pandas as pd

def predict_laptop_price(brand, processor_type, ram_size, storage, screen_size, operating_system):
    try:
        input_data = pd.DataFrame(
            {
                'Brand': [brand],
                'Processor Type': [processor_type],
                'RAM Size (GB)': [ram_size],
                'Storage (GB)': [storage],
                'Screen Size (inches)': [screen_size],
                'Operating System': [operating_system],
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
    ],
    outputs=gr.Textbox(label='Predicted Price ($)'),
    fn=predict_laptop_price,
    title='Laptop Price Prediction',
    description='Enter the details of the laptop to predict its price.'
).launch()
'''
    code_manager.save_code("deb2", deb2_code)

    # Example: eval2
    eval2_code = '''
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Train models
lr = LinearRegression()
lr.fit(x_train, y_train)

dt = DecisionTreeRegressor()
dt.fit(x_train, y_train)

rf = RandomForestRegressor()
rf.fit(x_train, y_train)

# Make predictions
y_pred_lr = lr.predict(x_test)
y_pred_dt = dt.predict(x_test)
y_pred_rf = rf.predict(x_test)

# Evaluate models
print("Linear Regression - MSE:", mean_squared_error(y_test, y_pred_lr))
print("Linear Regression - R2 Score:", r2_score(y_test, y_pred_lr))
print("Linear Regression - MAE:", mean_absolute_error(y_test, y_pred_lr))

print("\nDecision Tree - MSE:", mean_squared_error(y_test, y_pred_dt))
print("Decision Tree - R2 Score:", r2_score(y_test, y_pred_dt))
print("Decision Tree - MAE:", mean_absolute_error(y_test, y_pred_dt))

print("\nRandom Forest - MSE:", mean_squared_error(y_test, y_pred_rf))
print("Random Forest - R2 Score:", r2_score(y_test, y_pred_rf))
print("Random Forest - MAE:", mean_absolute_error(y_test, y_pred_rf))
'''
    code_manager.save_code("eval2", eval2_code)

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
