from filterdb import Filter
from genblock import GenBlock


# params
# csv - database file
# outFile - output markdown file (with full path)
# filter - main filter
# sub_filter - sub filter

class GenFiles:
    def gen_out(self, csv, outFile, filter=None, sub_filter=None):
        f = Filter()  # filter class object
        g = GenBlock()  # block class object

        # open output file
        with open(outFile, "w", encoding="UTF-8") as md_file:
            if filter != None and filter != "all_words":
                topic = sub_filter
                md_file.write("# " + topic + "\n\n")
            else:
                md_file.write("# All\n\n")

            # run filter
            row_list =  f.filter_db(csv, filter, sub_filter)
            for row in row_list:
                md_block = g.generate_block(row)
                md_file.write(md_block)

# test code below
# obj = GenFiles()
# obj.gen_out("C:\\Users\\aaroh\\OneDrive\\Documents\\GitHub\\marathi-shabd\\database\\db.csv", "out.md", filter="topic", sub_filter="science")
# gen_out("C:\\Users\\aaroh\\OneDrive\\Documents\\GitHub\\marathi-shabd\\database\\db.csv",
# filter="alphabet", sub_filter="s")

# tested ok (basic)
# gen_out("../../database/db.csv", "../alpha/a.md", filter="alphabet", sub_filter="a")
# gen_out("../../database/db.csv", "../topics/places.md", filter="topic", sub_filter="places")
# gen_out("../../database/db.csv", "../all.md", filter="all_words")

