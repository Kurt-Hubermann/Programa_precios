import pandas as pd
import os

# Function to get files in a folder
def get_files(folder):
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        if os.path.isfile(file_path) and not file_name.endswith('.gitkeep'):
            files = file_path
    return files

# Main script function
def script():
    path = get_files(os.path.join(os.getcwd(), 'Input'))
    data = pd.read_excel(path, dtype={'Codigo': str})
    first_row = list((data.iloc[:0]))
    df = pd.DataFrame(data)
    df.columns = first_row

    # Iterate over columns (except 'Codigo') to create .prn files
    for column in first_row[1:]:
        text = "" # Variable to store the content of the file

        # Iterate over rows of the DataFrame
        for index, row in df.iterrows():
            codigo = row['Codigo'] # Get the value in the 'Codigo' column
            value = row[column] # Get the value in the current column

            # Format the information and add it to the 'text' variable
            text += (' ' * (10 - len(str(column))) + str(column) +
                     ' ' * (12 - len(str(codigo))) + str(codigo) +
                     ' ' * (44 - len(str(value))) + str(value))
            text += '\n'

        # Save the content to the .prn file
        save_path = os.path.join(os.getcwd(), f'Output\\L{column}.prn')
        with open(save_path, "w") as archivo:
            archivo.write(text)

if __name__ == '__main__':
    script()