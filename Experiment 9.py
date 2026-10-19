import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Sample dataset
    data = {
        'Marks': [45, 56, 67, 78, 89, 90, 56, 73, 68, 92,
                  81, 77, 85, 69, 58, 64, 72, 88, 95, 49]
    }

    # Creating DataFrame
    df = pd.DataFrame(data)

    print("Dataset")
    print(df)

    # Display basic statistics
    print("\nStatistical Summary")
    print(df.describe())

    # --------------------------------------------------
    # HISTOGRAM
    # --------------------------------------------------

    plt.figure(figsize=(6, 4))

    plt.hist(df['Marks'], bins=6)

    # Mean line
    plt.axvline(df['Marks'].mean(), linestyle='--', label='Mean')

    # Median line
    plt.axvline(df['Marks'].median(), linestyle=':', label='Median')

    plt.title("Histogram of Marks")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")

    plt.legend()
    plt.show()

    # --------------------------------------------------
    # BOXPLOT
    # --------------------------------------------------

    plt.figure(figsize=(6, 4))

    plt.boxplot(df['Marks'])

    plt.title("Boxplot of Marks")
    plt.ylabel("Marks")

    plt.show()

    # --------------------------------------------------
    # VIOLIN PLOT
    # --------------------------------------------------

    plt.figure(figsize=(6, 4))

    sns.violinplot(y=df['Marks'])

    plt.title("Violin Plot of Marks")
    plt.ylabel("Marks")

    plt.show()

if __name__ == '__main__':
    main()