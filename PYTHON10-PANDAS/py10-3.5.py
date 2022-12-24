import pandas as pd

income = [478, 512, 196]
expenses = [156, 130, 270]
years = [2018, 2019, 2020]

def create_companyDF(income, expenses, years):
    return pd.DataFrame({"income": income, "expenses": expenses}, index=years)

def get_profit(df, year):
    if year not in df.index:
        return None
    else:
        return (df.loc[year].income - df.loc[year].expenses)

print(get_profit(create_companyDF(income, expenses, years), 2018))