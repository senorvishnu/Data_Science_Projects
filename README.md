Chicago Crime Analyzer: Data Analysis Documentation
1. Data Cleaning and Preparation (Python)
Objective:
Prepare the raw Chicago crime dataset for accurate analysis by handling missing data, standardizing formats, and removing inconsistencies.

Key Actions:
Loaded the dataset using Python’s pandas library.
Removed fully empty rows and columns to avoid processing meaningless data.
Filled missing “Location Description” values with “Unknown” to preserve records.
Dropped records missing geographic coordinates (Latitude/Longitude) to support mapping analysis.
Eliminated duplicate records to prevent data distortion.
Standardized the “Date” column to datetime format to enable temporal analysis.
Cleaned categorical text columns by removing leading/trailing spaces and standardizing capitalization.

Outcome:
Generated a clean, structured dataset saved as Final_Crime_Data_CLEANED.xlsx ready for deep analysis and visualization.

PFA the link for Power Bi Visualistion File - https://drive.google.com/drive/folders/13u1oI0-mU8FMZLxw664ZvjRr9MlPpadN?usp=sharing
PFA the link for Detailed DOcument of this project - https://docs.google.com/document/d/1L1AooV1Hf2rReXInz_31wTTAlYJNeA5g7zp7DtqV3u4/edit?usp=sharing
