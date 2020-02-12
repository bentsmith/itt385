import csv

csv_file = open("C:\\Users\\labuser\\Desktop\\Four-Cells.csv")

csv_reader = csv.reader(csv_file)

data = list(csv_reader)

for row in range(0,len(data)):
    for col in range(0,len(data[row])):
        
        print(row, col, data[row][col])