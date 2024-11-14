import pandas as pd

# File names
file_name = "output.xml"
excel_file = "testcode.xlsx"

# Read data from Excel
data = pd.read_excel(excel_file, sheet_name="Sheet1")

# Open the file in append mode
with open(file_name, "a") as file:
    # Iterate over each value in the DataFrame
    for column in data.columns:
        for value in data[column]:
            line = (
                f'<Element Name="COMMENT" Delimiter="|" Barcode="" Interface="1" Query="" Node_Catetory=""\n'
                f'        Module="" Bookmark="" Data_Value="" List_Values="" Format="" Default="" Data_Type=""\n'
                f'        Description="" Element_Id="1CMMT" TestCode="{value}" />\n'
            )
            file.write(line)

print(f"Data appended successfully to {file_name}.")
