import requests
from bs4 import BeautifulSoup

response = requests.get('https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub')

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.table
# print('\n\rows: \n\n', table_rows, '\n\n')

if table:
    # table_rows = list.sort(table.contents[1:], key=lambda row:  ) # pyright:ignore
    print(type(int(table.contents[5].contents[0].contents[0].contents[0].string)))
    






