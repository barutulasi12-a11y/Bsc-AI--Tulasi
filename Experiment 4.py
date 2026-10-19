import pandas as pd
import numpy as np
from scipy.stats import zscore

def main():
    # --------------------------------
    # Creating Sample Dataset
    # --------------------------------

    data = {
        "Name": ["Ravi", "Sita", "Kiran", "Ravi ", "Anu", "John",],
        "Marks": [85, 90, 78, 85, 300, 88],
    }

    df = pd.DataFrame(data)

    print("====== ORIGINAL DATASET ======")
    print(df)

    # --------------------------------
    # Finding Duplicate Rows
    # -------------------------------- 
    
    df_no_duplicates = df.drop_duplicates()
    print("\n====== DATASET AFTER REMOVING DUPLICATES ======")
    print(df_no_duplicates)

    # -------------------------------- 
    #Detecting Outliers using Z-Score
    # --------------------------------

    df_no_duplicates['z_score'] = zscore(df_no_duplicates['Marks'])
    print("\n====== Z-SCORE ======")
    print(df_no_duplicates)

    # Outlier where z-score >2or < -2
    outliers = df_no_duplicates[(df_no_duplicates['z_score'] > 2) | (df_no_duplicates['z_score'] < -2)]
    print("\n====== DETECTED OUTLIERS ======")
    print(outliers)

    #--------------------------------
    # Removing Outliers
    #--------------------------------

    cleaned_data = df_no_duplicates[(df_no_duplicates['z_score'] <= 2) & (df_no_duplicates['z_score'] >= -2)]
    print("\n====== DATASET AFTER REMOVING OUTLIERS ======")
    print(cleaned_data)

    #--------------------------------
    # Comparing Distributions
    # -------------------------------

    print("\n====== DISTRIBUTIONS BEFORE REMOVING OUTLIERS ======") 
    print(df_no_duplicates['Marks'].describe())

    print("\n====== DISTRIBUTIONS AFTER REMOVING OUTLIERS ======")
    print(cleaned_data['Marks'].describe())

    if __name__=='__main__':
        main()