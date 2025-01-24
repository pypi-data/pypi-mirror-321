# Databricks notebook source
# MAGIC %pip install markets_analytics_databricks --quiet
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

import pandas as pd
from markets_analytics_databricks import GSheetHelper

credentials = dbutils.secrets.get(scope="team-offprice-market-analytics-scope", key="bq_credential")
gsheet = GSheetHelper('1uW4pgUkh8wqdwOu1HqR8kZFUk5soKYXkiYj6UhjyHPw', credentials)
gsheet.read('Test', 'A1')

# COMMAND ----------

gsheet.write('Test', 'Markets Analytics', 'A3')

# COMMAND ----------

df = pd.DataFrame({
    'name': ['Viktor', 'Minh', 'Danyal', 'Ghada', 'Kashyap'],
    'title': ['Lead', 'Senior', 'Senior', 'Senior', 'Mid']
})

gsheet.write('Test', df, 'C1')

# COMMAND ----------

df = pd.DataFrame({
    'name': ['Viktor', 'Minh', 'Danyal', 'Ghada', 'Kashyap'],
    'title': ['Lead', 'Senior', 'Senior', 'Senior', 'Mid']
})

gsheet.write('Test', df, 'F1', header=False)

# COMMAND ----------

gsheet.delete('Test', 'C6:G6')
