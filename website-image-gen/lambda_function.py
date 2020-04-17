import pandas as pd
import numpy as np
import datetime

dt =  datetime.datetime.today()-datetime.timedelta(days=1)

data_link="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"+dt.strftime("%m-%d-%Y.csv")

df=pd.read_csv(data_link)

g=df.groupby("Country_Region")

print(g.sum()['US'])
