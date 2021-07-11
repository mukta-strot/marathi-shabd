import csv


class Sort:

    def sort(self, file):
        with open(file, encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            list_of_lists = []

            for row in csv_reader:
                list1 = row
                list1.pop(len(list1)-1)
                list_of_lists.append(list1)

            for i in range(1, len(list_of_lists) - 1):
                for j in range(i + 1, len(list_of_lists)):
                    if list_of_lists[i][0] > list_of_lists[j][0]:
                        for k in range(0, len(list_of_lists[0])):
                            list_of_lists[i][k], list_of_lists[j][k] = list_of_lists[j][k], list_of_lists[i][k]

            with open('sorteddb.csv', 'w', encoding="utf-8") as f:  # creating new file called sorteddb.csv
                for l in list_of_lists:
                    for i in range(0, len(l)):
                        f.write(l[i] + ",")
                    f.write("\n")

            return list_of_lists

#s = Sort()

#s.sort("db.csv")  # test code
