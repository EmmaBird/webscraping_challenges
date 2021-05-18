import requests
import pandas as pd
from bs4 import BeautifulSoup

def clean_power10_table(df, event, sex):
    table = df[2:]
    table = table.drop(table.columns[[2,3,5,8,13]], axis=1)
    table = table[table[0].apply(lambda x: str(x).isnumeric())]
    table.columns = ['rank', 'performance', 'pb', 'athlete', 'age_group', 'coach', 'club', 'comp_loc', 'comp_date']
    table['coach'] = table['coach'].fillna('N/A')
    table['age_group'] = table['age_group'].fillna('Senior')
    table['comp_date_sort'] = pd.to_datetime(table['comp_date'], format='%d %b %y')
    table['performance'] = round(table['performance'].astype(float), 2)
    table.insert(0, 'sport', 'Athletics')
    table.insert(1, 'event', '{}m'.format(event))
    table.insert(2, 'gender', sex)
    return table

def write_power10_table_to_csv(df, event, sex):
    df.to_csv(f"data/{event} ({sex}) GB Rankings.csv", index=False)
            