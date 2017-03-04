import csv

#this writes to a csv file:
def write_to_csv(csv_name, list):
    # Assuming res is a list of lists
    with open(csv_name, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(list)