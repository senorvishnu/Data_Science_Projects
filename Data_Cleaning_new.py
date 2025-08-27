import pandas as pd
import time
import os

class CrimeDataCleaner:
    def __init__(self, input_path):
        self.input_path = input_path
        self.df = None

    def load_data(self):
        print("Step 1: Loading Excel data...")
        start = time.time()
        self.df = pd.read_excel(self.input_path, engine="openpyxl")  # fast engine
        print(f"✔ Data loaded in {time.time() - start:.2f}s. Shape: {self.df.shape}")

    def clean_data(self):
        df = self.df

        print("Step 2: Dropping empty rows/cols...")
        df.dropna(axis=0, how='all', inplace=True)
        df.dropna(axis=1, how='all', inplace=True)

        print("Step 3: Handling missing values...")
        if 'Location Description' in df.columns:
            df['Location Description'].fillna('Unknown', inplace=True)
        if {'Latitude', 'Longitude'}.issubset(df.columns):
            df.dropna(subset=['Latitude', 'Longitude'], inplace=True)

        print("Step 4: Removing duplicates...")
        df.drop_duplicates(inplace=True)

        print("Step 5: Standardizing date column...")
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

        print("Step 6: Cleaning categorical columns...")
        for col in ['Primary Type', 'Description', 'Location Description']:
            if col in df.columns:
                df[col] = df[col].astype(str).str.strip().str.title()

        self.df = df  # update

    def save_data(self, output_path=None):
        if not output_path:
            output_path = self.input_path.replace('.xlsx', '_CLEANED.xlsx')
        print("Step 7: Saving cleaned data...")
        start = time.time()
        self.df.to_excel(output_path, index=False, engine="openpyxl")
        print(f"✔ Cleaned data saved to {output_path} in {time.time() - start:.2f}s.")

def main():
    input_path = r"E:\Python\Chicago_Crime_Analyser_Project\Crime_Data.xlsx"
    if not os.path.exists(input_path):
        print("❌ Error: Input file not found")
        return

    start_time = time.time()
    cleaner = CrimeDataCleaner(input_path)
    cleaner.load_data()
    cleaner.clean_data()
    cleaner.save_data()
    print(f"✅ Script finished in {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
