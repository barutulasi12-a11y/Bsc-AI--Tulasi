import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():

    # Sample Time Series Dataset
    data = {
        'Date': [
            '2025-01-01', '2025-02-01', '2025-03-01',
            '2025-04-01', '2025-05-01', '2025-06-01',
            '2025-07-01', '2025-08-01', '2025-09-01',
            '2025-10-01', '2025-11-01', '2025-12-01'
        ],
        'Sales': [120, 135, 150, 170, 165, 180,
                  200, 220, 210, 190, 175, 160]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    print("Original Dataset")
    print(df)

    # PARSE DATETIME COLUMN
    df['Date'] = pd.to_datetime(df['Date'])

    print("\nDataset after Parsing Date Column")
    print(df)

    # SET DATE AS INDEX
    df.set_index('Date', inplace=True)

    print("\nDataset with Datetime Index")
    print(df)

    # VISUALIZE TREND
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['Sales'], marker='o')
    plt.title('Sales Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.grid(True)
    plt.show()

    # VISUALIZE SEASONALITY
    df['Month'] = df.index.month_name()

    plt.figure(figsize=(10, 5))
    sns.barplot(x=df['Month'], y=df['Sales'])
    plt.title('Monthly Sales Seasonality')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.show()


if __name__ == "__main__":
    main()