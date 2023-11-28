# Program Description

The program takes an Excel file containing product prices, transforms them into a special format to be inserted into the billing program. The first column named 'Codigo' contains the product code, and the following columns are the different price lists that need to be modified, each with the price it should have for that product. Each price list is saved in a separate file.

## Example Excel File
    
        Codigo      1      2       4       5      7      8     9     15
    0     0039    169    172   176.0   158.0    180    150   172    142
    1     0040    344    350   359.0   323.0    367    307   350    289
    2     0041    654    666   683.0   615.0    700    584   666    551

# Data Splitting Script

This Python script takes the Excel file located in the 'Input' folder, where it is expected to have the 'Codigo' column followed by n columns of the lists to be modified, and creates a text file (.prn) for each additional column (except 'Codigo'). The generated text files are stored in the 'Output' folder.

## Operation

1. **Data Input:**
    - The `get_files(folder)` function is used to get the path of the Excel file in the 'Input' folder.
    - The Excel file is read using `pd.read_excel()`. The 'Codigo' column is treated as a string ('str').

2. **Creation of .prn Files:**
    - It iterates over the columns of the DataFrame, excluding the 'Codigo' column.
    - For each column, a text file (.prn) is created containing formatted information from each row of the DataFrame.

3. **Format of .prn File:**
    - Each .prn file is named 'L' followed by the name of the corresponding column.
    - Each line of the file contains:
        - 10 spaces for the column name.
        - 12 spaces for the value in the 'Codigo' column.
        - 44 spaces for the value in the current column.
        - Line break at the end of each row.

4. **Storage:**
    - The .prn files are saved in the 'Output' folder in the current directory.

## Execution

The script runs by running the file and performs the data splitting according to the described scheme.

## Requirements

- Python 3.x
- Pandas
