import pandas as pd

try:
    # Load the old and new CSV files into Pandas DataFrames
    old_data = pd.read_csv('old_csv.csv')  # Replace with the path to your old CSV file
    new_data = pd.read_csv('new_csv.csv')  # Replace with the path to your new CSV file

    # Ensure consistency in column names and data types
    old_data.columns = old_data.columns.str.strip()
    new_data.columns = new_data.columns.str.strip()

    # Check for duplicate records in the old and new files
    duplicate_ids_old = old_data[old_data.duplicated(subset=['ID'], keep=False)]['ID'].unique()
    if len(duplicate_ids_old) > 0:
        raise ValueError(f"Duplicate records found in the old CSV file. Duplicate IDs: {', '.join(map(str, duplicate_ids_old))}")

    duplicate_ids_new = new_data[new_data.duplicated(subset=['ID'], keep=False)]['ID'].unique()
    if len(duplicate_ids_new) > 0:
        raise ValueError(f"Duplicate records found in the new CSV file. Duplicate IDs: {', '.join(map(str, duplicate_ids_new))}")

    # Find new products (those that exist in the new file but not in the old file)
    new_products = new_data[~new_data['ID'].isin(old_data['ID'])].copy()  # Create a copy to avoid the warning

    # Safely add the 'status' column to the copied DataFrame
    new_products['status'] = 'new'

    # Find potential updated products (those that exist in both files)
    updated_products = new_data[new_data['ID'].isin(old_data['ID'])].copy()  # Create a copy to avoid the warning

    # Compare all columns for updated products
    def has_changes(row, old_data):
        return any(row[col] != old_data.set_index('ID').loc[row['ID'], col] for col in old_data.columns if col != 'ID')

    # Filter for rows where any column has changed
    updated_products = updated_products[updated_products.apply(lambda row: has_changes(row, old_data), axis=1)]

    # Safely add the 'status' column to the copied DataFrame
    updated_products['status'] = 'updated'

    # Combine new and updated products into one DataFrame
    final_result = pd.concat([new_products, updated_products])

    # Save the final result to a new CSV file
    final_result.to_csv('updated_and_new_products.csv', index=False)

    print("Comparison complete. Updated and new products saved to 'updated_and_new_products.csv'.")

except FileNotFoundError as fe:
    print(f"Error: File not found - {fe}")

except ValueError as ve:
    print(f"Error: {ve}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
