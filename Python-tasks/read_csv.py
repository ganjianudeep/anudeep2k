import csv
def data(file_name):
    header = ['name', 'Salary', 'country']
    data = [
        ['Smith', 2000, 'USA'],
        ['John', 3000, 'India'],
    ]
    with open(file_name, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
        list = []
    with open(file_name, 'r', encoding='UTF8') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for row in csv_reader:
            list.append(row)
        print(list)
        return list
file_name = 'data/read.csv'
new_list=data(file_name)


