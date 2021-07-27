import csv


class Filter:

    def filter_by_invalid_data(self, row_list):
        i = 0
        while i < len(row_list):
            if row_list[i][0] == '' or row_list[i][1] == '':
                row_list.pop(i)
                i -= 1
            i += 1

        return row_list

    def filter_by_topic(self, topic, row_list):
        i = 0
        while i < len(row_list):
            tag_list = row_list[i][2].split(";")
            tag_is = False
            for tag in tag_list:
                if tag == topic:
                    tag_is = True
                    break

            if not tag_is:
                row_list.pop(i)
                i -= 1
            i += 1

        return row_list

    def filter_by_alphabet(self, alphabet, row_list):
        i = 0
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
    
    def sort(self, row_list):
        for i in range(0, len(row_list) - 1):
            for j in range(i + 1, len(row_list)):
                if row_list[i][0].lower() > row_list[j][0].lower():
                    for k in range(0, len(row_list[0])):
                        row_list[i][k], row_list[j][k] = row_list[j][k], row_list[i][k]

        return row_list
                        
    def filter_db(self, csv, filter_type=None, sub_filter=None):

        row_list = self.gen_row_list(csv)
        row_list = self.sort(row_list)
        row_list = self.filter_by_invalid_data(row_list)

        if filter_type == None:
            return row_list
        elif filter_type == "invalid_data":
            return self.filter_by_invalid_data(row_list)
        elif filter_type == "all_words":
            return self.filter_by_invalid_data(row_list)
        elif filter_type == "topic":
            return self.filter_by_topic(sub_filter, row_list)
        elif filter_type == "alphabet":
            return self.filter_by_alphabet(sub_filter, row_list)


# test code below
# obj = Filter()
# print(obj.filter_db("C:\\Users\\aaroh\\OneDrive\\Documents\\GitHub\\marathi-shabd\\database\\db.csv", filter_type="topic", sub_filter="engineering"))
# print(obj.sort(obj.gen_row_list("C:\\Users\\aaroh\\OneDrive\\Documents\\GitHub\\marathi-shabd\\database\\db.csv")))
# obj.filter_by_alphabet("../database/db.csv", "e")
# obj.filter_by_topic("../database/db.csv", "science")
# obj.filter_by_alphabet("../database/db.csv", "f")
# obj.filter_db("../database/db.csv", "topic","science")
# obj.filter_db("../database/db.csv", "alphabet","s")
# obj.filter_db("../database/db.csv", "alphabet","","s")
