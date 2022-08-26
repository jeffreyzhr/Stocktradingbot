import pandas as pd
import numpy as np
import pickle

ticker = 'AAPL'
input_data = []
input_labels = []

with open(f'data/{ticker}.pkl', 'rb') as f:
    current = pickle.load(f)
    

def get_annual_data(current):
    
    a = current[f'{ticker} Annual EPS']
    b = current[f'{ticker} Annual Earnings']
    c = current[f'{ticker} Annual Outstanding Shares']
    d = current[f'{ticker} Annual PE ratio']
    hist = current[f'{ticker} Yearly Hist values']
    
    for year in a.keys():
        to_add = []
        to_add.append(a[year])
        to_add.append(b[year])
        to_add.append(c[year])
        to_add.append(np.mean(d[year]))
        to_add.append(np.mean(hist[year]['Volume'].to_list())) #added avg volume as a data point
        input_data.append(to_add)

def get_labels(current):
    hist = current[f'{ticker} Yearly Hist values']
    for year in hist.keys():
        input_labels.append(np.mean(hist[year]['Close'].to_list()))
        