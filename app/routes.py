from flask import render_template
import operator
from app import app
import pandas as pd
from itertools import islice

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

pd.options.display.float_format = '{:,.0f}'.format

data = pd.read_csv("owid-covid-data.csv")

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

#davidt pandas code

#table1 (tabla con mayores casos en el mundo 5 países)
csv = data.groupby(['iso_code','location','population','total_cases','total_deaths']).size().reset_index().groupby('iso_code').max()
table1 = csv.drop('OWID_WRL')
table11 = table1.sort_values(by ='total_deaths', ascending = False)
top10table1 = table11.head(n=10)

locationtable1 = top10table1['location'].values.tolist()
populationtable1 = top10table1['population'].values.tolist()
total_casestable1 = top10table1['total_cases'].values.tolist()
total_deathstable1 = top10table1['total_deaths'].values.tolist()

print("TABLE 1:")
print(locationtable1,populationtable1,total_casestable1,total_deathstable1)

#bctable1:
#top 7 countries that best managed covid-19 Uwu according to TIME Magazine (upale)
#bc = best_cases in the world

bctable1 = table11.loc[(table11['location'] == 'Taiwan') | (table11['location'] == 'Singapore') | (table11['location'] == 'South Korea') | (table11['location'] == 'New Zealand') | (table11['location'] == 'Australia') | (table11['location'] == 'United Arab Emirates')| (table11['location'] == 'Greece')]
bctable1 = bctable1.sort_values(by ='total_deaths', ascending = False)

locationbctable1 = bctable1['location'].values.tolist()
populationbctable1 = bctable1['population'].values.tolist()
total_casesbctable1 = bctable1['total_cases'].values.tolist()
total_deathsbctable1 = bctable1['total_deaths'].values.tolist()

print("BCTABLE1:")
print(locationbctable1,populationbctable1,total_casesbctable1,total_deathsbctable1)

#table2:
#top 10 worst countries filtered by total_deaths_per_million
table2 = data.groupby(['iso_code','location','total_cases','total_deaths','total_deaths_per_million','total_tests_per_thousand']).size().reset_index().groupby('iso_code').max()
table2 = table2.round(decimals=2)
sortable2 = table2.sort_values(by ='total_deaths_per_million', ascending = False)
top10t2 = sortable2.head(n=10)

locationtable2 = top10t2['location'].values.tolist()
total_casestable2 = top10t2['total_cases'].values.tolist()
total_deathstable2 = top10t2['total_deaths'].values.tolist()
total_deaths_per_milliontable2 = top10t2['total_deaths_per_million'].values.tolist()
total_tests_per_thousandtable2 = top10t2['total_tests_per_thousand'].values.tolist()

print("TABLE2:")
print(locationtable2,total_casestable2,total_deathstable2,total_deaths_per_milliontable2,total_tests_per_thousandtable2)

#bctable2
#top 7 countries that best managed covid-19 Uwu according to TIME Magazine (upale)
#bc = best_cases in the world

bc2t2 = table2.loc[(table2['location'] == 'Taiwan') | (table2['location'] == 'Singapore') | (table2['location'] == 'South Korea') | (table2['location'] == 'New Zealand') | (table2['location'] == 'Australia') | (table2['location'] == 'United Arab Emirates')| (table2['location'] == 'Greece')]
bc2t2 = bc2t2.sort_values(by ='total_cases', ascending = False)

locationbc2t2 = bc2t2['location'].values.tolist()
total_casesbc2t2 = bc2t2['total_cases'].values.tolist()
total_deathsbc2t2 = bc2t2['total_deaths'].values.tolist()
total_deaths_per_millionbc2t2 = bc2t2['total_deaths_per_million'].values.tolist()
total_tests_per_thousandbc2t2 = bc2t2['total_tests_per_thousand'].values.tolist()

print("BCTABLE2:")
print(locationbc2t2,total_casesbc2t2,total_deathsbc2t2,total_deaths_per_millionbc2t2,total_tests_per_thousandbc2t2)

#table3
#this table is sorted by the "total_cases_per_million", and it displays the top worst 10 countries.

table3 = data.groupby(['iso_code','location','population','total_cases_per_million','gdp_per_capita','extreme_poverty','diabetes_prevalence','cardiovasc_death_rate','male_smokers','female_smokers','aged_65_older']).size().reset_index().groupby('iso_code').max()
table3 = table3.round(decimals=2)
sortable3 = table3.sort_values(by ='total_cases_per_million', ascending = False)
top10t3 = sortable3.head(n=10)

locationtable3 = top10t3['location'].values.tolist()
populationtable3 = top10t3['population'].values.tolist()
total_cases_per_milliontable3 = top10t3['total_cases_per_million'].values.tolist()
gdp_per_capita_table3 = top10t3['gdp_per_capita'].values.tolist()
extreme_poverty_table3 = top10t3['extreme_poverty'].values.tolist()
diabetes_prevalence_table3 = top10t3['diabetes_prevalence'].values.tolist()
cardiovasc_death_rate_table3 = top10t3['cardiovasc_death_rate'].values.tolist()
male_smokers_table3 = top10t3['male_smokers'].values.tolist()
female_smokers_table3 = top10t3['female_smokers'].values.tolist()
aged_65_older_table3 = top10t3['aged_65_older'].values.tolist()

print('TABLE3:')
print(locationtable3,populationtable3,gdp_per_capita_table3,extreme_poverty_table3,diabetes_prevalence_table3,cardiovasc_death_rate_table3,male_smokers_table3,female_smokers_table3,aged_65_older_table3)

#table4
#this table will display the sick population in %

table4 = data.groupby(['iso_code','location','population','median_age','total_cases','total_tests_per_thousand','new_cases_per_million']).size().reset_index().groupby('iso_code').max()
table4 = table4.round(decimals=2)
table4['sick_population'] = ((table4['total_cases'] * 100) / table4['population']).round(decimals=2)
table4 = table4.sort_values(by ='sick_population', ascending = False)
table4top10 = table4.head(n=10)

locationtable4 = table4top10['location'].values.tolist()
populationtable4 = table4top10['population'].values.tolist()
median_agetable4 = table4top10['median_age'].values.tolist()
total_casestable4 = table4top10['total_cases'].values.tolist()
total_tests_per_thousandtable4 = table4top10['total_tests_per_thousand'].values.tolist()
new_cases_per_million = table4top10['new_cases_per_million'].values.tolist()
sick_population = table4top10['sick_population'].values.tolist()

print('TABLE4:')
print(locationtable3,populationtable3,gdp_per_capita_table3,extreme_poverty_table3,diabetes_prevalence_table3,cardiovasc_death_rate_table3,male_smokers_table3,female_smokers_table3,aged_65_older_table3,locationtable4,populationtable4,median_agetable4,total_casestable4,total_casestable4,total_tests_per_thousandtable4,new_cases_per_million,sick_population)

#table5
#this table will display the Fatality case ratio per country

table5 = data.groupby(['iso_code','location','population','median_age','total_cases','total_deaths','total_deaths_per_million']).size().reset_index().groupby('iso_code').max()
table5 = table5.round(decimals=2)
table5['case_fatality_ratio'] = ((table5['total_deaths'] * 100) / table5['total_cases']).round(decimals=2)
table5 = table5.sort_values(by =['case_fatality_ratio', 'population'], ascending = False)
table5top10 = table5.head(n=10)

locationtable5 = table5top10['location'].values.tolist()
populationtable5 = table5top10['population'].values.tolist()
median_agetable5 = table5top10['median_age'].values.tolist()
total_casestable5 = table5top10['total_cases'].values.tolist()
total_deathstable5 = table5top10['total_deaths'].values.tolist()
total_deaths_per_milliontable5 = table5top10['total_deaths_per_million'].values.tolist()
case_fatality_ratio = table5top10['case_fatality_ratio'].values.tolist()

print('TABLE5:')
print(locationtable3,populationtable3,gdp_per_capita_table3,extreme_poverty_table3,diabetes_prevalence_table3,cardiovasc_death_rate_table3,male_smokers_table3,female_smokers_table3,aged_65_older_table3,locationtable4,populationtable4,median_agetable4,total_casestable4,total_casestable4,total_tests_per_thousandtable4,new_cases_per_million,sick_population,locationtable5,populationtable5,median_agetable5,total_casestable5,total_deathstable5,total_deaths_per_milliontable5,case_fatality_ratio)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',max = max,countries=countries,values=values,worldValue=worldValue,valuesDeath=valuesDeath, locationtable1 = locationtable1, total_deathstable1 = total_deathstable1,populationtable1=populationtable1,total_casestable1=total_casestable1,locationbc2t2=locationbc2t2,total_casesbc2t2=total_casesbc2t2,total_deathsbc2t2=total_deathsbc2t2,total_deaths_per_millionbc2t2=total_deaths_per_millionbc2t2,total_tests_per_thousandbc2t2=total_tests_per_thousandbc2t2,locationtable3=locationtable3,populationtable3=populationtable3,total_cases_per_milliontable3=total_cases_per_milliontable3,gdp_per_capita_table3=gdp_per_capita_table3,extreme_poverty_table3=extreme_poverty_table3,diabetes_prevalence_table3=diabetes_prevalence_table3,cardiovasc_death_rate_table3=cardiovasc_death_rate_table3,male_smokers_table3=male_smokers_table3,female_smokers_table3=female_smokers_table3,aged_65_older_table3=aged_65_older_table3,locationtable4=locationtable4,populationtable4=populationtable4,median_agetable4=median_agetable4,total_casestable4=total_casestable4,total_tests_per_thousandtable4=total_tests_per_thousandtable4,new_cases_per_million=new_cases_per_million,sick_population=sick_population,locationtable5=locationtable5,populationtable5=populationtable5,median_agetable5=median_agetable5,total_casestable=total_casestable5,total_deathstable5=total_deathstable5,total_deaths_per_milliontable5=total_deaths_per_milliontable5,case_fatality_ratio=case_fatality_ratio)
