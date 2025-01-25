import os
import pandas as pd
import numpy as np

# Import the upload_file function from file_upload.py
from file_upload import upload_file

# Create some mock test data
def create_test_files():
    # Test CSV file with valid data
    df_valid = pd.DataFrame({
        'Criteria1': [1, 2, 3, np.nan],
        'Criteria2': [4, 5, 6, 7],
        'Criteria3': [8, 9, 10, 11]
    })
    df_valid.to_csv('test_valid.csv', index=False)
    
    # Test Excel file with valid data
    df_valid.to_excel('test_valid.xlsx', index=False)
    
    # Test CSV with missing columns
    df_missing_cols = df_valid.drop(columns=['Criteria3'])
    df_missing_cols.to_csv('test_missing_cols.csv', index=False)
    
    # Test CSV with non-numeric data in Criteria1
    df_non_numeric = df_valid.copy()
    df_non_numeric['Criteria1'] = ['a', 'b', 'c', 'd']
    df_non_numeric.to_csv('test_non_numeric.csv', index=False)
    
    # Test large file (simulate by repeating data)
    df_large = pd.concat([df_valid] * 10000, ignore_index=True)  # Creates a large file by repeating rows
    df_large.to_csv('test_large.csv', index=False)

    # Test file with missing values
    df_missing_vals = df_valid.copy()
    df_missing_vals['Criteria2'].iloc[2] = np.nan  # Missing value in Criteria2
    df_missing_vals.to_csv('test_missing_vals.csv', index=False)
    
    # Test file with duplicates
    df_duplicates = pd.concat([df_valid, df_valid], ignore_index=True)
    df_duplicates.to_csv('test_duplicates.csv', index=False)

# Run the tests
def run_tests():
    create_test_files()  # Create test files
    
    # Test valid CSV
    try:
        df = upload_file('test_valid.csv')
        print("Valid CSV test passed.")
    except Exception as e:
        print(f"Valid CSV test failed: {e}")
    
    # Test valid Excel
    try:
        df = upload_file('test_valid.xlsx')
        print("Valid Excel test passed.")
    except Exception as e:
        print(f"Valid Excel test failed: {e}")
    
    # Test missing columns
    try:
        df = upload_file('test_missing_cols.csv')
        print("Missing columns test passed.")
    except Exception as e:
        print(f"Missing columns test failed: {e}")
    
    # Test non-numeric data in Criteria columns
    try:
        df = upload_file('test_non_numeric.csv')
        print("Non-numeric data test passed.")
    except Exception as e:
        print(f"Non-numeric data test failed: {e}")
    
    # Test large file size
    try:
        df = upload_file('test_large.csv')
        print("Large file test passed.")
    except Exception as e:
        print(f"Large file test failed: {e}")
    
    # Test missing values
    try:
        df = upload_file('test_missing_vals.csv')
        print("Missing values test passed.")
    except Exception as e:
        print(f"Missing values test failed: {e}")
    
    # Test duplicates
    try:
        df = upload_file('test_duplicates.csv')
        print("Duplicates test passed.")
    except Exception as e:
        print(f"Duplicates test failed: {e}")

run_tests()
