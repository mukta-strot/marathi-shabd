import csv


class Filter:

    def filter_by_invalid_data(self, row_list):
        i = 1
        while i < len(row_list):
            if row_list[i][0] == '' or row_list[i][1] == '':
                row_list.pop(i)
                i -= 1
            i += 1

        return row_list

    def filter_by_topic(self, topic, row_list):
        i = 1
        while i < len(row_list):
            if row_list[i][2] != topic:
                row_list.pop(i)
                i -= 1
            i += 1

        return row_list

    def filter_by_alphabet(self, alphabet, row_list):
        i = 1
        while i < len(row_list):
            if row_list[i][0][0] != alphabet:
                row_list.pop(i)
                i -= 1
            i += 1

        return row_list

    def gen_row_list(self, file_name):
        row_list = []

        with open(file_name, encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            # skip the first row (i.e. the header row) when scanning csv
            next(csv_reader)
            for row in csv_reader:
                row_list.append(row)

        return row_list

    def filter_db(self, csv, filter_type, sub_filter=None):

        row_list = self.gen_row_list(csv)

        row_list = self.filter_by_invalid_data(row_list)

        if filter_type == "invalid_data":
            return self.filter_by_invalid_data(row_list)
        elif filter_type == "all_words":
            return self.filter_by_invalid_data(row_list)
        elif filter_type == "topic":
            return self.filter_by_topic(sub_filter, row_list)
        elif filter_type == "alphabet":
            return self.filter_by_alphabet(sub_filter, row_list)


#  test code below
#obj = Filter()

# obj.filter_by_alphabet("../database/db.csv", "e")
# obj.filter_by_topic("../database/db.csv", "science")
# obj.filter_by_alphabet("../database/db.csv", "f")
# obj.filter_db("../database/db.csv", "topic","science")
# obj.filter_db("../database/db.csv", "alphabet","s")
#obj.filter_db("../database/db.csv", "alphabet","","s")

