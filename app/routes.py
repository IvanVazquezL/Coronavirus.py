from flask import render_template
import operator
from app import app
import pandas as pd 
from itertools import islice

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

pd.options.display.float_format = '{:,.0f}'.format

data = pd.read_csv("Coronavirus_dataset.csv")
dicto = {}
print(data.groupby('location')['new_cases'].sum())
dicto = data.groupby('location')['new_cases'].sum()
sortedDicto = dict(sorted(dicto.items(), key=operator.itemgetter(1),reverse=True))
print(sortedDicto)

n_items = take(10, sortedDicto.items())

print(n_items)
countries = []
values = []
for key, value in n_items:
    countries.append(key)
    values.append(int(value))
    
print(countries)
print(values)

print(values[0])



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',countries=countries,values=values)