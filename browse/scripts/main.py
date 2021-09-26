from genOut import GenFiles
from topicsParser import TopicsParser
import string

f = GenFiles() # GenFiles object

# code to generate output markdown files

# all words
f.gen_out("../../database/db.csv", "../all.md", "all_words")

# alphabets
list_of_letters = list(string.ascii_lowercase)
for letter in list_of_letters:
    f.gen_out("../../database/db.csv", "../alpha/" + letter + ".md", "alphabet", letter)

# topics
tp = TopicsParser()
topics = tp.gen_topics("../../database/db.csv")
topics_file = open("../topics/00-topics-list.md", "w", encoding="UTF-8")
# topics list file - add heading
topics_file.write("Click on the topic to see words under it. \n \n")
for topic in topics:
    # generate individual topic files as per the topics-list
    f.gen_out("../../database/db.csv", '../topics/{}.md'.format(topic), "topic", "{}".format(topic))
    # add a bulleted list of topics linking to the topic files
    topics_file.write("- [" + topic + "]" + "(" + "{}.md".format(topic) + ")" + "\n")
