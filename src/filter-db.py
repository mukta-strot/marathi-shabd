# purpose - to filter the input csv data as per the provided arguments

# ### filter types ###
# - invalid data
# - all words
# - specific topic
# - specific alphabet (which will be initial of the english word)
# - TBD (more can be added)

# ### about invalid data filter ###
# the invalid data filter is to be run always before running any other filter,
# as it eliminates those data elements which have insufficient or invalid data
# insufficient data - any of the english or marathi word is missing
# invalid data - if english word contains non english characters (this can be
# thought of later, and is low priority right now), same for marathi word.

# IMP - make separate functions for each filter type
# as per the passed argument of the "filter type" call the relavant function

# steps
# 1. take passed csv data and filter type as argument
# 2. generate a truncated csv data structure as per the target filter
#    - call the specific filter function here
# 3. return this truncated data to the calling function
import csv


class Filter:

    def filter_by_invalid_data(self, c):
        with open(c, encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            row_list = []
            for row in csv_reader:
                row_list.append(row)

            print(row_list)
            i = 0
            while i < len(row_list):
                print(i)
                if row_list[i][0] == '' or row_list[i][1] == '':
                    row_list.pop(i)
                    i -= 1
                i += 1

        with open("filtered.csv", mode="w", encoding="utf-8") as return_file:
            for row in row_list:
                for i in row:
                    return_file.write(i + ",")
                return_file.write("\n")
        return return_file

    def filter_by_all_words(self):
        return

    def filter_db(self, csv, filter_type):
        if filter_type == "invalid_data":
            self.filter_by_invalid_data(csv)
        elif filter_type == "all_words":
            self.filter_by_all_words(csv)

#test code below
#obj = Filter()

#obj.filter_by_invalid_data("C:\\Users\\aaroh\\OneDrive\\Documents\\GitHub\\marathi-shabd\\database\\db.csv")
