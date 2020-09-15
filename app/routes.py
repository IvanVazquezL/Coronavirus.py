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

#Dictionaries
dicto = {}
dictDeaths = {}

#Pandas queries
dicto = data.groupby('location')['new_cases'].sum()
dictDeaths = data.groupby('location')['new_deaths'].sum()

#Sort the dictionary in descending order
sortedDicto = dict(sorted(dicto.items(), key=operator.itemgetter(1),reverse=True))
sortedDictDeath = dict(sorted(dictDeaths.items(), key=operator.itemgetter(1),reverse=True))

#Firs n items from a dictionary
n_items = take(10, sortedDicto.items())
n_DictDeath = take(10, sortedDictDeath.items())

def commaSeparate(number):
	return f"{number:,}";

countries = []
values = []
valuesDeath = []

for key, value in n_items:
    if key=="World":
        worldValue = commaSeparate(int(value))
    else:
        countries.append(key)
        values.append(int(value))

for key,value in n_DictDeath:
    if key!="World":
        valuesDeath.append(int(value))

print(countries)
print(values)

print(values[0])

def maxValue(limit):
    numberLen = len(str(limit)) - 2
    numberIncrement = int(str(limit)[1]) + 1
    NumberOriginalMinus = limit-int(str(limit)[0] + ("0"*(len(str(limit))-1)))
    return (((10**numberLen *numberIncrement) - NumberOriginalMinus)+limit)

max=maxValue(values[0])

#davidt: tabla con mayores casos de covid worldwide

import csv

file=open("top_5_c_total_cases.CSV", "r")
reader = csv.reader(file)
locationtable1 = []
populationtable1 = []
total_casestable1 = []
total_deathstable1 = []
for line in reader:
    locationtable1.append(line[0])
    populationtable1.append(line[1])
    total_casestable1.append(line[2])
    total_deathstable1.append(line[3])
    print(line)

print(locationtable1,populationtable1,total_casestable1,total_deathstable1)

#top 7 countries that best managed covid-19 Uwu according to TIME Magazine (upale)

import csv
file=open("best_cases_covid.CSV", "r")
reader = csv.reader(file)
locationtable2 = []
populationtable2 = []
total_casestable2 = []
total_deathstable2 = []
for line in reader:
    locationtable2.append(line[0])
    populationtable2.append(line[1])
    total_casestable2.append(line[2])
    total_deathstable2.append(line[3])
    print(line)

print(locationtable2,populationtable2,total_casestable2,total_deathstable2)

#top 10 worst countries according to the deaths_per_million

import csv
file=open("worst_total_d_per_million.CSV", "r")
reader = csv.reader(file)
locationtable3 = []
total_casestable3 = []
total_deathstable3 = []
total_deaths_per_milliontable3 = []
total_tests_per_thousandtable3 = []
for line in reader:
    locationtable3.append(line[0])
    total_casestable3.append(line[1])
    total_deathstable3.append(line[2])
    total_deaths_per_milliontable3.append(line[3])
    total_tests_per_thousandtable3.append(line[4])
    print(line)

print(locationtable3,total_casestable3,total_deathstable3,total_deaths_per_milliontable3,total_tests_per_thousandtable3)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',max = max,countries=countries,values=values,worldValue=worldValue)

@app.route('/graph2')
def graph():
    return render_template('graph2.html',max = max,countries=countries,values=values,worldValue=worldValue,valuesDeath=valuesDeath, locationtabla1 = locationtabla1, total_deathstable1 = total_deathstable1,populationtable1=populationtable1)
