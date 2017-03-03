import csv

def write_to_csv(csv_name, content):
    print (content)
    list = []
    list.append(content)
    # Assuming res is a list of lists
    with open(csv_name, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(list)