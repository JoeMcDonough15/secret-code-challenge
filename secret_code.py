import requests
from bs4 import BeautifulSoup

response = requests.get('https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub')

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.table

if table:
    table_rows = sorted(table.contents[1:], key=lambda row: (int(row.contents[0].contents[0].contents[0].string), int(row.contents[2].contents[0].contents[0].string))) # pyright:ignore
    print(table_rows)
    






