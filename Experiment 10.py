import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Sample dataset
    data = {
        'Maths': [78, 85, 96, 80, 86, 90, 70, 88, 92, 75],
        'Science': [84, 79, 95, 78, 88, 91, 72, 85, 94, 74],
        'English': [75, 82, 90, 76, 85, 89, 68, 84, 91, 73]
    }

    # Creating DataFrame
    df = pd.DataFrame(data)

    print("Dataset")
    print(df)

    # --------------------------------------------------
    # SCATTER PLOT
    # --------------------------------------------------

    plt.figure(figsize=(6, 4))

    plt.scatter(df['Maths'], df['Science'])

    plt.title("Scatter Plot: Maths vs Science")
    plt.xlabel("Maths Marks")
    plt.ylabel("Science Marks")

    plt.show()

    # --------------------------------------------------
    # CORRELATION MATRIX
    # --------------------------------------------------

    correlation = df.corr()

    print("\nCorrelation Matrix")
    print(correlation)

    plt.figure(figsize=(6, 4))

    sns.heatmap(correlation, annot=True)

    plt.title("Correlation Matrix Heatmap")

    plt.show()

    # --------------------------------------------------
    # PAIR PLOT
    # --------------------------------------------------

    sns.pairplot(df)

    plt.suptitle("Pair Plot of Subject Marks", y=1.02)

    plt.show()

if __name__ == '__main__':
    main()