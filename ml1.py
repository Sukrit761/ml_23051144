import pandas as pd

rows = 10

A = list(range(1, rows+1))
B = []
for i in range(1, rows+1):
    B.append("Item" + str(i))

C = []
for x in range(1, rows+1):
    C.append(x * 2)

D = [n*n for n in range(1, rows+1)]
E = [f"Data{x}" for x in range(1, rows+1)]

table = {
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "E": E
}

df = pd.DataFrame(table)
file_name = "sample_table.csv"
