import requests
from bs4 import BeautifulSoup

# helper functions
def extract_x_coordinate(row):
    # target the string text of the <span> inside the <p> inside the 1st <td> of the <tr> tag - convert to int for numeric sorting
    return int(row.contents[0].contents[0].contents[0].string)

def extract_character(row):
    # target the string text of the <span> inside the <p> inside the 2nd <td> of the <tr> tag
    return row.contents[1].contents[0].contents[0].string 

def extract_y_coordinate(row):
    # target the string text of the <span> inside the <p> inside the 3rd <td> of the <tr> tag - convert to int for numeric sorting
    return int(row.contents[2].contents[0].contents[0].string)

def convert_grid_to_string(grid):
    secret_message = '\n'
    for row in grid: 
        for char in row: 
            secret_message += char   # concatenate each character of the row to the secret_message string
        secret_message += '\n'  # in between each row, put a line break so all characters align vertically
    return secret_message


def decipher_secret_code(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.table

    # sort the table's tr tags by descending y coordinates and then by ascending x coordinates (for any tying y coordinates).  Leave off the first row as it is just header data.
    table_rows = sorted(table.contents[1:], key=lambda row: (-extract_y_coordinate(row), extract_x_coordinate(row))) 

    row_num = extract_y_coordinate(table_rows[0]) # set the initial row num to the highest row that we have
    col_num = 0 # initialize the col_num to 0 since all columns will build left to right
    grid = [] # initialize the grid to an empty array - will be an array of rows (arrays)
    current_row = [] # initialize the current_row (first row) to an empty array

    for table_row in table_rows:
        x_coordinate = extract_x_coordinate(table_row)
        y_coordinate = extract_y_coordinate(table_row)
        current_char = extract_character(table_row)

        if y_coordinate != row_num:
            # if the y coordinate is not equal to row_num, then we're finished building that row.  So, append the current_row to the grid and begin a new empty current_row.
            grid.append(current_row) 
            current_row = [] # reset current_row to empty array
            row_num = y_coordinate # also, set the row_num to be what the new y_coordinate is since we're finished with the previous row
            col_num = 0  # and reset the col_num to 0 for the new row
        while col_num < x_coordinate:
            # allow the col_num to catch up to the x_coordinate, appending spaces to current_row until it does
            current_row.append(' ') 
            col_num += 1      
        current_row.append(current_char) 
        # increment the col_num to prepare for the next iteration, where we will see the next x_coordinate
        col_num += 1

    # once the loop completes through all the table_rows, we still have to append our final row to the grid
    grid.append(current_row) 
    # then we can convert the grid to a string for easy reading when printed to the terminal
    secret_message = convert_grid_to_string(grid)
    return secret_message


# print the function's return value; the deciphered message
print(decipher_secret_code('https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'))


