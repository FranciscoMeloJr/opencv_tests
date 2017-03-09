import csv

#this writes to a csv file:
def write_to_csv(csv_name, list, flag):
    write_to_csv(csv_name, list, flag, "w")

#this writes to a csv file:
def write_to_csv(csv_name, list, flag, mode):
    print("write")
    if(flag):
        print (csv_name)
        print (list)
    # Assuming res is a list of lists
    with open(csv_name, mode) as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(list)

#this reads to a csv file:
def read_from_csv(csv_name, flag):
    list = []
    with open(csv_name, "r") as input:
        reader = csv.reader(input)
        for row in reader:
            list.append(row)

    if (flag):
        print(list)

    return list

#read_from_csv("../../python_results.csv", True)