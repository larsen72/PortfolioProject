# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 12:13:53 2023

@author: leldo
"""
#%%
# Initial imports
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_mergers_and_acquisitions'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

#%%
# Create DF from scraped data

table = soup.find_all('table')[1]
titles = table.find_all('th')
table_titles = [title.text.strip() for title in titles]
print(table_titles)

df_1900 = pd.DataFrame(columns = table_titles)

column_data = table.find_all('tr')
for row in column_data[1:]:
    rows_data = row.find_all('td')
    row = [data.text.strip() for data in rows_data]
    length = len(df_1900)
    df_1900.loc[length] = row
    
df_1900

#%%
# Create DF from scraped data

table = soup.find_all('table')[2]
titles = table.find_all('th')
table_titles = [title.text.strip() for title in titles]
print(table_titles)

df_1910 = pd.DataFrame(columns = table_titles)

column_data = table.find_all('tr')
for row in column_data[1:]:
    rows_data = row.find_all('td')
    row = [data.text.strip() for data in rows_data]
    length = len(df_1910)
    df_1910.loc[length] = row
    
df_1910

#%%
# Create DF from scraped data

table = soup.find_all('table')[3]
titles = table.find_all('th')
table_titles = [title.text.strip() for title in titles]
print(table_titles)

df_1920 = pd.DataFrame(columns = table_titles)

column_data = table.find_all('tr')
for row in column_data[1:]:
    rows_data = row.find_all('td')
    row = [data.text.strip() for data in rows_data]
    length = len(df_1920)
    df_1920.loc[length] = row
    
df_1920

#%%
# Create DF from scraped data

table = soup.find_all('table')[4]
titles = table.find_all('th')
table_titles = [title.text.strip() for title in titles]
print(table_titles)

df_1930 = pd.DataFrame(columns = table_titles)

column_data = table.find_all('tr')
for row in column_data[1:]:
    rows_data = row.find_all('td')
    row = [data.text.strip() for data in rows_data]
    length = len(df_1930)
    df_1930.loc[length] = row
    
df_1930

#%%
# Create DF from scraped data

table = soup.find_all('table')[5]
titles = table.find_all('th')
table_titles = [title.text.strip() for title in titles]
print(table_titles)

df_1940 = pd.DataFrame(columns = table_titles)

column_data = table.find_all('tr')
for row in column_data[1:]:
    rows_data = row.find_all('td')
    row = [data.text.strip() for data in rows_data]
    length = len(df_1940)
    df_1940.loc[length] = row
    
df_1940

#%%
# Create DF from scraped data

table = soup.find_all('table')[6]
titles = table.find_all('th')
table_titles = [title.text.strip() for title in titles]
print(table_titles)

df_1950 = pd.DataFrame(columns = table_titles)

column_data = table.find_all('tr')
for row in column_data[1:]:
    rows_data = row.find_all('td')
    row = [data.text.strip() for data in rows_data]
    length = len(df_1950)
    df_1950.loc[length] = row
    
df_1950

#%%
# Create DF from scraped data

table = soup.find_all('table')[7]
titles = table.find_all('th')
table_titles = [title.text.strip() for title in titles]
print(table_titles)

df_1960 = pd.DataFrame(columns = table_titles)

column_data = table.find_all('tr')
for row in column_data[1:]:
    rows_data = row.find_all('td')
    row = [data.text.strip() for data in rows_data]
    length = len(df_1960)
    df_1960.loc[length] = row
    
df_1960

#%%
# Create DF from scraped data

table = soup.find_all('table')[8]
titles = table.find_all('th')
table_titles = [title.text.strip() for title in titles]
print(table_titles)

df_1970 = pd.DataFrame(columns = table_titles)

column_data = table.find_all('tr')
for row in column_data[1:]:
    rows_data = row.find_all('td')
    row = [data.text.strip() for data in rows_data]
    length = len(df_1970)
    df_1970.loc[length] = row
    
df_1970

#%%
# Create DF from scraped data

table = soup.find_all('table')[9]
titles = table.find_all('th')
table_titles = [title.text.strip() for title in titles]
print(table_titles)

df_1980 = pd.DataFrame(columns = table_titles)

column_data = table.find_all('tr')
for row in column_data[1:]:
    rows_data = row.find_all('td')
    row = [data.text.strip() for data in rows_data]
    length = len(df_1980)
    df_1980.loc[length] = row
    
df_1980

#%%
# Create DF from scraped data

table = soup.find_all('table')[10]
titles = table.find_all('th')
table_titles = [title.text.strip() for title in titles]
print(table_titles)

df_1990 = pd.DataFrame(columns = table_titles)

column_data = table.find_all('tr')
for row in column_data[1:]:
    rows_data = row.find_all('td')
    row = [data.text.strip() for data in rows_data]
    length = len(df_1990)
    df_1990.loc[length] = row
    
df_1990

#%%
# Create DF from scraped data

table = soup.find_all('table')[11]
titles = table.find_all('th')
table_titles = [title.text.strip() for title in titles]
print(table_titles)

df_2000 = pd.DataFrame(columns = table_titles)

column_data = table.find_all('tr')
for row in column_data[1:]:
    rows_data = row.find_all('td')
    row = [data.text.strip() for data in rows_data]
    length = len(df_2000)
    df_2000.loc[length] = row
    
df_2000

#%%
# Create DF from scraped data

table = soup.find_all('table')[12]
titles = table.find_all('th')
table_titles = [title.text.strip() for title in titles]
print(table_titles)

df_2010 = pd.DataFrame(columns = table_titles)

column_data = table.find_all('tr')
for row in column_data[1:]:
    rows_data = row.find_all('td')
    row = [data.text.strip() for data in rows_data]
    length = len(df_2010)
    df_2010.loc[length] = row
    
df_2010.drop(labels = 'Ref', axis = 1, inplace = True)    
df_2010

#%%
# Merge DF's

frames = [df_1900, df_1910, df_1920, df_1930, df_1940, df_1950, df_1960, df_1970, df_1980, df_1990, df_2000, df_2010]

for i in frames:
    i.columns = ['rank', 'year', 'buyer', 'purchased', 'transaction_value_in_billions', 'inflation_adjusted_in_billions']

df_total = pd.concat(frames)

df_total.drop(labels = 'rank', axis = 1, inplace = True)
df_total['year'] = df_total['year'].astype(int)
df_total['transaction_value_in_billions'] = df_total['transaction_value_in_billions'].str.split('—').str[0].str.strip()
df_total['inflation_adjusted_in_billions'] = df_total['inflation_adjusted_in_billions'].str.split('—').str[0].str.strip()
df_total['transaction_value_in_billions'] = df_total['transaction_value_in_billions'].astype(float)
df_total['inflation_adjusted_in_billions'] = df_total['inflation_adjusted_in_billions'].astype(float)
df_total = df_total.reset_index()

df_total.info()

#%%
# Some graphing imports
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import numpy as np
sns.set(style = "darkgrid")
plt.figure(figsize = (100, 60))

#%%
# Lets take a look at transactions over time

sns.relplot(data = df_total,
           x = 'year',
           y = 'inflation_adjusted_in_billions')
plt.xticks(rotation = 45)
plt.xlabel('Year', fontsize = 10)
plt.ylabel('Transaction Value - Inflation Adjusted (in billions)', fontsize = 10)
plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(nbins = 20))
plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(nbins = 20))

plt.show()

#%%
# Non-adjusted transactions
sns.relplot(data = df_total,
           x = 'year',
           y = 'transaction_value_in_billions')
plt.xticks(rotation = 45)
plt.xlabel('Year', fontsize = 10)
plt.ylabel('Transaction Value (in billions)', fontsize = 10)
plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(nbins = 18))
plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(nbins = 20))

plt.show()

#%%
# Transactions with exponential curve
sns.relplot(data = df_total,
            x = 'year',
            y = 'inflation_adjusted_in_billions')

# Calculate exponential curve parameters
x = df_total['year']
y = df_total['inflation_adjusted_in_billions']
params = np.polyfit(x, np.log(y), 1)
a, b = np.exp(params[1]), params[0]

# Generate exponential curve
x_vals = np.linspace(min(x), max(x), 100)
y_vals = a * np.exp(b * x_vals)

# Plot exponential trendline
plt.plot(x_vals, y_vals, color='red', linestyle='--', label=f'Exponential Trendline: y = {a:.2f} * e^({b:.4f} * x)')
plt.legend()

plt.xticks(rotation=45)
plt.xlabel('Year', fontsize=10)
plt.ylabel('Transaction Value - Inflation Adjusted (in billions)', fontsize=10)
plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(nbins = 18))
plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(nbins = 20))
#plt.gca().invert_yaxis()

plt.show()

#%%
# Transactions with Linear trend

sns.relplot(data = df_total,
            x='year',
            y='inflation_adjusted_in_billions',
            kind = 'scatter')
sns.regplot(data = df_total,
            x = 'year',
            y = 'inflation_adjusted_in_billions',
            scatter = False,
            line_kws = {"color": "red", "alpha": 0.7, "lw": 2})
plt.xticks(rotation = 45)
plt.xlabel('Year', fontsize = 10)
plt.ylabel('Transaction Value (in billions)', fontsize = 10)
plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(nbins = 18))
plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(nbins = 20))
plt.ylim(-10, None)

plt.show()

#%%
# Lets take a look at the annual averages

df_annual_avg = df_total.drop(labels = 'buyer', axis = 1).drop(labels = 'purchased', axis = 1).groupby('year').mean()

sns.relplot(data = df_annual_avg,
           x = 'year',
           y = 'inflation_adjusted_in_billions',
           kind = 'line')
plt.xticks(rotation = 45)
plt.xlabel('Year', fontsize = 10)
plt.ylabel('Transaction Value - Inflation Adjusted (in billions)', fontsize = 10)
plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(nbins = 18))
plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(nbins = 20))

plt.show()

#%%
# A glance at the KKR - RJR Nabisco transaction

sns.relplot(data = df_total,
           x = 'year',
           y = 'inflation_adjusted_in_billions')
plt.xticks(rotation = 45)
plt.xlabel('Year', fontsize = 10)
plt.ylabel('Transaction Value - Inflation Adjusted (in billions)', fontsize = 10)
plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(nbins = 18))
plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(nbins = 20))

plt.scatter(df_total['year'][56], 
            df_total['transaction_value_in_billions'][56], 
            color='red',
            s=100)

#%%
# Split the data
df_total_sorted = df_total.sort_values(by=['year', 'inflation_adjusted_in_billions']).reset_index()
df_pre_jb = df_total_sorted[:85]
df_post_jb = df_total_sorted[85:]

#%%
# Lets plot the df_pre_jb data

sns.relplot(data = df_pre_jb,
           x = 'year',
           y = 'inflation_adjusted_in_billions',)
sns.regplot(data = df_pre_jb,
            x = 'year',
            y = 'inflation_adjusted_in_billions',
            scatter = False,
            line_kws = {"color": "red", "alpha": 0.7, "lw": 2})
plt.xticks(rotation = 45)
plt.xlabel('Year', fontsize = 10)
plt.ylabel('Transaction Value - Inflation Adjusted (in billions)', fontsize = 10)
plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(nbins = 18))
plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(nbins = 20))
plt.ylim(-1, None)

plt.show()

#%%
# df_post_jb

sns.relplot(data = df_post_jb,
           x = 'year',
           y = 'inflation_adjusted_in_billions')
sns.regplot(data = df_post_jb,
            x = 'year',
            y = 'inflation_adjusted_in_billions',
            scatter = False,
            line_kws = {"color": "red", "alpha": 0.7, "lw": 2})
plt.xticks(rotation = 45)
plt.xlabel('Year', fontsize = 10)
plt.ylabel('Transaction Value - Inflation Adjusted (in billions)', fontsize = 10)
plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(nbins = 18))
plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(nbins = 20))
plt.ylim(-10, None)

plt.show()

#%%
# Overlay the two lines onto df_total for comparison
sns.relplot(data = df_total,
           x = 'year',
           y = 'inflation_adjusted_in_billions')
sns.regplot(data = df_pre_jb,
            x = 'year',
            y = 'inflation_adjusted_in_billions',
            scatter = False,
            line_kws = {"color": "red", "alpha": 0.7, "lw": 2})
sns.regplot(data = df_post_jb,
            x = 'year',
            y = 'inflation_adjusted_in_billions',
            scatter = False,
            line_kws = {"color": "red", "alpha": 0.7, "lw": 2})
plt.xticks(rotation = 45)
plt.xlabel('Year', fontsize = 10)
plt.ylabel('Transaction Value - Inflation Adjusted (in billions)', fontsize = 10)
plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(nbins = 18))
plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(nbins = 20))
plt.ylim(-10, None)

plt.show()