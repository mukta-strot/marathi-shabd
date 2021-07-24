import csv

class TopicsParser:
    
    def gen_topics(self, file):
        with open(file, encoding="utf-8") as csv_file:
            topics = set()
            tags_column_index = 0
            csv_reader = list(csv.reader(csv_file, delimiter=','))
            tags_column_index = self.find_tags_column_index(csv_reader)
            for row in csv_reader:
                split_topics = row[tags_column_index].split(';')
                for temp_topic in split_topics:
                    if (temp_topic == ''):
                        pass
                    else:
                        topics.add(temp_topic)
            return sorted(list(topics))

    def find_tags_column_index(self, csv_reader):
        tags_column_index = 0
        for column in csv_reader[0]:
            if (column == 'tags'):
                return tags_column_index
            tags_column_index += 1


#TESTS

#t = TopicsParser()

#t.gen_topics("../../database/db.csv")
            