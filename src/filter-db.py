import csv


class Filter:

    @staticmethod
    def write_from_row_list(row_list):
        with open("filtered.csv", mode="w", encoding="utf-8") as return_file:
            for row in row_list:
                for i in row:
                    return_file.write(i + ",")
                return_file.write("\n")
        return return_file

    def filter_by_invalid_data(self, row_list):
        i = 1
        while i < len(row_list):
            if row_list[i][0] == '' or row_list[i][1] == '':
                row_list.pop(i)
                i -= 1
            i += 1

        return self.write_from_row_list(row_list)

    def filter_by_topic(self, topic, row_list):
        i = 1
        while i < len(row_list):
            if row_list[i][2] != topic:
                row_list.pop(i)
                i -= 1
            i += 1

        return self.write_from_row_list(row_list)

    def filter_by_alphabet(self, alphabet, row_list):
        i = 1
        while i < len(row_list):
            if row_list[i][0][0] != alphabet:
                row_list.pop(i)
                i -= 1
            i += 1

        return self.write_from_row_list(row_list)

    def filter_db(self, csv, filter_type, sub_filter=None):
        with open(csv, encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            row_list = []
            for row in csv_reader:
                row_list.append(row)

        if filter_type == "invalid_data":
            return self.filter_by_invalid_data(row_list)
        elif filter_type == "all_words":
            return self.filter_by_invalid_data(row_list)
        elif filter_type == "topic":
            return self.filter_by_topic(sub_filter, row_list)
        elif filter_type == "alphabet":
            return self.filter_by_alphabet(sub_filter, row_list)

#  test code below
#  obj = Filter()

#  obj.filter_by_alphabet("database\\db.csv", "e")
