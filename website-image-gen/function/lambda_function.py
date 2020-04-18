import pandas as pd
import numpy as np
import datetime
import geopandas as gpd
import difflib
import country_converter as coco
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import math
import io
import boto3



dt =  datetime.datetime.today()-datetime.timedelta(days=1)

data_link="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"+dt.strftime("%m-%d-%Y.csv")

df=pd.read_csv(data_link)
df.rename(columns = {'Country_Region':'iso_a3'}, inplace = True) 
  
g=df.groupby("iso_a3")
f=g['Confirmed'].sum()
    
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world = world[(world.pop_est>0) & (world.name!="Antarctica")]
    
standard_names = coco.convert(names=list(f.index), to='ISO3')
    
m=f.reset_index()
m["iso_a3"]=standard_names
    
world=world.merge(m, on='iso_a3')
    
world["cp"]=world["Confirmed"]/world["pop_est"]
    
N = 256
vals = np.ones((N, 4))
vals[:, 0] = np.linspace(.24, 1, N)
vals[:, 1] = np.linspace(.24, 0, N)
vals[:, 2] = np.linspace(.24, 0, N)
cmp = ListedColormap(vals)
    
vmin=world['cp'].min()
vmax=world['cp'].max()
    
fig, ax = plt.subplots(1, figsize=(30, 10))
ax.axis('off')
plt.rcParams['savefig.facecolor'] = '#3D3D3D'
sm = plt.cm.ScalarMappable(cmap=cmp, norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm.set_array([])
cb=fig.colorbar(sm, orientation="horizontal", fraction=0.02, pad=0.05, aspect = 50)
cb.outline.set_visible(False)
cb.ax.tick_params(size=0)
cb.ax.set_xlabel('Confirmed Cases/ Total Population', color='0.4')

plt.setp(plt.getp(cb.ax.axes, 'xticklabels'), color='0.4',size='large')

world.plot(column='cp', cmap=cmp, linewidth=1, ax=ax, edgecolor='0.3')
    

img_data = io.BytesIO()
plt.savefig(img_data,format='png',dpi=200,bbox_inches='tight')
img_data.seek(0)
    
s3 = boto3.resource('s3')
bucket = s3.Bucket('covid.arjungandhi.com')
bucket.put_object(Body=img_data, ContentType='image/png', Key='world.png')
