import csv


class Filter:

    def write_from_rowlist(self, row_list):
        with open("filtered.csv", mode="w", encoding="utf-8") as return_file:
            for row in row_list:
                for i in row:
                    return_file.write(i + ",")
                return_file.write("\n")
        return return_file

    def filter_by_invalid_data(self, c):
        with open(c, encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            row_list = []
            for row in csv_reader:
                row_list.append(row)

            print(row_list)
            i = 1
            while i < len(row_list):
                print(i)
                if row_list[i][0] == '' or row_list[i][1] == '':
                    row_list.pop(i)
                    i -= 1
                i += 1

        return self.write_from_rowlist(row_list)

    def filter_by_topic(self, c, topic):
        with open(c, encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            row_list = []
            for row in csv_reader:
                row_list.append(row)
            i = 1
            while i < len(row_list):
                print(i)
                if row_list[i][2] != topic:
                    row_list.pop(i)
                    i -= 1
                i += 1

        return self.write_from_rowlist(row_list)

    def filter_by_alphabet(self, c, alphabet):
        with open(c, encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            row_list = []
            for row in csv_reader:
                row_list.append(row)
            i = 1
            while i < len(row_list):
                print(i)
                if row_list[i][0][0] != alphabet:
                    row_list.pop(i)
                    i -= 1
                i += 1

        return self.write_from_rowlist(row_list)

    def filter_db(self, csv, filter_type, topic=None, alphabet=None):
        if filter_type == "invalid_data":
            return self.filter_by_invalid_data(csv)
        elif filter_type == "all_words":
            return self.filter_by_invalid_data()
        elif filter_type == "topic":
            return self.filter_by_topic(csv, topic)
        elif filter_type == "alphabet":
            return self.filter_by_alphabet(csv, alphabet)

#  test code below
#  obj = Filter()

#  obj.filter_by_alphabet("database\\db.csv", "e")
