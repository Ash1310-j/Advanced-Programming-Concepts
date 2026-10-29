import pandas as pd

def process_student_data(file_path):
    # 1. Read the student CSV file
    df = pd.read_csv(file_path)
    print("--- Original DataFrame ---")
    print(df)
    
    # 2. Identify missing values
    print("\n--- Missing Values Count Per Column ---")
    print(df.isnull().sum())
    
    # 3. Replace missing marks with the mean of the 'Marks' column
    # (Assuming the column name is 'Marks')
    if 'Marks' in df.columns:
        mean_marks = df['Marks'].mean()
        df['Marks'] = df['Marks'].fillna(mean_marks)
        print(f"\nMissing marks replaced with mean value: {mean_marks:.2f}")
    
    # 4. Calculate descriptive statistics
    print("\n--- Descriptive Statistics ---")
    statistics = df.describe()
    print(statistics)
    
    return df

# To run this, replace 'students.csv' with your actual file path
# processed_df = process_student_data('students.csv')