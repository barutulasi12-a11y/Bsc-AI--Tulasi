import pandas as pd

def main():
 data={
"Student": ["Ravi","sita","kiran","anu","john"],
"Marks":[85,90,78,92,88],
"Age":[ 20,21,19,22,20]
}
 df=pd.DataFrame(data)
 df.to_csv("student.csv",index=False)
 df.to_excel("student.xlsx",index=False)
 df.to_json("student.json",orient="records")

 csv_data=pd.read_csv("student.csv")
 excel_data=pd.read_excel("student.xlsx")
 json_data=pd.read_json("student.json")

 print("CSV Data:")
 print(csv_data)
 print("\nhead()")
 print(csv_data.head())
 print("\ninfo()")
 print(csv_data.info())
 print("\ndescribe()")
 print(csv_data.describe())
 print("\nshape")
 print(csv_data.shape)

if __name__ == '__main__':
    main()