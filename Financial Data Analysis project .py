#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


file_path ="C:/Users/Lenovo/Downloads/Financial Analytics data (1).csv" 


# In[3]:


df = pd.read_csv(file_path)


# In[4]:


print("First few rows:")
print(df.head())


# In[6]:


print("Column names:")
print(df.columns)


# In[7]:


print("Missing values:")
print(df.isnull().sum())


# In[8]:


print("Data types:")
print(df.dtypes)


# In[9]:


df.columns = [col.strip().lower() for col in df.columns]


# In[10]:


df.rename(columns={
    "serial number": "serial_number",
    "name of company": "company",
    "mar cap – crore": "market_cap_crore",
    "sales qtr – crore": "quarterly_sales_crore"
}, inplace=True)


# In[14]:


correct_column_name = None
for col in df.columns:
    if "mar cap" in col:
        correct_column_name = col
        break


# In[15]:


if correct_column_name:
    print("Using column name:", correct_column_name)


# In[16]:


plt.figure(figsize=(8, 6))
sns.histplot(df['mar cap - crore'], kde=True)
plt.title("Distribution of Market Capitalization (in Crores)")
plt.xlabel("Market Capitalization (in Crores)")
plt.ylabel("Density")
plt.show()


# In[33]:


correct_market_cap_column = None
for col in df.columns:
    if 'market cap' in col:
        correct_market_cap_column = col
        break


# In[34]:


correct_quarterly_sales_column = None
for col in df.columns:
    if 'quarterly' in col and 'sales' in col:
        correct_quarterly_sales_column = col
        break


# In[35]:


correct_company_column = None
for col in df.columns:
    if 'company' in col:
        correct_company_column = col
        break


# In[36]:


if correct_market_cap_column and correct_quarterly_sales_column and correct_company_column:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=correct_market_cap_column, y=correct_quarterly_sales_column, hue=correct_company_column)
    plt.title("Market Capitalization vs. Quarterly Sales")
    plt.xlabel("Market Capitalization (in Crores)")
    plt.ylabel("Quarterly Sales (in Crores)")
    plt.show()
else:
    print("One or more expected columns could not be found. Check for typos or inconsistencies in the dataset.")


# In[37]:


print("Column names in the DataFrame:")
print(df.columns.tolist())


# In[38]:



df.columns = [col.strip().lower() for col in df.columns]


# In[39]:


from difflib import get_close_matches

expected_columns = ["market_cap_crore", "quarterly_sales_crore", "company"]

for expected in expected_columns:
    matches = get_close_matches(expected, df.columns.tolist(), n=1, cutoff=0.5)
    if matches:
        print(f"Possible match for '{expected}': {matches[0]}")
    else:
        print(f"No matches found for '{expected}'")


# In[40]:



corrections = {
    "market_cap": "market_cap_crore",
    "sales_qtr": "quarterly_sales_crore",
    "name": "company"
}

df.rename(columns=corrections, inplace=True)

# Verify the updated column names
print("Updated column names:")
print(df.columns.tolist())


# In[41]:



print("DataFrame structure:")
print(df.head())
print("DataFrame info:")
print(df.info())


# In[42]:


plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="mar cap - crore", y="sales qtr - crore", hue="company")
plt.title("Market Capitalization vs. Quarterly Sales")
plt.xlabel("Market Capitalization (in Crores)")
plt.ylabel("Quarterly Sales (in Crores)")
plt.show()


# In[45]:



correlation = df[["mar cap - crore", "sales qtr - crore"]].corr()
print("Correlation between Market Capitalization and Quarterly Sales:")
print(correlation)


# In[48]:


df["sales_market_cap_ratio"] = df["sales qtr - crore"] / df["mar cap - crore"]


# In[50]:


plt.figure(figsize=(8, 6))
sns.barplot(data=df, x="company", y="sales_market_cap_ratio")
plt.title("Sales/Market Cap Ratio by Company")
plt.xlabel("Company")
plt.ylabel("Sales/Market Cap Ratio")
plt.show()


# In[ ]:




