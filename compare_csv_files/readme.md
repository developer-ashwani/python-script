# Product Comparison Script

This script compares two CSV files containing product data (`old_csv.csv` and `new_csv.csv`) to identify new and updated products. It checks for changes across all columns (such as `Title`, `Description`, `Price`, etc.) and generates a new CSV file (`updated_and_new_products.csv`) with the identified products marked as either `new` or `updated`.

## Features

- **Handles Duplicates**: Checks for duplicate records in both the old and new CSV files based on the `ID` column. If any duplicates are found, an error message is raised with the duplicate `ID`s.
  
- **Dynamic Column Comparison**: Compares all columns for changes, making it adaptable for future modifications to the CSV files (i.e., even if new columns are added in the future, they will be considered).

- **Exception Handling**: Handles various exceptions, including missing files and duplicate records, providing clear error messages.

- **Output**: The script generates a new CSV file containing products that are either new (not in the old file) or updated (changes detected in any column).

## Requirements

- **Python** (version 3.6 or higher)
- **Pandas** library (Install using `pip install pandas`)

## Input

1. **old_csv.csv**: The old CSV file containing the original product data.
2. **new_csv.csv**: The new CSV file containing the new and updated product data.

Both CSV files must contain at least the following columns:
- `ID`: A unique identifier for each product (should be the same in both files).
- Other product attributes (e.g., `Title`, `Description`, `Price`).

## Output

- **updated_and_new_products.csv**: A new CSV file containing:
  - `ID`: The unique product identifier.
  - `Title`, `Description`, `Price`: The product details.
  - `status`: A column indicating whether the product is `new` or `updated`.

## How to Use

1. **Prepare your CSV files**: Ensure your old and new product CSV files are correctly formatted and contain the required columns.
   
2. **Run the Script**: Execute the script using the following command:
   ```bash
   python compare_products.py

3. **Check the Output**: The script will create a new CSV file (updated_and_new_products.csv) with the comparison results.

**Example**
Input - old_csv.csv
ID,Title,Description,Price
1,Product A,Description A,100
2,Product B,Description B,200

Input - new_csv.csv
ID,Title,Description,Price
1,Product A,Description A Updated,100
3,Product C,Description C,150

Output - updated_and_new_products.csv
ID,Title,Description,Price,status
1,Product A,Description A Updated,100,updated
3,Product C,Description C,150,new