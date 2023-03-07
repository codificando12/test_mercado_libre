import csv


def export_csv(title, price):

    lst = []
    for tupla in zip(title, price):
        lst.append(tupla)

    with open('items_list.csv', mode='w', newline='') as csv_file:

        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(["Item title", "item price"])

        for count in range(len(lst)):
            csv_writer.writerow([lst[count][0], lst[count][1]])

    csv_file.close()

