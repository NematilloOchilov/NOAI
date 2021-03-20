"""Script Nematillo Ochilov tomonidan yozildi va dastur xato bashorat qilishiga u javob bermaydi!
Scriptni https://colab.research.google.com/ saytida ishga tushiring."""

# !pip install yfinance
# !pip install fbprophet

import yfinance
import pandas as pd
import datetime
from fbprophet import Prophet


data = yfinance.download('BTC-USD', strat='2020-12-01',  # mashina o'rganish davri
                         end=datetime.datetime.today(), interval='1d')  # davr opraliq birligi kun
df = pd.DataFrame()
df['y'] = data['Close']
df['ds'] = data.index
model = Prophet(daily_seasonality=True)
model.fit(df)
kelajak = model.make_future_dataframe(periods=730)  # kelajakni bashorat qilish davri
natija = model.predict(kelajak)
model.plot(natija)
