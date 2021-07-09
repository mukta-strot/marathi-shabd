import csv


class Sort:

    def sort(self, file):
        with open(file, encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 1
            english_list = [] # initializing lists for each column
            marathi_list = []
            tag_list = []
            english_ex = []
            marathi_ex = []

            for row in csv_reader:
                english_list.append(row[0])
                marathi_list.append(row[1])
                tag_list.append(row[2])
                english_ex.append(row[3])
                marathi_ex.append(row[4])


            for i in range(0, len(english_list)-1):
                for j in range(i+1, len(english_list)):
                    if english_list[i] > english_list[j]:
                        english_list[i], english_list[j] = english_list[j], english_list[i] # editing every list while sorting
                        marathi_list[i], marathi_list[j] = marathi_list[j], marathi_list[i]
                        tag_list[i], tag_list[j] = tag_list[j], tag_list[i]
                        english_ex[i], english_ex[j] = english_ex[j], english_ex[i]
                        marathi_ex[i], marathi_ex[j] = marathi_ex[j], marathi_ex[i]

            # print(english_list)

            # print(tag_list)
            print(f'Processed {line_count} lines.')

            with open('sorteddb.csv', 'w', encoding="utf-8") as f: # creating new file called sorteddb.csv
                f.write('en,mr,tags,en-ex,mr-ex\n')
                for i in range(0, len(english_list)):
                    f.write(english_list[i] + ',' + marathi_list[i] + ',' + tag_list[i] + ',' + english_ex[i] + ',' + marathi_ex[i] + ',\n')

            return [english_list, marathi_list, tag_list, english_ex, marathi_ex]


