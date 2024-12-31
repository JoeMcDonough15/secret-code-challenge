import requests
from bs4 import BeautifulSoup

response = requests.get('https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub')

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.table

if table:
    # sort the tr tags by descending y coordinates and ascending x coordinates for any tying y coordinates
    # this way, the higher rows (rows are represented by y_coordinates) will be at the top of the grid, and the lower rows at the bottom.  Columns (represented by x_coordinate) will increment from left to right.
    table_rows = sorted(table.contents[1:], key=lambda row: (-int(row.contents[2].contents[0].contents[0].string), int(row.contents[0].contents[0].contents[0].string))) # pyright:ignore
    # set the initial row num to the highest row that we have
    row_num = int(table_rows[0].contents[2].contents[0].contents[0].string) # pyright: ignore
    col_num = 0 # initialize the col_num to 0 since all columns will build left to right
    grid = [] # initialize the grid to an empty array - will be an array of rows (arrays)
    current_row = [] # initialize the current_row (first row) to an empty array
    for table_row in table_rows:
        y_coordinate = int(table_row.contents[2].contents[0].contents[0].string) # pyright: ignore
        # print('y coordinate: ', y_coordinate)
        x_coordinate = int(table_row.contents[0].contents[0].contents[0].string) # pyright: ignore
        # print('x coordinate: ', x_coordinate)
        current_char = table_row.contents[1].contents[0].contents[0].string # pyright: ignore
        if y_coordinate != row_num:
            # if the y coordinate is not equal to row_num, then we're finished building that row.  So, make a new row and append the current_row to the grid
            grid.append(current_row) # pyright: ignore
            row_num = y_coordinate # set the row_num to be what the new y_coordinate is since we're finished with the previous row
            col_num = 0  # reset the col_num to 0 for the new row
            current_row = [] # reset current_row to empty array
            # allow the col_num to catch up to the x_coordinate, appending spaces until it does
        while col_num < x_coordinate:
            current_row.append(' ') # pyright: ignore
            col_num += 1      
        current_row.append(current_char) # pyright: ignore
        # increment the col_num to prepare for the next iteration, where we will see the next x_coordinate
        col_num += 1
    
    # once the loop completes through all the table_rows, we still have to append our final row to the grid
    grid.append(current_row) # pyright: ignore


    secret_message = '\n'
    for row in grid: # pyright: ignore
        for char in row: # pyright: ignore
            secret_message += char # pyright: ignore  # concatenate each character of the row to the secret_message
        secret_message += '\n' # pyright: ignore # in between each row, put a line break

    print(secret_message)  # pyright: ignore
    






