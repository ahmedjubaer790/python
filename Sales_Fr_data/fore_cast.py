#import the libraries
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

#data loading
file_name='Sales_data.xlsx'
df=pd.read_excel(file_name)

#check column names
df.rename(columns={'Date': 'ds', 'SALES': 'y'}, inplace=True)

#input product name
product_forecast=input("Enter the product name for sales forecasting: ")
product_df=df[df['PRODUCT_NAME']==product_forecast].copy()

#check if the product exists
if product_df.empty:
    print("No data found for the specified product.")
else:
    #create model
    model=Prophet(yearly_seasonality=True,weekly_seasonality=True,
                  daily_seasonality=False)
    
    model.fit(product_df)

    #future data frame
    future_frame=model.make_future_dataframe(periods=30)
    #forecast
    forecast=model.predict(future_frame)

    #result
print("{product_forecast} sales forecast for the next 30 days")
#main forecast plot
fig1=model.plot(forecast)
plt.title(f"{product_forecast} Sales Forecast")
plt.xlabel("Date")
plt.ylabel("Sales")
#chart
fig2=model.plot_components(forecast)

plt.show()